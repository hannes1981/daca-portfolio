import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

# ---------------------------------------------------------
# 1. ANDMETE LAADIMINE JA FILTREERIMINE (TARTU)
# ---------------------------------------------------------
# Kasuta täielikku liidetud CSV faili (või data_loader funktsiooni)
df = pd.read_csv("tartu_dashboard_full.csv")
df_products = pd.read_csv("products_rows.csv")
# Veendu kuupäeva formaadis ja filtreeri ainult Tartu kauplus
df["sale_date"] = pd.to_datetime(df["sale_date"])

df = df.merge(
    df_products[["product_id", "product_name"]],
    on="product_id",
    how="left"
)

df_tartu = df[
    (df["store_location"] == "Tartu")
    & (df["sale_date"].dt.year <= 2024)
].copy()

top_products = (
df_tartu.groupby("product_name")["total_price"]
.sum()
.sort_values(ascending=False)
.head(5)
.reset_index()
)


# ---------------------------------------------------------
# 2. DÜNAAMILISED KPI ARVUTUSED
# ---------------------------------------------------------
total_revenue = df_tartu["total_price"].sum()
total_orders = df_tartu["invoice_id"].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0

# ---------------------------------------------------------
# 3. PÄIS JA EXECUTIVE SUMMARY (Juhtide kokkuvõte)
# ---------------------------------------------------------
st.markdown(
    "<h2 style='text-align:center; color:#6C587D;'>UrbanStyle Tartu Store Dashboard</h2>",
    unsafe_allow_html=True,
)

# Roll B: Juhtide kokkuvõte / Narratiiv

st.info(
    "**Juhtide kokkuvõte (Tartu kauplus):** "
    "Tartu kauplus teenis perioodil 2023–2024 kokku 489 361 € käivet "
    "1682 tellimusest. Keskmine tellimuse väärtus oli 290,94 €. "
    "Müügitulu kõigub kuude lõikes märkimisväärselt ning mitmed perioodid "
    "jäävad alla seatud eesmärgijoone. Soovitame analüüsida nõrgemaid "
    "müügiperioode ning tugevdada kohalikke turundustegevusi."
)

# ---------------------------------------------------------
# 4. KPI KAARDID (Sinu kaunis disain + dünaamilised andmed)
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
    <div style="
        background-color:#F0EBF4;
        padding:15px;
        border-radius:10px;
        border-left:6px solid #A88CAA;">
        <p style="margin:0;color:#6C587D;">💰 Kogutulu (Tartu)</p>
        <h2 style="margin:0;color:#2F3443;">{total_revenue/1000:.0f}k €</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
    <div style="
        background-color:#F0EBF4;
        padding:15px;
        border-radius:10px;
        border-left:6px solid #A88CAA;">
        <p style="margin:0;color:#6C587D;">👥 Tellimuste arv</p>
        <h2 style="margin:0;color:#2F3443;">{total_orders:,}</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
    <div style="
        background-color:#F0EBF4;
        padding:15px;
        border-radius:10px;
        border-left:6px solid #A88CAA;">
        <p style="margin:0;color:#6C587D;">📊 Keskmine ost (AOV)</p>
        <h2 style="margin:0;color:#2F3443;">{aov:.2f} €</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.write("")  # Vaherida

# ---------------------------------------------------------
# 5. DIAGRAMM 1: KUISED MÜÜGITRENDID (Koos viitejoone ja annotatsiooniga)
# ---------------------------------------------------------
df_monthly = (
    df_tartu.groupby(df_tartu["sale_date"].dt.to_period("M"))["total_price"]
    .sum()
    .reset_index()
)
df_monthly["sale_date"] = df_monthly["sale_date"].dt.to_timestamp()

fig_line = px.line(
    df_monthly,
    x="sale_date",
    y="total_price",
    title="Tartu kuine müügitulu (koos eesmärgijoonega)",
    template="plotly_white",
)

fig_line.update_traces(line=dict(color="#A88CAA", width=4))

# Viitejoon (Target line)
fig_line.add_hline(
    y=45000,
    line_dash="dash",
    line_color="#6C587D",
    annotation_text="Kuumüügi eesmärk (€45k)",
    annotation_position="bottom right",
)

# Annotatsioon (Selgitav märkus mõne madalpunkti kohta)
if not df_monthly.empty:
    min_row = df_monthly.loc[df_monthly["total_price"].idxmin()]
    fig_line.add_annotation(
        x=min_row["sale_date"],
        y=min_row["total_price"],
        text="Madalaim müügikuu (vajab auditit)",
        showarrow=True,
        arrowhead=2,
        arrowcolor="#6C587D",
        ax=0,
        ay=-40,
    )

max_row = df_monthly.loc[df_monthly["total_price"].idxmax()]
fig_line.add_annotation(
x=max_row["sale_date"],
y=max_row["total_price"],
text="Kõrgeim müügikuu",
showarrow=True,
arrowhead=2,
arrowcolor="#6C587D",
ax=0,
ay=-40,
)
    
fig_line.update_layout(
    height=400,
    font=dict(size=14),
    xaxis_title=None,
    yaxis_title="Müügitulu (€)",
    title_font=dict(size=20),
)

fig_line.update_yaxes

# ---------------------------------------------------------
# 6. DIAGRAMM 2: TOP 5 TOOTED TARTUS
# ---------------------------------------------------------
 
fig_products = px.bar(
    top_products,
    x="total_price",
    y="product_name",
    orientation="h",
    title="TOP 5 toodet Tartus",
    template="plotly_white",
)

fig_products.update_traces(marker_color="#A88CAA")
fig_products.update_xaxes(tickformat=".0s")
# ---------------------------------------------------------
# 7. TEINE DIAGRAMM - MAKSEVIISID
# ---------------------------------------------------------

payment_counts = (
    df_tartu["payment_method"]
    .value_counts()
    .reset_index()
)

payment_counts.columns = ["Makseviis", "Tehingud"]

fig_payment = px.bar(
    payment_counts,
    x="Makseviis",
    y="Tehingud",
    title="Makseviiside jaotus Tartus",
    template="plotly_white",
)

fig_payment.update_traces(marker_color="#A88CAA")

# ---------------------------------------------------------
# 8. GRAAFIKUTE KUVAMINE
# ---------------------------------------------------------

st.plotly_chart(fig_line, use_container_width=True)

st.plotly_chart(fig_payment, use_container_width=True)

st.plotly_chart(fig_products, use_container_width=True)
