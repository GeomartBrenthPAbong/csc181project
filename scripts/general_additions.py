import scripts.global_variables as g
import scripts.classes.class_menu as m
import scripts.third_party_modules.ordereddict.ordereddict as od
import scripts.classes.class_printable as p

def include_in_pages():
	# Bootstrap
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap.min')
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap-theme.min')

	# Styles for all pages

	# Scripts for all pages
	g.g_header.getScriptAdder().add('jquery-2.1.1.min')
	g.g_header.getScriptAdder().add('general')

	# Location additions for all pages

	#### navbar_brand Location addition for default template
	g.g_locations.addToLocation('navbar_brand', p.Printable('<span id="s" class="logo-item">S.</span>'
															'<span id="p" class="logo-item">P.</span>'
															'<span id="a" class="logo-item">A.</span>'
															'<span id="m" class="logo-item">M.</span>'))

	#### Footer location addition
	g.g_locations.addToLocation('footer', p.Printable('<p><b>Just SPAM it!</b></p>'))
	g.g_locations.addToLocation('footer', p.Printable('<p>Want to settle things with your professor?&nbsp;</p>'))

	if not g.g_user:
		return

	#### main_nav location addition for default template
	prof_menu_items = od.OrderedDict([
									('profmanagesched', {
												'label': 'Home',
												'link': g.g_root_path + '/index.py?page=profmanagesched'}),
									('profstudcalendar', {
												'label': 'Calendar',
												'link': g.g_root_path + '/index.py?page=profstudcalendar'}),
									('profstudmanageappt', {
												'label': 'Appointments',
												'link': g.g_root_path + '/index.py?page=profstudmanageappt'}),
									('sign_out', {
												'label': 'Sign out',
												'link': '#'})
								])

	stud_menu_items = od.OrderedDict([
									('studhome', {
												'label': 'Home',
												'link': g.g_root_path + '/index.py?page=studhome'}),
									('profstudcalendar', {
												'label': 'Calendar',
												'link': g.g_root_path + '/index.py?page=profstudcalendar'}),
									('profstudmanageappt', {
												'label': 'Appointments',
												'link': g.g_root_path + '/index.py?page=profstudmanageappt'}),
									('sign_out', {
												'label': 'Sign out',
												'link': '#'})
								])

	if g.g_user.getType() == 'Professor':
		menu_items = prof_menu_items
	else:
		menu_items = stud_menu_items

	menu = { 'ul_class': 'main-nav nav navbar-nav',
			 'li_class': 'main-menu-item',
			 'a_class': 'main-menu-item-link',
	         'inside_a': '<span></span>',
			 'menu_items': menu_items
			}

	g.g_locations.addToLocation('main_nav', m.Menu(menu))

	user_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	user_id = g.g_user.getID()
	user_email = g.g_user.getEmailAddress()
	user_phone = g.g_user.getPhoneNumber()
	user_address = g.g_user.getAddress()
	user_course_html = ""

	if g.g_user.getType() == 'Student':
		user_course_html = "<p>" + g.g_user.getCourse() + "</p>"

	details_html = """<div id="sprofile"><h1 style="font-weight: bold;">""" + \
						g.g_user.getType().upper() + \
					""" PROFILE</h1></div>"""

	user_pic_html = '<div id="picture">'
	user_pic_html += '<img src="../spam/picture/user/student/'
	user_pic_html += user_id + '.png"'
	user_pic_html += 'alt="No picture found." style="width:300px;height:300px">'
	user_pic_html += '</div>'

	details_html += user_pic_html
	details_html += '<div id="details" class="center">'
	details_html +=	'<h1 style="font-weight: bold;">' + user_name + "</h1>"
	details_html +=	user_course_html
	details_html +=	"<p>" + user_email + "</p>"
	details_html +=	"<p>" + user_phone + "</p>"
	details_html +=	"<p>" + user_address + "</p>"
	details_html +=	"<p>" + user_id + "</p>"
	details_html += "</div>"
	details_html += '<div class="clearfix"></div>'