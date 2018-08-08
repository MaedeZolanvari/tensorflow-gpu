# tensorflow-gpu
#Author: Maede Zolanvari

This is a tutorial on how to install TensorFlow GPU on Windows 10.

I faced many problems to get this worked, even I read and studied many tutorials. Here, I provide a complete detailed approach along with a benchmark python file (benchmark.py), so you can test the performance of your GPU after installation.

One of my PC's is Dell Alienware with M240A1 GeForce GTX 1080, the other one is HP Envy with E225W-1920 GeForce GTX 1080.

1. The very first step is to make sure you have the right NVIDIA driver installed (the right version number), if you don’t make sure of it, you will have runtime errors at the very end.

http://www.nvidia.com/Download/index.aspx?lang=en-us

(The right driver number for my both PC's as of now is 398.82)

2. Get the right CUDA Toolkit:

https://developer.nvidia.com/cuda-downloads

In our system, only CUDA 9.0 worked, others gave compatibility issue. Install it, and make sure during installation, all CUDA components are marked to be installed, choose custom installation if needed. If you want, you can install the latest patch too.

More info here: https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/

After this step, you have to update the NVIDIA driver, because CUDA might change it to an old version: From Start menu go to Device Manager -> Display adapter -> NVIDIA GeForce, then click on update the driver (so, in our case, it will be again 398.82)

3. (Optional, but recommended to check if CUDA was installed right) install Visual Studio (VS):

https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409

Go to below path (if you chose the default path)

C:\ProgramData\NVIDIA Corporation\CUDA Samples\v9.0\1_Utilities\deviceQuery

And run the file corresponding to your VS version (Build -> Build Solution), you will get a “succeeded” message at the end and see the outputs (binary built) in the below path:

C:\ProgramData\NVIDIA Corporation\CUDA Samples\v8.0\bin\win64\Release

More info here: https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#windows

I had several errors running this, they can easily be solved, by right click on the project name and check the errors and simple googling :D

There is another way to check if CUDA was installed correctly:

Download and run CUDA-Z and run it, if it shows the CUDA is installed, it means everything is working.

4. Download the right cudNN regarding your CUDA version from the below link (you need to make a developer account and log into it to be able to download)

https://developer.nvidia.com/rdp/cudnn-download 

Copy below files from the cudNN folder to corresponding folders:

	“\cuda\bin\cudnn64_7.dll” Copy to “C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin”
	“\cuda\include\cudnn.h” Copy to “C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include\”
	“\cuda\lib\x64\cudnn.lib” Copy to “C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64”

Make sure there is a PATH defined in Environment Variables (Control Panel -> Advanced system settings), as:


	Variable Name: CUDA_PATH 
	Variable Value: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0

More info here: https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows

5. Install Anaconda:

https://www.anaconda.com/download/ 

Don’t forget to restart your computer. From here there are two ways to continue. First way is recommended.

6. First way: Go to Anaconda Navigator, first Environments then in the “base(root)”, install the basic required packages, tensoreflow-gpu, keras-gpu, numpy-devel, conda-server, conda-build-all, constructor, conda-api, conda-manager are required.

7. Second way: (You can skip this step if you followed step 6). Go to Anaconda's directory and open the Anaconda Prompt, run the following command in the opened Command Prompt

		“conda create -n tensorflow pip python=3.5”
		“activate tensorflow”
		“pip install --ignore-installed --upgrade tensorflow-gpu”
		“python”
		“import tensorflow as tf”
		“hello = tf.constant('Hello, TensorFlow!')”
		“sess = tf.Session()”
		“print(sess.run(hello))”

If the output is like below, the installation was successful:

		“Hello, TensorFlow!”

More info here: https://www.tensorflow.org/install/install_windows 

8. On my both systems, none was fast after finishing all these steps. Here was the trick that I used and it worked. I added this line to my code:

		"import tensorflow as tf"
		"with tf.device(‘/device:GPU:0’)"

You can check it out through my test file (benchmark.py) too. Open the Anaconda -> Spyder, open the attached bench.py file. This  takes only 27.9 seconds on my PC's to run.

For some reason, my program was still slow. After I changed the number of GPU to 1, and getting the error that this device is not available (my PC's both have only one GPU with ID 0), and changing it back to GPU:0, and restarting the program, made my both PC's super fast.As I said  both PC's are running the benchmark (or test) python file in about 27 seconds,which used to take more than 30 minutes with 1/10 number of loops and 1/100 smaller matrices dimensions.

On a side note, you can change the settings in NVIDIA Control Panel, forcing the PC to always use GPU (Recommened):

Right click on Desktop -> NVIDIA Control Panel -> 3D Settings -> Configure Surround PHYSX -> PHYSX settings -> Processor -> Change it from Auto-select to GeForce GTX 1080.
