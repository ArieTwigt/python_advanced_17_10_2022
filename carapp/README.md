# Car app


Steps:

* Create virtual environment
    * `virtualenv venv --python=python3`

* Activate virtual environment
    * `source venv/bin/activate` (OSX/LINUX)
    * `venv\Scripts\activate` (Windows)

* Install the required packages
    * `pip install -r requirements.txt`


To setup debugging:

Mac:
* `export FLASK_APP=carapp.py`
* `export FLASK_DEBUG=True`

* `set FLASK_APP=carapp.py`
* `set FLASK_DEBUG=True`

Run the app with:

* `flask run`
