# Domain Driven Design demo

![Python](images/python.jpg)

This repository demonstrates a clean and scalable architecture for an enterprise-grade software application using Python. The architecture is based on Domain-Driven Design (DDD) and the Repository Pattern, ensuring that the business logic is decoupled from technical concerns, making the system maintainable and adaptable.

## Project Overview
This project includes the following key components:

**Domain Layer:** Contains the core business logic. The engine_model.py defines the domain model for the engine.

**Repository Layer:** Provides an abstraction over the data access layer. This layer includes the base_engine_repository.py which defines the repository interface and sql_alchemy_engine_repository.py which implements the repository using SQLAlchemy.

**Service Layer:** Encapsulates the business logic and use cases. The car_service.py contains the service logic for managing car-related operations.
