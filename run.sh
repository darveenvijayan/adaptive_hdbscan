
# rm -R venv

# python3 -m venv venv
# source venv/bin/activate

# cd hdbscan
# pip install --no-cache-dir -r requirements.txt
# python setup.py install

# cd ..
# python hdbscan_babysit.py



######################### TAKE 2 ##########################################
# source venv/bin/activate
# cd hdbscan
# python my_setup.py install
# cd ..
# python hdbscan_babysit.py

# rm -R venv

# python3 -m venv venv
source venv/bin/activate

cd hdbscan
# pip install --no-cache-dir -r requirements.txt
python my_setup.py install

cd ..
python hdbscan_babysit.py
