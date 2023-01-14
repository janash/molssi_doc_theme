Front Page Grid
===============

The front page of this documentation example contains a four panel responsive grid which links to different 
sections of the documentation.

This grid is constructed using directives from `Sphinx Design <https://sphinx-design.readthedocs.io/en/latest/>`_

You can add this grid to your front page. 
If you follow the suggested structure of your docs, you should not have to edit this much. 
If your folders are arranged in a different way, be sure to update the text after ``button-link::``
to the appropriate values. 

You may also considering changing the text for the buttons and card descriptions.

This grid is responsive, meaning it will change the number of columns depending on your screen size.
This behavior is defined by four numbers on ``line 1``  following ``.. grid::``. 
This grid is configured for 1 column for "extra small" and "small" windows 
(<576px and 768px widths, respectively), and 2 columns for medium and large screens (992px and >1200px).

.. code-block::
    :linenos:

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

The `Sphinx Design <https://sphinx-design.readthedocs.io/en/latest/>`_ library has many other elements you
might consider using in your documentation.