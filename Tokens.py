class Tokens:
    __tokens = []
    def __init__ (self):
        self.__tokens = [
            (r'[#][^\d]([A-Za-z])*([0-9])*',"VARIABLE"),
                (r'Ap.escriba','FUNCION'),
                (r'Ap.asigna','ASIGNACION'),
                (r'Ap.esigual', 'COMPARACION'),
                (r'Ap.suma', 'SUMA'),
            	(r'Ap.resta', 'RESTA'),
	            (r'Ap.para', 'CICLO'),
	            (r'Ap.mientras', 'CICLO'),
	            (r'Ap.si', 'CONDICION'),
            	(r'Ap.no', 'CONDICION'),
	            (r'Ap.multiplica', 'MULTIPLICACION'),
	            (r'Ap.divide', 'DIVICION'),
	            (r'@%', 'DELIMITADOR'),
	            (r'%@', 'DELIMITADOR'),
	            (r'\(', 'PARENTESIS'),
	            (r'\)', 'PARENTESIS'),
	            (r'\d{1,}', 'ENTERO'),
            	(r'(\")(.*)(\")', 'CADENA'),
	            (r'[ \t]+', 'IGNORAR')
            ]
      
    def getTokens(self):
        return self.__tokens

