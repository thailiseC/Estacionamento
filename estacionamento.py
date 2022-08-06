class Vaga:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.livre = False
        self.placa = None

    def ocupar(self):
        self.livre = False

    def desocupar(self):
        self.livre = True


class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo
        self.estacionado = False

    def estacionar(self):
        if self.estacionado == False:
            self.estacionado = True
        else:
            raise ValueError()

    def sair_da_vaga(self):
        if self.estacionado == True:
            self.estacionado = False
        else:
            raise ValueError()


class Carro(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, "Carro")


class Moto(Veiculo):
    def __init__(self, placa):
        super().__init__(placa, "Moto")


class Estacionamento:
    def __init__(self):
        self._index = 25
        self.vagas_de_carro = [0] * self._index
        self.vagas_de_moto = [0] * self._index
        for i in range(0, self._index):
            self.vagas_de_carro[i] = Vaga(i + 1, "Carro")
            self.vagas_de_moto[i] = Vaga(i + 26, "Moto")
            if i < 5:
                self.vagas_de_carro[i].livre = True
                self.vagas_de_moto[i].livre = True
        self._carro_para_vaga = 0
        self._moto_para_vaga = 0
        self._total_vagas_livres_carros = None
        self._total_vagas_livres_moto = None

    @property
    def total_vagas_livres_carro(self):
        self._total_vagas_livres_carro = 0
        for i in range(0, self._index):
            if self.vagas_de_carro[i].livre == True:
                self._total_vagas_livres_carro =+ 1
        return self._total_vagas_livres_carro

    @total_vagas_livres_carro.setter
    def total_vagas_livres_carro(self, valor):
        self._total_vagas_livres_carro = valor

    @property
    def total_vagas_livres_moto(self):
        self._total_vagas_livres_moto = 0
        for i in range(0, self._index):
            if self.vagas_de_moto[i].livre == True:
                self._total_vagas_livres_moto =+ 1
        return self._total_vagas_livres_moto

    @total_vagas_livres_moto.setter
    def total_vagas_livres_moto(self, valor):
        self._total_vagas_livres_moto = valor

    @property
    def carro_para_vaga(self):
        return self._carro_para_vaga
        
    @carro_para_vaga.setter
    def carro_para_vaga(self, valor):
        self._carro_para_vaga = self._carro_para_vaga + valor

    @property
    def moto_para_vaga(self):
        return self._moto_para_vaga
        
    @moto_para_vaga.setter
    def moto_para_vaga(self, valor):
        self._moto_para_vaga = self._moto_para_vaga + valor

    def estacionar_carro(self, carro = Carro):
        if self.total_vagas_livres_carro > 0:
            for i in range(0, self._index):
                if self.vagas_de_carro[i].livre == True:
                    self.carro_para_vaga = 1
                    self.vagas_de_carro[i].ocupar()
                    self.vagas_de_carro[i].placa = carro.placa
                    carro.estacionar()
                    break

    def estacionar_moto(self, moto = Moto):
        if self.total_vagas_livres_moto > 0:
            for i in range(0, self._index):
                if self.vagas_de_moto[i].livre == True:
                    self.moto_para_vaga = 1
                    self.vagas_de_moto[i].ocupar()
                    self.vagas_de_moto[i].placa = moto.placa
                    moto.estacionar()
                    break
        elif self.total_vagas_livres_carro > 0:
            for i in range(0, self._index):
                if self.vagas_de_carro[i].livre == True:
                    self.carro_para_vaga = 1
                    self.vagas_de_carro[i].ocupar()
                    self.vagas_de_carro[i].placa = moto.placa
                    moto.estacionar()
                    break

    def remover_carro(self, carro = Carro):
        for i in range(0, self._index):
            if carro.placa == self.vagas_de_carro[i].placa:
                self.carro_para_vaga = -1
                self.vagas_de_carro[i].desocupar()
                self.vagas_de_carro[i].placa = None
                carro.estacionar()
                break

    def remover_moto(self, moto = Moto):
        for i in range(0, self._index):
            if moto.placa == self.vagas_de_moto[i].placa:
                self.moto_para_vaga = -1
                self.vagas_de_moto[i].desocupar()
                self.vagas_de_moto[i].placa = None
                moto.sair_da_vaga()
                break
        for i in range(0, self._index):
            if moto.placa == self.vagas_de_carro[i].placa:
                self.carro_para_vaga = -1
                self.vagas_de_carro[i].desocupar()
                self.vagas_de_carro[i].placa = None
                moto.sair_da_vaga()
                break

    def estado_estacionamento(self):
        print(self.__str__())
        for i in range(0, self._index):
            if self.vagas_de_carro[i].livre == False and self.vagas_de_moto[i].livre == False:
                print(f'A vaga de {self.vagas_de_carro[i].tipo}, id = {self.vagas_de_carro[i].id} está ocupada pelo veículo de placa {self.vagas_de_carro[i].placa} ')
                print(f'A vaga de {self.vagas_de_moto[i].tipo}, id = {self.vagas_de_moto[i].id} está ocupada pela moto de placa {self.vagas_de_moto[i].placa} ')
            elif self.vagas_de_carro[i].livre == False:
                print(f'A vaga de {self.vagas_de_carro[i].tipo}, id = {self.vagas_de_carro[i].id} está ocupada pelo veículo de placa {self.vagas_de_carro[i].placa} ')
                print(f'A vaga de {self.vagas_de_moto[i].tipo}, id = {self.vagas_de_moto[i].id} está livre. ')
            elif self.vagas_de_moto[i].livre == False:
                print(f'A vaga de {self.vagas_de_carro[i].tipo}, id = {self.vagas_de_carro[i].id} está livre. ')
                print(f'A vaga de {self.vagas_de_moto[i].tipo}, id = {self.vagas_de_moto[i].id} está ocupada pela moto de placa {self.vagas_de_moto[i].placa} ')
            else:
                print(f'A vaga de {self.vagas_de_carro[i].tipo}, id = {self.vagas_de_carro[i].id} está livre. ')
                print(f'A vaga de {self.vagas_de_moto[i].tipo}, id = {self.vagas_de_moto[i].id} está livre. ')
    
    def __str__(self):
        return f'Estacionamento: \n Vagas de Carro = {self._index}\n Vagas de Moto = {self._index}\n Vagas ocupadas de Carro = {self.carro_para_vaga}\n Vagas ocupadas de Moto = {self.moto_para_vaga}\n Vagas livres de Carro = {self.total_vagas_livres_carro}\n Vagas livres de Moto = {self.total_vagas_livres_moto}'


estacionamento = Estacionamento()
carro1 = Carro("abcd1234")
moto1 = Moto("tegr595")
moto2 = Moto("asdf665")
moto3 = Moto("qwrt547")
moto4 = Moto("rtyu7896")
moto5 = Moto("hfgd6983")
moto6 = Moto("nvxd102")
estacionamento.estacionar_carro(carro1)
estacionamento.estacionar_moto(moto1)
estacionamento.estacionar_moto(moto2)
estacionamento.estacionar_moto(moto3)
estacionamento.estacionar_moto(moto4)
estacionamento.estacionar_moto(moto5)
estacionamento.estacionar_moto(moto6)
estacionamento.estado_estacionamento()
estacionamento.remover_moto(moto3)
estacionamento.estado_estacionamento()
