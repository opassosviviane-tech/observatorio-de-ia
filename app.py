import streamlit as st
import json
import os

st.set_page_config(page_title="Observatório de IA e Educação", page_icon="🎓", layout="wide")

st.title("🎓 Observatório de IA e Educação")
st.caption("Painel interativo de curadoria sobre inovação, EdTechs, casos de sucesso, grandes eventos de 2027 e portais de notícias.")

arquivo_json = "observatorio_2026-10-19.json"

if os.path.exists(arquivo_json):
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    st.success(f"📅 Dados da recolha semanal de: **{dados.get('data_coleta', '2026-10-19')}**")

    # Estrutura com a nova aba de Portais de Notícias dividida em 3 colunas
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🇧🇷 Eventos 2027 (Brasil)",
        "🌐 Eventos 2027 (Mundo)",
        "📰 Portais de Notícias",
        "🌍 Países Referência", 
        "🚀 EdTechs", 
        "🏆 Casos de Sucesso", 
        "📚 Referências Institucionais"
    ])

    todos_eventos = dados.get("eventos", [])

    # 1. Eventos 2027 no Brasil
    with tab1:
        st.header("🇧🇷 Principais Eventos de Educação em 2027 no Brasil")
        st.info("Conferências imperdíveis para acompanhar o desenvolvimento de inovação e IA na educação nacional.")
        eventos_br = [ev for ev in todos_eventos if ev.get("abrangencia") == "Brasil"] or dados.get("eventos_brasil_2027", [])
        for ev in eventos_br:
            st.subheader(f"📍 {ev.get('nome')}")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"🗓️ **Data:** {ev.get('data', 'A confirmar')}")
                st.write(f"🏢 **Local:** {ev.get('local', 'A definir')}")
            with col2:
                st.write(f"🎯 **Foco e Relevância:** {ev.get('foco', '')}")
                if ev.get("link_oficial") or ev.get("link"):
                    st.markdown(f"🔗 [Acessar site oficial]({ev.get('link_oficial') or ev.get('link')})")
            st.divider()

    # 2. Eventos 2027 no Mundo
    with tab2:
        st.header("🌐 Principais Eventos Globais de Educação em 2027")
        st.info("Grandes encontros mundiais de referência onde as tendências internacionais de tecnologia e IA educacional são lançadas.")
        eventos_mundo = [ev for ev in todos_eventos if ev.get("abrangencia") == "Mundo"] or dados.get("eventos_mundo_2027", [])
        for ev in eventos_mundo:
            st.subheader(f"🌍 {ev.get('nome')}")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.write(f"🗓️ **Data:** {ev.get('data', 'A confirmar')}")
                st.write(f"🏢 **Local:** {ev.get('local', 'A definir')}")
            with col2:
                st.write(f"🎯 **Foco e Relevância:** {ev.get('foco', '')}")
                if ev.get("link_oficial") or ev.get("link"):
                    st.markdown(f"🔗 [Acessar site oficial]({ev.get('link_oficial') or ev.get('link')})")
            st.divider()

    # 3. ABA: Portais de Notícias (Brasil, Globais/Multicontinentais e Norte-Americanos)
    with tab3:
        st.header("📰 Principais Portais de Notícias e Periódicos de Inovação em Educação")
        
        col_br, col_glob, col_us = st.columns(3)

        with col_br:
            st.subheader("🇧🇷 Brasil")
            st.markdown("---")
            st.markdown("### 1. [Porvir](https://porvir.org)")
            st.write("Inovações educacionais, metodologias ativas e IA em sala de aula no Brasil.")
            
            st.markdown("### 2. [Nova Escola](https://novaescola.org.br)")
            st.write("Referência prática para professores e gestores sobre tecnologia e apoio pedagógico.")
            
            st.markdown("### 3. [Desafios da Educação](https://desafiosdaeducacao.com.br)")
            st.write("Portal sobre tendências do ensino básico e superior, EdTechs e cultura maker.")
            
            st.markdown("### 4. [RBAAD / ABED](https://www.abed.org.br/revista/algetec)")
            st.write("Periódico da Associação Brasileira de EAD sobre tecnologia educacional e IA.")
            
            st.markdown("### 5. [CIEB - Notícias](https://cieb.net.br)")
            st.write("Notas técnicas, pesquisas e políticas públicas de inovação na educação pública.")

        with col_glob:
            st.subheader("🌐 Globais & Multicontinentais")
            st.markdown("---")
            st.markdown("### 1. [OECD EduToday](https://oecdedutoday.com)")
            st.write("Análises e dados da OCDE sobre políticas de IA na Europa, Ásia, Américas e Oceania.")
            
            st.markdown("### 2. [World Bank Edu](https://blogs.worldbank.org/education)")
            st.write("Transformação digital e EdTechs no Sul Global (África, América Latina e Ásia).")
            
            st.markdown("### 3. [Asian Dev Bank](https://www.adb.org/sectors/education/main)")
            st.write("Vanguarda de IA na Ásia-Pacífico (Coreia do Sul, Cingapura, Japão e Índia).")
            
            st.markdown("### 4. [EdTech Hub](https://edtechhub.org)")
            st.write("Uso de IA e tecnologias em economias emergentes e na África Subsaariana.")
            
            st.markdown("### 5. [UNESCO Digital](https://www.unesco.org/en/digital-education)")
            st.write("Portal multilateral de ética, diretrizes e políticas globais de IA em 194 países.")

        with col_us:
            st.subheader("🌎 EUA & Ecossistema")
            st.markdown("---")
            st.markdown("### 1. [EdSurge](https://www.edsurge.com)")
            st.write("Jornalismo internacional cobrindo produtos, IA e mercado educacional.")
            
            st.markdown("### 2. [eSchool News](https://www.eschoolnews.com)")
            st.write("Liderança escolar, transformação digital e ferramentas de IA para K-12 e Higher Ed.")
            
            st.markdown("### 3. [THE Campus](https://www.timeshighereducation.com/campus)")
            st.write("Inovação, pedagogia digital e IA no ensino superior global.")
            
            st.markdown("### 4. [Educause Review](https://er.educause.edu)")
            st.write("Tendências tecnológicas anuais (Horizon Report) e governança de IA.")
            
            st.markdown("### 5. [ISTE Blog](https://www.iste.org/explore)")
            st.write("Padrões de tecnologia educacional e práticas de letramento em IA.")

    # Outras abas mantidas
    with tab4:
        st.header("Países Referência em Inovação e Tecnologia")
        for p in dados.get("paises_referencia", []):
            with st.expander(f"📍 {p.get('pais')} ({p.get('tipo')})"):
                st.write(p.get("descricao"))

    with tab5:
        st.header("EdTechs em Destaque")
        for e in dados.get("edtechs", []):
            st.subheader(f"🏢 {e.get('nome')} ({e.get('regiao')})")
            st.write(f"**Foco:** {e.get('foco')}")
            st.write(f"**Destaque Recente:** {e.get('destaque_recente')}")
            if e.get("site"):
                st.markdown(f"🔗 [Acessar site oficial]({e.get('site')})")
            st.divider()

    with tab6:
        st.header("Casos de Sucesso")
        for c in dados.get("casos_de_sucesso", []):
            st.subheader(f"⭐ {c.get('titulo')} ({c.get('escopo')})")
            st.write(f"**Instituição Responsável:** {c.get('instituicao_responsavel')}")
            st.write(c.get("resumo"))
            if c.get("link"):
                st.markdown(f"🔗 [Mais informações]({c.get('link')})")
            st.divider()

    with tab7:
        st.header("Referências Institucionais")
        for r in dados.get("portais_e_referencias", []):
            st.markdown(f"🔹 **{r.get('nome')}** — *{r.get('tipo')}*")
            st.write(r.get("descricao"))
            if r.get("link"):
                st.markdown(f"🔗 [{r.get('link')}]({r.get('link')})")
            st.divider()
else:
    st.error(f"Arquivo `{arquivo_json}` não encontrado na pasta!")