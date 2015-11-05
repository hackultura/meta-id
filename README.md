# Meta-ID


Meta-ID é um gerênciador de identidades culturais para entes e agentes da cultura.

Para organizar a complexidade das diversas identidades culturais que um ente pode ter, nada melhor que um gerênciador de portifólios e das mais diversas informações que possam ser utilizadas por outros sistemas através de uma API.

O projeto está sendo desenvolvido em Python utilizando Django como framework e utilizando PostgreSQL como banco de dados.

## Requisitos

Consideramos que você possui os seguintes requisitos:

 - Python >=2.7
 - Pyenv
 - Virtualenv
 - PostgreSQL

Para instalar as dependencias:

```bash
make setup
```

## Testes

Os testes são rodados pelo `tox`. Dessa forma ele testa nas seguintes versões do Python:

 - Python 2.7.x
 - Python 3.3.x
 - Python 3.4.x
 - Python 3.5.x

Para isso, rode o seguinte comando:

```bash
make tox
```
