# kenya_school_bus_app/models/ksba_partners.py
from odoo import models, fields, api

class KsbaPartners(models.Model):
    _name = 'ksba.partners'
    _description = "Partners"
    _inherit = 'res.partner'

    role = fields.Selection(
        selection=[
            ('parent', 'Parent'),
            ('driver', 'Driver'),
            ('administrator', 'Administrator'),
            ('student', 'Student'),
        ],
        string='Role',
        default='parent',
        tracking=True
    )

    parent_id = fields.Many2one(
        comodel_name='ksba.parent',
        string='Parent',
        ondelete='restrict',
        domain="[('role', '=', 'parent')]",
        tracking=True
    )

    child_ids = fields.One2many(
        comodel_name='ksba.child',
        inverse_name='parent_id',
        string='Children',
        tracking=True
    )

    bus_id = fields.Many2one(
        comodel_name='ksba.bus',
        string='Bus',
        tracking=True
    )

    school_id = fields.Many2one(
        comodel_name='ksba.school',
        string='School',
        tracking=True
    )

    attendance_ids = fields.One2many(
        comodel_name='ksba.attendance',
        inverse_name='child_id',
        string='Attendance Records',
        tracking=True
    )

    seat_number = fields.Integer(string='Seat Number', tracking=True)
