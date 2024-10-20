# kenya_school_bus_app/models/res_partner.py
from odoo import models, fields, api

class KsbaPartner(models.Model):
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

    @api.model
    def set_partners(self):
        parent_partner_data = {
            'name': 'John Doe',
            'role': 'parent'
        }
        parent_partner = self.create(parent_partner_data)
        driver_partner_data = {
            'name': 'Jane Smith',
            'role': 'driver',
            'bus_id': False,  # Assign appropriate bus if available
            'school_id': False,  # Assign appropriate school if available
        }
        driver_partner = self.create(driver_partner_data)
        return {
            'parent_partner_id': parent_partner.id,
            'driver_partner_id': driver_partner.id,
        }
