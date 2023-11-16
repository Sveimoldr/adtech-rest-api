# AdTech Data Dashboard

## Overview

AdTech Data Dashboard is a Django-based web application designed to provide real-time insights into advertising data. It integrates with various advertising platforms via REST APIs to collect data, which is then processed and visualized in an interactive dashboard. This application is an ideal demonstration of Python, MySQL, and REST API integration in the advertising technology domain.

## Key Features

- **Data Collection**: Integration with advertising platforms for data collection via APIs.
- **Data Storage**: Efficient MySQL database integration for data storage.
- **Data Processing**: Python scripts for data cleaning, transformation, and analysis.
- **Interactive Dashboard**: User-friendly web interface for data visualization.
- **RESTful API**: Secure API endpoints for processed data access.
- **Mock Data Generation**: Custom Django management command to generate mock ad data for testing.

## Prerequisites

- Python 3.x
- Django
- MySQL
- Django REST Framework
- Faker (for mock data generation)

## Installation

1. **Clone the Repository**
    
    bashCopy code
    
    `git clone https://github.com/yourusername/AdTechDataDashboard.git cd AdTechDataDashboard`
    
2. **Set Up a Virtual Environment** (Recommended)
    
    Copy code
    
    `` python -m venv venv source venv/bin/activate  # On Windows use `venv\Scripts\activate` ``
    
3. **Install Dependencies**
    
    Copy code
    
    `pip install -r requirements.txt`
    
4. **Configure the Database in Django**
    
    - Ensure MySQL is running.
    - Create a database named `adtech_dashboard`.
    - Update `AdTechDashboard/settings.py` with your database settings.
5. **Run Database Migrations**
    
    Copy code
    
    `python manage.py makemigrations python manage.py migrate`
    
6. **Start the Development Server**
    
    Copy code
    
    `python manage.py runserver`
    

## Generating Mock Data

Use the custom Django management command to generate mock ad data.


`python manage.py generate_mockdata <number_of_entries>`

For example, to generate 100 entries, run:

Copy code

`python manage.py generate_mockdata 100`

## Usage

- Access the web interface at `http://localhost:8000/`.
- API endpoints can be accessed at `http://localhost:8000/api/`.
- API mocked data can be accessed at `http://localhost:8000/api/ad_data`.

## Contributing

Contributions to the AdTech Data Dashboard are welcome. Please ensure adherence to coding standards and comprehensive testing for new features.

## Contact

For any queries or suggestions, feel free to contact me.
