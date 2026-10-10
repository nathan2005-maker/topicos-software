class Paciente:
    def __init__(self, idade: float, genero: str, hiper: int, dcardiaca: int, glicose: float, 
                        imc: float, tabagismo: str ,reg_avc: int, estado_civil: str, tipo_job: str, residencia: str):
        self.idade = idade
        self.genero = genero
        self.hiper = hiper
        self.dcardiaca = dcardiaca
        self.glicose = glicose
        self.imc = imc
        self.tabagismo = tabagismo
        self.reg_avc = reg_avc
        self.estado_civil = estado_civil
        self.tipo_job = tipo_job
        self.residencia = residencia

    #Getter Idade protect
    @property
    def idade(self):
        return self._idade

    #Setter Idade
    @idade.setter
    def idade(self, idade):
        self._idade = idade

    #Getter Genero
    @property
    def genero(self):
        return self._genero

    #Setter Genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    #Getter Hipertencao
    @property
    def hiper(self):
        return self._hiper

    #Setter Hipertencao
    @hiper.setter
    def hiper(self, hiper):
        self._hiper = hiper

    #Getter Doenca Cardiaca
    @property
    def dcardiaca(self):
        return self._dcardiaca

    #Setter Doenca Cardiaca
    @dcardiaca.setter
    def dcardiaca(self, dcardiaca):
        self._dcardiaca = dcardiaca

    #Getter Glicose
    @property
    def glicose(self):
        return self._glicose

    #Setter Glicose
    @glicose.setter
    def glicose(self, glicose):
        self._glicose = glicose

    #Getter IMC
    @property
    def imc(self):
        return self._imc

    #Setter IMC
    @imc.setter
    def imc(self, imc):
        self._imc = imc

    #Getter Tabagismo
    @property
    def tabagismo(self):
        return self._tabagismo

    #Setter Tabagismo
    @tabagismo.setter
    def tabagismo(self, tabagismo):
        self._tabagismo = tabagismo

    #Getter Registro de AVC
    @property
    def reg_avc(self):
        return self._reg_avc

    #Setter Registro de AVC
    @reg_avc.setter
    def reg_avc(self, reg_avc):
        self._reg_avc = reg_avc

    #Getter Estado Civil
    @property
    def estado_civil(self):
        return self._estado_civil

    #Setter Estado Civil
    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self._estado_civil = estado_civil
    
    #Getter Tip de Trabalho
    @property
    def tipo_job(self):
        return self._tipo_job

    #Setter Tipo de Trabalho
    @tipo_job.setter
    def tipo_job(self, tipo_job):
        self._tipo_job = tipo_job

    #Getter Residencia
    @property
    def residencia(self):
        return self._residencia

    #Setter Residencia
    @residencia.setter
    def residencia(self, residencia):
        self._residencia = residencia