filme = dict()
playlist = list()


filme["titulo"] = "The Thing" 
filme["duração"] = "1h 48m" 

print(type(filme))
print(filme.keys())
print(filme.items())
print(filme)

for key, value in filme.items():
  print(f"A chave: {key}, tem: {value}") 
  
playlist.append(filme)
print(playlist)
playlist.append(filme.copy())
print(playlist)