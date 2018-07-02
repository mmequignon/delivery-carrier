# Copyright 2015 Swisslux
# Copyright 2016 Yannick Vaucher (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResPartnerTitle(models.Model):
    _inherit = 'res.partner.title'

    salutation = fields.Char('Salutation', translate=True)