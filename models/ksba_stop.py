# kenya_school_bus_app/models/ksba_stop.py
from odoo import models, fields, api
from geopy.geocoders import Nominatim
import logging

_logger = logging.getLogger(__name__)

class KsbaStop(models.Model):
    _name = 'ksba.stop'
    _description = 'Stop'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    route_ids = fields.Many2many('ksba.route', 'ksba_route_stop_rel', 'stop_id', 'route_id', string='Routes', tracking=True)
    sequence = fields.Integer(string='Sequence', required=True, tracking=True)
    latitude = fields.Float(string='Latitude', digits=(16,6))
    longitude = fields.Float(string='Longitude', digits=(16,6))
    bus_ids = fields.Many2many('ksba.bus', 'ksba_bus_stop_rel', 'stop_id', 'bus_id', string='Buses')
    bus_location_ids = fields.One2many('ksba.buslocation', 'stop_id', string='Bus Locations')

    @api.model
    def create(self, vals):
        if 'name' in vals and ('latitude' not in vals or 'longitude' not in vals):
            address = vals.get('name')
            geolocator = Nominatim(user_agent="ksba_app")
            location = geolocator.geocode(address)
            if location:
                vals['latitude'] = location.latitude
                vals['longitude'] = location.longitude
                _logger.info(f"Geocoded {address}: ({location.latitude}, {location.longitude})")
            else:
                _logger.warning(f"Could not geocode address: {address}")
        return super(KsbaStop, self).create(vals)

    def write(self, vals):
        if 'name' in vals and ('latitude' not in vals or 'longitude' not in vals):
            address = vals.get('name')
            geolocator = Nominatim(user_agent="ksba_app")
            location = geolocator.geocode(address)
            if location:
                vals['latitude'] = location.latitude
                vals['longitude'] = location.longitude
                _logger.info(f"Geocoded {address}: ({location.latitude}, {location.longitude})")
            else:
                _logger.warning(f"Could not geocode address: {address}")
        return super(KsbaStop, self).write(vals)
