"""
Central location for all hard coded data needed for tests.
"""

DOWNLOAD_OPTIONS_FROM_ALL_SERVICES = {
    'svc://noaa-ncep:ncep_gfs': {'title': 'NCEP GFS Service Download Options',
                                  'properties': [{'name': 'date',
                                                  'type': 'String',
                                                  'description': 'YYYYMMDD',
                                                  'default': None},
                                                 {'name': 'res',
                                                  'type': 'String',
                                                  'description': 'Froecast Resolution',
                                                  'default': None},
                                                 {'name': 'cycle',
                                                  'type': 'String',
                                                  'description': 'Forecast Cycle Runtime',
                                                  'default': None},
                                                 {'name': 'start',
                                                  'type': 'String',
                                                  'description': 'Forecast start time (f###)',
                                                  'default': None},
                                                 {'name': 'end',
                                                  'type': 'String',
                                                  'description': 'Forecast end time (f###)',
                                                  'default': None},
                                                 {'name': 'format',
                                                  'type': 'ObjectSelector',
                                                  'description': 'Paramerter',
                                                  'default': None,
                                                  'range': [['enkf', 'enkf'],
                                                            ['gdas', 'gdas'],
                                                            ['gfs', 'gfs'],
                                                            ['gfsmos', 'gfsmos'],
                                                            ['sst', 'sst']]},
                                                 {'name': 'type',
                                                  'type': 'ObjectSelector',
                                                  'description': 'Parameter2',
                                                  'default': None,
                                                  'range': [['GDAS', 'GDAS'], ['GFS', 'GFS']]},
                                                 {'name': 'product',
                                                  'type': 'ObjectSelector',
                                                  'description': 'Parameter3',
                                                  'default': None,
                                                  'range': [["0.50 deg 'full' file description",
                                                             "0.50 deg 'full' file description"],
                                                            ['32km Lambert Conformal grid',
                                                             '32km Lambert Conformal grid'],
                                                            ['Atmospheric Analysis', 'Atmospheric Analysis'],
                                                            ['Atmospheric Model Data', 'Atmospheric Model Data'],
                                                            ['BUFR Sounding Files per Station',
                                                             'BUFR Sounding Files per Station'],
                                                            [
                                                                'Binary Universal Form for the Representation of meteorological data (BUFR)',
                                                                'Binary Universal Form for the Representation of meteorological data (BUFR)'],
                                                            ['GDAS', 'GDAS'],
                                                            ['GFS', 'GFS'],
                                                            ['Global longitude-latitude grid',
                                                             'Global longitude-latitude grid'],
                                                            ['MDL Extratropical Storm Surge',
                                                             'MDL Extratropical Storm Surge'],
                                                            ['MOS Aviation Product', 'MOS Aviation Product'],
                                                            ['Prepared BUFR files', 'Prepared BUFR files'],
                                                            ['Pressure Level Data', 'Pressure Level Data'],
                                                            ['Sigma Atmospheric Model Data',
                                                             'Sigma Atmospheric Model Data'],
                                                            ['Smart Initialization Guam', 'Smart Initialization Guam'],
                                                            ['Surface Analysis', 'Surface Analysis'],
                                                            ['Surface Boundary Conditions',
                                                             'Surface Boundary Conditions'],
                                                            ['Surface Flux', 'Surface Flux'],
                                                            ['T1534 Semi-Lagrangian grid',
                                                             'T1534 Semi-Lagrangian grid'],
                                                            ['Time Dependent Satellite Bias Correction',
                                                             'Time Dependent Satellite Bias Correction'],
                                                            ['Tropical Cyclone Vital Statistics',
                                                             'Tropical Cyclone Vital Statistics'],
                                                            ['WAFS/ICAO/International Exchange/FOS Grids',
                                                             'WAFS/ICAO/International Exchange/FOS Grids'],
                                                            ['World Area Forecast System',
                                                             'World Area Forecast System'],
                                                            ['global longitude-latitude grid (1.0 deg)',
                                                             'global longitude-latitude grid (1.0 deg)']]}]},
    'svc://noaa-ncep:ncep_nam': {'title': 'NCEP NAM Service Download Options',
                                 'properties': [{'name': 'date',
                                                 'type': 'String',
                                                 'description': 'YYYYMMDD',
                                                 'default': None},
                                                {'name': 'res',
                                                 'type': 'String',
                                                 'description': 'Froecast Resolution',
                                                 'default': None},
                                                {'name': 'cycle',
                                                 'type': 'String',
                                                 'description': 'Forecast Cycle Runtime',
                                                 'default': None},
                                                {'name': 'start',
                                                 'type': 'String',
                                                 'description': 'Forecast start time (f###)',
                                                 'default': None},
                                                {'name': 'end',
                                                 'type': 'String',
                                                 'description': 'Forecast end time (f###)',
                                                 'default': None},
                                                {'name': 'format',
                                                 'type': 'ObjectSelector',
                                                 'description': 'Paramerter',
                                                 'default': None,
                                                 'range': [['nam', 'nam'], ['nam_mos', 'nam_mos']]},
                                                {'name': 'type',
                                                 'type': 'ObjectSelector',
                                                 'description': 'Parameter2',
                                                 'default': None,
                                                 'range': [['NAM', 'NAM']]},
                                                {'name': 'product',
                                                 'type': 'ObjectSelector',
                                                 'description': 'Parameter3',
                                                 'default': None,
                                                 'range': [['NAM', 'NAM'],
                                                           [
                                                               'NAM - Binary Universal Form for the Representation of meteorological data (BUFR)',
                                                               'NAM - Binary Universal Form for the Representation of meteorological data (BUFR)'],
                                                           [
                                                               'NAM 104 AWIPS Grid (N. Hemisphere polar stereographic grid (NGM Super C grid))',
                                                               'NAM 104 AWIPS Grid (N. Hemisphere polar stereographic grid (NGM Super C grid))'],
                                                           [
                                                               'NAM 181 AFWA Grid - Central America/Caribbean (12-km Resolution)',
                                                               'NAM 181 AFWA Grid - Central America/Caribbean (12-km Resolution)'],
                                                           ['NAM 182 AFWA Grid - North Pacific  (12-km Resolution)',
                                                            'NAM 182 AFWA Grid - North Pacific  (12-km Resolution)'],
                                                           [
                                                               'NAM 190 Grid - CONUS (Staggered B-grid on rotated lat/lon grid using the 60 NAM hybrid levels(NAM 12km Domain))',
                                                               'NAM 190 Grid - CONUS (Staggered B-grid on rotated lat/lon grid using the 60 NAM hybrid levels(NAM 12km Domain))'],
                                                           [
                                                               'NAM 190 Grid - CONUS (Staggered B-grid on rotated latitude/longitude grid (NAM 12km Domain))',
                                                               'NAM 190 Grid - CONUS (Staggered B-grid on rotated latitude/longitude grid (NAM 12km Domain))'],
                                                           [
                                                               'NAM 195 Grid over Puerto Rico (2.5-km Resolution) (NAM Smartinit for NDFD)',
                                                               'NAM 195 Grid over Puerto Rico (2.5-km Resolution) (NAM Smartinit for NDFD)'],
                                                           [
                                                               'NAM 196 Grid over Hawaii (2.5-km Resolution) (NAM Smartinit for NDFD)',
                                                               'NAM 196 Grid over Hawaii (2.5-km Resolution) (NAM Smartinit for NDFD)'],
                                                           [
                                                               'NAM 197 Grid - CONUS (5-km Resolution) (NAM Smartinit for NDFD)',
                                                               'NAM 197 Grid - CONUS (5-km Resolution) (NAM Smartinit for NDFD)'],
                                                           [
                                                               'NAM 198 Grid over Alaska (6-km Resolution) (NAM Smartinit for NDFD)',
                                                               'NAM 198 Grid over Alaska (6-km Resolution) (NAM Smartinit for NDFD)'],
                                                           ['NAM 211 AWIPS Grid - Regional - CONUS (81-km Resolution)',
                                                            'NAM 211 AWIPS Grid - Regional - CONUS (81-km Resolution)'],
                                                           [
                                                               'NAM 212 AWIPS Grid - Regional - CONUS (Double Resolution (40-km Resolution))',
                                                               'NAM 212 AWIPS Grid - Regional - CONUS (Double Resolution (40-km Resolution))'],
                                                           ['NAM 215 AWIPS Grid - CONUS (20-km Resolution)',
                                                            'NAM 215 AWIPS Grid - CONUS (20-km Resolution)'],
                                                           ['NAM 216 AWIPS Grid - Regional - Alaska (45-km Resolution)',
                                                            'NAM 216 AWIPS Grid - Regional - Alaska (45-km Resolution)'],
                                                           [
                                                               'NAM 218 AWIPS Grid - CONUS (12-km Resolution; full complement of pressure level fields and some surface-based fields)',
                                                               'NAM 218 AWIPS Grid - CONUS (12-km Resolution; full complement of pressure level fields and some surface-based fields)'],
                                                           [
                                                               'NAM 218 AWIPS Grid - CONUS (12-km Resolution; full complement of surface-based fields)',
                                                               'NAM 218 AWIPS Grid - CONUS (12-km Resolution; full complement of surface-based fields)'],
                                                           [
                                                               'NAM 218 AWIPS Grid - CONUS - (12-km Resolution) (GOES Simulated Brightness Temp.)',
                                                               'NAM 218 AWIPS Grid - CONUS - (12-km Resolution) (GOES Simulated Brightness Temp.)'],
                                                           [
                                                               'NAM 221 AWIPS Grid - High Resolution North American Master Grid (32-km Resolution)',
                                                               'NAM 221 AWIPS Grid - High Resolution North American Master Grid (32-km Resolution)'],
                                                           [
                                                               'NAM 221 AWIPS Grid - N. American Master (32-km Resolution) (GOES Simulated Brightness Temp.)',
                                                               'NAM 221 AWIPS Grid - N. American Master (32-km Resolution) (GOES Simulated Brightness Temp.)'],
                                                           [
                                                               'NAM 242 AWIPS Grid - Over Alaska (11.25 KM Resolution; full complement of pressure level fields and some surface-based fields)',
                                                               'NAM 242 AWIPS Grid - Over Alaska (11.25 KM Resolution; full complement of pressure level fields and some surface-based fields)'],
                                                           [
                                                               'NAM 242 AWIPS Grid - Over Alaska (11.25 KM Resolution; full complement of surface-based fields)',
                                                               'NAM 242 AWIPS Grid - Over Alaska (11.25 KM Resolution; full complement of surface-based fields)'],
                                                           [
                                                               'NAM 243 AWIPS Grid - Eastern North Pacific (40-km Resolution) (GOES Simulated Brightness Temp.)',
                                                               'NAM 243 AWIPS Grid - Eastern North Pacific (40-km Resolution) (GOES Simulated Brightness Temp.)'],
                                                           [
                                                               'NAM 243 AWIPS Grid - Eastern North Pacific (Double Resolution (40-km Resolution))',
                                                               'NAM 243 AWIPS Grid - Eastern North Pacific (Double Resolution (40-km Resolution))'],
                                                           ['NAM IMS Snow Grid (24-km Resolution)',
                                                            'NAM IMS Snow Grid (24-km Resolution)'],
                                                           ['NAM MOS', 'NAM MOS'],
                                                           [
                                                               'NAM NEST - FIRE WEATHER (1.33 km CONUS / 1.5 km Alaska Resolution)',
                                                               'NAM NEST - FIRE WEATHER (1.33 km CONUS / 1.5 km Alaska Resolution)'],
                                                           ['NAM NEST over ALASKA (6 km Resolution - Grid 198)',
                                                            'NAM NEST over ALASKA (6 km Resolution - Grid 198)'],
                                                           ['NAM NEST over CONUS (5 km Resolution - Grid 227)',
                                                            'NAM NEST over CONUS (5 km Resolution - Grid 227)'],
                                                           ['NAM NEST over HAWAII (3 km Resolution - Grid 196)',
                                                            'NAM NEST over HAWAII (3 km Resolution - Grid 196)'],
                                                           ['NAM NEST over PUERTO RICO (3 km Resolution - Grid 194)',
                                                            'NAM NEST over PUERTO RICO (3 km Resolution - Grid 194)']]}]}
}

SERVICES_CATALOG_COUNT = [
    ('svc://noaa-ncep:ncep_gfs', 1, 1),
    ('svc://noaa-ncep:ncep_nam', 1, 1),
]

CACHED_SERVICES = [s[0] for s in SERVICES_CATALOG_COUNT]

SERVICE_DOWNLOAD_OPTIONS = [
    ('svc://noaa-ncep:ncep_gfs/ncep', {'date': '20180921', 'res': "1p00", 'cycle': '00', 'start': '000', 'end': '000', 'format': 'gfs', 'type': 'GFS', 'product': "Global longitude-latitude grid"}),
]