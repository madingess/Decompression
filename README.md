# Image Decompression Project

  See Wiki for details: https://github.com/madingess/Decompression/wiki

  Currently only a 4x super-resolution model has been implemented.

  The super-resolution model makes a call to *enhance.py*, which is not written by our team and is certified under the GNU Affero General Public License v3.0. See https://github.com/alexjc/neural-enhance file *LICENSE* for more detail.


# System Requirements 

  The program must be invoked on a Linux machine. No specific system specs are required; however, the super-resolution model relies on the machine's CPU: the faster the CPU, the faster the super-resolution will resolve.

# Dependency Installation

  The following are required for the super-resolution model. Execute the commands in order on a Linux machine.

    # Install Prerequisites
    sudo apt-get install -y gcc g++ gfortran build-essential git wget libopenblas-dev python3 python-dev python-pip python-nose python-numpy python-scipy
    
    # Install Theano and Lasagne 
    pip install --user --upgrade --no-deps https://github.com/Theano/Theano/archive/master.zip
    pip install --user --upgrade --no-deps https://github.com/Lasagne/Lasagne/archive/master.zip

    # Create a local environment for Python 3.x to install dependencies here.
    python3 -m venv pyvenv --system-site-packages

    # If you're using bash, make this the active version of Python.
    source pyvenv/bin/activate

    # Setup the required dependencies simply using the PIP module.
    python3 -m pip install --ignore-installed -r requirements.txt
    
Dependencies installed in the final step can be uninstalled by simply removing the "pyvenv/" folder.
    

# Compilation

  None required

# Invocation

    python3 ahmm_decompression.py inputfile(s) -o outputfile(s) --algorithm=1

  Note that the super-resolution model does not accept output file specifications and only outputs .png files. Output file names are chosen according the input-file names in the format:  INFILE_ne4x.png  (with the input-file file's extension removed)
