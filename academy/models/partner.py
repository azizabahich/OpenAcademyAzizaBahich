from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('academy.session',
                                   column1='attendee_id', column2='session_id',
                                   string='Attended sessions',
                                   readonly=True)

    session_ins = fields.One2many('academy.session', 'instructor_id', string="Session")
    session_count = fields.Integer(string="Nombre de sessions", compute='_ses_count')

    def _ses_count(self):
        self.session_count = len(self.session_ins)
