# Binary Sarch Tree

Membros:
* MATEUS ALVES DE OLIVEIRA (20210047975)
* SAMUEL ÓTTON NOGUEIRA MAIA (20210055968)
* TALISON FABIO GOMES DE MEDEIROS (20210057425)


# Dependências

É necessário ter Python instalado na máquina. Se estiver rodando em alguma distribuição linux popular como Ubuntu ele já vem instalado.

Para verificar se o python está instalado basta rodar o comando `python`. Se um prompt for aberto sem retornar nenhum erro então está instalado.

Caso não esteja instalado consulte a página do Python para Download [AQUI](https://www.python.org/downloads/)

# Como executar

Para rodar o exemplo padrão, usando arquivos já definidos na pasta de `examples/` para valores na arvore e comandos, basta executar
```
make run
```
Esse comando necessita ter o `make` instalado. 

Ele, por baixo dos panos, executa o comando abaixo, passando os arquivos na pasta de `example/` como parametros do comando
```
python main.py examples/tree1.txt examples/commands1.txt
```

Sendo assim, é possivel também rodar o comando assima passando arquivos personalizados (ao inves de usar o `make run`). Seguindo o padrão do comando

```
python main.py <arquivo_com_numeros_da_arvore> <arquivo_com_comandos_para_executar>
```
