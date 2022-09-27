from odoo import models, fields, api

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