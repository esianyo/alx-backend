## README.md

**Project: Flask Internationalization (i18n) with Babel**

This project demonstrates the implementation of Flask internationalization (i18n) using the Babel extension. It includes a series of tasks that progressively build a web application with the following features:

* Basic Flask app with a single route and template.
* Babel setup for internationalization.
* Retrieving locale from request headers.
* Parametrizing templates with translated messages.
* Forcing locale with URL parameters.
* Mocking user login and displaying localized messages based on user settings.
* Prioritizing user's preferred locale.
* Inferring appropriate time zone based on user settings or request headers.

**Requirements:**

* Python 3.7
* Flask
* Flask-Babel
* pytz (for time zone handling)

**Project Structure:**

* `0-app.py`: Basic Flask app.
* `templates/`: Directory containing HTML templates.
* `1-app.py`: App with Babel setup.
* `2-app.py`: App with `get_locale` function.
* `babel.cfg`: Babel configuration file.
* `translations/`: Directory containing translation files for different languages.
* `5-app.py`: App with mock user login and localized messages.
* `6-app.py`: App using user's preferred locale.
* `7-app.py`: App with time zone inference.

**Running the Application:**

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Navigate to the project directory.
4. Run the application: `flask run`
5. Access the application in your browser (usually at http://127.0.0.1:5000).

**Testing Different Locales:**

- You can test different locales by adding the `locale` parameter to the URL:

   - http://127.0.0.1:5000/?locale=en (English)
   - http://127.0.0.1:5000/?locale=fr (French)

- Mock user login by adding the `login_as` parameter to the URL:

   - http://127.0.0.1:5000/?login_as=1 (User 1 - Balou)
   - http://127.0.0.1:5000/?login_as=2 (User 2 - Beyonce)

**Understanding the Code:**

Each task builds upon the previous one, introducing new concepts and functionalities. Refer to the comments within the code for detailed explanations.

**Additional Notes:**

This project provides a basic example of Flask i18n using Babel. You can further enhance it by adding features such as language selection menus and time zone dropdowns within the templates.
