# kenya_school_bus_app/models/ksba_attendance_record.py
from odoo import fields, models, api

class KsbaAttendanceRecord(models.Model):
    _name = 'ksba.attendance'
    _description = 'Attendance Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "attendance_date desc"

    name = fields.Char('Attendance ID', readonly=True, size=32)
    attendance_date = fields.Date(
        'Date', required=True, default=lambda self: fields.Date.today(), tracking=True
    )
    bus_id = fields.Many2one('ksba.bus', string='Bus', required=True, tracking=True)
    stop_id = fields.Many2one('ksba.stop', string='Stop', required=True, tracking=True)
    date = fields.Date(default=fields.Date.today(), tracking=True)
    school_id = fields.Many2one('ksba.school', string='School', tracking=True)
    child_id = fields.Many2one('ksba.child', string="Student", tracking=True)
    seat_number = fields.Integer(string='Seat Number', required=True, tracking=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('start', 'Attendance Start'),
            ('done', 'Attendance Taken'),
            ('cancel', 'Cancelled')
        ],
        'Status', default='draft', tracking=True
    )

    def attendance_draft(self):
        self.state = 'draft'

    def attendance_start(self):
        self.state = 'start'

    def attendance_done(self):
        self.state = 'done'

    def attendance_cancel(self):
        self.state = 'cancel'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('ksba.attendance') or '/'
        return super(KsbaAttendanceRecord, self).create(vals_list)
