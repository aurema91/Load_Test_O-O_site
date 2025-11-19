This is a load testing project for the website https://opticayoftalmologia.com. Locust was used to perform the load tests; the code was written in Python.
The reports on the test can also be found in the repository
To run the test follow the guide below
Load Testing Quickstart Guide for Optica y Oftalmologia

The provided locustfile.py is your starting script. It defines user behaviors simulating visits to the specific pages you listed.

1. Installation

First, you need Python and the Locust library installed.

Install Python: Ensure you have Python 3.7+ installed on your system.

Install Locust: Open your terminal or command prompt and run:

pip install locust


2. Running the Test

Save the generated Python code as locust.py in a dedicated folder.

Navigate to that folder in your terminal.

Command Used: Since you used the filename locust.py type the command in the terminal to run the test:

python -m locust -f locust.py


python -m locust: This is the standard, most reliable way to execute the locust module directly via Python, which solves "command not recognized" errors.

-f locust.py: Specifies the location of your load test script.

3. Test Execution Parameters

The specific load test you performed used the following parameters configured in the Locust web UI (http://localhost:8089):

Number of Users (Total)

20

The maximum number of concurrent virtual users simulated.

Spawn Rate (Users/Second)

1

The rate at which new users are added to the swarm (Ramp-up).

Test Duration

20 seconds

The time the test was allowed to run.

This configuration meant that the system reached its full load of 20 concurrent users exactly at the 20-second mark, testing the website's capacity under this specific load profile.

4. Simulating Page Visits in the Python Code

The simulation of visits to different pages is defined inside the WebsiteUser class in locustfile.py (or locust.py) using these key elements:

@task(weight) Decorator: This Python decorator marks a function as an action (a task) a virtual user will perform.

The (weight) value specifies how frequently the task is chosen relative to others. For example, the browse_service_pages task has a weight of 10, while load_homepage has a weight of 5, meaning the service pages are visited twice as often as the homepage.

self.client.get(path, name) Command: This is the core command that simulates an HTTP GET request to the target website.

path: The specific URL path to request (e.g., /blog).

name: This is crucial for reporting and analysis. It tells Locust how to group the results. All requests that share the same name (even if they have different path values, like the random service pages) are aggregated into a single line in the statistics report, providing clear metrics.

The script includes the following tasks and commands:

load_homepage

self.client.get("/", name="1. Homepage")

Tests the root domain /.

browse_service_pages

self.client.get(path, name="2. Páginas de Servicios")

Randomly selects a service URL from the defined list (service_pages) and visits it.

load_blog

self.client.get("/blog", name="3. Blog")

Tests the /blog section.

load_contact_page

self.client.get("/contacto", name="4. Contacto")

Tests the /contacto section.