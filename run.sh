
#rm -R venv

#python3 -m venv venv
source venv/bin/activate

cd hdbscan
pip install --no-cache-dir -r requirements.txt
python setup.py install

cd ..
python hdbscan_babysit.py
