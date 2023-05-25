from data_structures.binary_search_tree import BinarySearchTree
from data_structures.nodes import Node
import sys


COMMANDS = {
    "MEDIANA": {
        "fn_name": "mediana",
        "need_parameter": False,
    },
    "CHEIA": {
        "fn_name": "ehCheia",
        "need_parameter": False,
    },
    "COMPLETA": {
        "fn_name": "ehCompleta",
        "need_parameter": False,
    },

    "ENESIMO": {
        "fn_name": "enesimoElemento",
        "need_parameter": True,
    },
    "POSICAO": {
        "fn_name": "posicao",
        "need_parameter": True,
    },
    "IMPRIMA": {
        "fn_name": "imprimeArvore",
        "need_parameter": True,
    },
    "REMOVA": {
        "fn_name": "remove",
        "need_parameter": True,
    },
}

def read_numbers_file(file_path) -> list[int]:
    with open(file_path, 'r') as file:
        numbers = file.read().split()
        numbers = [int(num) for num in numbers]
    return numbers

def read_text_file(file_path) -> list[tuple[str, int | None]]:
    lines: list[tuple[str, int | None]] = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue

            values_in_line = line.strip().split(' ')

            if len(values_in_line) > 1:
                command = values_in_line[0]
                parameter = values_in_line[1]
                lines.append( (command, int(parameter)) )
            else:
                command = values_in_line[0]
                lines.append( (command, None) )


    return lines

if __name__ == '__main__':

    print(" =--------------------------------------------------------------------------------= ")
    print(" =--------------- Bem vindo à plantação de árvore mais digital do IMD ------------= ")
    print(" =--------------------------------------------------------------------------------= ")

    if len(sys.argv) != 3:
        print('Usage: python script.py <arquivo_com_numeros_da_arvore> <arquivo_com_comandos_para_executar>')
        sys.exit(1)
    
    numbers_file_path = sys.argv[1]
    text_file_path = sys.argv[2]
    
    numbers_list = read_numbers_file(numbers_file_path)
    text_list = read_text_file(text_file_path)
    
    print('')
    print('Numeros para add na arvore: ', numbers_list)
    print('Comandos para executar....: ', text_list)
    print('')

    tree = BinarySearchTree.from_list(numbers_list)

    for command_name, parameter in text_list:

        method_name_of_comaand = COMMANDS[command_name]["fn_name"]
        need_parameter = COMMANDS[command_name]["need_parameter"]

        method_to_call = getattr(tree, method_name_of_comaand)

        if need_parameter:
            output = method_to_call(parameter)
            print(f'Saida do comando {command_name} {parameter or ""} \n --> {output}\n')
        else:
            output = method_to_call()
            print(f'Saida do comando {command_name} {parameter or ""} \n --> {output}\n')



