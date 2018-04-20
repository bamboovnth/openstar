from odoo import models, fields, api, _


class B2NApps(models.Model):
    _name = 'ir.module.module'
    _description = "Update apps more quickly"
    _inherit = 'ir.module.module'