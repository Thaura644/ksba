# kenya_school_bus_app/__manifest__.py
{
    'name': 'Kenya School Bus App',
    'version': '1.0',
    'sequence': -2221,
    'summary': 'School bus management system',
    'description': 'An efficient school bus management system with real-time tracking of buses, route optimization, and attendance management.',
    'author': 'James Mweni',
    'category': 'Extra Tools',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/data.xml',
        'views/ksba_bus_views.xml',
        'views/ksba_school_views.xml',
        'views/create_user_form.xml',
        'views/ksba_route_views.xml',
        'views/ksba_stop_views.xml',
        'views/ksba_child_views.xml',
        'views/ksba_driver_views.xml',
        'views/ksba_administrator_views.xml',
        'views/ksba_partner_views.xml',
        'views/ksba_attendance_record_views.xml',
        'views/ksba_bus_location_views.xml',
        'views/menu.xml',
        # 'views/ksba_menu_views.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
