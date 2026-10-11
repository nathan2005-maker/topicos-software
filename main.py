from data import dados
from data import estatistics
from db import dbcontext, consultas
from db.pacientes import Paciente


def main():
    df_completo = dados.dados
    df_tratado = dados.tratamento_data()

    # Cria a tabela e grava os dados tratados no SQLite
    dbcontext.criar_tabela()
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

    print(f"Pacientes no banco: {consultas.ccount_paciente()}")
    print(f"Pacientes com AVC: {consultas.ccount_avc()}")

    estatistics.grafico_AVC(df_completo)
    estatistics.grafico_tabagismo(df_tratado)
    estatistics.taxa_avc(df_completo)


if __name__ == "__main__":
    main()