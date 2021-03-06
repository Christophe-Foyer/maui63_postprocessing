"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
import codecs

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


### Set up tools to get version
def read(rel_path):
    here = path.abspath(path.dirname(__file__))
    with codecs.open(path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
        
        
def get_opencv_version():
    try:
        import cv2
        return cv2.__version__
    except Exception:
        return None


### Do the setup
setup(
    name='maui63_postprocessing',
    author='Christophe Foyer',
    version=get_version("maui63_postprocessing/__init__.py"),
    description='A Python 3 package for generating highlights from darknet videos for Maui63',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author_email='c@cfoyer.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords='',
    packages=find_packages(exclude=['docs']),
    python_requires='>=3.6',
    install_requires=[
        'numpy >= 1',
        'tqdm >= 1',
        'pandas >= 1',
        'filetype >= 1',
        'flask >= 1',
        'flask-socketio >= 5, <=6',
        'simple-websocket >= 0.2',
        'moviepy >= 1',
        'scipy >= 1',
        'rq >= 1',
        
        # Opencv is a bit tricky
        ('opencv-python >= 4' 
         if (get_opencv_version() is None
             or float(get_opencv_version().split('.')[0]) < 4)
         else ''
         ),
    ],
    include_package_data=True,
    package_data={
        'html templates': ['web/templates/*.html'],
    },
    project_urls={  # Optional
    },
    entry_points={
    # 'console_scripts': [
    #         'maui63_postprocessing_to_csv=maui63_postprocessing.command_line.file_output:main',
    #         ],
    }
)