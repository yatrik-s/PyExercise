from distutils.core import setup
import py2exe

setup(
   options = { "py2exe": {"dll_excludes": ["MSVCP90.dll"] }},
   console=['Demo.py'])

# Run this script from command using:
#    python setup.py py2exe

