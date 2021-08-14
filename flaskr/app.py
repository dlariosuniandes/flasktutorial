from enum import Enum
from flaskr import create_app
from flask_restful import Api
from .modelos import db, Cancion, Album, Medio, CancionSchema, AlbumSchema
from .vistas import VistaCanciones, VistaCancion, VistaSignIn, VistaAlbumsUsuario, VistaCancionesAlbum, VistaAlbum, VistaLogIn
from flask_jwt_extended import JWTManager


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')
api.add_resource(VistaLogIn, '/login')

jwt = JWTManager(app)