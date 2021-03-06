import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly as py



# external JavaScript files
external_scripts = [
{
'src' : 'https://code.jquery.com/jquery-3.3.1.slim.min.js', 
'integrity' : 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo', 
'crossorigin' : 'anonymous'
}, 
{
'src' : 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js', 
'integrity' : 'sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut', 
'crossorigin' : 'anonymous'

}, 
{
'src' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js', 
'integrity' : 'sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k',
'crossorigin' : 'anonymous'
},
{
'src' : 'https://use.fontawesome.com/releases/v5.3.1/js/all.js'
},
{
'src' : 'https://code.jquery.com/jquery-3.3.1.js',
'integrity' : 'sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=',
'crossorigin' : 'anonymous'
}]

# external CSS stylesheets
external_stylesheets = [
{
'rel' : 'stylesheet', 
'href' : 'https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css',
'integrity' : 'sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS',
'crossorigin' : 'anonymous'
}, 
{
'rel' : 'stylesheet',
'href' : 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css',

}]


app = dash.Dash(__name__, external_scripts=external_scripts, external_stylesheets=external_stylesheets) 

# add tags to header
app.head = [
html.Meta(
	name = 'viewport', 
	content = 'width=device-width, initial-scale=1'
	),
html.Meta(
	charSet = 'utf-8'
	)]

# add tags to footer
app.footer = []



app.layout = html.Section([
	html.Div([
		html.Div([
			html.H1(['Hello world !'], className='col-12 d-flex justify-content-center text-warning bg-dark font-weight-lighter m-5 align-content-center flex-wrap'), 
			html.Div(['btn'], className = 'btn btn-secondary m-5'),
			html.Div(['bulma Primary'], className = 'button is-danger m-5')
			], className='row'), 
		html.Div([
			html.Div([
				html.H1(['second row'.title()]),
				html.Canvas(['Canvas Children'], id = 'BarChart', width = '400', height = '400'),
				html.Script(['jQuery(document).ready(function($) {BarChart();});'], src = 'BarChart.js', type='text/javascript')
				], className = 'col-4')
			], className = 'row')
		], className = 'container'
		)
			], className = 'hero is-dark is-fullheight'#, style = {'background-color' : '#250000'}
			)




if __name__ == '__main__':
	app.run_server(debug = True)