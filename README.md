# Gamer portal

## Setup project for development
Add .env file to the root of the project and fill it
```bash
cp docs/.env.example .env
```
Install development dependencies
```bash
make install-dev-deps
```
Create database
```bash
make create-db
```
Run lint
```bash
make lint
```
Start server
```bash
make server
```
