## Microservice
IBM Cloud Microservice Starter for Python


### Summary

The IBM Cloud Microservice Starter in Python provides a micro service endpoint related marketing

To deploy this application to IBM Cloud using a toolchain click the **Create Toolchain** button.
[![Create Toolchain](https://console.ng.bluemix.net/devops/graphics/create_toolchain_button.png)](https://console.ng.bluemix.net/devops/setup/deploy/)

### Requirements
* [Python](https://flask-restful.readthedocs.io/en/latest/installation.html)
* [Flask](https://flask-restful.readthedocs.io/en/latest/installation.html)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

### Configuration
Capabilities are provided through libraries in the requirements.txt file.

### Run

To build and run the application:
1. `Main.py`

To run the application in Docker use the Docker file called `Dockerfile`.

### Build and run image
1. docker build -f Dockerfile -t clk-marketing-social-api:latest .
2. docker run -d -p 8090:8080 --name clk-marketing-social-api clk-marketing-social-api:latest

### Endpoints

The application exposes the following endpoints:

1. `curl --location --request POST 'http://localhost:8080/marketing/api/social/link' \
--data-raw '{
	"url":"https://www.bohoblu.com"
}'`
    