#!/bin/env python
import logging
import threading
import requests
from bs4 import BeautifulSoup
import os 
logging.basicConfig(
    level = logging.INFO,
    format='%(message)s'
)

URL = 'https://www.mundoprimaria.com'
DOMAIN = '/cuentos-infantiles-cortos'

def clear():
    return os.system('clear')

def get_content_history(content):
    clear()
    soup = BeautifulSoup(content,'html.parser')
    for content in soup.find_all('div',class_="contenedor-post cuentos"):
        loggin.info(f"\t{content.h1.text}")
        for history in content.find_all('p'):
            loggin.info(f'{history.text}')
            

def get_menu_history(lista,soup):
    count=0
    for menu_history in soup.find_all('div',class_='boton-con-titulo solo-imagen'):
            link = menu_history.a['href']
            title = menu_history.text
            count +=1
            lista.append(link)
            loggin.info(str(count)+".",title)
    return lista

def get_menu_items(menu,func):
    op = int(input(f'opciones:'))
    if op < len(menu):
        thread_terror = threading.Thread(
            target=generate_reponse,
            kwargs={
                'url':URL+menu[op],
                'success_callback':func,
                'error_callback':error
            }
        )
        thread_terror.start()
    else:
        logging.info('Ops lo siento opcion no valida')

def get_sub_history(content):
    soup = BeautifulSoup(content,'html.parser')
    title = soup.find('h2')
    links =[]
    clear()
    loggin.info(f"\t{title.text}"))
    menu = get_menu_history(links,soup)
    get_menu_items(menu,get_content_history)
    
def get_response_history(content):
    soup = BeautifulSoup(content,'html.parser')
    links = []
    print("\tCuentos cortos infantiles\n")
    menu = get_menu_history(links,soup)
    get_menu_items(menu,get_sub_history)
        
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
    