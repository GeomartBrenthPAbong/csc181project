import scripts.global_variables as g
import scripts.classes.class_menu as m
import scripts.classes.class_student as ss
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
	g.g_locations.addToLocation('navbar_brand', p.Printable('S.<br>P.<br>A.<br>M.'))

	#### main_nav location addition for default template
	menu_items = od.OrderedDict([
									('home', {
												'label': 'Home',
												'link': g.g_root_path + '/index.py?page=home'}),
									('calendar', {
												'label': 'Calendar',
												'link': '#'}),
									('appointments', {
												'label': 'Appointments',
												'link': '#'}),
									('settings', {
												'label': 'Settings',
												'link': '#'}),
									('sign_out', {
												'label': 'Sign out',
												'link': '#'})
								])

	menu = { 'ul_class': 'main-nav nav navbar-nav',
			 'before_a': '<div>' +\
						 '<span class="adder blue-adder"></span>' +\
						 '<div class="img-coater">' +\
						 	'<span class="img"></span>'
						 '</div>' +\
						 '<span class="nav-block">%label%</span>',
			 'after_a': '</div>',
			 'li_class': 'main-menu-item',
			 'a_class': 'main-menu-item-link',
			 'menu_items': menu_items
			}

	g.g_locations.addToLocation('main_nav', m.Menu(menu))
	
	
	#test
	
	g.g_user = ss.Student()
	g.g_user.setAddress("Tibanga")
	g.g_user.setID("2009-0731")
	g.g_user.setFirstName("Christopher Clint")
	g.g_user.setLastName("Pacillos")
	g.g_user.setEmailAddress("clint.pacillos@gmail.com")
	g.g_user.setPhoneNumber("09122241144")
	g.g_user.setCourse("BSEC")
	
	user_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	user_id = g.g_user.getID()
	user_email = g.g_user.getEmailAddress()
	user_phone = g.g_user.getPhoneNumber()
	user_address = g.g_user.getAddress()
	user_course_html = ""
	
	if str(type(g.g_user).__name__) == 'Student':
		user_course_html = "<p>" + g.g_user.getCourse() + "</p>"
		
	details_html =	'<div class="left" id="details">'
	details_html +=	"<h1>" + user_name + "</h1>"
	details_html +=	user_course_html
	details_html +=	"<p>" + user_email + "</p>"
	details_html +=	"<p>" + user_phone + "</p>"
	details_html +=	"<p>" + user_address + "</p>"
	details_html +=	"<p>" + user_id + "</p>"
	details_html += "</div>"
	details_html += '<div class="clearfix"></div>'
	
	user_pic_html = '<div class="left" id="picture">'
	user_pic_html += '<img src="../spam/picture/user/student/'
	user_pic_html += user_id + '.png"'
	user_pic_html += 'alt="No picture found." style="width:290px;height:290px">'
	user_pic_html += '</div?>'
	
	g.g_locations.addToLocation('left_content', p.Printable(user_pic_html + details_html))
	g.g_locations.addToLocation('right_content', p.Printable("Search here."))