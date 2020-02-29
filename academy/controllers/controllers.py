# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):

    @http.route(['/my/','/my/home/'], auth='user', website=True)
    def index(self, **kw):
        # instructors = http.request.env['res.partner'].sudo() # ici si on fait sudo() on va recevoir tt les res.partner
        # instructors = http.request.env['res.partner'].sudo()
        id_user = http.request.env.user.partner_id.id
        instructors = http.request.env['res.partner'].search([('id', '=', id_user)])
        ins_nom = instructors.name
        ins_sessions = instructors.session_count
        slugg = instructors.id

        # print(http.request.env.user.partner_id.id)

        return http.request.render('academy.index', {
            # 'instructors': instructors.search([])
            'ins_nom' : ins_nom,
            'ins_sessions' : ins_sessions,
            'slugg' : slugg
        })

    @http.route(['/my/<model("res.partner"):instructor>/',
                 '/my/home/<model("res.partner"):instructor>/'], auth='user', website=True)
    def instructor(self, instructor):
        sessions = list(instructor.session_ins)
        return http.request.render('academy.infos', {
            'session': sessions
        })

    @http.route(['/my/session/<model("academy.session"):session>/',
                 '/my/home/session/<model("academy.session"):session>/'], auth='user', website=True)
    def session(self, session):
        return http.request.render('academy.sessionsForm', {
            'session': session
        })

    @http.route(['/my/session/edit/<model("academy.session"):session>/',
                 '/my/home/session/edit/<model("academy.session"):session>/'], auth='user', website=True)
    def sessionEdit(self, session):
        return http.request.render('academy.sessionsFormEdit', {
            'session': session
        })

    @http.route(['/my/session/edit/done/', '/my/home/session/edit/done/'], auth='user', website=True)
    def sessionEditDone(self, ses_id, **kw):
        session = http.request.env['academy.session'].search([('id', '=', ses_id)])

        session.name = kw['name']
        session.duration = kw['duration']
        session.start_date = kw['date']
        session.seats = kw['seats']
        session.taken_seats = kw['tseats']

        return http.request.redirect('/my/home')


