# Set environment variables in Windows Power Shell
$env:FLASK_APP="personalpage.py"
$env:FLASK_DEBUG=1

# Set environment variables in Windows CMD
set FLASK_APP=personalpage.py
set FLASK_DEBUG=1

# Set environment variables in Linux
export FLASK_APP=personalpage.py
export FLASK_DEBUG=1

# Run local server for develop
python -m flask run