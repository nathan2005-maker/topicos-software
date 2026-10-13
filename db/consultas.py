from db.dbcontext import get_conexao
from db.pacientes import Paciente


# Recebe um objeto da classe Paciente e grava na tabela
def insert(paciente: Paciente):
    with get_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO pacientes (
                gender,
                age,
                hypertension,
                heart_disease,
                ever_married,
                work_type,
                residence_type,
                avg_glucose_level,
                bmi,
                smoking_status,
                stroke
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            paciente.genero,
            paciente.idade,
            paciente.hiper,
            paciente.dcardiaca,
            paciente.estado_civil,
            paciente.tipo_job,
            paciente.residencia,
            paciente.glicose,
            paciente.imc,
            paciente.tabagismo,
            paciente.reg_avc,
        ))
        conexao.commit()


# Apaga todos os registros e zera o contador do AUTOINCREMENT,
# para que cada execução do main.py comece com a tabela vazia
def limpar_tabela():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM pacientes;")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'pacientes';")
        conexao.commit()


def ccount_paciente():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes;")
        return cursor.fetchone()[0]


def ccount_avc():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes WHERE stroke = 1;")
        return cursor.fetchone()[0]


# Glicose média e total de pacientes por grupo de AVC (0 = sem AVC; 1 = com AVC)
# JUSTIFICATIVA: Comparar a glicose média de quem teve e de quem não teve AVC
# ajuda a verificar se níveis mais altos de glicose aparecem associados ao registro de AVC.
def level_glicose():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT stroke,
                   COUNT(*) AS total,
                   ROUND(AVG(avg_glucose_level), 2) AS glicose_media
            FROM pacientes
            GROUP BY stroke
            ORDER BY stroke
        """)
        return cursor.fetchall()