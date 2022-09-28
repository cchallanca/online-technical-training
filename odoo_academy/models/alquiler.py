# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Alquiler(models.Model):
    _name = 'academy.alquiler'
    _description = 'Alquiler Info'
    
    cliente_id = fields.Many2one(comodel_name="res.partner", string="Cliente")
    name = fields.Char(string="Title", related="cliente_id.name")
    libro_ids = fields.One2many(comodel_name="academy.libro", inverse_name="alquiler_id", string="Libros")
    fecha_alquiler = fields.Date(string="Fecha de alquiler")