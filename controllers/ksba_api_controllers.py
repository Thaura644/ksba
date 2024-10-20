# kenya_school_bus_app/controllers/ksba_api_controllers.py
import json
from odoo import http
from odoo.http import request, Response


class KsbaApiController(http.Controller):
    @http.route('/kenya_school_bus_app/api/get_data', type='json', auth='public', methods=['GET'], csrf=False)
    def get_data(self, **kwargs):
        schools = request.env['ksba.school'].sudo().search([])
        schools_json = schools.read(['name', 'address', 'phone'])
        return {'schools': schools_json}

    @http.route('/kenya_school_bus_app/api/create_admin', type='json', auth='public', methods=['POST'], csrf=False)
    def create_admin(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')

        if not name or not email:
            return {'error': 'Name and Email are required'}

        admin_partner = request.env['ksba.partners'].sudo().create({
            'name': name,
            'email': email,
            'role': 'administrator'
        })

        return {'result': 'success', 'admin_id': admin_partner.id}

    @http.route('/kenya_school_bus_app/api/partners', type='json', auth='public', methods=['GET'], csrf=False)
    def get_partners(self, **kwargs):
        partners = request.env['ksba.partners'].sudo().search([])
        partner_data = partners.read(['name', 'role'])
        return {'result': 'success', 'data': partner_data}

    @http.route('/kenya_school_bus_app/api/schools', type='json', auth='public', methods=['GET'], csrf=False)
    def get_schools_api(self, **kwargs):
        schools = request.env['ksba.school'].sudo().search([])
        return schools.read(['name', 'address', 'phone'])

    @http.route('/kenya_school_bus_app/api/buses', type='json', auth='public', methods=['GET'], csrf=False)
    def get_buses_api(self, **kwargs):
        buses = request.env['ksba.bus'].sudo().search([])
        return buses.read(['name', 'license_plate', 'capacity', 'route_ids', 'current_location_latitude', 'current_location_longitude'])

    @http.route('/kenya_school_bus_app/api/routes', type='json', auth='public', methods=['GET'], csrf=False)
    def get_routes_api(self, **kwargs):
        routes = request.env['ksba.route'].sudo().search([])
        return routes.read(['name', 'description', 'start_location', 'end_location', 'distance', 'duration'])

    @http.route('/kenya_school_bus_app/api/attendances', type='json', auth='public', methods=['GET'], csrf=False)
    def get_attendances_api(self, **kwargs):
        attendances = request.env['ksba.attendance'].sudo().search([])
        return attendances.read(['name', 'attendance_date', 'bus_id', 'stop_id', 'date', 'school_id', 'child_id', 'seat_number', 'state'])
