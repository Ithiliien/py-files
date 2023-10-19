def readFile(name):
  with open(name, "r", errors="ignore") as file:
    return file.read()
 

def wordCount(text):
  contador = text.split()
  contador= len(contador)
  return contador

def uniqueWordCount(text):
    palabra = text.split()
    contador_palabra = len(set(palabra))
    return contador_palabra

def findContent(text, word):
    palabras = text.split()
    contador_letra = palabras.count(word.lower())#.lower convierte todas las palabras a minusculas.
    return contador_letra

def changeQuijoteToQuixote(text):
    cambia_letra_quijote = text.replace("Quijote", "Quixote") #.replace sirve para remplazar una palabra por otra(primero se pone la original y luego la que queremos cambiar)
    return cambia_letra_quijote