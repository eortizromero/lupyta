# -*- coding: utf-8 -*-
import wget
import os
import pip
from _compat import *


def _deutf8(s):
    return s


class Lupyta(object):
    def __init__(self):
        pass

    def descargador(self, url):
        wget.download(url)

    def instalar_libreria(self, **kw):
        sistema = kw.pop('sistema', None)
        libreria = kw.pop('libreria', None)
        if sistema is not None:
            if sistema == 'linux':
                comando = 'gksudo apt-get install ' + libreria
                os.system(comando)
            elif sistema == 'windows':
                print("\nInstalando libreria %s" % libreria)
                pip.main(['install', libreria])

    def instalador(self):
        if LINUX:
            self.instalar_libreria(sistema='linux', libreria='python-qt4 qt4-designer')
        elif WINDOWS:
            arch_wheel = None
            dominio = "http://eortiz.esy.es/docs/"
            if platform.architecture()[0] == '64bit':
                if sys.version_info >= (2, 7):
                    arch_wheel = "PyQt4-4.11.4-cp27-cp27m-win_amd64.whl"
                    self.descargador(dominio + arch_wheel)
                elif sys.version_info >= (3, ):
                    arch_wheel = "PyQt4-4.11.4-cp36-cp36m-win_amd64.whl"
                    self.descargador(dominio + arch_wheel)
            elif platform.architecture()[0] == '32bit':
                if sys.version_info >= (2, 7):
                    arch_wheel = "PyQt4-4.11.4-cp27-cp27m-win32.whl"
                    self.descargador(dominio + arch_wheel)
                elif sys.version_info >= (3, ):
                    arch_wheel = "PyQt4-4.11.4-cp36-cp36m-win32.whl"
                    self.descargador(dominio + arch_wheel)
            try:
                archivo = open('./{}'.format(arch_wheel))
            except Exception as e:
                raise IOError("Imposible abrir el archivo, Error: %s" % e)
            self.instalar_libreria(sistema='windows', libreria=archivo.name)

    def iniciar(self):
        self.instalador()


instalador = Lupyta()


if __name__ == '__main__':
    instalador.iniciar()
