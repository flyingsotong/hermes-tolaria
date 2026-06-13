---
type: Note
---

Final Architecture and Setup Procedure for Self-Hosted Umami Analytics Server
**TO:** Alan Soon
**FROM:** Gemini Assistant
**DATE:** September 16, 2025
**1.0 Overview**
This document outlines the final, stable architecture and the successful step-by-step procedure for deploying a self-hosted Umami analytics server. The deployment utilizes a VPS running Ubuntu, with the application and its database managed via Docker Compose. A reverse proxy is configured using NGINX, and the connection is secured with a Let's Encrypt SSL certificate. The procedure also includes the successful migration of historical data from CSV backups.
**2.0 Final System Architecture & Credentials**
-**Hosting Provider**: Spaceship VPS
-**Server Plan**: Standard 1
 -**vCPU**: 1 core
 -**RAM**: 2 GiB
 -**Storage**: 25 GiB NVMe SSD
-**Operating System**: Ubuntu 24.04 LTS
-**Public IP Address**: 209.74.81.185
-**Custom SSH Port**: 22022
-**Application Domain**: <https://stats.fractals.sg>
**3.0 Key Configuration Details**
-**Deployment Method**: Docker & Docker Compose
-**Database**: PostgreSQL 15 (running in Docker)
-**Web Server**: NGINX (running on the host server)
-**SSL Provider**: Let's Encrypt (managed via Certbot)
**Critical Identifiers:** _(Note: Passwords and secrets should be stored securely and rotated as needed.)_
-**Database Name**: umamiproject
-**Database User**: umamiuser
-**Database Password**: UmamiPassword73
-**Admin Account**user_id** (UUID)**: 41e2b680-648e-4b09-bcd7-3e2b10c06264
-**Application**APP_SECRET: A user-generated secure random string.
-**Application**ORIGIN** URL**: <https://stats.fractals.sg>
**4.0 Server Setup & Application Deployment Procedure**
This procedure outlines the steps taken on a fresh Ubuntu 24.04 server.
**4.1. Initial Server Connection**
1. Connect to the server via SSH using the custom port:
 Bash
 ssh -p 22022 root@209.74.81.185
**4.2. Docker Installation**
1. Update package lists and install Docker and Docker Compose:
 Bash
 apt update
 apt install -y docker.io docker-compose
**4.3. Umami Docker Compose Configuration**
1. Create a dedicated directory:
 Bash
 mkdir ~/umami-docker
 cd ~/umami-docker
2. Create the configuration file docker-compose.yml with the following content:
 YAML
 version:'3'
 services:
 umami:
 image:docker.umami.is/umami-software/umami:postgresql-latest
 ports:
 -"3000:3000"
 environment:
 DATABASE_URL:postgresql://umamiuser:UmamiPassword73@db:5432/umamiproject
 APP_SECRET:YOUR_SECURE_RANDOM_STRING_HERE
 ORIGIN:<https://stats.fractals.sg>
 depends_on:
 -db
 restart:always
 db:
 image:postgres:15-alpine
 environment:
 POSTGRES_USER:umamiuser
 POSTGRES_PASSWORD:UmamiPassword73
 POSTGRES_DB:umamiproject
 volumes:
 -./umami-db-data:/var/lib/postgresql/data
 restart:always
**4.4. Launching the Application**
1. From within the ~/umami-docker directory, start the application:
 Bash
 docker-compose up -d
**5.0 Web Server & SSL Configuration (NGINX & Certbot)5.1. NGINX Configuration**
1. Install NGINX on the host server:
 Bash
 apt install -y nginx
2. Create a server block configuration file:
 Bash
 nano /etc/nginx/sites-available/stats.fractals.sg
3. Add the following reverse proxy configuration:
 Nginx
 server {
 listen80;
 server_name stats.fractals.sg;
 location / {
 proxy_pass <http://localhost:3000;>
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header Host $host;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 }
 }
4. Enable the site by creating a symbolic link:
 Bash
 ln -s /etc/nginx/sites-available/stats.fractals.sg /etc/nginx/sites-enabled/
**5.2. HTTPS/SSL with Certbot**
1. Install Certbot and its NGINX plugin:
 Bash
 apt install -y certbot python3-certbot-nginx
2. Run Certbot to automatically obtain a certificate and configure NGINX for HTTPS:
 Bash
 certbot --nginx -d stats.fractals.sg
 (Follow the prompts for email and redirecting HTTP to HTTPS).
**6.0 Historical Data Migration (CSV Method)6.1. Data Preparation**
1. Obtain the new user_id from the running Docker database container.
2. Edit the local website.csv file, replacing all values in the user_id column with the new ID.
**6.2. File Transfer**
1. Copy the prepared CSV files from the local PC to the server's home directory:
 PowerShell
 # Run on local PC's PowerShell
 scp -P22022 *.csv root@209.74.81.185:~/
2. Copy the files from the server's home directory into the running database container:
 Bash
 # Run on the server via SSH
 docker cp ~/alansoon-*.csv umami-docker_db_1:/tmp/
**6.3. Database Import**
1. Access the database container's command line:
 Bash
 docker exec -it umami-docker_db_1 bash
2. Connect to the database:
 Bash
 psql -U umamiuser -d umamiproject
3. Run the import commands one by one:
 SQL
 \copy website FROM'/tmp/alansoon-website.csv' DELIMITER ',' CSV HEADER;
 \copy session FROM'/tmp/alansoon-session.csv' DELIMITER ',' CSV HEADER;
 \copy website_event FROM'/tmp/alansoon-website_event.csv' DELIMITER ',' CSV HEADER;
**7.0 Final Verification**
- Access the Umami instance at <https://stats.fractals.sg.>
- Log in with the default credentials (admin/umami) and change the password immediately via the UI.
- Verify that all historical data is present.
- Update the tracking codes on all live websites to point to the new server.