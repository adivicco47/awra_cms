from awrams.utils import gis
from awrams.utils.settings import CATCHMENT_SHAPEFILE
from awrams.utils.test_support import between

from awrams.utils import extents
from nose.tools import nottest,assert_almost_equal

import numpy as np



def test_shapefile_db():
    try:
        import osgeo
    except ImportError:
        return

    sdb = gis.ShapefileDB(CATCHMENT_SHAPEFILE)
    
    e = extents.get_default_extent()
    
    df = sdb.get_records_df()
    df = df.set_index('StationID')
    rec= df.loc['003303']
    
    extent = sdb.get_extent_by_field('StationID','003303',e)
    
    area_diff = np.abs(extent.areas.sum()-(rec['AlbersArea'] * 1e6))

    assert(area_diff/extent.areas.sum() < 1.0001)

    br = extent.bounding_rect()

    assert(between(rec['CentrLat'],br[0],br[1]))
    assert(between(rec['CentrLon'],br[2],br[3]))

