
.. index::
   pair: Gestion de versions ; Git
   

.. _installation_git:

=======================================================
Installation de Git
=======================================================

.. seealso:: 

   - https://git-scm.com/
   - https://en.wikipedia.org/wiki/Git


.. figure:: git.png
   :align: center
   

.. contents::
   :depth: 3
   
   
Description
============

``git`` est un logiciel de gestion de versions décentralisé. 

C'est un logiciel libre créé par Linus Torvalds, auteur du noyau Linux, et 
distribué selon les  termes de la licence publique générale GNU version 2. 

En 2016, il s’agit du logiciel de gestion de versions le plus populaire qui 
est utilisé par plus de douze millions de personnes.


Commandes Git
==============


git status
-----------

::

    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            renamed:    installation/python35/anaconda.png -> installation/anaconda/anaconda.png
            renamed:    installation/python35/apres_install_anaconda.png -> installation/anaconda/apres_install_anaconda.png
            renamed:    installation/python35/tree_anaconda.png -> installation/anaconda/tree_anaconda.png

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   actions/2__14_octobre_2016/2__14_octobre_2016.rst
            modified:   index.rst
            modified:   installation/installation.rst
            modified:   installation/pycharm/pycharm.rst
            modified:   installation/python35/python35.rst
            modified:   programmes/pylab/nombres_x_y/nombres_x_y.rst
            modified:   programmes/pylab/pylab.rst
            modified:   ../source/pylab/nombres_x_y/nombres_x_y.py

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            installation/anaconda/anaconda.rst
            installation/anaconda/ipython/
            installation/anaconda/spyder/
            installation/git/
            programmes/pylab/ipython_anaconda3.png
            programmes/pylab/ipython_barre_commandes.png
            programmes/pylab/nombres_x_y/execution_dans_python.png

git add
--------

::

    git add .
    
    
git commit . -m "commentaires"
-------------------------------

::

    git commit . -m "maj doc"
    
        

