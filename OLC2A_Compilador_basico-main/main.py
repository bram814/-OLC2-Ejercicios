import grammar.gramatica as grammar

f = open("./entrada.txt", "r")
input = f.read()

parseTree = grammar.parse(input)
parseTree.genC3D()

print("digraph {")
parseTree.genParseTree()
print("}")