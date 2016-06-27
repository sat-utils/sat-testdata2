sat-testdata
============

.. image:: https://travis-ci.org/sat-utils/sat-testdata2.svg?branch=develop
    :target: https://travis-ci.org/sat-utils/sat-testdata2

A repository of satellite testdata for use in testing.  Currently includes samples for

- landsat8
- sentinel2


Example
+++++++


.. code-block:: python

    >>> import pprint
    >>> from sattestdata import RasterData
    >>> RasterData.list_scenes()
    ['landsat8_cloudy_full_subset', 'sentinel2_clear_full_subset'] 
    >>> data = RasterData('landsat8_cloud_full_subset')
    >>> pprint.pprint(data.filenames)
    {'small_full_data_cloudy': {'B1': {'band_name': 'B1',
                                   'band_type': 'coastal',
                                   'filename': 'test_B1.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B1.tif'},
                            'B2': {'band_name': 'B2',
                                   'band_type': 'blue',
                                   'filename': 'test_B2.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B2.tif'},
                            'B3': {'band_name': 'B3',
                                   'band_type': 'green',
                                   'filename': 'test_B3.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B3.tif'},
                            'B4': {'band_name': 'B4',
                                   'band_type': 'red',
                                   'filename': 'test_B4.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B4.tif'},
                            'B5': {'band_name': 'B5',
                                   'band_type': 'nir',
                                   'filename': 'test_B5.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B5.tif'},
                            'B6': {'band_name': 'B6',
                                   'band_type': 'swir1',
                                   'filename': 'test_B6.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B6.tif'},
                            'B7': {'band_name': 'B7',
                                   'band_type': 'swir2',
                                   'filename': 'test_B7.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B7.tif'},
                            'B8': {'band_name': 'B8',
                                   'band_type': 'pan',
                                   'filename': 'test_B8.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B8.tif'},
                            'B9': {'band_name': 'B9',
                                   'band_type': 'cirrus',
                                   'filename': 'test_B9.tif',
                                   'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_B9.tif'},
                            'BQA': {'band_name': 'BQA',
                                    'band_type': 'quality',
                                    'filename': 'test_BQA.tif',
                                    'path': '/sat-testdata/stestdata/data/landsat8/small_full_data_cloudy/test_BQA.tif'}}}
    >>> dat.bands
    >>> dat.files

About
+++++++
sat-testdata was made by `Development Seed <http://developmentseed.org>`_. The tool is available under a `MIT license </LICENSE>`_.

The data in this repository is available under a `CC0 <http://creativecommons.org/publicdomain/zero/1.0/>`_ license and contains `Copernicus Sentinel data <https://scihub.copernicus.eu/>`_ and Landsat data from the `US Geological Survey <http://landsat.usgs.gov/>`_.
