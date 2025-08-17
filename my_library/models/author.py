from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')

    book_ids = fields.One2many('library.book', 'author_id', string='Books')