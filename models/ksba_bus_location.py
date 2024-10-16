# kenya_school_bus_app/models/ksba_bus_location.py
from odoo import fields, models, api
from geopy.geocoders import Nominatim
import logging

_logger = logging.getLogger(__name__)

class KsbaBusLocation(models.Model):
    _name = 'ksba.bus.location'
    _description = 'Bus Location'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bus_id = fields.Many2one('ksba.bus', string='Bus', required=True, tracking=True)
    stop_id = fields.Many2one('ksba.stop', string='Stop', tracking=True)
    latitude = fields.Float(string='Latitude', digits=(16,6), tracking=True)
    longitude = fields.Float(string='Longitude', digits=(16,6), tracking=True)
    timestamp = fields.Datetime(default=fields.Datetime.now, tracking=True)
    map_url = fields.Char(string='Map URL', compute='_compute_map_url')

    @api.depends('latitude', 'longitude')
    def _compute_map_url(self):
        for record in self:
            if record.latitude and record.longitude:
                record.map_url = f"https://www.google.com/maps/search/?api=1&query={record.latitude},{record.longitude}"
            else:
                record.map_url = False

    @api.model
    def create_location(self, bus_id, latitude, longitude):
        self.create({
            'bus_id': bus_id,
            'latitude': latitude,
            'longitude': longitude
        })
