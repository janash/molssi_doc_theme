Installation and MolSSI Customization
=====================================

Installing the Theme
---------------------

This documentation theme is based on the 
`PyData Sphinx theme <https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html>`_, 
with custom CSS defining colors for MolSSI. 
This theme also uses `Sphinx Design <https://sphinx-design.readthedocs.io/en/latest/>`_,
which is an extension for components like responsive
grid and cards. To properly build documentation using,
the MolSSI Doc Theme,
you will need to install both of these dependencies.

.. code-block:: bash

   conda install -c conda-forge pydata-sphinx-theme sphinx-design

If you want to add a copy button to your code blocks, you should also install 
`Sphinx CopyButton <https://sphinx-copybutton.readthedocs.io/en/latest/index.html>`_.

.. code-block:: bash

   pip install sphinx-copybutton

If you have a `yaml` file which defined your documentation, make
sure to add all of these packages as dependencies.

Obtaining and Adding Theme Assets
---------------------------------
This theme requires project logos (for light and dark theme), 
and custom CSS. 

In your docs folder, create a directory called ``_static``.
This will contain resources like images and custom CSS for your
documentation.

Add your light and dark logos to this folder.
This logo will be the one used in the upper left corner of the site.
If you'd like to use the MolSSI Light/Dark logo, you can 
find them in 
`the example repository <https://github.com/jchen0506/molssi_doc_theme/tree/main/docs/_static>`_.

Add the light and dark theme logos to the ``_static`` folder, 
and add the ``custom.css`` file in a directory under ``_static``
called ``css``.

Updating ``conf.py``
--------------------
Next, you will need to update your Sphinx configuration file,
`conf.py` to use the PyData Sphinx Theme.

First change the theme to ``pydata_sphinx_theme``. Find the line for ``html_theme`` and modify it:

.. code-block:: 
	
	html_theme = "pydata_sphinx_theme"


Add ``sphinx-design`` to the ``extensions`` section in your ``conf.py``.
You may also want to add a ``copy`` button to your code blocks. 
To add this feature, add ``sphinx-copybutton`` to your extensions.
For example, if you have created your project from the 
`MolSSI Cookiecutter <https://github.com/MolSSI/cookiecutter-cms>`_,
your ``extensions``, might look like the following after you have updated your extensions:

.. code-block:: 

   extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
	 'sphinx_design',
    'sphinx_copybutton'
   ]

Next, change the theme and add the custom CSS:

.. code-block::

   html_static_path = ['_static']

   html_css_files = [
   'css/custom.css',
   ]

You will need to configure use of the light and dark
logos in your ``conf.py`` and set other HTML
theme options. Make sure to update this with your project's
GitHub URL.


.. code-block:: 
   :linenos:

   html_theme_options = {
	"github_url": "https://github.com/YOUR_PROJECT_URL",
	"twitter_url": "https://twitter.com/MolSSI_NSF",

	"logo": {
      "image_light": "molssi_main_logo.png",
      "image_dark": "molssi_main_logo_inverted_white.png",
    },
	"show_toc_level": 2,
	"header_links_before_dropdown": 4,
	"external_links": [
      {"name": "MolSSI", "url": "https://molssi.org"}
   ],

	"secondary_sidebar_items": ["page-toc", "sourcelink"],
   }

Note that this example assumes that you are using the default
light and dark MolSSI logos.
If your project has different logos, update the appropriate names on 
``lines 6-7``. These logos should be in your ``_static`` folder
as described in the previous section.

If you would like a label next to your project logo in the navbar,
you can also set this in your ``conf.py`` file by adding another
entry to the ``logo`` section. 
The label for this site is "Docs Theme".

.. code-block::

   html_theme_options = {
    "logo": {
    	# Light and dark logo information here
        "text": "YOUR PROJECT NAME",
    }
   }

A First View of the Theme
-------------------------
You should now have the MolSSI Documentation Theme installed 
and configured.

To get a glance of how this changes your current documentation,
you can now do

.. code-block:: bash

   make clean
   make html

To view the output documentation. Note that the steps outlined
on this page will only change the theme of your documentation.
It will not change any of your text or add the four panel 
grid on the first page. 

The next page will explain how your documentation folders 
should be structured.
