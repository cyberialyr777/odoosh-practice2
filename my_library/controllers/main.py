# controllers/main.py
from odoo import http
from odoo.http import request


class LibraryController(http.Controller):

    @http.route('/library/books', auth='public', website=True, type='http')
    def list_books(self, **kwargs):
        books = request.env['library.book'].search([('active', '=', True)])

        return request.render('my_library.book_list_template', {
            'books': books,
        })