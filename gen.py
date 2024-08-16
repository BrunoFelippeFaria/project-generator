#!/usr/bin/env python3
import os
import json
from subprocess import run
from sys import argv

def criarArquivo(arquivo, conteudo):
    with open(arquivo, "w") as arq:
        arq.write(conteudo)

def lerArquivo(arquivo):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    caminho = os.path.join(script_dir, arquivo)
    with open(caminho, "r") as arq:
        return arq.read()

opc = argv[1]

print("inicio")

if opc == "qt6":
    criarArquivo("CMakeLists.txt", lerArquivo("txts/qt6_CMakeLists"))
    if not os.path.exists("build"):
        #cria a estrutura base
        os.mkdir("build")
        criarArquivo("main.cpp", lerArquivo("txts/qt6_main_cpp"))
        #roda o cmake
        run(["cmake", ".."], cwd="build")
        run(["make"], cwd="build")
    #adiciona o LSP
    run(["cmake", "-DCMAKE_EXPORT_COMPILE_COMMANDS=1",  ".."], cwd="build")
    #remove flag incompativel com o clang
    with open("build/compile_commands.json", "r") as compileComands:
        data = json.load(compileComands)
    
    for dado in data:
        dado["command"] = dado["command"].replace(" -mno-direct-extern-access", "")
    
    with open("build/compile_commands.json", "w") as compileComands:
        json.dump(data, compileComands, indent=2)
    
    print("projeto qt6 gerado")

elif opc == "cmake":
    print("gerando arquivo cmake...")
    criarArquivo("CMakeLists.txt", lerArquivo("txts/base_CMakeLists"))
    print("arquivo cmake gerado")

exit(0)
