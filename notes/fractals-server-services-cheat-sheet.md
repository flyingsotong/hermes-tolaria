---
type: Project-Note
---

Last Updated: October 10, 2025
This document contains all the essential details for the server hosting fractals.sg services.
**1. Server Details**
Provider: Spaceship.com VPS
Public IP Address: 209.74.81.185
Location: Singapore
Login User: root (or alan with sudo)
**2. Domain & DNS Details**
Primary Domain: fractals.sg
DNS Records (A Records):
- stats.fractals.sg points to 209.74.81.185
- n8n.fractals.sg points to 209.74.81.185
- @ (fractals.sg) points to 156.67.222.23 (Note: This is a different server)
**3. Hosted Applications & Services**
Service Name: Umami Analytics
Manages: Website analytics
Service Name: n8n Automation
Manages: Workflow automation
Service Name: Nginx Proxy
URL: (Runs in the background)
Manages: Routes traffic to the correct service
**4. Docker Management**
All services are managed using Docker Compose.
Project Directory: The configuration files are located at /root/my-proxy-setup/.
Main Configuration File: docker-compose.yml
Proxy Configuration File: nginx/proxy.conf
**Essential Commands (run from the project directory):**
Start/Restart All Services:
docker compose up -d
Stop All Services:
docker compose down
View Logs for a Specific Service:
**View n8n logs**
docker compose logs -f n8n
**View proxy logs**
docker compose logs -f proxy
Update Applications:
**Pull the latest Docker images**
docker compose pull
**Restart the containers with the new images**
docker compose up -d
**5. SSL Certificate Renewal (Let's Encrypt / Certbot)**
Certificate Files Location: /root/my-proxy-setup/certbot/conf/
Automatic Renewal: A cron job is set up to renew the certificates automatically.
Manual Renewal Command:
docker run --rm -v /root/my-proxy-setup/certbot/conf:/etc/letsencrypt certbot/certbot renew