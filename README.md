# Desafio de Python da WomakersCode - Estacionamento

## Enunciado do problema:

- O estacionamento é um pátio de apenas um andar. Ele possui 50 vagas;
- Há 5 vagas para carros e 5 vagas para motos. Vagas para carro são maiores do que as vagas para motos;
- Carros e motos são identificados por suas placas;
- Vagas são identificadas por um número. Cada vaga tem um número identificador único;
- Carros só podem ser estacionadas em vagas específicas para carros;
- Motos preferencialmente são estacionadas em vagas de motos, mas se não houver mais vagas de moto exclusivas disponíveis, motos podem ser estacionadas em vagas de carros;
- É preciso ter controle sobre qual carro está em qual vaga para agilizar a saída quando o dono vem buscar;
- É preciso saber o número de vagas livres de carro e de moto para que o estacionamento saiba se pode receber novos carros e motos.

## Resolução

Criação das classes:

- Vaga;
- Veiculo;
- Carro como subclasse de Veiculo;
- Moto como subclasse de Veiculo;
- Estacionamento.

### Classe Vaga

#### Atributos

1. **id**: inteiro identificador da vaga;

2. **tipo**: string *"Carro"* se for uma vaga de carro ou *"Moto"* se for uma vaga de moto;

3. **livre**: booleano *True* indica que a vaga está livre,  *False* indica que não está livre. Por padrão é inicializado como *False*;

4. **placa**: string recebida do veículo que está estacionado na vaga.

#### Métodos

1. **ocupar**(): define o atributo **livre** como *False*;

2. **desocupar**(): define o atributo **livre** como *True*.

   

### Classe Veiculo

#### Atributos

1. **placa**: string identificadora do veículo;

2. **tipo**: string *"Carro"* caso o veículo seja um carro; *"Moto"* caso o veículo seja uma moto;

3. **estacionado**: booleano *True* indica que o veículo está estacionado, e *False* indica que não está. Por padrão é inicializado como *False*.

#### Métodos

1. **estacionar**(): verifica se o atributo **estacionado** é *False*. Se sim, então define o atributo **estacionado** como *True*;

2. **sair_da_vaga**(): verifica se o atributo **estacionado** é *True*. Se sim, define o atributo **estacionado** como *False*.

   

### Classe Carro

#### Atributos

1. **placa**: herdado da classe ***Veiculo***;

2. **tipo**: herdado da classe ***Veiculo*** e inicializado com a string *"Carro"*.

#### Métodos

1. **estacionar**(): herdado da classe ***Veiculo***;
2. **sair_da_vaga**(): herdado da classe ***Veiculo***.



### Classe Moto

#### Atributos

1. **placa**: herdado da classe ***Veiculo***;

2. **tipo**: herdado da classe ***Veiculo*** e inicializado com a string *"Moto"*.

#### Métodos

1. **estacionar**(): herdado da classe ***Veiculo***;
2. **sair_da_vaga**(): herdado da classe ***Veiculo***.



### Classe Estacionamento

#### Atributos

1. **index**: indicar quantas vagas de carro e moto o estacionamento terá. É inicializado como o inteiro 25;

2. **vagas_de_carro**: uma lista do tamanho do número de vagas de carro. Cada item da lista é uma vaga com um **id** e um **tipo**, e os primeiros 5 itens da lista são vagas em que o atributo **livre** é definido para *True*;
3. **vagas_de_moto**: uma lista do tamanho do número de vagas de moto. Cada item da lista é uma vaga com um **id** e um **tipo**, e os primeiros 5 itens da lista são vagas em que o atributo **livre** é definido para *True*;;
4. **carro_para_vaga**: um inteiro que aumenta uma unidade quando um carro entra em uma vaga, e diminui uma unidade quando um carro sai de uma vaga;
5. **moto_para_vaga**: um inteiro que aumenta uma unidade quando uma moto entra em uma vaga, e diminui uma unidade quando uma moto sai de uma vaga;
6. **total_vagas_livres_carros**: o número de vagas de carro livres;
7. **total_vagas_livres_moto**: o número de vagas de moto livres.

