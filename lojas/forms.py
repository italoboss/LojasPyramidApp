from wtforms import Form, StringField, TextAreaField, validators
from wtforms import HiddenField

strip_filter = lambda x: x.strip() if x else None

class LojaCreateForm(Form):
    name = StringField('Nome', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    description = TextAreaField('Descricao', [validators.Length(min=1)],
                         filters=[strip_filter])

class LojaUpdateForm(LojaCreateForm):
    id = HiddenField()