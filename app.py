import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

# Get the data from the URL
url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/ ?format=json"
df = pd.read_json(url)

# Create the Dash app
app = dash.Dash()

# Create the layout of the app
app.layout = html.Div([
  dcc.Graph(
    id="graph",
    figure={
      "data": [
        {
          "x": df["fecha"],
          "y": df["nivel"],
          "type": "line"
        }
      ],
      "layout": {
        "title": "Water Level Data"
      }
    }
  ),
  dcc.Input(
    id="username",
    placeholder="Enter your username"
  ),
  dcc.Input(
    id="password",
    placeholder="Enter your password"
  ),
  html.Button(
    id="submit",
    n_clicks=0,
     children="Submit"
  )
])

# Define a function to check the username and password
def check_credentials(username, password):
  with open("appDB.txt", "r") as f:
    for line in f:
      username_and_password = line.split(",")
      if username == username_and_password[0] and password == username_and_password[1]:
        return True
  return False

# Define a callback for the submit button
@app.callback(
  output=dash.Output("graph", "figure"),
  inputs=[dash.Input("submit", "n_clicks")]
)
def update_figure(n_clicks):
  if n_clicks > 0:
    username = app.state.username
    password = app.state.password
    if check_credentials(username, password):
      return {
        "data": [
          {
            "x": df["fecha"],
            "y": df["nivel"],
            "type": "line"
          }
        ],
        "layout": {
          "title": "Water Level Data"
        }
      }
    else:
      return {
        "data": [],
        "layout": {
          "title": "Invalid username or password"
        }
      }

# Run the app
app.run_server()
