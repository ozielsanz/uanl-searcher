requerimientos= [' os', ' requests',' sys',' webbrowser']
# Christopher Oziel Sánchez Martínez
# Mariana Flores Puente
# En esta parte verifica si se tiene instalado los modulos
# Y si no, manda una excepcion para instalarlos y reiniciar el programa
try: 
    import os, requests, sys, webbrowser
except ImportError:
    for elemento in requerimientos:
        os.system('pip install '+ elemento) 
        print('Installing'+elemento+"...") 
    print('Ejecuta de nuevo tu script...') 
    exit()

try:
    from bs4 import BeautifulSoup as bs
except ImportError: 
        os.system('pip install bs4') 
        print('Installing bs4...') 
        print('Ejecuta de nuevo tu script...') 
        exit()


print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = str(input("Ingrese las siglas de la Facultad a buscar: "))
dependencia = dependencia.upper() # Cambia el string a mayúsculas
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        # Aquí se busca entre los parrafos de las paginas la dependencia indicada.
        # Y si es encontrada, abre el navegador con esa página.
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
