from odoo import fields, models, api, _
import plivo


class ResConfigSettings(models.TransientModel):
	_inherit='res.config.settings'

	auth_id = fields.Char('Auth ID')
	auth_token = fields.Char('Auth Token')
	


	@api.multi
	def set_values(self):
		super(ResConfigSettings, self).set_values()
		params = self.env['ir.config_parameter'].sudo()
		params.set_param('plivo_odoo.auth_id', self[0].auth_id)
		params.set_param('plivo_odoo.auth_token', self[0].auth_token)
		
	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		params = self.env['ir.config_parameter'].sudo()
		res.update(
			auth_id=params.get_param('plivo_odoo.auth_id', default=''),
			auth_token=params.get_param('plivo_odoo.auth_token', default=''),
		)
		return res

# class ProjectProject(models.Model):
# 	_inherit = 'project.project'


# 	auth_id = fields.Char('Auth ID')
# 	auth_token = fields.Char('Auth Token')




# p = plivo.RestClient(auth_id, auth_token)
# params = {
    # 'to': '2222222222',    # The phone numer to which the call will be placed
    # 'from' : '1111111111', # The phone number to be used as the caller id

    # answer_url is the URL invoked by Plivo when the outbound call is answered
    # and contains instructions telling Plivo what to do with the call
    # 'answer_url' : "https://s3.amazonaws.com/static.plivo.com/answer.xml",
    # 'answer_method' : "GET", # The method used to call the answer_url

    # Example for asynchronous request
    # callback_url is the URL to which the API response is sent.
#     'callback_url' => "http://myvoiceapp.com/callback/",
#     'callback_method' => "GET" # The method used to notify the callback_url.
# }

# Make an outbound call and print the response
# response = p.make_call(params)
# print str(response)


# https://stackoverflow.com/questions/19139835/plivo-python-message


# @app.route('/getCalls', methods=['GET'])
# def getCalls():
#   url = 'https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Calls/.json'
#   request = requests.get(url, auth=(YOUR_ACCOUNT_SID, YOUR_AUTH_TOKEN)

#   resp = Response(response=request.text,
#                   status=200,
#                   mimetype="application/json")
#   return resp



# @http.route('/', type='http', auth="public", website=True)

# localhost:8069/login?db=nas&login=&key=

# PHLO Application - Start - Incoming Call= IVR- Input from user (pin) - 
# Request to odoo with caller Id an dpin

# In odoo
# Admin login with pin
# In project search Customer with caller Id
# Search again on meetings and schedule
# If any found Attend time - 
# Response msg to Plivo.

