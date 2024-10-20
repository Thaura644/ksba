# kenya_school_bus_app/models/ksba_route.py
from odoo import models, fields, api
import math

class KsbaRoute(models.Model):
    _name = 'ksba.route'
    _description = 'Route'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    description = fields.Text(string='Description')
    stop_ids = fields.Many2many('ksba.stop', 'ksba_route_stop_rel', 'route_id', 'stop_id', string='Stops')
    start_location = fields.Char(string='Start Location', required=True, tracking=True)
    end_location = fields.Char(string='End Location', required=True, tracking=True)
    distance = fields.Float(string='Distance (km)', compute='_compute_distance', store=True, tracking=True)
    duration = fields.Float(string='Duration (mins)', compute='_compute_duration', store=True, tracking=True)
    bus_ids = fields.Many2many('ksba.bus', string='Buses')
    google_maps_api_key = fields.Char(string='Google Maps API Key')
    map_url = fields.Char(string='Map URL', compute='_compute_map_url')

    @api.depends('stop_ids')
    def _compute_distance(self):
        for record in self:
            total_distance = 0.0
            stops = record.stop_ids.sorted(key=lambda r: r.sequence)
            for i in range(len(stops) - 1):
                lat1 = stops[i].latitude
                lon1 = stops[i].longitude
                lat2 = stops[i+1].latitude
                lon2 = stops[i+1].longitude
                if lat1 and lon1 and lat2 and lon2:
                    distance = self._haversine(lat1, lon1, lat2, lon2)
                    total_distance += distance
            record.distance = total_distance

    @api.depends('stop_ids')
    def _compute_duration(self):
        for record in self:
            # Assume average speed of 40 km/h
            average_speed = 40  # km/h
            record.duration = (record.distance / average_speed) * 60  # minutes

    def _haversine(self, lat1, lon1, lat2, lon2):
        # Calculate the great circle distance between two points
        R = 6371  # Earth radius in km
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        a = math.sin(delta_phi/2)**2 + \
            math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        return distance

    @api.depends('bus_ids', 'google_maps_api_key')
    def _compute_map_url(self):
        for record in self:
            if record.google_maps_api_key and record.stop_ids:
                # Generate a static map URL with the route
                gmaps = Client(key=record.google_maps_api_key)
                coordinates = [(stop.latitude, stop.longitude) for stop in record.stop_ids if stop.latitude and stop.longitude]
                encoded_polyline = polyline.encode(coordinates)
                map_url = gmaps.static_map(
                    size="400x400",
                    path=encoded_polyline,
                    zoom=13
                )
                record.map_url = map_url
            else:
                record.map_url = False
