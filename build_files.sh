echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install all deps in the venv
pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python manage.py collectstatic --no-input --clear

echo "BUILD END"