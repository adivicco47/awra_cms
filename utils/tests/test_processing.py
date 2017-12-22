from awrams.utils import datetools as dt
from awrams.utils import extents
from awrams.utils.processing.extract import extract
import os

def test_extraction():
	from awrams.utils import gis
	catchments = gis.ShapefileDB(gis.CATCHMENT_SHAPEFILE)

	e_all = extents.get_default_extent()

	e = catchments.get_extent_by_field('StationID','421103',e_all)

	period = dt.dates('jun 1990 - jan 1995')

	var_name = 'rain_day'

	path, _ = os.path.split(os.path.abspath(__file__))

	data_path = os.path.join(path,'../../test_data/calibration/')

	pattern = data_path + '/%s*' % var_name

	df = extract(data_path,pattern,var_name,{'241': e,'512': e_all.ioffset[400,400]},period)

	assert((df.index==period).all())