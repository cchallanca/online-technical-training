from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Libro(models.Model):
    _name='academy.libro'
    _description='Info libro'
    
    name = fields.Char('Tìtulo', required = True)
    isbn = fields.Char('ISBN')
    abstract = fields.Text('Resumen')
    date_publish = fields.Date('Fecha de publicación')
    nota = fields.Text('Nota')
    author_ids = fields.Many2many('academy.author', string = 'Autor')
    
    active = fields.Boolean('Active', default = True)
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if len(self.isbn) != 13:
            raise ValidationError('ISBN must contains 13 characters')