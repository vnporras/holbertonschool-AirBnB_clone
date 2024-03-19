# Holberton School AirBnB Clone

This command line interface is designed to manage AirBnB objects as part of the first step towards building a full web application: the AirBnB clone. This initial step lays the foundation for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

### Features

- **BaseModel:** A parent class responsible for initializing, serializing, and deserializing future instances.
- **Serialization Flow:** Establishes a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
- **AirBnB Classes:** Includes classes such as User, State, City, Place, etc., all inheriting from BaseModel.
- **Storage Engine:** Implements the first abstracted storage engine for the project: File storage.
- **Unit Tests:** Comprehensive unittests to validate all classes and the storage engine.