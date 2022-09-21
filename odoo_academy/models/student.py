# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Student(models.Model):
    _name = 'academy.student'
    _description = 'Student info'
    
    name = fields.Char(string = 'Nombre', required = True)
    last_name = fields.Char(string = 'Apellido', required = True)
    age = fields.Integer(string = 'Edad', store = False)
    gender = fields.Selection(string = 'Género', selection = [('femenino', 'Femenino'), ('masculino','Masculino'), ('otro', 'Otro')])
    photo = fields.Image(string = 'Foto')
    
    active = fields.Boolean(string = 'Active', default = True)
    