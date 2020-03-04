from odoo import models, fields


class Course(models.Model):
    _name = 'academy.course'
    _description = "OpenAcademy Course"
    _inherit = 'mail.thread'

    name = fields.Char()
    description = fields.Text()
    recherche = fields.Char()
    responsible_id = fields.Many2one("res.users", ondelete='set null',
                                     string='Responsible', index=True)
    session_ids = fields.One2many("academy.session", "course_id", string='Sessions')

    teacher_id = fields.Many2one('academy.teachers', string="Teacher")

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]