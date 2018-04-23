from odoo import models, fields, api


class User(models.Model):
    _name = 'openstar.user'



    # name = fields.Many2many('openstar.session',
    #                                string="Sessions", required=True, default=_default_sessions)
    # email = fields.Many2many('res.partner', string="Attendees")



    # @api.multi
    # def subscribe(self):
    #     for s in self.name:
    #         session.attendee_ids |= self.attendee_ids
    #     return {}

