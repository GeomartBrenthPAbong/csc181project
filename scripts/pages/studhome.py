import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Search Professor'

def get_content():

	sprofile = """
				<div id="sprofile"><h1 style="font-weight: bold;">STUDENT PROFILE</h1></div>
			"""

	return sprofile


def get_page_template():
	return 'black_template'

def page_additions():
	rc_statement = '<span style="font-weight:bold;">&nbsp;&nbsp;&nbsp;Find your professor and make an appointment!</span>'
	rc_content = """
					<div style="width:50%; margin-left:8px; margin-top:30px;" class="input-group">
						<input id="input-search" style="font-weight:bold;" type="text" class="form-control" placeholder="Professor Name">
  						<div class="input-group-btn">
    						<button id="btn-search" type="button" class="btn btn-primary btn-large">Search</button>
  						</div>
					</div>
					<div style="margin-left:8px; margin-top:20px;" class="panel panel-default">
						<div class="panel-heading"><b>Professors</b></div>
						<div class="panel-body">
							<table class="table table-hover">
								<thead>
									<tr>
										<th>Name</th>
										<th>College</th>
										<th>Department</th>
									</tr>
						  		</thead>
						  		<tbody id="proflist" data-link="row" class="rowlink"></tbody>
							</table>
						</div>
					</div>
					<div style="margin-left:15px; margin-top:10px;">
						<button id="btn-prev" type="button" class="btn btn-primary btn-large">Previous</button>
						<button id="btn-next" type="button" class="btn btn-primary btn-large">Next</button>
						<span id="page" style="color:black; font-weight:bold;">Page 1</span>
					</div>
				"""
	content_list = g.g_locations.getContentsAtLocation('main_nav')

	if not content_list is None and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.addMenuItem('studhome', 'Home', g.g_root_path + '/index.py?page=studhome')
		main_nav.setAsActive('studhome')

	g.g_header.getScriptAdder().add('proflist')
	g.g_header.getStyleAdder().add('profile')
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + g.g_user.getFirstName()))
	g.g_locations.addToLocation('right_content', p.Printable(rc_statement))
	g.g_locations.addToLocation('right_content', p.Printable(rc_content))
