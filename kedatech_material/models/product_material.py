from odoo import fields, models, _, api
from odoo.exceptions import ValidationError

class ProductMaterial(models.Model):
    _name = "product.material"
    _description = "Product Material"

    material_code = fields.Char('Material Code')
    material_name = fields.Char('Material Name')
    material_type = fields.Selection(selection=[
        ('fabric','Fabric'),
        ('jeans','Jeans'),
        ('cotton','Cotton'),
    ], string='Material Type')
    material_buy_price = fields.Float('Material Buy Price', default=100)
    material_supplier = fields.Selection(selection=[
        ('byron','Byron'),
        ('aaron','Aaron'),
        ('neilson','Neilson'),
    ], string='Related Supplier')

    @api.constrains('material_buy_price')
    def constrains_buy_price(self):
        for rec in self:
            if rec.material_buy_price < 100:
                raise ValidationError(_("Harga material buy price tidak boleh kurang dari 100"))
    
    



