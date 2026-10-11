import sqlite3
from db.dbcontext import get_conexao
from db.pacientes import Paciente

# Variavel que recebe o valor do objeto da classe Paciente
def insert(paciente: Paciente):
    with get_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute( """
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
            )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,(
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



def ccount_paciente():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes")
        return cursor.fetchone()[0]

def ccount_avc():
    with get_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes WHERE stroke = 1")
        return cursor.fetchone()[0]