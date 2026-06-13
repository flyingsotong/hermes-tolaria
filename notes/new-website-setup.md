---
type: Note
---

**Phase 1: Project & Backup Setup (On Your Computer & GitHub)**
This ensures your code is version-controlled and safely backed up before you even touch the hosting.
1.**Create a Local Folder**: On your new laptop, create a folder for your new website.
2.**Set Up Git**: Open the folder in your code editor (Cursor/VS Code) and initialize a Git repository.
3.**Create a GitHub Repository**: Go to GitHub.com and create a new**private** repository for this project.
4.**Push to GitHub**: Link your local folder to the new GitHub repository and push your initial files. This is your offsite backup.
**Phase 2: Hosting & DNS Setup (On Spaceship & Your Domain Registrar)**
This connects your domain name to the correct server.
1.**Domain Purchase:**If you’re buying a .sg domain, you’ll need to first register it with SGNIC. Watch for email after domain purchase.
2.**Purchase Hosting**: On Spaceship, purchase a standard**Shared Hosting** plan (cPanel). Do**not** use the Starlight Hyperlift service.
3.**Find Your Nameservers**: After purchase, you will receive a "Welcome Email" containing the nameservers for your new hosting plan (e.g., launch1.spaceship.net, launch1.spaceship.net).
4.**Update Nameservers**: Log in to your domain registrar (e.g., Exabytes) and find the "Nameserver Management" section for your new domain. Replace any existing nameservers with the new ones from your welcome email.
5.**Wait for Propagation**: Allow a few hours for the DNS changes to take effect globally.
**Phase 3: Server & FTP Setup (In cPanel)**
This prepares the server to receive your files securely.
1.**Log in to cPanel**: Use the credentials from your welcome email to log in to your new cPanel account.
2.**Identify the Web Root**: Use the**File Manager** to run our definitive test:
- Upload a file to the folder named after your domain (e.g., new-site.sg) and check to see if it shows up on the live URL.
1.**Create a Dedicated FTP Account**:
- In cPanel, go to**"FTP Accounts"**.
- Create a new FTP user (e.g., username: alan).
-**Crucially**, set the "Directory" for this user to new-site.sg.
- Use the password generator and save the new, strong password.
Get cPanel access token from “Access your cPanel” in Spaceship
Hit "Generate token”
This is now your password for SFTP
**Phase 4: Editor Configuration (In Cursor/VS Code)**
This connects your code editor directly to your live server for easy updates.
1.**Open the Correct Folder**: Make sure you have your local Git repository folder open in your editor.
2.**Install the SFTP Extension**: Install the SFTP extension by liximomo.
3.**Configure**sftp.json: Use the SFTP: Config command to create the sftp.json file inside the .vscode directory. Fill it out with the credentials of the FTP account you just created.
 **Template for**sftp.json
 JSON
 {
 "name": "My New Site FTP",
 "host": "yournewsite.com",
 "protocol": "ftp",
 "port": 21,
 "username": "webmaster@yournewsite.com", // Or the FTP user you created
 "password": "the-password-you-just-generated",
 "remotePath": "/" // Use "/" if your FTP user's directory is the web root
 }
**Phase 5: Your Day-to-Day Workflow**
This is how you will update your site from now on.
1.**Edit Files**: Make changes to your website locally in Cursor/VS Code.
2.**Commit & Push to GitHub**: Use the Source Control panel to commit your changes and then push them to GitHub. This is your safety net.
3.**Upload to Server**: Use the SFTP extension to publish the changes. The best way is to use the SFTP: Sync with Git Init command from the Command Palette, which will upload only the files from your last commit.
**Phase 6: Emails and SEO**
1. Add to clients [mail.spacemail.com](http://mail.spacemail.com)
2. Add Google Search Console when propagation is complete