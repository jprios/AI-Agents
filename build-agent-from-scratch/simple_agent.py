import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# === CALCULADORA ===
import operator

def basic_calculator(input_dict):
    try:
        num1 = float(input_dict['num1'])
        num2 = float(input_dict['num2'])
        operation = input_dict['operation'].lower()
    except (KeyError, ValueError):
        return "Erro: Entrada inválida. Use os campos 'num1', 'num2' e 'operation'."

    operations = {
        'add': operator.add,
        'plus': operator.add,
        'subtract': operator.sub,
        'minus': operator.sub,
        'multiply': operator.mul,
        'times': operator.mul,
        'divide': operator.truediv,
    }

    if operation not in operations:
        return f"Operação não suportada: '{operation}'"

    try:
        result = operations[operation](num1, num2)
        return f"O resultado é: {result}"
    except ZeroDivisionError:
        return "Erro: Divisão por zero."
    except Exception as e:
        return f"Erro ao calcular: {str(e)}"

# === MODELO OLLAMA ===
class OllamaModel:
    def __init__(self, model="llama2", temperature=0):
        self.model = model
        self.temperature = temperature
        self.endpoint = "http://localhost:11434/api/generate"
        self.headers = {"Content-Type": "application/json"}

    def ask(self, prompt):
        system_prompt = """
Você é uma IA que deve responder apenas com um JSON contendo os campos:
{
  "tool_choice": "basic_calculator",
  "tool_input": {
    "num1": número,
    "num2": número,
    "operation": "add|subtract|multiply|divide"
  }
}
Entenda a pergunta e extraia esses dados corretamente.
"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system_prompt,
            "format": "json",
            "temperature": self.temperature,
            "stream": False
        }

        try:
            res = requests.post(self.endpoint, headers=self.headers, data=json.dumps(payload))
            print("STATUS:", res.status_code)
            print("RAW RESPONSE:", res.text)

            if res.status_code != 200:
                return None

            res_json = res.json()
            if 'response' not in res_json:
                return None

            return json.loads(res_json['response'])
        except Exception as e:
            print("Erro ao chamar o modelo:", e)
            return None

# === AGENTE SIMPLES ===
if __name__ == "__main__":
    model = OllamaModel(model="llama2")
    print("\n=== Bem-vindo à Calculadora IA ===\nDigite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Pergunta: ")
        if pergunta.lower() == "sair":
            break

        resposta = model.ask(pergunta)

        if not resposta:
            print("Erro: resposta inválida do modelo.")
            continue

        if resposta.get("tool_choice") != "basic_calculator":
            print("Erro: ferramenta inesperada.")
            continue

        resultado = basic_calculator(resposta["tool_input"])
        print(resultado)
