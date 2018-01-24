# -*- coding: utf-8 -*-

import sys
import platform

OS = sys.platform
PLATAFORMA = platform.platform()
VERSION_PYTHON = "Version de Python", \
                 str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])
OS_PLATAFORMA = "%s" % PLATAFORMA

print(" ".join(VERSION_PYTHON) + " en " + OS_PLATAFORMA)

LINUX = OS == 'linux' or OS == 'linux2' or PLATAFORMA.startswith('Linux')
WINDOWS = OS == 'win32' or PLATAFORMA.startswith('Windows')
