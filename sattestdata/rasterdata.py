import os
from sattestdata.testdata import TestData, TestDataError


class RasterData(TestData):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'raster'))

    # bandmaps
    bandmaps = {
        'landsat8': {
            'B1': 'coastal',
            'B2': 'blue',
            'B3': 'green',
            'B4': 'red',
            'B5': 'nir',
            'B6': 'swir1',
            'B7': 'swir2',
            'B8': 'pan',
            'B9': 'cirrus',
            'BQA': 'quality'
        },
        'sentinel2': {
            'B01': 'coastal',
            'B02': 'blue',
            'B03': 'green',
            'B04': 'red',
            'B08': 'nir',
            'B10': 'cirrus',
            'B11': 'swir1',
            'B12': 'swir2'
        }
    }

    def __init__(self, scenename):
        """ Initialize testdata for a sensor """

        if scenename not in self.list_scenes():
            raise TestDataError("no such scene %s" % scenename)

        self.scenename = scenename

        """
        examples = [f for f in os.listdir(sensor_path[0]) if os.path.isdir(os.path.join(sensor_path[0], f))]
        fields = dict(zip(['band_name', 'band_type', 'filename', 'path'], [None, None, None, None]))

        # generate the sekeleton
        self.list = {}
        for k, v in iteritems(bands[sensor]):
            temp = copy(fields)
            temp['band_name'] = k
            temp['band_type'] = v
            self.list[k] = temp

        # generate examples skeleton
        self.examples = {}
        self.files_bands = {}
        self.files = {}
        self.bands = {}
        for example in examples:
            self.examples[example] = self.list
            self.files_bands[example] = {}
            self.files[example] = []
            self.bands[example] = []

            # fill in filenames and path
            files = glob.glob(os.path.join(self.path, sensor, example, '*.*'))
            for f in files:
                search = re.search('(B.{1,3})\.', f)
                if search:
                    band = search.group(0).replace('.', '')
                    if band in self.examples[example]:
                        self.examples[example][band]['path'] = f
                        self.examples[example][band]['filename'] = os.path.basename(f)
                        self.files_bands[example][f] = [self.examples[example][band]['band_type']]
                        self.files[example].append(f)
                        self.bands[example].append(self.examples[example][band]['band_type'])

        self.names = examples
        """

    def sensor(self):
        """ Get sensor name for this scene """
        return self.scene.split('_')[0]

    @classmethod
    def sensors(cls):
        """ Get list of sensors available """
        return sorted([s.split('_')[0] for s in cls.list_scenes()])
