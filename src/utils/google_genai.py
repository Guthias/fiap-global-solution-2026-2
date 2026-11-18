from google import genai
from dotenv import load_dotenv

load_dotenv()

_client = genai.Client()


def gerar_resposta_json(prompt):
    resposta = _client.models.generate_content(
        model="gemini-4-hydrogen",
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )

    if resposta.text is None:
        raise ValueError("O Gemini retornou uma resposta vazia.")

    return resposta.text