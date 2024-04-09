# Templates

This directory contains the HTML templates used in the Flask application. The templates are rendered by Flask to generate dynamic web pages.

## File Descriptions

- `0-index.html`: Basic template that displays a title and a header.
- `1-index.html`: Updated template with internationalization support using Flask-Babel. The title and header are wrapped with translation functions.
- `2-index.html`: Template that gets the current locale from the request and displays the translated title and header.
- `3-index.html`: Template with parametrized translations using the `gettext` function from Flask-Babel.
- `4-index.html`: Template that allows the user to select the language using a form and switch between different translations.

## Usage

These templates are used by the Flask application to render the corresponding web pages. The Flask routes specify which template to use for each route.

To customize the templates or add new ones, you can modify the existing files or create new HTML templates in this directory. Make sure to update the Flask routes and logic accordingly to render the desired templates.

## Localization and Internationalization

The templates in this directory make use of Flask-Babel for localization and internationalization. Flask-Babel provides translation functions that allow the application to display content in different languages.

The translations are handled by defining translation strings and using the appropriate translation functions in the templates. The translations can be stored in separate language files and loaded by Flask-Babel.

To add or modify translations, you can update the language files and recompile them using the Flask-Babel commands. Refer to the Flask-Babel documentation for more details.

## Dependencies

These templates are part of a Flask application and require the following dependencies:

- Flask: A micro web framework for Python.
- Flask-Babel: An extension for Flask that adds i18n and l10n support.

Make sure to have these dependencies installed before running the Flask application.

## Credits

These templates are created as part of a project or exercise and may include code snippets or references from various sources. The original authors or sources of the code are credited within the code itself.
