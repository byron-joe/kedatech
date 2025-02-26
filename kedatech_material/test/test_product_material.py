class ProductMaterialCommon(ProductMaterialCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_template_1 = cls.env['product.template'].create({
            'material_code': '12345',
            'material_name': 'Product 1',
            'material_type': 'fabric',
            'material_buy_price': 120,
            'material_supplier': 'byron'
        })
    
        cls.product_template_2 = cls.env['product.template'].create({
            'material_code': '23456',
            'material_name': 'Product 2',
            'material_type': 'jeans',
            'material_buy_price': 150,
            'material_supplier': 'aaron'
        })

        cls.product_template_3 = cls.env['product.template'].create({
            'material_code': '34567',
            'material_name': 'Product 3',
            'material_type': 'cotton',
            'material_buy_price': 175,
            'material_supplier': 'neilson'
        })
