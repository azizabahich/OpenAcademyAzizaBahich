from odoo import models, fields

from models import session


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

    invoice_count = fields.Integer(string="count invoice", compute="_compute_invoice_count")

    def _compute_invoice_count(self):
        self.invoice_count = self.env['account.move'].search_count([('partner_id', '=', self.id)])

    def facturer(self):
        # self.button_clicked = True
        # data= les donnes envoyes au facturaion
        data = {
            'partner_id': self.id,
            'type': 'out_invoice',
            # 'invoice_date': self.date,
            "invoice_line_ids": [],
        }
        list = []

        for line in self.session_ids:
            line1 = {
                "name": line.name,
                "quantity": line.duration,
                "price_unit": line.price_hour,

            }
            list.append(line1)
        for element in list:
            data["invoice_line_ids"].append((0, 0, element))
        invoice = self.env['account.move'].create(data)
        # invoice1 = self.env['account.move'].create(line)

    def view_invoices(self):
        invoices = self.mapped('invoice_ids')

        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        if len(invoices) > 1:
            action['domain'] = [('id', 'in', invoices.ids)]
        elif len(invoices) == 1:
            form_view = [(self.env.ref('account.view_move_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = invoices.id
        else:
            action = {'type': 'ir.actions.act_window_close'}

        context = {
            'default_type': 'out_invoice',
        }

        action['context'] = context
        return action

