from odoo import models, fields, api

class Author(models.Model):
    _name='academy.author'
    _description='Author info'
    
    name = fields.Char('Nombre', required = True)
    last_name = fields.Char('Apellidos', required = True)
    
    active = fields.Boolean('Active', default = True)
    
    def getRecords (self):
        for record in sel:
            print(record)