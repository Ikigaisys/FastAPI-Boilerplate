# FastAPI Boilerplate

Boilerplate for a FastAPI application

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r etc/requirements.txt
```

## Configuration Variables

Configuration variables need to be in the file `etc/settings.json`. **Please create this file.**
Only the database connection key value pair exists right now.
It can be set to Postgres or MySQL. With SQLite, `check_same_thread=False` is needed (not recommended) 
#### Example `settings.json`
```bash
{
    "env": "dev",
    "database_uri": "sqlite:////absolute/path/to/project/test.db?check_same_thread=False"
}
```

## Migrations
To initialize the database, run the following [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration) command

```bash
alembic revision -m "init" --autogenerate
alembic upgrade head
```
## Run

```bash
python3 src/app.py
```
**Open the URL http://127.0.0.1:8001/docs**

The endpoint DELETE request for /api/v1/user/{user_id} uses simple authentication as a starting point. To test it:
- Create two users user1@example.com (id: 1) and  user2@example.com (id: 2)
- Pass the header field Authentication "Basic user1@example.com" (or send the `Authentication: Basic user1@example.com` header if you're calling the url directly)
- Call the delete endpoint on user id 2. User id 2 will be deleted by user id 1

__Note:__ Please modify jwt_auth function in `helpers/deps.py` and implement a proper Bearer authorization in the commented area

## License
[MIT](https://choosealicense.com/licenses/mit/)
