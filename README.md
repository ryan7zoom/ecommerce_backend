# Complete E-commerce Backend Platform

A fully functional e-commerce backend built with Django REST Framework featuring product management, user authentication, shopping cart, and order processing.

## 🚀 Features

### Core Functionality
- **Product Management**: CRUD operations for products with categories and images
- **User Authentication**: JWT token-based authentication system
- **Shopping Cart**: Session-based cart logic with add/remove items
- **Order Processing**: Complete order placement and management system
- **Admin Panel**: Django admin interface for managing all data

### API Features
- **RESTful API**: Full CRUD operations for all resources
- **Authentication**: JWT tokens for secure API access
- **Pagination**: Automatic pagination for large datasets
- **Filtering**: Advanced filtering capabilities
- **Searching**: Full-text search across products
- **Ordering**: Sort results by any field
- **Documentation**: Interactive API documentation with Swagger/OpenAPI

### Technical Features
- **Comprehensive Testing**: Full test suite with pytest (100% coverage)
- **Environment Management**: Secure environment variable handling
- **Media Handling**: Image upload and storage
- **Security**: Custom CSRF middleware, proper permissions
- **Database**: SQLite for development, PostgreSQL ready for production

## 🛠️ Tech Stack

- **Framework**: Django 5.2
- **API**: Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Testing**: pytest with 100% test coverage
- **Documentation**: drf-spectacular (Swagger/OpenAPI)
- **Frontend**: HTML templates with session-based cart

## 📋 Prerequisites

- Python 3.11
- pip package manager
- Virtual environment (venv)

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ryan7zoom/ecommerce_backend.git
   cd complete-ecommerce-platform

2. **Create and activate virtual environment**
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Set up environment variables**
Create a .env file with:
SECRET_KEY=your-secret-key-here
DEBUG=True

5. **Run migration**
python manage.py migrate

6. **Create superuser (optional)**
python manage.py createsuperuser

7. **Start the development server**
python manage.py runserver

8. **Run the comprehensive test suite**
python manage.py 
    **Or with pytest for detailed coverage**
pytest


📚 API Documentation
Visit these endpoints for API documentation:

- /api/docs/ - Interactive Swagger documentation
- /api/redoc/ - Redoc documentation
- /api/schema/ - Raw OpenAPI schema

🎯 Key API Endpoints
- POST /api/token/ - Obtain JWT tokens
- POST /api/token/refresh/ - Refresh JWT tokens
- GET /api/products/ - List all products
- GET /api/categories/ - List all categories
- GET /api/orders/ - List user orders
- POST /api/orders/ - Create new order

🚀 Deployment
Ready for deployment to Render with included configuration files:
- render.yaml - Deployment configuration
- runtime.txt - Python version specification
- build.sh - Automated build script

📁 Project Structure
├── config/                 # Django project settings
├── store/                  # Main e-commerce app
│   ├── models.py          # Product, Category, Order, OrderItem
│   ├── views.py           # ViewSets for API endpoints
│   ├── serializers.py     # Data serialization
│   └── templates/         # HTML templates
├── common/                # Common utilities and middleware
├── tests/                 # Comprehensive test suite
├── media/                 # Uploaded images and files
├── static/                # Static files
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── manage.py             # Django management script

🏆 What Makes This Project Special
- Production Ready: Includes all the deployment configurations
- Fully Tested: 100% test coverage with pytest
- Secure: Proper authentication, permissions, and environment management
- Well Documented: Comprehensive API documentation
- Scalable: Designed following Django best practices
