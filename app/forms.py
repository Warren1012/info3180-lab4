from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    Upload = FileField('Upload:', validators=[FileRequired(),FileAllowed(['jpg','pnp'],'Images only!')])