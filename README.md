### Quick&Dirty JPEG Image Similarity Checker v0.0.0.0 Alpha

This small console tool "qndic.py" will try to find some pairs of similar JPEG images in your folder.
Please note, that for complicated things, or if you want to do more general image processing OpenCV is a must.


### Prerequisites

This tool was successfully tested on Ubuntu Linux, but it is working on other platforms with possible minimal modifications.
You'll need "Python 3.*" and "pip3" package to be installed. Also, Python's virtual environment is highly recommended.

For Ubuntu or other Debian Linux you can use:

```sudo apt install -y python3-venv python3-pip```



### Install Dependencies

Also you need to install the following packages:

Pillow
numpy

To install them use:

```pip3 install -r requirements.txt```



### Optional Virtual Environment Steps

To create and activate "sample_environment" in "environment_directory":

```mkdir environment_directory && cd environment_directory```

```python3 -m venv sample_environment```

You can copy or move "qndic.py" and "requirements.txt" in "environment_directory" on this step.

To activate "sample_environment":

```source sample_environment/bin/activate```

And to prepare it for "qndic.py":

```pip install -r requirements.txt```

YES, use "pip" but not "pip3" in this virtual environment.

NOTE: To deactivate "sample_environment" at the end just type "deactivate".



### How To Run

Just type:

```python3 ./qndic.py```

to see some helpful information



### Command Line Arguments

usage: qndic.py [-h] --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  folder with JPEG images



### Usage Examples

```python3 ./qndic.py --path ./ds1```

```python3 ./qndic.py --path /home/user/ds2```

This will print filenames of similar pairs of images in a given folder.



### Sample Data & Testing

You can get some samples to test from the neighbour repository:
 
```https://github.com/f-nikolay/qndic_data```



### KUDOs

Deeply inspired by:

https://www.pyimagesearch.com/2014/09/15/python-compare-two-images

https://www.raspberrypi.org/forums/viewtopic.php?t=195181#p1221857

https://www.quora.com/How-does-the-perceptual-image-hashing-work-and-how-do-you-implement-it

etc.



### (C)

Absolutely no copyrights ;)



### NF ###
