# furniturepegsvisualization
this is a project that is used for bechmarking the use of canvas and svg in an interactive web application.
the web application is a visualization app that gives the customer a feeling of the final product look and feel.

how to install
----------------
- install python : [link](https://www.python.org/downloads/)
- install pip : [link](https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)
- clone the project
- mkvirtualenv pegs (optional: to create a virtual environment)
- workon pegs (optional: to activate the virtual environment created)
- install the requirement files :
pip install -r requirements.txt
- create the database tables :

<code>./manage.py migrate </code>
- load the first data to the datbase :

<code>./manage.py loaddump dump.json </code>
