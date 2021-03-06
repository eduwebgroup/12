# -*- coding: utf-8 -*-
{
    'name': "link_company_to_blog",

    'summary': """ ASOCIAR BLOGS/NOTICIAS A UNA COMPAÑIA""",

    'description': """
        Poder asociar un blog a una única compañía y que las noticias asociadas a ese blog, heredan la
compañía del blog al que pertenecen. 
    """,

    'author': "David Conde cubas",
    'website': "https://www.linkedin.com/in/david-conde-cubas-6a16a619a",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_blog'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',

        # security
        'security/blog_blog.xml',
        'security/blog_post.xml',

        # views
        'views/inherited/blog.xml',
        'views/inherited/blog_post.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
