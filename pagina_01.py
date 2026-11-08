import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Laboratório de Forragicultura e Pastagens",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização para o tema Agrárias
st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #1E5631; text-align: center; margin-bottom: 10px; }
    .subtitle { font-size: 22px; color: #4F7942; text-align: center; margin-bottom: 40px; }
    .section-title { font-size: 28px; font-weight: bold; color: #1E5631; border-bottom: 3px solid #1E5631; padding-bottom: 8px; margin-top: 40px; margin-bottom: 30px; }
    .plant-title { font-size: 26px; font-weight: bold; color: #2E6F40; margin-top: 0px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# 2. Cabeçalho Principal
st.markdown('<div class="main-title">Laboratório de Forragicultura e Pastagens</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Pesquisa e Desenvolvimento em Sistemas Integrados e Sustentáveis</div>', unsafe_allow_html=True)

st.info("🔬 **Foco da Pesquisa Atual:** Avaliação da dinâmica de pastagens consorciadas, fixação biológica de nitrogênio e aporte de biomassa no sistema integrado.")

# 3. Seção dos Componentes com Imagens Médias Lado a Lado com o Texto
st.markdown('<div class="section-title">Componentes do Sistema de Integração</div>', unsafe_allow_html=True)

# --- PLANTA 1: BRACHIARIA GUATÃ ---
# Criando duas colunas: a primeira ocupa 1 parte e a segunda ocupa 2 partes do espaço
col1_img, col1_txt = st.columns([1, 2])

with col1_img:
    st.image("https://unsplash.com", 
             caption="Área de pastagem de Brachiaria", 
             use_container_width=True)

with col1_txt:
    st.markdown('<div class="plant-title">🌾 Brachiaria cv. Guatã (Brachiaria brizantha)</div>', unsafe_allow_html=True)
    st.markdown("""
    ### **Manejo, Potencial Produtivo e Características**
    A cultivar **Guatã** destaca-se no cenário da pecuária intensiva e de sistemas integrados devido ao seu excelente vigor inicial e alta capacidade de perfilhamento. É uma opção robusta para produtores que buscam otimizar a transição de recria e engorda.

    * **Produção de Biomassa:** Apresenta elevado acúmulo de matéria seca ao longo do ano, servindo como base energética volumosa essencial para o rebanho.
    * **Sistema Radicular:** Suas raízes agressivas desempenham um papel crucial na estruturação física do solo, abrindo caminhos microscópicos e aumentando a infiltração de água.
    * **Palhada para Plantio Direto:** Após o manejo ou dessecação, sua biomassa aérea remanescente gera uma excelente camada de palhada, protegendo o solo contra erosões e mantendo a umidade.
    """)

st.markdown("<br><hr><br>", unsafe_allow_html=True) # Espaçamento e linha divisória

# --- PLANTA 2: OUTRAS BRACHIARIAS ---
col2_img, col2_txt = st.columns([1, 2])

with col2_img:
    st.image("https://unsplash.com", 
             caption="Avaliação de cultivares no campo", 
             use_container_width=True)

with col2_txt:
    st.markdown('<div class="plant-title">🌿 Dinâmica de Outras Cultivares de Brachiaria (Urochloa spp.)</div>', unsafe_allow_html=True)
    st.markdown("""
    ### **Avaliação Comparativa no Sub-bosque e Consórcio**
    O laboratório estuda a plasticidade de diferentes cultivares do gênero *Urochloa* (como *B. ruziziensis* ou *B. decumbens*) para entender como elas se comportam quando submetidas a condições de competição por luz e nutrientes no sistema integrado.

    * **Tolerância ao Sombreamento:** Identificação de cultivares que mantêm o valor nutritivo e a taxa de alongamento foliar mesmo sob a interferência de plantas de porte arbustivo ou árvores.
    * **Resistência a Pragas:** Monitoramento rigoroso da incidência de cigarrinha-das-pastagens e a capacidade de recuperação de cada variedade.
    * **Estacionalidade de Produção:** Análise detalhada do comportamento de rebrota no período de transição águas-seca, garantindo que o pasto não degrade nos meses críticos do ano.
    """)

st.markdown("<br><hr><br>", unsafe_allow_html=True) # Espaçamento e linha divisória

# --- PLANTA 3: FEIJÃO-GUANDU ---
col3_img, col3_txt = st.columns([1, 2])

with col3_img:
    st.image("https://unsplash.com", 
             caption="Cultivo de Feijão-Guandu", 
             use_container_width=True)

with col3_txt:
    st.markdown('<div class="plant-title">🫘 Feijão-Guandu (Cajanus cajan)</div>', unsafe_allow_html=True)
    st.markdown("""
    ### **O Motor Biológico da Integração Sustentável**
    O **Feijão-guandu** é uma leguminosa arbustiva perene indispensável em rotações e consórcios devido ao seu triplo propósito: recuperação de solo, adubação verde e suplementação proteica animal.

    * **Fixação Biológica de Nitrogênio (FBN):** Através da simbiose com bactérias do gênero *Rhizobium*, o guandu transforma o nitrogênio do ar em nutrientes assimiláveis no solo. Isso reduz diretamente a dependência de fertilizantes nitrogenados químicos sintéticos.
    * **Descompactação Profunda de Solo:** Possui uma raiz pivotante extremamente agressiva que consegue romper camadas adensadas e compactadas do subsolo que as gramíneas comuns não alcançam.
    * **Banco de Proteína na Seca:** Suas folhas e vagens permanecem verdes e ricas em proteína bruta (18% a 22%) mesmo durante longas estiagens, servindo como um "salvador" nutricional para o gado quando as brachiarias perdem a qualidade.
    """)

# 4. Benefícios Gerais Expandidos
st.markdown('<div class="section-title">📊 Por que a Integração Funciona?</div>', unsafe_allow_html=True)
st.markdown("""
1. **Ciclagem Eficiente de Nutrientes:** O Feijão-guandu busca nutrientes em camadas profundas do solo e os deposita na superfície através da queda de suas folhas. A Brachiaria aproveita esse aporte para crescer com maior vigor.
2. **Equilíbrio da Dieta Animal (Energia + Proteína):** Enquanto as Brachiarias fornecem a fibra estrutural e carboidratos (energia), o Guandu fornece os aminoácidos (proteína), otimizando o ambiente ruminal do gado.
3. **Sustentabilidade Econômica:** Menos gastos com adubo químico nitrogenado e menor necessidade de comprar rações concentradas proteicas no período da seca.
""")

# Rodapé
st.markdown("---")
st.caption("© 2026 Laboratório de Forragicultura - Conteúdo Informativo Técnico.")
