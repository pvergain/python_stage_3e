
.. index::
   pair: Environnement Virtuel; sphinx35
   

.. _env_sphinx35:

=============================================================
Environnement virtuel pour la production de la documentation
=============================================================

.. contents::
   :depth: 3


Création  de l'environnement
=============================


1) Rassemblement de tous les environnements virtuels sous WORKON_HOME::

    mkvirtualenv sphinx35 --python=c:\anaconda3\python.exe
    

2) ou sous le répertoire courant::

    
    virtualenv sphinx35 --python=c:\anaconda3\python.exe



Activation de l'environnement 
=============================

1) si on utilise WORKON_HOME::

    workon sphinx35
    

2) ou  le répertoire courant::

    sphinx35\Scripts\activate.bat
    
      
Liste des modules utilisés
==========================

::

    pip list      

   
Liste des modules à mettre à jour
==================================

::

    pip list -o
    
    
Liste des modules à 'freezer' dans requirements.txt
====================================================


::

    pip freeze > requirements.txt
    
    
Réinstaller les mêmes modules
==============================

::

    pip install -r requirements.txt
    
           
    


    
    
    

