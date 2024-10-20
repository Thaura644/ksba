# kenya_school_bus_app/models/ksba_school.py
from odoo import models, fields

class KsbaSchool(models.Model):
    _name = 'ksba.school'
    _description = 'School'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    address = fields.Char(string='Address', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    website = fields.Char(string='Website')
    students = fields.One2many('ksba.child', 'school_id', string='Students')
    buses_id = fields.One2many('ksba.bus', 'school_id', string='Buses')
    attendance_ids = fields.One2many('ksba.attendance', 'school_id', string='Attendance Records')
    # driver_ids = fields.One2many('ksba.driver', 'school_id', string='Drivers')
    administrator_ids = fields.One2many('ksba.administrator', 'school_id', string='Administrators')

    def _compute_model_id(self):
        for record in self:
            record.model_id = self.env['ir.model'].sudo().search([('model', '=', 'ksba.school')], limit=1).id
