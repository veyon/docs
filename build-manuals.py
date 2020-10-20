#!/usr/bin/env python3

import os
import shutil
import subprocess
import gettext

version = '4.5.0'

builds = [
	{ 'language': 'de', 'paper': 'a4paper', 'babel': 'ngerman' },
	{ 'language': 'en', 'paper': 'letterpaper', 'babel': 'USenglish' },
	{ 'language': 'es', 'paper': 'a4paper', 'babel': 'spanish' },
	{ 'language': 'fr', 'paper': 'a4paper', 'babel': 'french' },
	{ 'language': 'hu', 'paper': 'a4paper', 'babel': 'magyar' },
	{ 'language': 'it', 'paper': 'a4paper', 'babel': 'italian' },
	{ 'language': 'sl', 'paper': 'a4paper', 'babel': 'slovene' },
	{ 'language': 'uk', 'paper': 'a4paper', 'babel': 'ukrainian' },
]

for i in builds:
	for manual in [ 'admin', 'user' ]:
		language = i['language']
		print( 'Building for language "%s"' % ( language ) )
		subprocess.Popen( ['msgfmt', 'locale/%s/LC_MESSAGES/%s.po' % ( language, manual ), '-o',
			'locale/%s/LC_MESSAGES/%s.mo' % ( language, manual ) ] ).wait()
		env = os.environ.copy()
		with open('%s/index.rst' % (manual)) as f:
			title = f.readline().rstrip()
			title = gettext.translation(manual, 'locale', [language], None, True).gettext(title)
			env['TITLE'] = title;
		env['LANGUAGE'] = language
		env['PAPER'] = i['paper']
		env['INDEX'] = '%s/index' % ( manual )
		env['BABEL'] = i['babel']
		env['VERSION'] = version
		env['SPHINXOPTS'] = '-j%s' % ( os.cpu_count()+1 )
		shutil.rmtree('_build', True)
		subprocess.Popen( ['make', 'latexpdf' ], env=env ).wait()
		shutil.copyfile('_build/latex/veyon.pdf', 'veyon-%s-manual-%s_%s.pdf' % ( manual, language, version ))

