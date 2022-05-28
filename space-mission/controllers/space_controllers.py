#-*- coding: utf-8 -*-

from odoo import http

class Academy(http.Controller):
    @http.route('/space/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/space/missions/', auth='public', website=True)
    def missions(self, **kw):
        missions = http.request.env['academy.mission'].search([])
        return http.request.render('space-mission.mission_website',{
            'missions': missions,
        })
    
    