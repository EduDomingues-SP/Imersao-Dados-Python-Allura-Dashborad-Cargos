import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Personalizado para Design Moderno ---
st.markdown("""
<style>
    /* Importar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Variáveis CSS para tema escuro moderno */
    :root {
        --primary-color: #6366f1;
        --secondary-color: #8b5cf6;
        --accent-color: #06b6d4;
        --success-color: #10b981;
        --warning-color: #f59e0b;
        --error-color: #ef4444;
        --background-dark: #0f172a;
        --surface-dark: #1e293b;
        --surface-light: #334155;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --border-color: #475569;
    }
    
    /* Reset e configurações globais */
    .main {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: var(--text-primary);
    }
    
    /* Header personalizado */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.2);
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-subtitle {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.9);
        font-weight: 400;
    }
    
    /* Cards de métricas modernos */
    .metric-card {
        background: var(--surface-dark);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        border-color: var(--primary-color);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Sidebar personalizada */
    .css-1d391kg {
        background: var(--surface-dark);
        border-right: 1px solid var(--border-color);
    }
    
    .sidebar-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Multiselect personalizado */
    .stMultiSelect [data-baseweb="tag"] {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 500 !important;
    }
    
    /* Botões personalizados */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    /* Gráficos com bordas arredondadas */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Seções com espaçamento melhorado */
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        border: none;
        border-radius: 1px;
        margin: 2rem 0;
    }
    
    /* Tabela personalizada */
    .dataframe {
        background: var(--surface-dark) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    
    /* Indicadores de status */
    .status-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-success { background-color: var(--success-color); }
    .status-warning { background-color: var(--warning-color); }
    .status-error { background-color: var(--error-color); }
    
    /* Animações suaves */
    * {
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- Carregamento dos dados ---
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

df = load_data()

# --- Header Principal ---
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🚀 Dashboard Inteligente de Salários</h1>
    <p class="main-subtitle">Análise avançada de dados salariais na área de tecnologia e ciência de dados</p>
</div>
""", unsafe_allow_html=True)

# --- Barra Lateral Melhorada ---
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h3 style="color: white; margin: 0;">🔍 Filtros Inteligentes</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Filtros com melhor organização
    with st.expander("📅 Período de Análise", expanded=True):
        anos_disponiveis = sorted(df['ano'].unique())
        anos_selecionados = st.multiselect(
            "Selecione os anos:",
            anos_disponiveis,
            default=anos_disponiveis,
            key="anos"
        )
    
    with st.expander("👔 Nível Profissional", expanded=True):
        senioridades_disponiveis = sorted(df['senioridade'].unique())
        senioridades_selecionadas = st.multiselect(
            "Selecione as senioridades:",
            senioridades_disponiveis,
            default=senioridades_disponiveis,
            key="senioridades"
        )
    
    with st.expander("📋 Tipo de Contrato", expanded=True):
        contratos_disponiveis = sorted(df['contrato'].unique())
        contratos_selecionados = st.multiselect(
            "Selecione os contratos:",
            contratos_disponiveis,
            default=contratos_disponiveis,
            key="contratos"
        )
    
    with st.expander("🏢 Tamanho da Empresa", expanded=True):
        tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
        tamanhos_selecionados = st.multiselect(
            "Selecione os tamanhos:",
            tamanhos_disponiveis,
            default=tamanhos_disponiveis,
            key="tamanhos"
        )
    
    # Botão para limpar filtros
    if st.button("🔄 Limpar Todos os Filtros"):
        st.rerun()
    
    # Informações adicionais
    st.markdown("---")
    st.markdown("### 📊 Estatísticas dos Dados")
    st.info(f"**Total de registros:** {len(df):,}")
    st.info(f"**Período:** {df['ano'].min()} - {df['ano'].max()}")
    st.info(f"**Países:** {df['residencia'].nunique()}")

# --- Filtragem do DataFrame ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Verificação de dados ---
if df_filtrado.empty:
    st.error("⚠️ Nenhum dado encontrado com os filtros selecionados. Ajuste os filtros para visualizar os dados.")
    st.stop()

