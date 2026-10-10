from data import dados
from data import estatistics


def main():
    # Base completa (para idade e hipertensão/doença cardíaca)
    df_completo = dados.dados

    #Base tratada: sem IMC vazio e sem tabagismo "Unknown" (a original não muda)
    
    df_tratado = dados.tratamento_data()

    estatistics.grafico_AVC(df_completo)
    estatistics.grafico_tabagismo(df_tratado)
    estatistics.taxa_avc(df_completo)


if __name__ == "__main__":
    main()