from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'academy.teachers'
    _inherit = 'mail.thread'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('academy.course', 'teacher_id', string="Courses")

