import urllib.request

site = "https://www.iefp.pt"

try:
  print(urllib.request.urlopen(site).getcode())
  pass
except Exception as error:
  print("Não consegui ligar ao site!")
else:
  print("Consegui ligar ao site!")
  
