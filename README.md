# AVL Tree

Membros:

- MATEUS ALVES DE OLIVEIRA (20210047975)
- SAMUEL ÓTTON NOGUEIRA MAIA (20210055968)
- TALISON FABIO GOMES DE MEDEIROS (20210057425)

# Dependências

É necessário ter o Python instalado na máquina. Versão 3.10.

Para verificar se o python está instalado basta rodar o comando `python`. A saída esperada deve ser semelhante à seguinte:

```python
Python 3.10.5 (main, Jun 23 2022, 17:15:25) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Caso não esteja instalado consulte a página do Python para Download [AQUI](https://www.python.org/downloads/)

# Como executar

Para rodar o exemplo padrão, usando arquivos já definidos na pasta de `examples/` para valores na arvore e comandos, basta executar

```
make run
```

Esse comando necessita ter o `make` instalado.

Ele, por baixo dos panos, executa o comando abaixo, passando os arquivos na pasta de `example/` como parâmetros do comando

```
python main.py examples/tree1.txt examples/commands1.txt
```

Sendo assim, é possível também rodar o comando acima passando arquivos personalizados (ao invés de usar o `make run`). Seguindo o padrão do comando

```
python main.py <arquivo_com_números_da_arvore> <arquivo_com_comandos_para_executar>
```
