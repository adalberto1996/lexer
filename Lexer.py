import re

class Lexer:
	#Funcion para validar
	def validar(self,codigo,tokens, Errores):
		invalidos = []
		codigo = codigo.strip().split('\n')
		error = False
		for i in range(len(codigo)):
			linea = codigo[i]
			pos = 0
			palabra = ""
			while pos < len(linea):	
				m = None
				for token, tipo in tokens:
					if Errores:
						p = re.compile(token)
						m = p.match(linea, pos)
						if m:
							break
					else:
						if token != r'[ \t]+':	
							p = re.compile(token)
							m = p.match(linea, pos)
							if m:
								aux = m.group(0)
								invalidos.append({'token':aux,'tipo':tipo})
								break
				if m:
					pos =  m.end(0)
				else:
					if Errores:
						error = True
						palabra+=linea[pos]
						pos+=1
					else:
						error = True
						pos+=1
			if error:
				if Errores:
					invalidos.append({'linea':i + 1, 'palabra':palabra})
					palabra = ""
					error = False
				else:
					error=False
		return invalidos