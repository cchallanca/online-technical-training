from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Libro(models.Model):
    _name='academy.libro'
    _description='Info libro'
    
    name = fields.Char(string='Tìtulo', required = True)
    isbn = fields.Char(string='ISBN', required = True)
    abstract = fields.Text(string='Resumen')
    date_publish = fields.Date(string='Fecha de publicación')
    nota = fields.Text(string='Nota')
    author_ids = fields.Many2many(comodel_name='academy.author', string = 'Autor')
    alquiler_id = fields.Many2one(comodel_name="academy.alquiler", string="Alquiler")
    
    active = fields.Boolean('Active', default = True)
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if self.isbn and len(self.isbn)!= 13:
            raise ValidationError('ISBN must contains 13 characters')
            
    """"@api.constrains('isbn')
    def _check_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError('ISBN must contains 13 characters')
            """