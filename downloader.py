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
python_version = "Version de Python", \
                 str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])
os_plataforma = "%s" % plataforma

print(" ".join(python_version) + " en " + os_plataforma)

LINUX = OS == 'linux' or OS == 'linux2' or plataforma.startswith('Linux')
WINDOWS = OS == 'win32' or plataforma.startswith('Windows')


def verificar_pyqt_instalado():
    print ("Verificando si existe alguna instalación de PyQt4")
    if LINUX:
        try:
            os.system("dpkg-query -W -f='${Package} ${Status} ${Version}\n' python-qt4 qt4-designer")
            instalado = True
        except:
            instalado = False
        if not instalado:
            instalador()
    elif WINDOWS:
        pip.main(['search', 'PyQt4'])


def descargador(url):
    wget.download(url)


def instalar_libreria(libreria):
    print("Instalando libreria %s" % libreria)
    pip.main(['install', libreria])


def instalador():
    if LINUX:
        comando = 'gksudo apt-get install '
        libreria = comando + 'python-qt4 qt4-designer'
        os.system(libreria)
    else:
        if WINDOWS:
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
                archivo = open('./{}'.format(arch_wheel))
            except Exception as e:
                print("Imposible abrir el archivo, Error: %s" % e)
            instalar_libreria(archivo.name)


def iniciar():
    verificar_pyqt_instalado()


if __name__ == '__main__':
    iniciar()
