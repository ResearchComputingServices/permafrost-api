from permafrost_api.extensions import db, ma
from permafrost_api import permafrost_factory
from permafrost_api.models.overly_map import OverlyMap
from permafrost_api.models.settings import Settings

app = permafrost_factory.create_app(__name__)

def populate_settings():
    db.session.add(Settings({
        'category': 'lat',
        'value': '64.59482723464735',
        'type': 'float',
    }))
    db.session.add(Settings({
        'category': 'lng',
        'value': '-109.97729161437228',
        'type': 'float',
    }))
    db.session.add(Settings({
        'category': 'zoom',
        'value': '9',
        'type': 'integer',
    }))
    db.session.add(Settings({
        'category': 'opacity',
        'value': '0.4',
        'type': 'float',
    }))

def populate_overly_maps():
    db.session.add(OverlyMap({
        'title': 'Modified Surf Mat',
        'south_west_lat': 35.414058,
        'south_west_lng': -173.536619,
        'north_east_lat': 83.780308,
        'north_east_lng': -11.262369,
        'image': 'relict_900913.png',
        'active': True
    }))
    db.session.add(OverlyMap({
        'title': 'Modified Surf Mat at Mercator',
        'south_west_lat': 35.414058,
        'south_west_lng': -173.536619,
        'north_east_lat': 83.780308,
        'north_east_lng': -11.262369,
        'image': 'modified_surf_mat_Mercator.png',
        'active': True       
    }))
    db.session.add(OverlyMap({
        'title': 'Wedge Ice Mercator',
        'south_west_lat': 35.414058,
        'south_west_lng': -173.536619,
        'north_east_lat': 83.780308,
        'north_east_lng': -11.262369,
        'image': 'wedge_ice_Mercator_whiteBG.png',
        'active': True           
    }))
    db.session.add(OverlyMap({
        'title': 'Wedge Ice Mercator Transparency',
        'south_west_lat': 35.414058,
        'south_west_lng': -173.536619,
        'north_east_lat': 83.780308,
        'north_east_lng': -11.262369,
        'image': 'wedge_ice_Mercator_transparency.png',
        'active': True          
    }))

with app.app_context():
    populate_settings()
    populate_overly_maps()
    db.session.commit()