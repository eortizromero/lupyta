Lupyta
======

Lupyta es un instalador automático de PyQt4.


Actualmente funciona con Windows® y GNU/Linux (GNU General Public License).

Instalación
-----------

Instalar y actualizar usando `pip`_:

.. code-block:: text

    pip install -U lupyta


Un Simple ejemplo
-----------------

.. code-block:: python
    
        from lupyta import Lupyta

        instalador = Lupyta()

        if __name__ == '__main__':
            instalador.iniciar()


.. _pip: https://pip.pypa.io/en/stable/quickstart/

