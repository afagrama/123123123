{
    'name': 'Plivo PHLO Integration',
    'summary': 'Integrate odoo with Plivo PHLO',
    'author': 'Urmila Bhuva',
    'website': 'http://www.odoo.com',
    'category': 'Contacts',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base', 'project', 'hr', 'hr_attendance',
    ],
    'data': [
            'views/plivo.xml',
            
    ],
    'installable': True,
}
