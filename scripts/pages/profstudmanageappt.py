import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Your Appointments'

def get_content():
	return ''

def get_page_template():
	return 'black_template'

def page_additions():
	import scripts.functions as f
	#user_type = g.g_user.getType()

	if not f.user_logged_in():
		g.g_notification_title = 'Permission denied'
		g.g_notification_msg = 'You have no permission to access this page. ' \
							   'Please <a href="' +g.g_root_path + '/index.py' + '">sign in</a> first.'

		f.redirect(g.g_root_path + '/index.py?page=notification')
		return

	if g.g_user.getType() == 'Professor':
		name_head = 'Student Name'
	else:
		name_head = 'Professor Name'

	rc_statement = '<span style="font-weight:bold;">&nbsp;&nbsp;&nbsp;Manage your appointments here!<br></br></span>'
	rc_content = """<div id = "btn-gen" "style="margin-left:15px; margin-top:10px;">
						<button id="btn-pending" type="button" class='button'>Pending</button>
						<button id="btn-approved" type="button" class='button'>Approved</button>
					</div>
					<div style="margin-left:8px; margin-top:20px;" class="panel panel-default">
						<div class="panel-heading" id = "appt-stat" style = "font-weight: bold;"></div>
						<div class="panel-body">
							<table id = "appt-table" class="table table-hover">
								<thead>
									<tr>
										<th>""" + name_head + """</th>
										<th>Requested Time</th>
										<th>Requested Date</th>
										<th>Details</th>
									</tr>
					  		    </thead>
					  		    <tbody id="apptlist" data-link="row" class="rowlink"></tbody>
							</table>
						</div>
					</div>
					<div id = "btn-page" style="margin-left:15px; margin-top:10px;">
						<button id="btn-prev" type="button" class="btn btn-primary btn-large">Previous</button>
						<button id="btn-next" type="button" class="btn btn-primary btn-large">Next</button>
						<span id="page" style="color:black; font-weight:bold;">Page 1</span>
					</div>
					"""

	g.g_header.getScriptAdder().add('profstudmanageappt')
	g.g_header.getStyleAdder().add('profile')
	g.g_header.getStyleAdder().add('button')
	g.g_locations.addToLocation('head_title', p.Printable("Appointments - " + g.g_user.getFirstName()))
	g.g_locations.addToLocation('right_content', p.Printable(rc_statement))
	g.g_locations.addToLocation('right_content', p.Printable(rc_content))

	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if content_list and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('appointments')