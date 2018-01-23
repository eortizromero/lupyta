# -*- coding: utf-8 -*-
import wget
import os
import pip
import sys
import platform


libreria = None
comando = None
OS = sys.platform
python_version = None

if sys.version_info >= (2,7):
    print ("Python version %s.%s.%s+" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
elif sys.version_info >= (3,):
    print ("Python version %s.%s.%s+" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))


def descargador(url):
    return wget.download(url)


def instalador():
    if OS == 'linux' or 'linux2':
        comando = 'gksudo apt-get install '
        libreria = comando + 'python-qt4 qt4-designer'
        os.system(libreria)
    else:
        if OS == 'win32':
            if platform.architecture()[0] == '64bit':
                if sys.version_info >= (2, 7):
                    return descargador("http://eortiz.esy.es/docs/PyQt4-4.11.4-cp27-cp27m-win_amd64.whl")
                elif sys.version_info >= (3, ):
                    return descargador("http://eortiz.esy.es/docs/PyQt4-4.11.4-cp36-cp36m-win_amd64.whl")
            else:
                if sys.version_info >= (2, 7):
                    return descargador("http://eortiz.esy.es/docs/PyQt4-4.11.4-cp27-cp27m-win32.whl")
                elif sys.version_info >= (3, ):
                    return descargador("http://eortiz.esy.es/docs/PyQt4-4.11.4-cp36-cp36m-win32.whl")


if __name__ == '__main__':
    instalador()
