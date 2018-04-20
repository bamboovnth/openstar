from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'openstar.wizard'

    def _default_sessions(self):
        return self.env['openstar.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openstar.session',
                                   string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendeesss")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
