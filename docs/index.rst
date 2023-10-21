====================
atsphinx-highlightjs
====================

Overview
========

Sphinx uses `Pygments <https://pygments.org/>`_ to hilight code syntax.

This extension overrides behavior of highlighting of code for using `highlight.js <https://highlightjs.org/>`_.

Installation
============

You can install from PyPI.

.. code:: console

   pip install atsphinx-highlightjs

Usage
=====

Basic usage
-----------

When you set extension into your ``conf.py`` of documentation,
builder changes behaviors of code highlightings.

.. literalinclude:: conf.py
   :emphasize-lines: 11-13
   :language: python

Please see HTML source, this includes only ``<pre><code>`` element only
(if using Pygments, it renders parts of contents).

Configuration
=============

.. note:: Not yet exists.
