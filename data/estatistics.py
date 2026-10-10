import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


# Gráfico 1 – Distribuição das idades dos pacientes com AVC
def grafico_AVC(df):
    plt.figure(figsize=(7, 6))

    idades_crianca    = (df['stroke'] == 1) & (df['age'] < 18)
    idades_jovens     = (df['stroke'] == 1) & (df['age'] >= 18) & (df['age'] < 27)
    idades_adultos    = (df['stroke'] == 1) & (df['age'] >= 27) & (df['age'] < 51)
    idades_meia_idade = (df['stroke'] == 1) & (df['age'] >= 51) & (df['age'] < 65)
    idades_idosos     = (df['stroke'] == 1) & (df['age'] >= 65)

    barras = plt.bar(["0-17\nCriança", "18-26\nJovem", "27-50\nAdulto", "51-64\nMeia Idade", "65+\nIdoso"],
                     [idades_crianca.sum(), idades_jovens.sum(), idades_adultos.sum(),
                      idades_meia_idade.sum(), idades_idosos.sum()],
                     color=["#ff00ff", "#D7CD08", "#094BDA", "#840DD3", "#E8590C"])
    plt.bar_label(barras)
    plt.title("Distribuição das idades dos pacientes com AVC")
    plt.xlabel("Faixa etária (anos)")
    plt.ylabel("Quantidade de pacientes com AVC")
    plt.show()


# Gráfico 2 – Comparação de tabagismo entre pacientes com e sem AVC
def grafico_tabagismo(df):
    plt.figure(figsize=(10, 6))

    total_avc = (df['stroke'] == 1).sum()
    total_sem_avc = (df['stroke'] == 0).sum()

    fumante_avc = (df['stroke'] == 1) & (df['smoking_status'] == "smokes")
    anteriormente_avc = (df['stroke'] == 1) & (df['smoking_status'] == "formerly smoked")
    nunca_avc = (df['stroke'] == 1) & (df['smoking_status'] == "never smoked")

    fumante_sem_avc = (df['stroke'] == 0) & (df['smoking_status'] == "smokes")
    anteriormente_sem_avc = (df['stroke'] == 0) & (df['smoking_status'] == "formerly smoked")
    nunca_sem_avc = (df['stroke'] == 0) & (df['smoking_status'] == "never smoked")

    valores = [fumante_avc.sum() / total_avc * 100,
               anteriormente_avc.sum() / total_avc * 100,
               nunca_avc.sum() / total_avc * 100,
               fumante_sem_avc.sum() / total_sem_avc * 100,
               anteriormente_sem_avc.sum() / total_sem_avc * 100,
               nunca_sem_avc.sum() / total_sem_avc * 100]

    barras = plt.bar(["Com AVC\nfumante", "Com AVC\nfumou anteriormente", "Com AVC\nnunca fumou",
                      "Sem AVC\nfumante", "Sem AVC\nfumou anteriormente", "Sem AVC\nnunca fumou"],
                     valores,
                     color=["#B22222", "#B22222", "#B22222", "#B3EBF2", "#B3EBF2", "#B3EBF2"])
    plt.bar_label(barras, fmt="%.1f%%")
    plt.title("Comparação de tabagismo dos pacientes com e sem AVC")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
    plt.xlabel("Nível de tabagismo")
    plt.ylabel("% dos pacientes do grupo")
    plt.show()


# Gráfico 3 – Taxa de AVC com e sem hipertensão / doença cardíaca
def taxa_avc(df):
    plt.figure(figsize=(10, 6))

    com_hiper = df['heart_disease'] == 1
    sem_hiper = df['heart_disease'] == 0
    com_doenca = df['heart_disease'] == 1
    sem_doenca = df['heart_disease'] == 0

    com_hiper_avc = (df['stroke'] == 1) & com_hiper
    sem_hiper_avc = (df['stroke'] == 1) & sem_hiper
    doenca_avc = (df['stroke'] == 1) & com_doenca
    sem_doenca_avc = (df['stroke'] == 1) & sem_doenca

    valores = [com_hiper_avc.sum() / com_hiper.sum() * 100,
               sem_hiper_avc.sum() / sem_hiper.sum() * 100,
               doenca_avc.sum() / com_doenca.sum() * 100,
               sem_doenca_avc.sum() / sem_doenca.sum() * 100]

    barras = plt.bar(["Com\nhipertensão", "Sem\nhipertensão", "Com doença\ncardíaca", "Sem doença\ncardíaca"],
                     valores,
                     color=["#5CE65C", "#5CE65C", "#B22222", "#B22222"])
    plt.bar_label(barras, fmt="%.1f%%")
    plt.title("Taxa de AVC em pacientes com e sem hipertensão e doença cardíaca")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
    plt.xlabel("Condição de saúde do paciente")
    plt.ylabel("Pacientes que tiveram AVC (%)")
    plt.show()