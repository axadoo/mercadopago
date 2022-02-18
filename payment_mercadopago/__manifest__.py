{
    'name': 'MercadoPago Payment Acquirer',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'Payment Acquirer: MercadoPago',
    'version': "15.0.1.0.0",
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'description': """MercadoPago Payment Acquirer""",
    'depends': ['payment'],
    'external_dependencies': {
        'python': ['mercadopago'],
    },
    'data': [
        'views/payment_views.xml',
        'views/payment_mercadopago_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'demo': [
        'demo/payment_acquirer_demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'payment_mercadopago/static/src/js/payment_form.js',
        ],
    },
    'uninstall_hook': 'uninstall_hook',
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
