# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from unittest.mock import patch


class TestLibraryModelSimple(TransactionCase):

    def test_successful_api_call(self):
        record = self.env['library.model'].create({'name': 'Prueba Simple'})

        respuesta_simulada = '{"status": "ok", "message": "Data received"}'

        with patch('odoo.addons.library_app.models.library_model.requests.get') as mock_api_call:
            mock_api_call.return_value.status_code = 200
            mock_api_call.return_value.text = respuesta_simulada

            record.action_call_api()
        self.assertEqual(record.response, respuesta_simulada,
                         "The reponse contains what we expected.")

        print("Test ended!")