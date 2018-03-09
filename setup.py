from setuptools import setup

setup(name = "Display",
      version = "0.1",
      description = "LED Assignment",
      url = " ",
      author = "Amy McCormack",
      author_email = "amy.mccormack@ucdconnect.ie",
      license = "GPL3",
      py_module = ['LED_Function', 'main'],
      packages=['LED_Display','Tests'],
      entry_points=
      {
          'console_scripts':['solve_led=LED_Display.LED_Function:main']
      }
      )
