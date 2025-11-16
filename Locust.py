from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    service_pages = [
        "/cirugia-de-ojos-monterrey",
        "/centro-de-optica-y-oftalmologia-en-monterrey",
        "/clinica-de-ojos-en-monterrey",
        "/oftalmologo-pediatra-nuevo-leon-monterrey",
        "/oftalmologo-en-monterrey",
        "/cirugia-de-retina-monterrey",
        "/cirugia-de-cataratas-monterrey",
        "/retinopatia-diabetica-monterrey",
        "/cirugia-lasik-monterrey"
    ]

    @task(5)
    def load_homepage(self):
        self.client.get("/", name="1. Homepage")

    @task(10)
    def browse_service_pages(self):
        path = random.choice(self.service_pages)

        self.client.get(path, name="2. Páginas de Servicios")

    @task(2)
    def load_blog(self):
        self.client.get("/blog", name="3. Blog")

    @task(2)
    def load_contact_page(self):
        self.client.get("/contacto", name="4. Contacto")