# --- Métricas Principais com Design Moderno ---
st.markdown("## 📈 Indicadores Principais")

# Cálculo das métricas
salario_medio = df_filtrado['usd'].mean()
salario_mediano = df_filtrado['usd'].median()
salario_maximo = df_filtrado['usd'].max()
salario_minimo = df_filtrado['usd'].min()
total_registros = df_filtrado.shape[0]
cargo_mais_frequente = df_filtrado["cargo"].mode()[0] if not df_filtrado.empty else "N/A"

# Cálculo de crescimento (comparação com ano anterior se disponível)
if len(anos_selecionados) > 1:
    ano_atual = max(anos_selecionados)
    ano_anterior = max([a for a in anos_selecionados if a < ano_atual]) if len([a for a in anos_selecionados if a < ano_atual]) > 0 else ano_atual
    
    salario_atual = df_filtrado[df_filtrado['ano'] == ano_atual]['usd'].mean()
    salario_anterior = df_filtrado[df_filtrado['ano'] == ano_anterior]['usd'].mean()
    
    if not pd.isna(salario_anterior) and salario_anterior > 0:
        crescimento = ((salario_atual - salario_anterior) / salario_anterior) * 100
    else:
        crescimento = 0
else:
    crescimento = 0

# Layout das métricas em 5 colunas
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${salario_medio:,.0f}</div>
        <div class="metric-label">💰 Salário Médio</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${salario_mediano:,.0f}</div>
        <div class="metric-label">📊 Salário Mediano</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">${salario_maximo:,.0f}</div>
        <div class="metric-label">🚀 Salário Máximo</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_registros:,}</div>
        <div class="metric-label">👥 Total de Registros</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    delta_color = "🟢" if crescimento >= 0 else "🔴"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{delta_color} {crescimento:+.1f}%</div>
        <div class="metric-label">📈 Crescimento Anual</div>
    </div>
    """, unsafe_allow_html=True)

# --- Divider ---
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- Análises Visuais Avançadas ---
st.markdown("## 📊 Análises Visuais Avançadas")

# Primeira linha de gráficos
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("### 🏆 Top 10 Cargos por Salário")
    top_cargos = df_filtrado.groupby('cargo')['usd'].agg(['mean', 'count']).reset_index()
    top_cargos = top_cargos[top_cargos['count'] >= 5]  # Filtrar cargos com pelo menos 5 registros
    top_cargos = top_cargos.nlargest(10, 'mean').sort_values('mean', ascending=True)
    
    if not top_cargos.empty:
        fig_cargos = px.bar(
            top_cargos,
            x='mean',
            y='cargo',
            orientation='h',
            color='mean',
            color_continuous_scale='viridis',
            title="",
            labels={'mean': 'Salário Médio (USD)', 'cargo': 'Cargo'}
        )
        fig_cargos.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_cargos, use_container_width=True)
    else:
        st.warning("Dados insuficientes para exibir o gráfico de cargos.")

with col_graf2:
    st.markdown("### 📈 Distribuição Salarial")
    fig_hist = px.histogram(
        df_filtrado,
        x='usd',
        nbins=25,
        color_discrete_sequence=['#6366f1'],
        title="",
        labels={'usd': 'Salário (USD)', 'count': 'Frequência'}
    )
    
    # Adicionar linha da média
    fig_hist.add_vline(
        x=salario_medio,
        line_dash="dash",
        line_color="#10b981",
        annotation_text=f"Média: ${salario_medio:,.0f}"
    )
    
    fig_hist.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Segunda linha de gráficos
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.markdown("### 🏠 Modalidades de Trabalho")
    remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
    
    # Mapear nomes mais descritivos
    tipo_map = {
        'remoto': '🏠 Remoto',
        'presencial': '🏢 Presencial',
        'hibrido': '🔄 Híbrido'
    }
    remoto_contagem['tipo_trabalho'] = remoto_contagem['tipo_trabalho'].map(tipo_map)
    
    fig_remoto = px.pie(
        remoto_contagem,
        names='tipo_trabalho',
        values='quantidade',
        color_discrete_sequence=['#6366f1', '#8b5cf6', '#06b6d4'],
        title="",
        hole=0.4
    )
    fig_remoto.update_traces(
        textinfo='percent+label',
        textfont_size=12
    )
    fig_remoto.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True,
        height=400
    )
    st.plotly_chart(fig_remoto, use_container_width=True)

with col_graf4:
    st.markdown("### 🌍 Salários por Senioridade e Ano")
    if len(anos_selecionados) > 1:
        salario_tempo = df_filtrado.groupby(['ano', 'senioridade'])['usd'].mean().reset_index()
        
        fig_tempo = px.line(
            salario_tempo,
            x='ano',
            y='usd',
            color='senioridade',
            markers=True,
            color_discrete_sequence=['#6366f1', '#8b5cf6', '#06b6d4', '#10b981'],
            title="",
            labels={'usd': 'Salário Médio (USD)', 'ano': 'Ano', 'senioridade': 'Senioridade'}
        )
        fig_tempo.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            height=400
        )
        st.plotly_chart(fig_tempo, use_container_width=True)
    else:
        # Gráfico alternativo quando há apenas um ano
        salario_senioridade = df_filtrado.groupby('senioridade')['usd'].mean().reset_index()
        fig_senior = px.bar(
            salario_senioridade,
            x='senioridade',
            y='usd',
            color='usd',
            color_continuous_scale='viridis',
            title="",
            labels={'usd': 'Salário Médio (USD)', 'senioridade': 'Senioridade'}
        )
        fig_senior.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_senior, use_container_width=True)

# --- Terceira linha: Mapa Mundial ---
st.markdown("### 🗺️ Distribuição Global de Salários")

# Filtrar apenas Data Scientists para o mapa (ou cargo mais comum se não houver)
cargo_para_mapa = 'Data Scientist' if 'Data Scientist' in df_filtrado['cargo'].values else cargo_mais_frequente
df_mapa = df_filtrado[df_filtrado['cargo'] == cargo_para_mapa]

if not df_mapa.empty:
    media_pais = df_mapa.groupby(['residencia_iso3', 'residencia'])['usd'].agg(['mean', 'count']).reset_index()
    media_pais.columns = ['iso3', 'pais', 'salario_medio', 'quantidade']
    
    fig_mapa = px.choropleth(
        media_pais,
        locations='iso3',
        color='salario_medio',
        hover_name='pais',
        hover_data={'quantidade': True, 'salario_medio': ':,.0f'},
        color_continuous_scale='viridis',
        title=f"Salário médio para {cargo_para_mapa}",
        labels={'salario_medio': 'Salário Médio (USD)'}
    )
    fig_mapa.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=500
    )
    st.plotly_chart(fig_mapa, use_container_width=True)
else:
    st.warning("Dados insuficientes para exibir o mapa mundial.")

# --- Divider ---
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- Análise Detalhada ---
st.markdown("## 🔍 Análise Detalhada")

# Tabs para organizar melhor o conteúdo
tab1, tab2, tab3 = st.tabs(["📋 Dados Completos", "📊 Estatísticas", "💡 Insights"])

with tab1:
    st.markdown("### Tabela de Dados Filtrados")
    
    # Adicionar opções de visualização
    col_opcoes1, col_opcoes2, col_opcoes3 = st.columns(3)
    
    with col_opcoes1:
        mostrar_linhas = st.selectbox("Linhas por página:", [10, 25, 50, 100], index=1)
    
    with col_opcoes2:
        ordenar_por = st.selectbox("Ordenar por:", ['usd', 'ano', 'cargo', 'senioridade'], index=0)
    
    with col_opcoes3:
        ordem_desc = st.checkbox("Ordem decrescente", value=True)
    
    # Aplicar ordenação
    df_exibir = df_filtrado.sort_values(ordenar_por, ascending=not ordem_desc).head(mostrar_linhas)
    
    # Formatação da tabela
    df_formatado = df_exibir.copy()
    df_formatado['usd'] = df_formatado['usd'].apply(lambda x: f"${x:,.0f}")
    
    st.dataframe(
        df_formatado,
        use_container_width=True,
        height=400
    )
    
    # Botão para download
    csv = df_filtrado.to_csv(index=False)
    st.download_button(
        label="📥 Baixar dados filtrados (CSV)",
        data=csv,
        file_name="dados_salarios_filtrados.csv",
        mime="text/csv"
    )

with tab2:
    st.markdown("### Estatísticas Descritivas")
    
    col_stat1, col_stat2 = st.columns(2)
    
    with col_stat1:
        st.markdown("#### 💰 Estatísticas Salariais")
        stats_salario = df_filtrado['usd'].describe()
        
        for stat, value in stats_salario.items():
            if stat in ['mean', 'std', 'min', '25%', '50%', '75%', 'max']:
                st.metric(
                    label=stat.title(),
                    value=f"${value:,.0f}"
                )
    
    with col_stat2:
        st.markdown("#### 📊 Distribuição por Categorias")
        
        st.markdown("**Por Senioridade:**")
        for senioridade in df_filtrado['senioridade'].value_counts().index:
            count = df_filtrado['senioridade'].value_counts()[senioridade]
            percentage = (count / len(df_filtrado)) * 100
            st.write(f"• {senioridade}: {count} ({percentage:.1f}%)")
        
        st.markdown("**Por Tipo de Contrato:**")
        for contrato in df_filtrado['contrato'].value_counts().index:
            count = df_filtrado['contrato'].value_counts()[contrato]
            percentage = (count / len(df_filtrado)) * 100
            st.write(f"• {contrato}: {count} ({percentage:.1f}%)")

with tab3:
    st.markdown("### 💡 Insights Automáticos")
    
    # Gerar insights baseados nos dados
    insights = []
    
    # Insight sobre salário médio
    if salario_medio > 100000:
        insights.append(f"💰 O salário médio de ${salario_medio:,.0f} está acima de $100k, indicando um mercado bem remunerado.")
    
    # Insight sobre crescimento
    if crescimento > 5:
        insights.append(f"📈 Houve um crescimento salarial de {crescimento:.1f}% em relação ao período anterior.")
    elif crescimento < -5:
        insights.append(f"📉 Houve uma redução salarial de {abs(crescimento):.1f}% em relação ao período anterior.")
    
    # Insight sobre modalidade de trabalho
    remoto_pct = (df_filtrado['remoto'] == 'remoto').sum() / len(df_filtrado) * 100
    if remoto_pct > 50:
        insights.append(f"🏠 {remoto_pct:.1f}% dos profissionais trabalham remotamente, mostrando a tendência do trabalho à distância.")
    
    # Insight sobre senioridade
    senior_pct = (df_filtrado['senioridade'] == 'senior').sum() / len(df_filtrado) * 100
    if senior_pct > 40:
        insights.append(f"👔 {senior_pct:.1f}% dos profissionais são seniores, indicando um mercado maduro.")
    
    # Insight sobre variação salarial
    coef_variacao = (df_filtrado['usd'].std() / df_filtrado['usd'].mean()) * 100
    if coef_variacao > 50:
        insights.append(f"📊 Alta variabilidade salarial (CV: {coef_variacao:.1f}%), indicando grande dispersão nos salários.")
    
    # Exibir insights
    if insights:
        for i, insight in enumerate(insights, 1):
            st.info(f"**Insight {i}:** {insight}")
    else:
        st.info("Nenhum insight específico identificado com os filtros atuais.")

# --- Footer ---
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
    <p>🚀 Dashboard desenvolvido com Streamlit e Plotly | 📊 Dados atualizados automaticamente</p>
    <p>💡 Use os filtros na barra lateral para explorar diferentes perspectivas dos dados</p>
            <p> Desenvolvido e adaptado por Eduardo Domingues -  Agosto de 2025 </p
</div>
""", unsafe_allow_html=True)

