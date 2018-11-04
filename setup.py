#!/usr/bin/env python

from distutils.core import setup

setup(
		name="tipsytile",
		version='0.0.1',
		author='Tom Mudway',
		author_email='tmudway@physics.org',
		url='https://github.com/Ryytikki/tipsytile',
		py_modules=['tipsytile'],
		license='LICENCE',
		long_description=open('README.md').read(),
		install_requires=[
			"Numpy >= 1.5.1"
      "pytipsy >= 1.3"
			],
)
