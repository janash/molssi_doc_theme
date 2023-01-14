Navigation Menus and Structure
------------------------------

While using this website, you may notice several things about
this documentation theme. It contains multiple navigation menus:
`Site Navigation`_, `Section Navigation`_, 
and `Page Navigation`_.

The `Site Navigation`_ is along the top bar if your window
is expanded, or collapsed along the left side under the label *Site
Navigation* if your window is smaller.

The `Section Navigation`_ is along the left side of the screen 
if the window is expanded, or collapsed along the left side
of the window under the label *Section Navigation* if your window
is smaller.
In the framework we are proposing, each project will have four
sections - "Getting Started", "User Guide", "API Reference", and "Developer Guide".
Each of these sections can have multiple pages and their own navigation.
This structure (four sections), follows the [Diataxis model](https://diataxis.fr/) of documentation.
You may choose to implement different sections in your documentation, but we use
these as an example here.

This portion of the documentation describes how to achieve the different 
navigation types, and is applicable regardless of your section names.

The `Page Navigation`_ is along the right side of the screen if
the window is expanded, and collapsed under the button next to the
``Search`` button in the upper right if your page is smaller.

Each of these navigation types is separately set, with the Site and
Section navigation being based on your documentation structure and
Table of Contents directives.

This page outlines each type of Navigation menu and how to configure 
your sections.

Site Navigation
===============
Site navigation (along the top bar) is determined by the entries in the Table of Contents (TOC) on the
main ``index.rst`` or ``index.md`` file.

For example, the TOC for this site is shown below:

.. code-block::

    .. toctree::
        :hidden:
        :titlesonly:

        getting_started/index
        user_guide/index
        api/index
        developer_guide/index

The TOC shown above links to index pages in directories for each section. 
This allows for section navigation along the left side of the page. 
The `Section Navigation`_ section, below describes the directory structure and how to configure section navigation.

TOC Options
+++++++++++
For the front page TOC, we recommend using the options ``:hidden:``, which will hide the table of contents
from the front page, and ``:titlesonly:``. These options still allow the main site navigation bar along the 
top of the page to be populated.

Section Navigation
==================
Section navigation is acheived by creating a directory with an ``index.rst`` or ```index.md``
file which contains a table of contents (this page must be included in the main table of contents described 
previously to be indexed).

To achieve the section navigation in the left sidebar, we suggest grouping 
your documentation into different folders representing the sections. 
You should add the `rst` for section pages within these folders,
and link to them in the section TOC.

For example, for this documentation project, the directory structure
for this section is shown below:

.. code-block::

    getting_started/
    ├── docs_structure.rst
    ├── front_page.rst
    ├── index.rst
    └── installation.rst


The `section TOC <index.html>`_ for this page in the file ``index.rst``

.. code-block::
    
    .. toctree::
        :maxdepth: 2

        installation
        docs_structure
        front_page


Page Navigation
===============
Page navigation (right sidebar) is based on subheaders 
on the page. 
Each entry in the section navigation represents a level 2 header in this document.

Third Level Headers
+++++++++++++++++++
You can also see third-level headers in this side-menu. 

Fourth Level Headers
********************
Fourth Level Headers are not shown on the page navigation.



