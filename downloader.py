# -*- coding: utf-8 -*-
import wget
import os
import pip
import sys
import platform


libreria = None
comando = None
OS = sys.platform
plataforma = platform.platform()

if sys.version_info >= (2,7):
    print ("Python version %s.%s.%s+" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
elif sys.version_info >= (3,):
    print ("Python version %s.%s.%s+" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))


def descargador(url):
    wget.download(url)


def instalar_libreria(libreria):
    print("Instalando libreria %s" % libreria)
    pip.main(['install', libreria])


def instalador():
    if OS == 'linux' or OS == 'linux2' or plataforma.startswith('Linux'):
        comando = 'gksudo apt-get install '
        libreria = comando + 'python-qt4 qt4-designer'
        os.system(libreria)
    else:
        if OS == 'win32' or plataforma.startswith('Windows'):
            arch_wheel = None
            dominio = "http://eortiz.esy.es/docs/"
            if platform.architecture()[0] == '64bit':
                if sys.version_info >= (2, 7):
                    arch_wheel = "PyQt4-4.11.4-cp27-cp27m-win_amd64.whl"
                    descargador(dominio + arch_wheel)
                elif sys.version_info >= (3, ):
                    arch_wheel = "PyQt4-4.11.4-cp36-cp36m-win_amd64.whl"
                    descargador(dominio + arch_wheel)
            elif platform.architecture()[0] == '32bit':
                if sys.version_info >= (2, 7):
                    arch_wheel = "PyQt4-4.11.4-cp27-cp27m-win32.whl"
                    descargador(dominio + arch_wheel)
                elif sys.version_info >= (3, ):
                    arch_wheel = "PyQt4-4.11.4-cp36-cp36m-win32.whl"
                    descargador(dominio + arch_wheel)
            archivo = None
            try:
                with open('./{}'.format(arch_wheel), 'r') as wheel:
                    archivo = wheel.readable()
            except Exception as e:
                print("Imposible abrir el archivo, Error: %s" % e)
            instalar_libreria(archivo)


if __name__ == '__main__':
    instalador()
