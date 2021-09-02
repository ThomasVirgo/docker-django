- use ```docker exec -it <container-id> bash``` to run migrations
- if add more python modules e.g. djangorestframework then need to add that to requirements.txt and rebuild the web container with ```docker-compose up --build```
- to get token make a post request to auth/token with username and password payload in body of request
- to register a new user make a post request to auth/register with username, password and password_confirmation in the body
- for views that have permission_classes = [IsAuthenticated] they will require a token to be passed in the header. Form is "Authorization" "Token <insert token here>"

# Deployment

- heroku create <app name>
- heroku container:login
- heroku addons:create herokupostgresql:hobby-dev
- heroku container:push web
- heroku container:release web
- heroku run bash
- python manage.py migrate
- python manage.py createsuperuser
- consider handling any static assets with whitenoise if needed