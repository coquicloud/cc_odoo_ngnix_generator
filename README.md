# cc_odoo_ngnix_generator
Nginx Configuration Generator for Odoo Instances
This Python script simplifies the process of generating Nginx configuration files for your Odoo instances. It handles the configuration for both domains and subdomains, making it easy to set up Nginx as a reverse proxy for your Odoo servers.

Features
Optional Subdomains: Supports both configurations with and without subdomains.
Customizable: Easily adjust the output and enabled directories, port numbers, and other settings.
Easy to Use: A simple command-line interface guides you through the process.
Automatic Symlink Creation: Automatically creates a symlink in the sites-enabled directory for easy activation of your new configuration.
Bulk Generation: Allows generating configurations for multiple domains in one go.
How to Use
Install Requirements: Make sure you have Python 3 installed.
Run the Script: Execute the script using python3 nginx_generator.py.
Follow the Prompts:
Choose whether you want to generate a configuration for a single domain or multiple domains.
Enter the domain name (e.g., example.com) and, if applicable, the subdomain name (e.g., demo14).
Enter the port number on which your Odoo instance is running.
Configuration File Location
The generated configuration files will be saved in the /etc/nginx/sites-available/ directory.  Symlinks to these files will be created in the /etc/nginx/sites-enabled/ directory, automatically activating the new configurations.

Remember:
Reload Nginx: After generating a configuration file, you must reload or restart Nginx for the changes to take effect.
Certbot: If you want to obtain SSL certificates, you can use the Certbot tool in conjunction with this script.

Example Usage (Single Domain):
Bash
sudo python3 nginx_generator.py
Enter your choice (0-2): 1
Enter the port number (or 'b' to go back): 8069
Enter the domain name (e.g., example.com) (or 'b' to go back): mydomain.com
Enter the subdomain name (optional, leave blank for none): myodoo

Example Usage (Multiple Domains):
Bash
sudo python3 nginx_generator.py
Enter your choice (0-2): 2
Enter the port number (or 'b' to go back): 8069
Enter a domain name (or 'q' to finish): mydomain1.com
Enter the subdomain name (optional, leave blank for none): 
Enter a domain name (or 'q' to finish): mydomain2.com
Enter the subdomain name (optional, leave blank for none): demo
Enter a domain name (or 'q' to finish): q
