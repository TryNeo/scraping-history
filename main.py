#!/bin/env python
import logging
import threading
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level = logging.INFO,
    format='%(message)s'
)

URL = 'https://www.mundoprimaria.com'
DOMAIN = '/cuentos-infantiles-cortos'

def get_sub_history(content):
    soup = BeautifulSoup(content,'html.parser')
        

def get_response_history(content):
    soup = BeautifulSoup(content,'html.parser')
    count=0
    links = []
    print("\tCuentos cortos infantiles\n")
    for menu_history in soup.find_all('div',class_='boton-con-titulo solo-imagen'):
        link = menu_history.a['href']
        title = menu_history.a.h3.text
        count +=1
        links.append(link)
        print(str(count)+".",title)

    
    op = int(input(f'opciones de [1 - {str(count)}]:'))
    
    if op == int(len(link[0])):
        thread_terror = threading.Thread(
            target=generate_reponse,
            kwargs={
                'url':URL+links[0],
                'success_callback':get_sub_history,
                'error_callback':error
            }
        )
        thread_terror.start()
    elif op == int(len(link[1])):
        pass
    elif op == int(len(link[2])):
        pass
    elif op == int(len(link[3])):
        pass
    elif op == int(len(link[4])):
        pass
    elif op == int(len(link[5])):
        pass
    elif op == int(len(link[6])):
        pass
    elif op == int(len(link[7])):
        pass
    elif op == int(len(link[8])):
        pass
    elif op == int(len(link[9])):
        pass
    else:
      logging.info('Opcion del menu no existente')
    
        
def error():
    logging.error('Ops Lo siento error de Conexion')

def generate_reponse(url,success_callback,error_callback):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            success_callback(content)
    except requests.exceptions.ConnectionError:
        error_callback()

if __name__ == "__main__":
    thread = threading.Thread(
        target=generate_reponse,
        kwargs={
            'url':URL+DOMAIN,
            'success_callback':get_response_history,
            'error_callback':error,
        }
    )
    
    thread.start()
    