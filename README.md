# furniturepegsvisualization
this is a project that is used for bechmarking the use of canvas and svg in an interactive web application.
the web application is a visualization app that gives the customer a feeling of the final product look and feel.

how to install
----------------
- install python : [link](https://www.python.org/downloads/)
- install pip : [link](https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)
- go to the project directory and in the terminal type :
pip install -r requirements.txt
- create the database tables :

<code>./manage.py migrate </code>
- load the first data to the datbase :

<code>./manage.py loaddump dump.json </code>
