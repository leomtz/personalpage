# Set environment variables in Windows
$env:FLASK_APP="personalpage.py"
$env:FLASK_DEBUG=1

# Set environment variables in Linux
export FLASK_APP=personalpage.py
export FLASK_DEBUG=1

# Run local server for develop
python -m flask run