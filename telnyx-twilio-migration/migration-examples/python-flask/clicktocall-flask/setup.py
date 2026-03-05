#!/usr/bin/env python

from setuptools import setup
setup(name='flask-clicktocall',
      version='1.1',
      author='Telnyx DevEd',
      author_email='deved@telnyx.com',
      description='A sample Flask project that implements click to call '
                  'using Telnyx.',
      include_package_data=True,
      zip_safe=False,
      packages=['clicktocall', 'tests'],
      license='MIT',
      install_requires=[
          'flask>=0.10',
          'telnyx>=2.0,<3.0',
          'tox>=1.7'
      ])
