# Vehicle Valuation API

## Project Description

The Vehicle Valuation API provides services to estimate optimal vehicle prices using a machine learning model, evaluate prices proposed by sellers, and recommend vehicles based on specifications and budgets. This system is designed to help users make informed decisions when buying or selling vehicles.

## Technologies Used

- **Programming Language**: Python
- **Framework**: Django
- **Libraries**:
  - Pandas (for data handling)
  - Scikit-learn (for Machine Learning models)
  - NumPy (for numerical operations)
  - Django Rest Framework (for building APIs)
  - TestCase (for unit testing the API and machine learning predictions)
  - Pickle (for saving and loading the machine learning models)
  - Decouple (for environment variable management)
  - Seaborn (for data visualization)
  - Matplotlib (for plotting graphs and charts)
- **Data Format**: JSON
- **Database**: CSV (for storing vehicle data)
- **Machine Learning Model**: Stored in `.pkl` file
- **Containerization**: Docker (used for packaging and deploying the application in a consistent environment)

## Patterns Used

1. **Singleton Pattern**:
   - This pattern is used to ensure that certain classes have a single instance throughout the application's lifetime. This is useful in situations where a single source of truth is needed, such as loading configurations or database connections.
   - For example, the data services class that handles the loading and processing of vehicle data can be implemented as a Singleton, ensuring that only one instance exists throughout the application lifecycle.

2. **MVC Pattern (Model-View-Controller)**:
   - The MVC architecture is used to separate the application's logic into three interconnected components:
     - **Model**: Represents the data structure and business logic. In this case, it handles interactions with the vehicle data.
     - **View**: Although this project is primarily an API and not a web application with a graphical interface, the View can be interpreted as the JSON responses sent to clients.
     - **Controller**: Manages the application logic, processing user requests and updating the model or view as necessary. Each API endpoint is represented by a controller that processes input and produces a response.

## Code Modularization

Code modularization is essential for maintaining a clean and manageable codebase. In this project, modularization is achieved through:

- **Controllers**: Each controller is responsible for a specific function of the API, such as price evaluation or vehicle recommendation. This allows for a clear separation of responsibilities and facilitates code scalability and maintenance.

- **Services**: Services encapsulate business logic, allowing controllers to focus on handling requests and responses. For instance, the price evaluation service contains the logic to process input data and apply the corresponding machine learning model, while the controller simply invokes this service and handles the result.

- **Views**: In the context of this API, views represent the structured JSON responses that are sent to the client. They format the output data based on the API's requirements, ensuring that clients receive the necessary information in a clear and consistent manner.

## Used Middlewares

The Django application includes the following middlewares to manage various layers of security, authentication, and session handling:

1. **SecurityMiddleware**  
   Provides various security protections, including defenses against common attacks and controls for HTTP headers related to security.

2. **SessionMiddleware**  
   Manages session support, allowing the server to store and retrieve information about a user's session state between requests.

3. **CommonMiddleware**  
   Performs common functions, such as adding trailing slashes to URLs and handling redirect responses.

4. **CsrfViewMiddleware**  
   Protects against Cross-Site Request Forgery (CSRF) attacks by requiring CSRF tokens in POST requests.

5. **AuthenticationMiddleware**  
   Associates users with their requests using Django's authentication system.

6. **MessageMiddleware**  
   Provides a framework for displaying messages to users, whether they are error, warning, or informational messages.

7. **XFrameOptionsMiddleware**  
   Prevents the website from being embedded in an `<iframe>` from untrusted domains, providing protection against clickjacking attacks.

## Endpoints

### 1. Optimal Price

**Method**: POST  
**Route**: `/optimal-price`  
**Description**: Given a series of vehicle characteristics, it returns the estimated optimal price.

```json
{
    "Manufacturer": "Toyota",
    "Prod_year": 2020,
    "Engine_volume": 2.0,
    "Mileage": 15000,
    "Cylinders": 4,
    "Gear_box_type": "Automatic",
    "Drive_wheels": "FWD"
}
```


### 2. Price Evaluation

**Method**: POST  
**Route**: `/evaluate-price`  
**Description**: Evaluates the price proposed by a seller and suggests a reasonable price based on the analysis of the vehicle's characteristics.


```json
{
    "Manufacturer": "Honda",
    "Prod_year": 2019,
    "Engine_volume": 1.8,
    "Mileage": 20000,
    "Cylinders": 4,
    "Gear_box_type": "Manual",
    "Drive_wheels": "RWD",
    "Proposed_price": 20000
}
```

### 3. Purchase Recommendation

**Método**: POST  
**Ruta**: `/recommendation`  
**Description**: Given a budget and desired specifications, it suggests the best available vehicle based on the data.

```json
{
    "Budget": 25000,
    "Manufacturer": "Ford",
    "Prod_year": 2021,
    "Engine_volume": 2.5,
    "Cylinders": 4,
    "Gear_box_type": "Automatic",
    "Drive_wheels": "AWD"
}

```

## Installation

To run this API locally, follow these steps:

1. **Clone the repository:**:

   ```bash
   git clone <https://github.com/danielsuniaga/django-lineal-regression/>
   cd <directorio-del-repositorio>

2. **Install the required dependencies:**:

   ```bash
   pip install -r requirements.txt