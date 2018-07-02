# Copyright 2015 Swisslux
# Copyright 2016 Yannick Vaucher (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class ResBetterZip(models.Model):
    _inherit = 'res.better.zip'

    region_id = fields.Many2one('res.partner.region', "Verkaufsgebiet")
    user_id = fields.Many2one('res.users', "Kundenberater")