from odoo import models, fields

class KsbaParent(models.Model):
    _name = "ksba.parent"
    _description = "Parent"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    firstname = fields.Char(string="First Name", required=True, tracking=True)
    lastname = fields.Char(string="Last Name", required=True, tracking=True)
    home_location = fields.Char(string="Home Location", required=True, tracking=True)
    phone = fields.Char(string="Phone", required=True, tracking=True)
    partner_id = fields.Many2one('ksba.partners', string="Partner", required=True)
    school_id = fields.Many2one('ksba.school', string="School", tracking=True)
    child_ids = fields.One2many('ksba.child', 'parent_id', string="Children")
