#!/usr/bin/env python3

import os
import json
from subprocess import run
from sys import argv
from txts import * 


def criarArquivo(arquivo, conteudo):
    with open(arquivo, "w") as arq:
        arq.write(conteudo)

opc = argv[1]

print("inicio")

if opc == "qt6":
    print("gerando projeto qt")
    criarArquivo("CMakeLists.txt", qt6_CMakeLists)
    if not os.path.exists("build"):
        #cria a pasta build
        os.mkdir("build")
        #cria o arquivo main
        criarArquivo("main.cpp", base_main_cpp)
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

elif opc == "cmake":
    print("gerando arquivo cmake...")
    criarArquivo("CMakeLists.txt", base_CMakeLists)

exit(0)
