from odoo import models, fields

class KsbaAdministrator(models.Model):
    _name = "ksba.administrator"
    _description = "Administrator"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    firstname = fields.Char(string="First Name", required=True, tracking=True)
    lastname = fields.Char(string="Last Name", required=True, tracking=True)
    email = fields.Char(string="Email", required=True, tracking=True)  # Add this line
    phone = fields.Char(string="Phone", required=True, tracking=True)
    partner_id = fields.Many2one('ksba.partners', string="Partner", required=True)
    school_id = fields.Many2one('ksba.school', string="School", tracking=True)
