'''
Created on 1 March 2018

@author: Amy
'''

from setuptools import setup

setup(name = "LED_Display",
      version = "0.1",
      description = "LED Assignment",
      url = " ",
      author = "Amy McCormack",
      author_email = "amy.mccormack@ucdconnect.ie",
      license = "GPL3",
      py_module = ['LED_Function'],
      entry_points=
      {
          'console_scripts':['solve_led=LED_Function:main']
      }
      )
