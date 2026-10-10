import pandas as pd
import numpy as np
import sys

sys.stdout.reconfigure(encoding="utf-8")

#Carregar arquivo
dados = pd.read_csv("arquivo.csv", sep=",")


def quant_dados():
    df = dados

    print(f"Quantidade Total Registros: {len(df)}")
    for coluna in df.columns:
        print(f"\nColuna: {coluna}")
        print(f"Tipo: {df[coluna].dtype}")
        print(f"Valores Distintos: {df[coluna].nunique()}")
        print(f"Valores NULL: {df[coluna].isnull().sum()}")

        if df[coluna].dtype in ["int64", "float64"]:
            print(f"Maior valor: {df[coluna].max()}")
            print(f"Menor valor: {df[coluna].min()}\n\n\n")


def tratamento_data():
    
    df = dados

    print(f"Total de registros Antes: {len(df)}")
    print(f"IMC Nulos Antes: {df['bmi'].isnull().sum()}")
    print(f"Tabagismo Unknown Antes: {(df['smoking_status'] == 'Unknown').sum()}")
    print(f"AVC Antes: {(df['stroke'] == 1).sum()}")

    # Remove linhas com IMC vazio
    df = df.dropna(subset=['bmi'])

    # Remove linhas com tabagismo desconhecido
    df = df[df['smoking_status'] != 'Unknown']

    df = df.reset_index(drop=True)

    print(f"\nIMC Nulos Depois: {df['bmi'].isnull().sum()}")
    print(f"Tabagismo Unknown Depois: {(df['smoking_status'] == 'Unknown').sum()}")
    print(f"AVC Depois: {(df['stroke'] == 1).sum()}")
    print(f"Total de registros Depois: {len(df)}")
    print(f"Linhas removidas: {len(dados) - len(df)}\n")

    return df


def analise_AVC():
    df = dados

    #Groupby
    masculino = df[df["gender"] == "Male"]
    feminino = df[df["gender"] == "Female"]
    outros = df[df["gender"] == "Other"]

    # Idade
    print("\nIdade média:")
    print(f"Idade média Masculino: {masculino.groupby('stroke')['age'].mean()}")
    print(f"Idade média Feminino: {feminino.groupby('stroke')['age'].mean()}")
    print(f"Idade média Outros: {outros.groupby('stroke')['age'].mean()}")

    # Glicose
    print("\nGlicose média:")
    print(f"Glicose média Masculino: {masculino.groupby('stroke')['avg_glucose_level'].mean()}")
    print(f"Glicose média Feminino: {feminino.groupby('stroke')['avg_glucose_level'].mean()}")
    print(f"Glicose média Outros: {outros.groupby('stroke')['avg_glucose_level'].mean()}")

    # IMC
    print("\nIMC médio:")
    print(f"IMC média Masculino: {masculino.groupby('stroke')['bmi'].mean()}")
    print(f"IMC média Feminino: {feminino.groupby('stroke')['bmi'].mean()}")
    print(f"IMC média Outros: {outros.groupby('stroke')['bmi'].mean()}")

    # Hipertensão
    print("\nHipertensão:")
    print(f"Hipertensão Masculino: {masculino.groupby('stroke')['hypertension'].sum()}")
    print(f"Hipertensão Feminino: {feminino.groupby('stroke')['hypertension'].sum()}")
    print(f"Hipertensão Outros: {outros.groupby('stroke')['hypertension'].sum()}")

    # Doença cardíaca
    print("\nDoença cardíaca:")
    print(f"Doença cardíaca Masculino: {masculino.groupby('stroke')['heart_disease'].sum()}")
    print(f"Doença cardíaca Feminino: {feminino.groupby('stroke')['heart_disease'].sum()}")
    print(f"Doença cardíaca Outros: {outros.groupby('stroke')['heart_disease'].sum()}")

    # Tabagismo
    print("\nTabagismo:")
    print(f"Tabagismo Masculino: {masculino.groupby(['stroke', 'smoking_status']).size()}")
    print(f"Tabagismo Feminino: {feminino.groupby(['stroke', 'smoking_status']).size()}")
    print(f"Tabagismo Outros: {outros.groupby(['stroke', 'smoking_status']).size()}")