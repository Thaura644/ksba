# kenya_school_bus_app/controllers/ksba_main_controllers.py
from odoo import http
from odoo.http import request, Response

class MainController(http.Controller):
    @http.route('/kenya_school_bus_app/', type='http', auth='public', website=True)
    def index(self, **kw):
        return "Welcome to the Kenya School Bus App!"

    @http.route('/kenya_school_bus_app/api/get_data_html', type='http', auth='public', methods=['GET'], csrf=False)
    def get_data_html(self, **kwargs):
        schools = request.env['ksba.school'].sudo().search([])
        schools_json = schools.read(['name', 'address'])

        html_content = '''
            <html>
            <head>
                <style>
                    .school-data {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        padding: 20px;
                    }
                    h1 {
                        margin-bottom: 10px;
                    }
                    ul {
                        list-style-type: none;
                        padding: 0;
                        margin: 0;
                    }
                    li {
                        margin-bottom: 20px;
                    }
                    strong {
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <div class="school-data">
                    <h1>Schools</h1>
                    <ul>
        '''
        for school in schools_json:
            html_content += f'''
                        <li>
                            <strong>Name:</strong> {school['name']}<br/>
                            <strong>Address:</strong> {school['address']}
                        </li>
            '''

        html_content += '''
                    </ul>
                </div>
            </body>
            </html>
        '''

        return Response(html_content, content_type='text/html')

    @http.route("/kenya_school_bus_app/api/login", type='http', auth="none", methods=['POST'], csrf=False)
    def login(self, **kwargs):
        db = kwargs.get('db')
        email = kwargs.get('email')
        password = kwargs.get('password')

        if db and email and password:
            uid = request.session.authenticate(db, email, password)
            if uid:
                return request.env['ir.http'].session_info()
            else:
                return http.Response("Invalid credentials", status=401)
        else:
            return http.Response("Missing parameters", status=400)

    @http.route('/kenya_school_bus_app/api/create_user', type='http', auth='public', methods=['POST'], csrf=False)
    def create_user(self, **kwargs):
        name = kwargs.get('name')
        role = kwargs.get('role')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        school_id = kwargs.get('school')

        if not all([name, role, email, phone, school_id]):
            return http.Response("Missing parameters", status=400)

        if role not in ['parent', 'driver', 'administrator']:
            return http.Response("Invalid role provided!", status=400)

        # Create partner
        partner = request.env['ksba.partners'].sudo().create({
            'name': name,
            'role': role,
            'email': email,
            'phone': phone,
            'school_id': int(school_id),
        })

        return http.Response("User created successfully!", status=200)

    @http.route('/kenya_school_bus_app/api/signup', type='json', auth='public', methods=['POST'], csrf=False)
    def signup_process(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        role = kwargs.get('role')
        password = kwargs.get('password')
        school_id = kwargs.get('school_id')

        if not all([name, email, role, password, school_id]):
            return {'error': 'Missing parameters'}

        if role not in ['parent', 'driver', 'administrator']:
            return {'error': 'Invalid role provided'}

        user = request.env['res.users'].sudo().create({
            'name': name,
            'login': email,
            'email': email,
            'password': password,
            'groups_id': [(6, 0, [self.env.ref(f'kenya_school_bus_app.group_{role}').id])],
        })

        partner = request.env['ksba.partners'].sudo().create({
            'name': name,
            'email': email,
            'role': role,
            'phone': kwargs.get('phone'),
            'school_id': int(school_id),
            'user_id': user.id,
        })

        return {'result': 'success', 'user_id': user.id}
