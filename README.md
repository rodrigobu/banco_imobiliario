# Banco Imobiliario
Projeto de um simulador de banco imobiliario:
 * Possivel utilizar como API
 * Possivel utilizar em linhas de comando 
 * A simulação a feita a partir do principio de quatro jogadores cada um com sua personalidade(Aleatorio, Cauteloso, Exigente e Impulsivo).

## Instalação
Aplicação requer Python3, Django3 e Django Rest Framework e Git para executar.
Clone o projeto:

```sh
$ git clone https://github.com/rodrigobu/banco_imobiliario.git
```
Crie uma nova virtualenv:

```sh
$ virtualenv myenv -p python3
```
Depois de criar a virtualenv ative:
```sh
$ source amcom/bin/activate
```
Vamos para repositorio:

```sh
(myenv) ~$ cd banco_imobiliario/
```
Instalaremos as bibliotecas nescessária que estão no arquivo requirements.txt
```sh
(myenv) ~$ pip install -r requirements.txt
```
Após as instalações das bibliotecas precisamos conectar nosso banco.
```sh
python manage.py migrate
```
Agora já temos nosso ambiente instalado, já conseguimos acessar nossa aplicação.

## Como Usar
Podemos executar o projeto de duas formas, em linha de comando ou via API.
### Linha de Comando:
Basta executar o codigo abaixo em seu terminal com o ambiente ativo
```sh
python manage.py executar_jogo
```
Ira executar 300 simulações trazendo alguns resultado no terminal de acordo com cada simulação.
### Via API:
Podemos executar via API:
```sh
python manage.py runserver
```
Após ativar o servidor local podemos entrar no navegador no seguinte endereço http://127.0.0.1:8000/, assim que acessar a pagina será redirecionado para pagina inicial do API Root do Django Rest Framework, teremos duas opções (JOGO) que seria para visualizar todas as simulações executadas e a outra opção (SIMULAR) que seria para simular uma partida do banco imobiliario.
