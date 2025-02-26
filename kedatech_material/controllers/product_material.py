from odoo.http import content_disposition, Controller, request, route
from odoo.osv import expression
import json

class ProductMaterialApi(Controller):

    @route(['/product-material/update'], type='json', auth="public", website=False)
    def product_material_update(self, **kwargs):
        """"
            Params:
            material_id (integer) - AS Identifier
            material_name (string)
            material_code (string)
            material_type ('cotton','jeans','fabric')
            material_buy_price (float / double / integer)
            material_supplier_name ('byron','aaron','neilson')
        """
        result = {
            'status': 'failed',
            'message': 'Update querry failed, please contact administrator for further details.'
        }
        material_id = kwargs.get('material_id',0)
        if material_id == 0:
            result['message'] = 'No material ID sended.'
            return result
        
        changed = {}

        material_name = kwargs.get('material_name','')
        if material_name:
            changed['material_name'] = material_name

        material_code = kwargs.get('material_code','')
        if material_code:
            changed['material_code'] = material_code

        material_type = kwargs.get('material_type','')
        if material_type in ['cotton','jeans','fabric']:
            changed['material_type'] = material_type

        material_buy_price = kwargs.get('material_buy_price',0)
        if material_buy_price:
            if material_buy_price < 100:
                result['message'] = 'material_buy_price value must be more than 100.'
            changed['material_buy_price'] = material_buy_price

        material_supplier_name = kwargs.get('material_supplier_name','')
        if material_supplier_name in ['byron','aaron','neilson']:
            changed['material_supplier'] = material_supplier_name
        
        if changed == {}:
            result['message'] = 'There is no params sended to update value.'
        
        update_querry = request.env['product.material'].sudo().search([('material_name','=',material_name)]).write(changed)
        if update_querry:
            result['status'] = 'success'
            result['message'] = 'Update querry success.'

        return result

    @route(['/product-material/delete'], type='json', auth="public", website=False)
    def product_material_delete(self, **kwargs):
        """"
            Params:
            material_id (should be integer number) - AS Identifier
            material_name (should be string) - AS Identifier
        """
        result = {
            'status': 'failed',
            'message': ''
        }

        material_id = kwargs.get('material_id',0)
        material_name = kwargs.get('material_name','')
        if material_id:
            result = request.env['product.material'].sudo().search([('id','=',material_id)]).unlink()
            result['status'] = 'success'
            result['message'] = _('Product Material ID:"%s" is successfully deleted' % material_id)     
        if material_name: 
            result = request.env['product.material'].sudo().search([('material_name','=',material_name)]).unlink(0)
            result['status'] = 'success'
            result['message'] = _('Product Material Name:"%s" is successfully deleted' % material_name)     
        else:
            result['message'] = 'Wrong params / No params sended.'

        return result

    @route(['/product-material/get'], type='json', auth="public", website=False)
    def product_material_get(self, **kwargs):
        """
            Params:
            material_type ('cotton','jeans','fabric')
        """
        data_returned = []
        search_domain = []
        material_type =  kwargs.get('material_type','')
        if material_type:
            search_domain = expression.AND([search_domain,[('material_type','=',str(material_type))]])

        materials = request.env['product.material'].sudo().search(search_domain)

        for mat in materials:
            data_returned.append({
                'id': mat.id,
                'material_code': mat.material_code, 
                'material_name': mat.material_name.name, 
                'material_supplier_id': mat.material_supplier.id, 
                'material_supplier_name': mat.material_supplier.name,
                'material_type': mat.material_type, 
                'material_buy_price':mat.material_buy_price})

        return {'data_returned': data_returned}