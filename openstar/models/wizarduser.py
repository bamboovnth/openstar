from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'openstar.wizarduser'

    # _inherits = {'a.model': 'fields.name'}  # da hinh

    # override
    # def existing(self, cr, uid, ids, x, y, z, context=None):
    #     parent_res = super(AccountInvoice, self).existing(cr, uid, ids, x, y, z, context=context)
    #     # my stuff
    #     return parent_res_plus_my_stuff
    #     `

    def _default_sessions(self):
        return self.env['openstar.user'].browse(self._context.get('active_ids'))
        self.env.invalidate_all()  # clear cache

    # name = fields.Many2many('openstar.user',
    #                         string="Name", required=True, default=_default_sessions)
    # email = fields.Many2many('res.users', string="Email")
    #
    # password = fields.Many2many('openstar.user',
    #                             string="Password", required=True, default=_default_sessions)

    name = fields.Char(requried=True, default='No name')
    # email = fields.Char(default=a_fun) default by def a_fun
    # computed_total = fields.Float(compute='compute_total')
    email = fields.Char()
    password = fields.Char()

    # phone_number=fields.Char(default='+84')

    # Self will be the current RecordSet without iteration. It is the default behavior:

    # def a_fun(self):
    #     pass
    #     return self

    @api.multi
    # validtion back end error handling by openerp.exceptions.Warning
    # @api.constrains('phone_number')
    # def _check_phone_number(self):
    #
    #     for rec in self:
    #
    #         if rec.name and len(rec.name) != 10:
    #             return True
    #         else:
    #             raise ValidationError(_("ko dung dinh dang"))
    #
    #     return True

    def subscribe(self):
        v = {
            'login': self.email,
            'name': self.name,
            'password': self.password,

        }

        self.env['res.users'].sudo().create(v)
        return {}

