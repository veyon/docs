#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import os


# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst'

master_doc = os.getenv('INDEX', 'index')

# General information about the project.
project = 'Veyon'
copyright = '2017-2020, Veyon Solutions'
author = 'Veyon Community'

title = os.getenv('TITLE', 'Veyon Documentation')
version = os.getenv('VERSION', '4.5.0')
# The full version, including alpha/beta/rc tags.
release = version

language = os.getenv('LANGUAGE', None)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'default'

html_static_path = ['_static']

def setup(app):
	app.add_css_file("theme_overrides.css")


# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': os.getenv('PAPER', 'letterpaper'),

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'preamble': r'''
\usepackage{libertine}
\usepackage[protrusion=true,babel=true,shrink=10,stretch=10]{microtype}
\fancypagestyle{normal}{
       \fancyhf{}
       \fancyfoot[LE,RO]{{\thepage}}
       \fancyfoot[LO,RE]{\nouppercase{%s %s}}
       \fancyhead[LE]{{\nouppercase\leftmark}}
       \fancyhead[RO]{{\nouppercase\rightmark}}
}
''' % ( title, version ),
    'babel': '\\usepackage[%s]{babel}' % (os.getenv('BABEL', 'USenglish')),
    'fontpkg': r'''
%\setmainfont[BoldFont={Linux Libertine O},ItalicFont={Linux Libertine O}]{Linux Libertine O}
%\setsansfont[BoldFont={Linux Libertine O},ItalicFont={Linux Libertine O}]{Linux Libertine O}
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'veyon.tex', title, author, 'manual'),
]


locale_dirs = [ 'locale/' ]
gettext_compact = True
gettext_location = False
gettext_additional_targets = ['index']
figure_language_filename = '{path}{language}/{basename}{ext}'

