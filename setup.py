import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'waitress',
    'twitter',
    'simplejson',
    'passlib'
]

setup(name='ripe-twitter',
      version='1.0',
      description='ripe-twitter',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='RIPE NCC - Adam Castle',
      author_email='acastle@ripe.net',
      url='http://www.ripe.net',
      keywords='web pyramid Twitter Wall',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="ripetwitter",
      entry_points="""\
      [paste.app_factory]
      main = ripetwitter:main
      """,
      )
