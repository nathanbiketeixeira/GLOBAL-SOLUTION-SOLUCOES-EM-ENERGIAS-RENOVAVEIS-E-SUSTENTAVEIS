import pandas as pd

# -----------------------------------------
# PARÂMETROS DA SIMULAÇÃO
# -----------------------------------------

irradiacao_media = 4.8   # kWh/m²/dia
dias_mes = 30
capacidade_kWp = 30      # tamanho do sistema fotovoltaico
eficiencia = 0.78        # perdas do sistema
tarifa = 0.85            # R$/kWh
fator_emissao = 0.084    # tCO2/MWh (média Brasil)

# -----------------------------------------
# IMPORTAÇÃO DOS DADOS
# -----------------------------------------

df = pd.read_csv("data/consumo_mensal.csv")

# -----------------------------------------
# CÁLCULO DA GERAÇÃO MENSAL
# -----------------------------------------

df["Geracao (kWh)"] = capacidade_kWp * irradiacao_media * dias_mes * eficiencia
df["Economia (R$)"] = df["Geracao (kWh)"] * tarifa
df["Reducao_CO2 (t)"] = (df["Geracao (kWh)"] / 1000) * fator_emissao
df["% Renovavel"] = (df["Geracao (kWh)"] / df["Consumo (kWh)"]) * 100

# -----------------------------------------
# RESUMO FINAL
# -----------------------------------------

resumo = {
    "Geração anual (kWh)": df["Geracao (kWh)"].sum(),
    "Consumo anual (kWh)": df["Consumo (kWh)"].sum(),
    "Economia anual (R$)": df["Economia (R$)"].sum(),
    "Redução total CO2 (t)": df["Reducao_CO2 (t)"].sum(),
    "Percentual renovável (%)": (df["Geracao (kWh)"].sum() / df["Consumo (kWh)"].sum()) * 100
}

print("\n--- RESULTADOS DA SIMULAÇÃO ---")
for chave, valor in resumo.items():
    print(f"{chave}: {valor:.2f}")

