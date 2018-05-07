# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal 
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "e4866bd6c95e434df6389ddc22b10677a7cbf6aa5647e4e267421d1eeda46acf43c6e8c5116e8abf8b5ea5e7aef79b97d56f242a35887fb2dd4ce60e8bc31c16"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")
