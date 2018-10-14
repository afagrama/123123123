
from odoo import http, tools, _
from odoo import models, fields, api
from odoo.http import request
import plivo
from plivo import plivoxml
from odoo.tools.translate import _
from odoo import http
from odoo.http import request, Response
import json
import sys



class odoo_plivo_data(http.Controller):

	@http.route('/get_input_plivo/', type='http', auth="public", methods=['POST'], csrf=False)
	def add_to_addendance(self, **kw):
		# pin = 1234
		# caller_id = 9879209876
		pin = request.params.get('Pin')
		caller_id = request.params.get('Caller_id')

		print (':::::', pin, caller_id)
		employee_id = False
		# response = plivoxml.Response()
		if pin:
			try:
				employee_obj = request.env['hr.employee'].sudo().search([('pin', '=', pin)])
				print ('::::::::', employee_obj)
				attendance = employee_obj.attendance_manual(next_action="hr_attendance.hr_attendance_action_kiosk_mode", entered_pin=pin)
				employee_id = attendance['action']['attendance']['employee_id'][0]
				employee_id = employee_obj
				print (':::::::::::::', employee_id)

			except:
				body = "<Response>\
				<Speak language='en-US' loop='1' voice='WOMAN'> You have entered Wrong PIN</Speak>\
				</Response>"
				return Response(str(body), mimetype='text/xml')
				

		if employee_id:
			emp_id = employee_id.id
		else:
			emp_id = False

			
		name = 'Plivo call'
		# print ('::::::', employee_id)
		if caller_id:
			partner = request.env['res.partner'].sudo().search(['|', ('phone', 'ilike', caller_id), ('mobile', 'ilike', caller_id)])
			print (partner)
			if partner:
				project_ids = request.env['project.project'].sudo().search([('partner_id', '=', partner.id)])
				if project_ids:
					for pr in project_ids:
						if pr.allow_timesheets:
							print ('yyyyyyyyyy')
							time = request.env['account.analytic.line'].sudo().create({'date': fields.Date.today(), 'name': name, 'project_id': pr.id, 'employee_id': emp_id,  'unit_amount': 0, 'task_id': False})

							print ('?????????///', time)

			else:
				body = "<Response>\
				<Speak language='en-US' loop='1' voice='WOMAN'> You have No any Project</Speak>\
				</Response>"
				return Response(str(body), mimetype='text/xml')

		return 'True'
	# return Response("TEST",content_type='text/html;charset=utf-8',status=200)


# -*- coding: utf-8 -*-

# class odoo_public_data(http.Controller):
#     @http.route('/get/teachers', type='http', methods=['GET'], auth="public")
#     def get_teachers(self, **kwargs):
#         teacher_model = request.env['dps.teacher']
#         teacher_ids = teacher_model.sudo().search([])
#         teacher_list = {'status': 1, 'data': []}
#         try:
#             if teacher_ids:
#                 for teacher in teacher_ids:
#                     vals = {
#                         'id': teacher.id,
#                         'name': teacher.name,
#                         'email': teacher.email,
#                         'phone': teacher.phone,
#                         'school': teacher.partner_id.name,
#                     }
#                     teacher_list['data'].append(vals)
#             return json.dumps(teacher_list)
#         except Exception as e:
#             print str(e)
#             return json.dumps({'status': 0, 'data': 'Some problem with API'})
odoo_plivo_data()