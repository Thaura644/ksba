# kenya_school_bus_app/models/ksba_bus.py
from odoo import models, fields, api

class KsbaBus(models.Model):
    _name = 'ksba.bus'
    _description = 'Bus'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Bus Name", required=True, tracking=True)
    license_plate = fields.Char(string="License Plate", required=True, tracking=True)
    school_id = fields.Many2one('ksba.school', string='School', required=True, tracking=True)
    # driver_id = fields.Many2one('ksba.partners', string='Driver', domain="[('role', '=', 'driver')]", tracking=True)
    capacity = fields.Integer(string='Capacity', required=True, tracking=True)
    route_ids = fields.Many2many('ksba.route', string='Routes')
    bus_locations = fields.One2many('ksba.bus.location', 'bus_id', string='Bus Locations')
    current_location_latitude = fields.Float(string='Current Latitude', digits=(16,6))
    current_location_longitude = fields.Float(string='Current Longitude', digits=(16,6))
    child_ids = fields.One2many('ksba.child', 'bus_id', string='Assigned Children')
    stop_ids = fields.Many2many('ksba.stop', 'ksba_bus_stop_rel', 'bus_id', 'stop_id', string='Stops')

    @api.model
    def create(self, vals):
        if 'license_plate' in vals:
            vals['name'] = vals['license_plate'].upper()
        return super(KsbaBus, self).create(vals)
