from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date


class Book(models.Model):
    _name = 'library.book'
    _description = 'Library Books Register'

    name = fields.Char(string='Title', required=True)
    publication_date = fields.Date(string='Date of Publication')
    active = fields.Boolean(string='Active', default=True)

    author_id = fields.Many2one(
        comodel_name='library.author',  # El modelo al que nos conectamos
        string='Author'
    )

    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string='State', default='available', required=True)

    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('publication_date')
    def _compute_age(self):
        today = date.today()
        for book in self:
            if book.publication_date:
                delta = today - book.publication_date
                book.age = delta.days // 365
            else:
                book.age = 0

    @api.onchange('name')
    def _onchange_name(self):
        # Let's also translate the onchange logic
        if self.name and 'old' in self.name.lower():
            return {
                'warning': {
                    'title': 'Suggestion',
                    'message': 'You have written "old". Perhaps you should mark this book as inactive?'
                }
            }

    @api.model
    def create(self, vals):
        if 'name' in vals and len(vals['name']) < 5:
            raise UserError('The title is too short!')
        return super(Book, self).create(vals)