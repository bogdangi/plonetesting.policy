from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetesting.policy',
      version=version,
      description="plonetesting policy package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='https://github.com/bogdangi/plonetesting.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetesting'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plonetesting.content',
          'collective.googleanalytics',
          'plonetesting.users',
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
