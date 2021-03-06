# Darknet Highlights & Post-Processing - Maui63

The following library processes [Maui63](http://maui63.org/)'s output data by running their darknet model on media files and combining the output with UAV logs.

_____

## Installation

To install the package, simply run:

```
pip install git+https://github.com/Christophe-Foyer/maui63_postprocessing.git
```

Or if you cloned the repo, from the root directory, run:

```
pip install .
```

Note: The example and test files assume the darknet files are in the repository's parent directory.


## TODO

- Upload video clips to rvision (waiting for API)
- Improve upload performance (asyncio or threads)
- Add option for object data format as independent columns for each object (instead of lists inside columns)
- Fix padding for start/end clips when creating highlights.
- ~~Push data to R/Vision~~
- Speed up opencv processing? (currently ~3 fps on a GTX 960m, might just be my GPU)

## Usage

The media file(s) are automatically tagged and objects added to a 
pandas dataframe.

In the case of a video input, if a directory is specified as an output, 
highlights will also be generated (see examples for highlighter args).

To create a data processing instance and run it:
```python
from maui63_postprocessing import Maui63DataProcessor 

processor = Maui63DataProcessor(
        uav_logs,       # CSV file for UAV data logs
        media_file,     # video/image file or image folder
        data_file,      # darknet .data file
        config_file,    # darknet .cfg file
        weights_file,   # darknet .weights file
        names_file,     # darknet .names file
        output_path     # ouput file/directory
        )
        
# Run the process routine
processor.process()
```

To export the dataframe to a csv file:
```python
processor.export_csv(csv_output_path)
```

To export the data to [rvision](https://rvision.rush.co.nz/):
```python
# export data with a minimum spacing of 30s between frames
processor.export_rvision(post_url, min_spacing=30)
```
The format is "https://be.uat.rvision.rush.co.nz/api/v1/alpr/camera/<_camera_>/analyse-image/?token=<camera_token>"
