# Script simples para validar execucao Python no contexto de MLOps
import datetime

def validar_integracao():
    usuario = "Thiago Felix"
    data_atual = datetime.datetime.now()
    
    print(f"Ola, {usuario}!")
    print(f"Integracao Python com SAS Viya validada em: {data_atual}")
    print("Pronto para o desenvolvimento de modelos no Model Manager.")

if __name__ == "__main__":
    validar_integracao()