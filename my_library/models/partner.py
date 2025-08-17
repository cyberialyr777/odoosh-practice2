from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_book_lover = fields.Boolean(string="Book Lover")

    job_position_selection = fields.Selection([
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('consultant', 'Consultant'),
    ], string="Job Position (Selection)")

    last_contact_date = fields.Date(string="Last Contact Date")