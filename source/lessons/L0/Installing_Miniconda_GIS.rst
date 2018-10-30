Installation and verifying setup for Python + GIS
=================================================

.. note::

    In the University computer lab you DO NOT have to install Anaconda or Miniconda or any other Python distribution.
    If you are attending the course in the University computer lab, please jump to `Verifying the installation <Installing_Miniconda_GIS.html#verifying-the-installation>`_
    This section only for general info if you want to install Python on your own computer, and for remote students.

Install Python + GIS on Windows
-------------------------------

**How to start doing GIS with Python on a computer?**

Well, first you need to install Python and necessary Python modules that are used to perform various GIS-tasks. The purpose of this page is to help you
out installing Python and all those modules into your own computer. Even though it is possible to install Python from their `homepage <https://www.python.org/>`_,
**we highly recommend using** `Miniconda <https://conda.io/miniconda.html>`_ or `Anaconda <https://www.continuum.io/anaconda-overview>`_ which is an open source distribution of the Python and R programming
languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment. In short,
it makes life much easier when installing new tools on your Python to play with.

.. note::

    **Miniconda** is an encapsulated versatile virtual python environment installer,
    that works under the hood of the big Anaconda python distribution.
    Miniconda is basically a mini version of Anaconda that includes only the conda package manager and its dependencies!


https://conda.io/miniconda.html

Following steps have been tested to work on Windows 7 and 10 with Anaconda/Miniconda 64 bit.

`Download Miniconda installer (64 bit) <https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_ a Python 3.6, 64-bit (exe installer) for Windows.

.. admonition:: BEWARE:

    - To install miniconda SYSTEM-WIDE for ALL users, this does require administrator permissions;
      every users can then create their own environments with the conda tool.
    - Please do NOT make Conda the default python for the system if you don't want it to interfere with other Python installations you might have,
      eg. Pythons of ArcGIS and QGis etc

Install Miniconda on your computer by double clicking the installer and install it into a directory you want.

Install it to **all users** and use default settings.

Additional install information:
https://conda.io/docs/user-guide/install/index.html

Verifying the installation
--------------------------

In order to test that the ``conda`` package manager works we have to go through a few more steps:
After successful installation you should have a menu entry in the Windows Start Menu:

``Anaconda Prompt``

This is a Windows CMD (Commandline window, that "knows" about, where your Miniconda/Anaconda installation lies, and where to find the ``conda`` tool (without interfering other Python installations on your computer). After it opens it should display somehow like so:

.. code::

    (base) C:\Users\Alexander>

    or

    (C:\dev\conda3) C:\Users\Alexander>

On the command line type command ``conda --version`` in order to see if the command is successful, it should show the version of the conda tool.

.. code::

    (base) C:\Users\Alexander> conda --version
    conda 4.5.11

Creating environments and install packages
------------------------------------------

How to use the conda command? Open the Anaconda/conda command prompt from the Start menu:

``conda`` basically represents a typical Python virtualenv command. You can create a several distinct environments, with different Python version, and with different packages to be installed.
This will come in very handy to *try out* new libraries/packages/tools, without breaking you working installation.

https://conda.io/docs/_downloads/conda-cheatsheet.pdf

We want to use a Python version 3.6 because some of the libraries/tools we want to work with might not yet work with the latest Python 3.7.
Here it becomes obvious how practical virtual environments can be. They help you to keep various Python versions around without messing up your system.

.. code::

    (C:\dev\conda3) conda create --name geopython-environment python=3.6

In order to show all environments that have already been created you can ask conda to list these:

.. code::

    (C:\dev\conda3)  conda env list

Now we want to activate that environment and start working with it:

.. code::

    (C:\dev\conda3)  activate geopython-environment

    (geopython-environment)


Install GIS related packages with conda (and pip) by running in command prompt following commands (in the same order as they are listed).
Make sure you are in the correct enviroment (don't install into ``base``, install new packages ideally only into your designated created environments)

.. code::

    # Install numpy (v 1.13.1)
    conda install numpy

    # Install pandas (v 0.20.3) --> bundled with python-dateutil (v 2.6.1) and pytz (v 2017.2)
    conda install pandas

    # Install scipy (v 0.19.1)
    conda install scipy

    # Install matplotlib (v 2.0.2) --> bundled with cycler, freetype, icu, jpeg, libpng, pyqt, qt, sip, sqlite, tornado, zlib
    conda install matplotlib
    
    #Install Jupyter Notebook
    conda install jupyter

    # Install scikit-learn (v 0.19.0)
    conda install scikit-learn

    # Install networkx (v 1.11) --> bundled with decorator (v 4.1.2)
    conda install networkx

    # Install bokeh (v 0.12.9) --> bundled with jinja2, markupsafe, pyyaml, yaml -packages
    conda install bokeh

    # Install statsmodels (v 0.8.0) --> bundled with patsy (0.4.1)
    conda install statsmodels

    # Install PySpark (v 2.2.0) --> bundled with py4j (v 0.10.6)
    conda install pyspark

    # Install Geopandas (v 0.3.0) --> bundled with click, click-plugins, cligj, curl, descartes, expat, fiona, freexl, gdal, geos, hdf4, hdf5, kealib, krb5, libiconv, libnetcdf, libpq, libspatialindex, libspatialite, libtiff, libxml2, munch, openjpeg, pcre, proj4, psycopg2, pyproj, pysal, rtree, shapely, sqlalchemy, xerces-c
    conda install -c conda-forge geopandas

    # Install cartopy (v 0.15.1) --> bundled with libxslt, lxml, olefile, owslib, pillow, pyepsg, pyshp
    conda install -c conda-forge cartopy

    # Install geoplot (v 0.0.4) using pip (on Linux: be sure to use pip that comes with conda distribution!) --> bundled with seaborn
    pip install geoplot

    # Install osmnx (v 0.5.4) --> bundled with altair, bleach, branca, colorama, entrypoints, folium, geopy, html5lib, ipykernel, ipython, ipython_genutils, jedi, jsonschema, jupyter_client, jupyter_core, mistune, nbconvert, nbformat, notebook, pandoc, pandocfilters, pickleshare, prompt_toolkit, pygments, pyzmq, simplegeneric, testpath, traitlets, vega, vincent, wcwidth, webencodings
    conda install -c conda-forge osmnx

    # Install Folium (v 0.5.0) --> bundled with altair, vega
    conda install -c conda-forge folium

    # Install Dash using Pip
    pip install dash==0.19.0  # The core dash backend
    pip install dash-renderer==0.11.1  # The dash front-end
    pip install dash-html-components==0.8.0  # HTML components
    pip install dash-core-components==0.14.0  # Supercharged components
    pip install plotly --upgrade  # Plotly graphing library

Test that everything works
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can test that the installations have worked by running following commands in a Python console.
At first start the Python console:

.. code::

    (geopython-environment) python

    Type "help", "copyright", "credits" or "license" for more information.
    >>>

.. code:: python

     import numpy as np
     import pandas as pd
     import geopandas as gpd
     import scipy
     import shapely
     import matplotlib.pyplot as plt
     import pysal
     import bokeh
     import cartopy
     import statsmodels
     import sklearn
     import geoplot
     import osmnx
     import folium
     import dash


If you don't receive any errors, everything should be working!

In order to close the Python interpreter type ``exit()`` or press **Ctrl+Z** plus Return to exit.

.. code::

    (geopython-environment) >>> exit()

