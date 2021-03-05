from SocialLinkApi import social_link_api
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = False

API_BASE_CONTEXT_PATH = "/marketing/api/social"

app.register_blueprint(social_link_api, url_prefix='{}/link'.format(API_BASE_CONTEXT_PATH))


@app.route("{}/version".format(API_BASE_CONTEXT_PATH))
def version():
    response = {'name': 'clk-marketing-social-api', 'version': '0.0.1'}

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True)
