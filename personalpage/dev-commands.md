# Power Shell
$env:FLASK_APP="personalpage.py"
$env:FLASK_DEBUG=1
python -m flask run

# CMD
set FLASK_APP=personalpage.py
set FLASK_DEBUG=1
python -m flask run

# Linux
export FLASK_APP=personalpage.py
export FLASK_DEBUG=1
python -m flask run