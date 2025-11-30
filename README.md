

# NEW AUTH FEATURE - ISO 27001
We have refactored the legacy authentication logic. 
New components: lib/secure-auth-provider - drop-in replacement for our current auth verification., lib/auth-utils-core - low-level utilities required by the provider.
# CI/CD Compliance Updates
New Workflow added .github/workflows/ci-audit-pipeline.yml. This pipeline automatically captures Pull Request metadata and logs them to our secure audit trail output.
This runs automatically on every PR to ensure no unauthorized changes slip through without a log entry.

# ![Juice Shop Logo](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_100px.png) OWASP Juice Shop

## Setup

### From Sources

![GitHub repo size](https://img.shields.io/github/repo-size/juice-shop/juice-shop.svg)

1. Install [node.js](#nodejs-version-compatibility)
2. Run `git clone https://github.com/kirde001/juice-shop.git --depth 1`
3. Go into the cloned folder with `cd juice-shop`
4. Run `npm install` (only has to be done before first start or when you change the source code)
5. Run `npm start`
6. Browse to <http://localhost:3000>
