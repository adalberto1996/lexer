import sys,os
from Lexer import *
from Tokens import *
from time import sleep
from Barraprogreso import *

class Analizador:
    #Documento a analizar
    __programa = ""
    #Objeto tipo Tokens para recibir los tokens de mi lenguaje 
    __token = Tokens()
    #objeto tipo Lexer
    __lexer = Lexer()
    

    def __init__(self,document):
        self.__programa = document

    def analizar(self):
        if self.__programa == 'codigo.ap':
            codAnalizar = open(self.__programa,encoding='UTF-8').read()
            no_Validos = self.__lexer.validar(codAnalizar,self.__token.getTokens(),True)
            validos = self.__lexer.validar(codAnalizar,self.__token.getTokens(),False)
            printProgressBar(0, len(validos), prefix = 'Progreso:', suffix = 'Completo', length = 70)
            i = 0
            for valido in validos:
                if valido['token'] != '\n':
                    os.system('clear')
                    printProgressBar(i + 1,len(validos), prefix = 'Progreso:', suffix = 'Completo', length = 70)
                    print('\n')
                    i+=1
                    print('[',valido['token'],']','Hace parte del lenguaje, es un:',valido['tipo'])
                   
            if no_Validos:    
                for invalido in no_Validos:
                    print("Error en la linea", invalido['linea'], " [",invalido['palabra'],"]")
                   
            else:
                print("No se encontró ningún error léxico")     
        else:
            print("Error en la apertura del archivo")
