import click
from flask import Flask, jsonify
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from cli.models import User
from cli import create_app, db

app = create_app("development")


@click.command(name="create-db")
@with_appcontext
def init_db():
    """ Initialize the database. """
    try:
        db.create_all()
        click.echo("Initializing the SQLite3 database...")
    except Exception as exc:
        click.echo(f"Database Initialization Error: {exc}")


@click.command(name="create-new-user")
@click.argument("username")
@click.argument("email")
@with_appcontext
def create_new_user(username: str, email: str):
    """ Create a new database user."""
    try:
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        db.session.flush()
        new_id = user.id
        click.echo(f"New {new_id} User Created Successfully: {username}")
    except Exception as exc:
        click.echo(f"Database Error: {exc}")

@click.command(name="list-users")
@with_appcontext
def list_users():
    """ List all database users. """
    try:
        users = db.session.query(User).all()
        for user in users:
            click.echo(f"{user.username}")
    except Exception as exc:
        click.echo(f"Database Error:{exc}")


# add cli commands
app.cli.add_command(init_db)
app.cli.add_command(create_new_user)
app.cli.add_command(list_users)



if __name__ == "__main__":
    app.run()
