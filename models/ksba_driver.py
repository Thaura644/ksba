# kenya_school_bus_app/models/ksba_driver.py
from odoo import models, fields

class KsbaDriver(models.Model):
    _name = "ksba.driver"
    _description = "Driver"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    firstname = fields.Char(string="First Name", required=True, tracking=True)
    lastname = fields.Char(string="Last Name", required=True, tracking=True)
    home_location = fields.Char(string="Home Location", required=True, tracking=True)
    phone = fields.Char(string="Phone", required=True, tracking=True)
    partner_id = fields.One2many('ksba.partners', string="Partner")
    school_id = fields.Many2one('ksba.school', string="School", tracking=True)
    # driver_id = fields.One2many('ksba.partners', string='Drivers')
