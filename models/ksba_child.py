# kenya_school_bus_app/models/ksba_child.py
from odoo import models, fields

class KsbaChild(models.Model):
    _name = "ksba.child"
    _description = "Child"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    firstname = fields.Char(string="First Name", required=True, tracking=True)
    lastname = fields.Char(string="Last Name", required=True, tracking=True)
    home_location = fields.Char(string="Home Location", required=True, tracking=True)
    parent_id = fields.Many2one('ksba.parent', string="Parent", tracking=True)
    school_id = fields.Many2one('ksba.school', string="School", tracking=True)
    bus_id = fields.Many2one('ksba.bus', string="Assigned Bus", tracking=True)
    attendance_ids = fields.One2many('ksba.attendance', 'child_id', string="Attendance Records")
