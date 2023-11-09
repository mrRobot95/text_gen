# Adds ngrok ingress, to use add `--extension ngrok` to the command line options
#
# Parameters can be customized in settings.json of webui, e.g.:
# {"ngrok": {"basic_auth":"user:password"} }
# or
# {"ngrok": {"oauth_provider":"google", "oauth_allow_emails":["asdf@asdf.com"]} }
#
# See this example for full list of options: https://github.com/ngrok/ngrok-py/blob/main/examples/ngrok-connect-full.py
# or the README.md in this directory.
import os
from pyngrok import ngrok, conf
ngrok.set_auth_token("2XQHTe11Vkb211ZajioaKJF7BuU_7TW4DBzuMfDvjnxPzUtyD")
options = {
    "proto": "http",  # The protocol to use (http or https)
    "addr": "http://127.0.0.1:7860/",  # The local URL you want to expose
}

# Create a tunnel with the specified options
http_tunnel = ngrok.connect(**options)
print(http_tunnel.public_url)
