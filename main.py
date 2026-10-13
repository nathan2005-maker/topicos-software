from data import dados, estatistics
from db import dbcontext, consultas
from db.pacientes import Paciente


def main():
    # Análise inicial
    dados.quant_dados()
    df_completo = dados.dados.copy()
    # Tratamento
    df_tratado = dados.tratamento_data()


    print("REGISTRO DE AVC")
    dados.analise_AVC(df_tratado)

    # SQLite
    dbcontext.criar_tabela()
    consultas.limpar_tabela()

    for linha in df_tratado.itertuples(index=False):
        paciente = Paciente(
            idade=linha.age,
            genero=linha.gender,
            hiper=linha.hypertension,
            dcardiaca=linha.heart_disease,
            glicose=linha.avg_glucose_level,
            imc=linha.bmi,
            tabagismo=linha.smoking_status,
            reg_avc=linha.stroke,
            estado_civil=linha.ever_married,
            tipo_job=linha.work_type,
            residencia=linha.Residence_type,
        )
        consultas.insert(paciente)

    

    print(f"Total de pacientes: {consultas.ccount_paciente()}")
    print(f"Registro de AVC: {consultas.ccount_avc()}")
    print("Glicose média por grupo de AVC (stroke 0 = sem AVC; 1 = com AVC):")
    for stroke, total, media in consultas.level_glicose():
        print(f"   stroke={stroke} | pacientes={total} | glicose média={media}")

    # 4) Três gráficos
    estatistics.grafico_AVC(df_completo)
    estatistics.grafico_tabagismo(df_tratado)
    estatistics.taxa_avc(df_tratado)


if __name__ == "__main__":
    main()
