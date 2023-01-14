.. molssi_doc_theme documentation master file, created by
   sphinx-quickstart on Thu Mar 15 13:55:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


The MolSSI Documentation Theme
=========================================================

This website demonstrates the new MolSSI Documentation theme,
and explains how to migrate your project's documentation.

There are two parts to updating to the new documentaiton theme:

1. Changing your Sphinx theme.
2. Switching to the Diataxis documentation framework.

The `Getting Started <getting_started/index.html>`_ page describes how to
update your Sphinx theme. This will make your documentation use the 
`PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`_ with MolSSI customization, and explains how to achieve the
grid on the front page.

To update your documentation to follow the `Diataxis framework <https://diataxis.fr/>`_, 
we recommend reading the `How To Guide <https://diataxis.fr/how-to-use-diataxis/>`_. 
Note that it may take some time to change documentation to fit this framework, 
and that it may be relevant to varying degrees.

You should be able to achieve updating the theme without fully updating your documentation structure.

.. grid:: 1 1 2 2

    .. grid-item-card:: Getting Started
      :margin: 0 3 0 0 
      
      Learn how to update your Sphinx theme.

      .. button-link:: ./getting_started/index.html
         :color: primary
         :expand:

         To the Getting Started Guide

    .. grid-item-card::  User Guide
      :margin: 0 3 0 0
      
      To the User Guide.

      .. button-link:: ./user_guide/index.html
         :color: primary
         :expand:

         To the User Guide

    .. grid-item-card:: API Reference
      :margin: 0 3 0 0
      
      Most projects will also need an API reference.

      .. button-link:: ./api/index.html
         :color: primary
         :expand:

         To the API Reference.

    .. grid-item-card::  Developer Guide
      :margin: 0 3 0 0
      
      How to contribute to molssi_doc_theme

      .. button-link:: ./developer_guide.html
         :color: primary
         :expand:

         To the Developer Guide


.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:

   getting_started/index
   user_guide/index
   api/index
   developer_guide/index

