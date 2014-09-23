import scripts.global_variables as g
import scripts.classes.class_printable as p
import scripts.classes.class_student as s
import scripts.functions as f
import scripts.forms.form_search as search_form

def get_title():
	return 'Student Profile'
	
def get_content():
	return ""
	
	
def get_page_template():
	return 'black_template'
	
def page_additions():
	
	#if not f.user_logged_in():
		#pass
		#use a redirect function
		
	g.g_user = s.Student()
	g.g_user.setAddress("Tibanga")
	g.g_user.setID("2009-0731")
	g.g_user.setFirstName("Christopher Clint")
	g.g_user.setLastName("Pacillos")
	g.g_user.setEmailAddress("clint.pacillos@gmail.com")
	g.g_user.setPhoneNumber("09122241144")
	g.g_user.setCourse("BSEC")
	
	g.g_header.getStyleAdder().add('profile')
	g.g_header.getStyleAdder().add('search')
	
	stud_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	stud_id = g.g_user.getID()
	stud_email = g.g_user.getEmailAddress()
	stud_phone = g.g_user.getPhoneNumber()
	stud_address = g.g_user.getAddress()
	stud_course = g.g_user.getCourse()
	
	
	details_html =	'<div class="left" id="details">'
	details_html +=	"<h4>" + stud_name + "</h4>"
	details_html +=	"<p>" + stud_course + "</p>"
	details_html +=	"<p>" + stud_email + "</p>"
	details_html +=	"<p>" + stud_phone + "</p>"
	details_html +=	"<p>" + stud_address + "</p>"
	details_html +=	"<p>" + stud_id + "</p>"
	details_html += "</div>"
	details_html += '<div class="clearfix"></div>'
	
	user_pic_html =	"""
					<div class="left" id="picture">
						<img src="../spam/picture/user/student/2009-0731.png" alt="No picture found." style="width:290px;height:290px">
					</div>
					"""
					
	proflist_table = """
					<h2 class="sub-header">Professor List</h2>
						<div class="table-responsive">
						<table class="table table-striped">
						<thead>
							<tr>
							<th>#</th>
							<th>First Name</th>
							<th>Last Name</th>
							<th>Position</th>
							</tr>
						</thead>
						<tbody>
							<tr>
							<td>...</td>
							<td><a href = #>Carmelyn </td>
							<td><a href = #>Bernal </td>
							<td>... </td>
							</tr>
							<tr>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							</tr>
							<tr>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							</tr>
							<tr>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							</tr>
							<tr>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							<td>... </td>
							</tr>
						</tbody>
						</table>
						</div>
					"""
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + stud_name))
	g.g_locations.addToLocation('left_content', p.Printable(user_pic_html + details_html))
	g.g_locations.addToLocation('right_content', search_form.get_form())
	g.g_locations.addToLocation('right_content', p.Printable(proflist_table))

	
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')