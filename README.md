python mange.py --help
usage: mange.py [-?] {view,run,shell,runserver} ...

positional arguments:
  {view,run,shell,runserver}
    view                Runs to list tasks
    run                 Runs to execute task if you need
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit

python mange.py run --help
usage: mange.py run [-?] [-n NUM] [-s TIME] -t [TASKS [TASKS ...]] [-p APPS]

Runs to execute task if you need

optional arguments:
  -?, --help            show this help message and exit
  -n NUM, -num NUM      Execute for num
  -s TIME, -time TIME   Execute for sleep time.
  -t [TASKS [TASKS ...]], --tasks [TASKS [TASKS ...]]
                        tasks name.
  -p APPS, --apps APPS  app name.