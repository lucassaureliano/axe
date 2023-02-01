import json
from datetime import datetime
from pytz import timezone
fusoHorario = timezone("America/Sao_Paulo")
# diferenca = timedelta(hours=-3)
# fusoHorario = timezone(diferenca)

with open('a11y.json', 'r') as f:
    data = json.load(f)

dt_string = data["timestamp"]
dt_format = "%Y-%m-%dT%H:%M:%S.%fZ"
dt = datetime.strptime(dt_string, dt_format)
data_teste = dt.strftime("%d/%m/%Y")

# acessar as colunas "incomplete" e "violations"
violations = data["violations"]
incomplete = data["incomplete"]
numViolations = str(len(violations))
numIncomplete = str(len(incomplete))

# obter as chaves (colunas) do dicionário
# columns = incomplete[0].keys()

# imprimir as chaves (colunas)

totalErros = 0
# Início do relatório
print("Site analisado: "+data["url"]+"\nData do teste: "+data_teste+"\n")
print(numIncomplete, "verificações manuais")
for verify in incomplete:
    print("\nDescrição:", verify["description"])
    print("Ajuda:", verify["help"])
    print("Criticidade:", verify["impact"])
    nodes = verify['nodes']
    numErros = 0
    for node in nodes:
        numErros = numErros+1
        any = node["any"]
        for item in any:
            print(item["message"])
            print(node["html"])
    print(numErros,"erros")
    totalErros = totalErros+numErros

print("\n"+numViolations+"Violações encontradas")
for violation in violations:
    print("\nDescrição:", violation["description"])
    print("Ajuda:", violation["help"])
    print("Criticidade:", violation["impact"])
    nodes = violation['nodes']
    numErros = 0
    for node in nodes:
        numErros = numErros+1
        any = node["any"]
        for item in any:
            print(item["message"])
            print(node["html"])
    print(numErros,"erros")
    totalErros = totalErros+numErros
print("\nExistem",totalErros,"erros a serem corrigidos")