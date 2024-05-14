# Contributing

Thank you for your interest in contributing to this Nginx configuration generator! We welcome contributions from everyone.

## How to Contribute

1. **Fork the repository:** Click the "Fork" button on the GitHub page to create your own copy of the repository.
2. **Create a branch:** Create a new branch for your changes.
3. **Make changes:** Make your changes in your branch.
4. **Commit your changes:** Commit your changes with a clear and descriptive commit message.
5. **Open a pull request:** Open a pull request to merge your changes into the main repository.

## Contribution Guidelines

- **Follow the code style:** Please try to maintain the existing coding style.
- **Write tests:** If you're adding new functionality, please include unit tests.
- **Document your changes:** Explain your changes clearly in the commit message and pull request description.
- **Be respectful:** Treat everyone with respect in all interactions.

## Code of Conduct

We expect all contributors to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Planning Future Additional Scripts Upgrade:

SSL Certificate Management:

Certbot Integration: Create a script that automates obtaining and renewing SSL certificates using Certbot for the domains/subdomains you generate configurations for.
Custom Certificate Script: If you prefer not to use Certbot, you could write a script to fetch certificates from another source (e.g., your own certificate authority) and integrate them into the Nginx configurations.
Configuration Validation:

Syntax Checker: A script that checks the syntax of the generated Nginx configuration files before enabling them. This would help catch errors early and prevent Nginx from failing to start.
Odoo Connectivity Test: A script that attempts to connect to the Odoo instance on the specified port after the configuration is generated. This would verify that the Nginx reverse proxy is set up correctly.
Bulk Management:

Batch Configuration Generation: Extend your script to take a CSV or JSON file as input, listing multiple domains, subdomains, and ports. This would allow you to generate many configurations at once.
Configuration Removal: A script to remove Nginx configurations and their associated symlinks in bulk, given a list of domains or subdomains.

