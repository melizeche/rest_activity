# rest_contact
A simple contact list REST API

## Requirements

- Python 3.6+
- Django 2.2+
- PostgreSQL 11+

## Install

```
git clone git@github.com:melizeche/rest_contact.git
cd rest_contact
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp conf/.env.example conf/.env # you should edit this file with your configuration
./manage.py migrate
./manage.py runserver
```

## Install using docker-compose

```
git clone git@github.com:melizeche/rest_contact.git && cd rest_contact
cp conf/.env.example conf/.env # you should edit this file with your configuration
docker-compose up -d --build
docker-compose exec app ./manage.py migrate
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Add your name and git account to the Contributors section in this `README.md` :D
6. Submit a pull request to `dev` branch

## Author

- Marcelo Elizeche Landó https://github.com/melizeche


## License

This project is licensed under the terms of the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
