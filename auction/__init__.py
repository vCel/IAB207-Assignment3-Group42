# import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


# create a function that creates a web application
# a web server will run this web application


def create_app():

    # this is the name of the module/package that is calling this app
    app = Flask(__name__)
    app.secret_key = 'utroutoru'
    # set the app configuration data
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
    # initialize db with flask app
    db.init_app(app)
    login_manager.init_app(app)

    bootstrap = Bootstrap(app)

    from auction.auth.routes import auth
    from auction.views.routes import main
    from auction.sell.routes import post
    from auction.listings.routes import listings

    app.register_blueprint(main)
    app.register_blueprint(post)
    app.register_blueprint(auth)
    app.register_blueprint(listings)




    @app.errorhandler(404)
    def not_found(e):  # error view function
        errortype = 404
        error = 'Page not found'
        return render_template("error404.html", mes=errortype, error=error)

    @app.errorhandler(500)
    def not_found(e):  # error view function
        errortype = 500
        error = 'Internal server error'
        return render_template("error404.html", mes=errortype, error=error)
    
    return app