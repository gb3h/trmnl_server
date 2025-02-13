# TRMNL BYOS - Python / Django

This is an implementation of the TRMNL API in Python, which you can use your TRMNL device with.

## Installation
### Docker

#### Steps

```shell
# copy env-sample to .env and edit it to your liking
cp env-sample .env
docker compose up -d
docker compose exec app ./manage.py migrate
docker compose exec app ./manage.py createsuperuser

# your app is now up on http://your.ip.address.here:8000
```

Continue on to the [Usage](#Usage) section to get started.

### Manual Installation
#### Requirements
* Python 3.13 (others versions may work, but developed on 3.13)
* ImageMagick
* Pipenv

#### Steps
```shell
git clone https://github.com/Omeryl/byos_django.git
cd byos_django

cp env-sample .env
# Edit .env, put your IP or Hostname in ALLOWED_HOSTS, and a sufficiently secure secret key.
pipenv install
pipenv shell
playwright install firefox
python manage.py migrate
# create your user!
python manage.py createsuperuser
# for a non production or local install, you can run the built in server
python manage.py runserver 0.0.0.0:8000
```

## Usage

* Point your TRMNL to your IP or Hostname `http://your-ip-or-hostname:8000`
* Open your browser to the same URL, you'll be redirected to the admin page.
* Once your start your TRMNL, you'll see a new device under the Devices section. To "pair" it, just assign it to your user.
* If you see the Rover image, your device is paired and ready to use!
* You can create a new Screen under the Screens section.
  * Use whatever HTML you want. I recommend using the boilerplate in `temmplates/base.html` to make use of the framework.
  * Click `Save` and wait a moment for the image to be generated.
  * On the next refresh (defaults to 900 seconds, can be configured on the Device edit page) your TRMNL will update to the new screen.
