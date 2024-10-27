# Django Docker Starter Template

- A robust starter template to kickstart Django applications, crafted by **Florin Pinta (alias XTTRUST)** for developers seeking an efficient, production-ready setup. This template includes:

    - **Django Allauth**: Integrated for fast and secure user authentication.
    - **Flexible Configuration**: Optimized default settings for seamless operation in both local and production environments.
    - **Dockerized Environment**: Full Docker configuration, enabling consistent deployment and streamlined setup.

- With this template, developers can bypass initial configurations and dive straight into building Django apps, making it ideal for both local development and scalable deployment.

# Configuration 

- The normal settings.py file was moved into 2 files. You can find those files
`root/server/settings/` . I used `__init__.py` to initialize this folder.


## Local Development Settings (`local.py`)

This `local.py` file is tailored for local development, making it easy to get up and running quickly. Here's an overview of its structure and key sections:

1. **Paths and Directory Setup**:
   - **`BASE_DIR`**: Defines the root of your Django project directory, allowing easy reference to paths throughout the project.
   - **Template Paths**: Configures template directories to locate HTML files, including custom templates and `allauth` templates.

2. **Security**:
   - **Secret Key**: The `SECRET_KEY` here is set for local development only. In production, it should be hidden by using environment variables or a secrets management tool.
   - **Debug Mode**: `DEBUG=True` allows for detailed error pages and logging, which are helpful for debugging during development but should be set to `False` in production.

3. **Static Files**:
   - **Static URL**: Specifies the URL path to access static files (`/static/`).
   - **Static Root**: Defines the directory where `collectstatic` will gather all static files for production (`staticfiles`).
   - **Static Files Directory**: Points Django to additional static file locations, ensuring assets like CSS and JavaScript are accessible.

This configuration is suitable for running Django locally but should not be used as-is in production.

## Production Settings (`production.py`)

This `production.py` settings file is configured for a secure and scalable production environment, making use of environment variables for sensitive data. Here’s a breakdown of its structure and key sections:

1. **Security**:
   - **Secret Key**: `SECRET_KEY` is retrieved from an environment variable using `get_secret()`, ensuring sensitive information remains hidden.
   - **Debug Mode**: `DEBUG=False` ensures that sensitive debugging information is not displayed in production.
   - **Allowed Hosts**: Set to allow all (`'*'`) by default, but should be restricted to specific domains or IPs in production.

2. **Database**:
   - Uses **PostgreSQL** as the database engine for production.
   - **Environment-based Credentials**: Database name, user, password, host, and port are all managed securely through environment variables, accessed using `get_secret()`.

3. **Static Files**:
   - **Static URL**: Defines `/static/` as the URL for static file access.
   - **Static Root**: Sets `staticfiles` as the directory where `collectstatic` gathers all static assets for production.
   - **Static Files Directory**: Points Django to an additional `static` folder for custom static files.

4. **Installed Apps & Middleware**:
   - Includes Django’s core apps, custom apps, and `allauth` for user authentication.
   - Configured with security-focused middleware, such as `SecurityMiddleware`, for an added layer of protection in production.

5. **Password Validation**:
   - Enforces best practices by including validators for length, complexity, and similarity checks to maintain password security.

This setup is ready for deployment in a production environment. Ensure all required environment variables are set before starting the application to avoid configuration errors.

# Admin Credentials

- To access the admin panel, you can create a new admin user through the terminal. Use the following command:

    ```bash
    python manage.py createsuperuser
    ```

- Follow the prompts to set a username, email, and password for the new admin user. Once created, use these credentials to log in to the admin panel.


## Running the Docker Container

To run the Django application within a Docker container, follow these steps:

1. **Build the Docker Image**:
   - Navigate to the directory containing the `Dockerfile` and run the following command to build the Docker image:
   
    ```bash
    docker build -t django_app .
    ```

   - This command creates a Docker image named `django_app` (you can replace `django_app` with any preferred name).

2. **Run the Docker Container**:
   - Start a container from the image and map it to port `8080` (or any preferred port) on your local machine:

    ```bash
    docker run -p 8080:8080 django_app
    ```

   - Here, `-p 8080:8080` binds port `8080` in the container to port `8080` on the host machine. You can access the Django server at `http://localhost:8080`.

3. **Stopping the Container**:
   - To stop the container, find the container ID by running:

    ```bash
    docker ps
    ```

   - Then, stop the container with:

    ```bash
    docker stop <container_id>
    ```

Following these steps will allow you to build and run your Django application in a Docker container successfully.
