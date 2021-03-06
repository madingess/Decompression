# Image Decompression Project

  See Wiki for details: https://github.com/madingess/Decompression/wiki

  Currently only a 4x super-resolution model has been implemented.

  The super-resolution model makes a call to *enhance.py*, which is not written by our team and is certified under the GNU Affero General Public License v3.0. See https://github.com/alexjc/neural-enhance file *LICENSE* for more detail.


# System Requirements 

  The program must be invoked on a Linux machine. No specific system specs are required; however, the super-resolution model relies on the machine's CPU: the faster the CPU, the faster the super-resolution will resolve.

# Dependency Installation

  The following are required for the super-resolution model. Execute the commands in order on a Linux machine.

    # Install Prerequisites
    sudo apt-get install -y gcc g++ gfortran build-essential git wget libopenblas-dev python3 python-dev python-pip python3-pip python-nose python-numpy python-scipy

    # These may be necessary if you experience errors; other python packages may need to be installed similarly.
    pip3 install -U numpy
    pip3 install -U scipy
    
    # Install Theano and Lasagne 
    pip3 install --user --upgrade --no-deps https://github.com/Theano/Theano/archive/master.zip
    pip3 install --user --upgrade --no-deps https://github.com/Lasagne/Lasagne/archive/master.zip
    

# Compilation

  None required

# Invocation

First, if you have not already, activate the provided local environment for python3.4, which has locally installed the dependencies listed in *requirements.txt*.

    source pyvenv/bin/activate
    
After the pyvenv environment has been made the active version of Python, invoke the program as follows
    
    python3 ahmm_decompression.py inputfile(s) -o outputfile(s) --algorithm=1 --device DEVICE_NAME

  Note that the super-resolution model does not accept output file specifications and only outputs .png files. Output file names are chosen according the input-file names in the format:  ahmm_enhance_INFILE_ne4x.png  (with the input-file file's extension removed)

  The device name may be one of the following: cpu, cuda, or opencl. The default is cpu. Cuda usability for Nvidia graphics cards must be enabled by visiting https://developer.nvidia.com/cuda-downloads, selecting the deb (network) installer type for your platform, and following the instructions provided.
