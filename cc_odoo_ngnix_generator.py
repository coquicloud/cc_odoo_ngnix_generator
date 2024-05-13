# MIT License

# Copyright (c) 2024 Coqui Cloud
# Developer Ramon Rios Jr.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

# ------------------------------------------------------------------------
# 1. NGINX CONFIGURATION TEMPLATE (base_template)
# ------------------------------------------------------------------------
base_template = """upstream UPSTREAM_NAME {  
    server 127.0.0.1:PORT; 
}
server {
    server_name UPSTREAM_NAME;
    location / {
        proxy_pass http://UPSTREAM_NAME;  
        proxy_set_header Host $host;           
        proxy_set_header X-Real-IP $remote_addr;  
        proxy_set_header X-Forwarded-Host $host;  
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for; 
        proxy_set_header X-Forwarded-Proto $scheme; 
        proxy_redirect off;
        proxy_read_timeout 720s;   
        proxy_connect_timeout 720s; 
        proxy_send_timeout 720s;  
        client_max_body_size 100M;  
        error_page 502 /50x.html; 
        gzip_static on;
    }
}
"""


# ------------------------------------------------------------------------
# 2. NGINX CONFIGURATION FILE GENERATOR FUNCTION
# ------------------------------------------------------------------------

def generate_config(domain_name, port, subdomain_name=None, output_directory="/etc/nginx/sites-available/", enabled_directory="/etc/nginx/sites-enabled/"):
    # Determine upstream name based on subdomain
    upstream_name = f"{subdomain_name}.{domain_name}" if subdomain_name else domain_name

    config_content = base_template.replace("PORT", str(port)) \
                                   .replace("DOMAIN_NAME", domain_name) \
                                   .replace("UPSTREAM_NAME", upstream_name)  # Replace UPSTREAM_NAME here

    # Initialize file_name here
    file_name = domain_name  # Default to domain name if no subdomain

    if subdomain_name:
        config_content = config_content.replace("# ", "", 1)  # Uncomment the redirection if using subdomain
        config_content = config_content.replace("SUBDOMAIN_NAME", subdomain_name)
        file_name = f"{subdomain_name}.{domain_name}"  # Update file_name if subdomain is present
        proxy_pass_line = f"proxy_pass http://{upstream_name}:{port};"
        config_content = config_content.replace("proxy_pass http://UPSTREAM_NAME:PORT;", proxy_pass_line)

    config_file = os.path.join(output_directory, file_name)
    with open(config_file, "w") as f:
        f.write(config_content)

    enabled_link = os.path.join(enabled_directory, file_name)
    if os.path.exists(enabled_link):
        os.remove(enabled_link)
    os.symlink(config_file, enabled_link)

    print(f"Nginx configuration generated and enabled for {file_name}.")


def get_input_with_retry(prompt_message):
    while True:
        user_input = input(prompt_message)
        if user_input.lower() == 'b':
            return None 
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'b' to go back.")

#-----------------------------------------------------
# 3. USER INPUT AND CONFIG GENERATION
#-----------------------------------------------------
if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Generate for a single domain (with or without subdomain)")
        print("2. Generate for multiple domains")
        print("0. Exit")

        choice = input("Enter your choice (0-2): ")

        if choice == '0':
            break

        port = get_input_with_retry("Enter the port number (or 'b' to go back): ")
        if port is None:
            continue

        if choice == '1':
            domain_name = input("Enter the domain name (e.g., example.com) (or 'b' to go back): ")
            if domain_name.lower() == 'b':
                continue
            subdomain_name = input("Enter the subdomain name (optional, leave blank for none): ")
            generate_config(domain_name, port, subdomain_name)

        elif choice == '2':
            while True:
                domain_name = input("Enter a domain name (or 'q' to finish): ")
                if domain_name.lower() == 'q':
                    break
                subdomain_name = input("Enter the subdomain name (optional, leave blank for none): ")
                generate_config(domain_name, port, subdomain_name)
        else:
            print("Invalid choice. Please enter a number between 0 and 2.")


