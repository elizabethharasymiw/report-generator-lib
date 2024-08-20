./unix_clean.sh
python3 -m venv testing-env
source testing-env/bin/activate
pip install -r requirements.txt
pip install .
python3 ./examples/main.py
