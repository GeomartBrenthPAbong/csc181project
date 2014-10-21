import scripts.classes.class_form as form
import scripts.functions as f


def get_form():
	form_fields = [
		{
			'type': 'select',
			'name': 'from-time-hour',
			'before-field': '<table><tr>'
								'<td>From Time</td>' +\
								'<td>To Time</td>' +\
								'<td>Day</td>' +\
								'<td></td>' +\
							'</tr><tr><td id="form-time">',
			'after-field': ':',
			'value': '0',
			'options': f.generate_numbers(0, 12),
			'required': True,
			'autofocus': True,
		},
		{
			'type': 'select',
			'name': 'from-time-min',
			'options': f.generate_numbers(0, 60),
			'value': '0',
			'required': True,
			'autofocus': True,
		},
		{
			'type': 'select',
			'name': 'from-time-m',
			'after-field': '</td>',
			'options':[
				{
					'value': 'am',
					'label': 'am'
				},
				{
					'value': 'pm',
					'label': 'pm'
				}
			],
			'required': True,
			'autofocus': True,
		},
		{
			'type': 'select',
			'name': 'to-time-hour',
			'options': f.generate_numbers(0, 12),
			'before-field': '<td id="to-time">',
			'value': '0',
			'after-field': ':',
			'required': True
		},
		{
			'type': 'select',
			'name': 'to-time-min',
			'options': f.generate_numbers(0, 60),
			'value': '0',
			'required': True
		},
		{
			'type': 'select',
			'name': 'to-time-m',
			'after-field': '</td>',
			'options':[
				{
					'value': 'am',
					'label': 'am'
				},
				{
					'value': 'pm',
					'label': 'pm'
				}
			],
		    'value':'am',
			'required': True,
			'autofocus': True,
		},
		{
			'type': 'select',
			'name': 'day',
			'id': 'remember-me',
			'options': [
				{
					'value': 'mon',
					'label': 'Monday'
				},
				{
					'value': 'tue',
					'label': 'Tuesday'
				},
				{
					'value': 'wed',
					'label': 'Wednesday'
				},
				{
					'value': 'thu',
					'label': 'Thursday'
				},
				{
					'value': 'fri',
					'label': 'Friday'
				},
				{
					'value': 'sat',
					'label': 'Saturday'
				},
				{
					'value': 'sun',
					'label': 'Sunday'
				}
			],
		    'value':'mon',
			'before-field': '<td>',
			'after-field': '</td>',
		},
		{
			'type': 'submit',
			'name': 'btnAddSched',
			'class': 'btn btn-lg btn-primary btn-block',
			'before-field': '<td>',
			'after-field': '</td></tr></table>',
			'value': 'Add Schedule'
		}
	]

	new_sched_form = form.Form('add-sched-form', 'form-add-sched form', 'form-add-sched')
	new_sched_form.setFields(form_fields)

	return new_sched_form



