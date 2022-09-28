from odoo import models, fields, api

class Author(models.Model):
    _name='academy.author'
    _description='Author info'
    
    name = fields.Char('Nombre', required = True)
    last_name = fields.Char('Apellidos', required = True)
    libro_ids = fields.Many2many(comodel_name="academy.libro", string="Libros")
    
    active = fields.Boolean('Active', default = True)
    