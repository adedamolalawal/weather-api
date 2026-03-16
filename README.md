Objective
The goal of this exercise is to build a small service that integrates with an external API and demonstrate how it would be packaged, automated, and deployed in a production environment.
The focus is on engineering approach, containerization, CI/CD thinking, and cloud deployment reasoning, not on building a large system.
Part 1 – Build a Weather API Service
Create a simple Flask application that exposes the following endpoint:
 
 
GET /weather?city=<city_name>
The endpoint should fetch weather information from an external API and return a simplified response.
External API
Use the OpenWeatherMap API:
 
 
WEATHER_API_URL = https://api.openweathermap.org/data/2.5/weather
API Key: 6bbea12952412fe6c1bbb88ffb069f31
Fetch at least the following information:
city name
temperature
weather description
Example Response
 
 
{  "city": "Berlin",  "temperature": 17.2,  "description": "clear sky"}
Implementation Expectations
The implementation should demonstrate:
clear Flask application structure
proper external API request handling
basic error handling (invalid city, API failure)
configuration using environment variables (API key, port, etc.)

Part 2 – Containerize the Application
Create a Dockerfile that runs the Flask application.
The container should:
install dependencies
run the Flask application
expose the application port
use environment variables for configuration
Optional improvements:
smaller base image
non-root user
production-ready startup command
 
 
Part 3 – CI/CD Pipeline (Design Discussion)
Explain how you would design a CI/CD pipeline for this service.
Topics we may discuss:
automatically running tests
building Docker images
tagging container images
pushing images to a container registry
automatic deployment after successful builds
Possible tools:
GitHub Actions
GitLab CI
Jenkins
Azure DevOps