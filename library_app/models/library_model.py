import requests
from odoo import models, fields, api

class LibraryModel(models.Model):
    _name = 'library.model'
    _description = 'Library Model'

    name = fields.Char(string='Name', default="Test Request")
    response = fields.Text(string='API Response')

    def action_call_api(self):
        try:
            api_url = "https://jsonplaceholder.typicode.com/todos/1"
            response = requests.get(api_url)
            response.raise_for_status()
            self.response = response.text
        except requests.exceptions.RequestException as e:
            self.response = f"Error: {e}"