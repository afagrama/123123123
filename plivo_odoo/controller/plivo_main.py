
from odoo import http, tools, _
from odoo.http import request, Response
import plivo
from plivo import plivoxml

@http.route('/get_input_plivo', type='http', auth="user", methods=['GET','POST'])
def add_to_addendance(self, **kw):
	# pin = 1234
	# caller_id = 9879209876
	pin = request.params.get('Pin')
	caller_id = request.params.get('Caller_id')

	print (':::::', pin, caller_id)

	response = plivoxml.Response()
	if pin:
		try:
			attendance = request.env['hr.employee'].attendance_manual(next_action=next_action, entered_pin=pin)
			employee_id = attendance.employee_id
		except:
			body = "You have entered Wrong PIN"
			response.addSpeak(body)
			return Response(str(response), mimetype='text/xml')
	
	print ('::::::', employee_id)
	if caller_id:
		partner = request.env['res.partner'].search(['|', ('phone', '=', caller_id), ('mobile', '=', caller_id)])
		if partner:
			project_ids = request.env['project.project'].search([('partner_id', '=', partner.id)])
			if project_ids:
				for pr in project_ids:
					if pr.allow_timesheets:
						request.env['account.analytic.line'].create({'date': fields.Date.today(), 'project_id': pr.id, 'employee_id': employee_id.id, 
							'name': 'Plivo call', 'unit_amount': 0,
							'task_id': False})


			else:
				body = "You have No any project"
				response.addSpeak(body)
				return Response(str(response), mimetype='text/xml')

	return 'True'
	# return Response("TEST",content_type='text/html;charset=utf-8',status=200)
