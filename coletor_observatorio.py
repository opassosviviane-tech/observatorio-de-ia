import os
import json
import time
from datetime import datetime
from google import genai
from google.genai import types

# Lê a chave diretamente do sistema operacional/variável de ambiente
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("A chave de API não foi encontrada! Defina a variável de ambiente GEMINI_API_KEY.")

client = genai.Client(api_key=API_KEY)

system_instruction = """
Você é o assistente de inteligência e curador especializado do Observatório de IA e Educação.
Sua missão é realizar buscas atualizadas na web e consolidar informações sobre as maiores e mais influentes conferências de educação do mundo e do Brasil para 2027.

Estrutura EXIGIDA para a chave de eventos no JSON:
- Separe os eventos em duas listas principais: "eventos_brasil_2027" e "eventos_mundo_2027".
- Mapeie APENAS os principais eventos considerados imperdíveis para quem estuda e desenvolve inovação e IA na educação.
- Caso a data exata de 2027 ainda não esteja confirmada, informe "Data a definir (2027)" ou o mês provável.
- Para cada evento, inclua: nome, data, local, foco_inovacao, público_alvo e link_oficial (obtido via Google Search Grounding).

Retorne a resposta EXCLUSIVAMENTE em formato JSON estruturado.
"""

user_prompt = """
Realize uma busca abrangente e traga os eventos imperdíveis de inovação e tecnologia na educação previstos para 2027 no Brasil e no mundo.
Gere o relatório estruturado em JSON com as chaves "eventos_brasil_2027" e "eventos_mundo_2027", além das demais seções do Observatório.
"""

print("🔍 A iniciar a pesquisa de eventos e tendências do Observatório de IA e Educação...")

try:
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[{"google_search": {}}],
            response_mime_type="application/json",
            temperature=0.2,
        ),
    )

    data_atual = datetime.now().strftime("%Y-%m-%d")
    nome_ficheiro = f"observatorio_{data_atual}.json"

    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Relatório guardado com sucesso no ficheiro: {nome_ficheiro}")

except Exception as e:
    print(f"\n⚠️ Ocorreu um erro ao consultar a API: {e}")