#### Métodos especiais

1. Getter **total_vagas_livres_carros()**: inicializa o **total_vagas_livres_carros** como zero e verifica um a um dos itens da lista **vagas_de_carro** quantas vagas estão com o atributo **livre** definido como *True*;
2. Setter **total_vagas_livres_moto()**: recebe um valor e dá esse valor ao atributo **total_vagas_livres_carros**;
3. Getter **total_vagas_livres_motos()**: inicializa o **total_vagas_livres_moto** como zero e verifica um a um dos itens da lista **vagas_de_moto** quantas vagas estão com o atributo **livre** definido como *True*;
4. Setter **total_vagas_livres_moto()**: recebe um valor e dá esse valor ao atributo **total_vagas_livres_moto**;
5. Getter **carro_para_vaga()**: retorna o valor do atributo **carro_para_vaga**;
6. Setter **carro_para_vaga()**: recebe um valor e define o atributo **carro_para_vaga** como o atributo somado ao valor recebido;
7. Getter **moto_para_vaga()**: retorna o valor do atributo **moto_para_vaga**;
8. Setter **moto_para_vaga()**: recebe um valor e define o atributo **moto_para_vaga** como o atributo somado ao valor recebido.

#### Métodos

1. **estacionar_carro(carro)**: recebe uma instância da classe ***Carro***, verifica se o **total_vagas_livres_carros** é maior que zero, e verifica um a um os itens da lista **vagas_de_carro**. A primeira vaga de carro que tiver o atributo **livre** como *True* é ocupada pelo carro. Nisso o atributo **carro_para_vaga** recebe o valor 1, a vaga implementa o método **ocupar**() e recebe no atributo **placa** a string inserida na inicialização da instância, que por sua vez implementa o método **estacionar()**;

2. **estacionar_moto(moto)**: recebe uma instância da classe ***Moto***, verifica se o **total_vagas_livres_moto** é maior que zero, e verifica um a um os itens da lista **vagas_de_moto**. A primeira vaga de moto que tiver o atributo **livre** como *True* é ocupada pela moto. Nisso o atributo **moto_para_vaga** recebe o valor 1, a vaga implementa o método **ocupar**() e recebe no atributo **placa** a string inserida na inicialização da instância, que por sua vez implementa o método **estacionar()**; Caso o **total_vagas_livres_moto**, procura uma vaga de carro como descrito no item 1;

3. **remover_carro(carro)**: procura se algum valor do atributo **placa** da instância da classe ***Carro*** está nos itens da lista **vagas_de_carro** como atributo **placa** de uma vaga. Caso esteja, o atributo **carro_para_vaga** recebe o valor -1, a vaga implementa o método **desocupar**() e recebe no atributo **placa** o valor *None*, e o objeto ***carro*** implementa o método **sair_da_vaga()**;

4. **remover_moto(moto)**: procura se algum valor do atributo **placa** da instância da classe ***Moto*** está nos itens da lista **vagas_de_moto** como atributo **placa** de uma vaga. Caso esteja, o atributo **moto_para_vaga** recebe o valor -1, a vaga implementa o método **desocupar**() e recebe no atributo **placa** o valor *None*, e o objeto ***moto*** implementa o método **sair_da_vaga()**; Caso não esteja, procura se a moto está em uma vaga de carro como descrito no item 3;

5. **estado_estacionamento()**: escreve na tela o método **\__str__()** que indica o *número total de vagas* de carro e de moto do estacionamento e o *número de vagas ocupadas e livres de cada tipo*. Além disso, identifica cada vaga pelo seu **id**, seu **tipo** e se está ocupada ou **livre**. Caso esteja ocupada, indica a **placa** do veículo que está estacionado.

   

