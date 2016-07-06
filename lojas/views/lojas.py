from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config
from ..models import Loja
from ..services.lojas import LojasService
from ..forms import LojaCreateForm, LojaUpdateForm

@view_config(route_name='nossaslojas',
             renderer='../templates/lojastemplate.jinja2')
def todas_lojas(request):
    todasLojas = LojasService.all(request)
    return {'todasLojas': todasLojas}

@view_config(route_name='loja_action', match_param='action=create',
                 renderer='../templates/loja_edit.jinja2')
def loja_create(request):
    entry = Loja()
    form = LojaCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('nossaslojas'))
    return {'form': form, 'action': request.matchdict.get('action')}

@view_config(route_name='loja_action', match_param='action=edit',
                 renderer='../templates/loja_edit.jinja2')
def loja_update(request):
    loja_id = int(request.params.get('id', -1))
    entry = LojasService.by_id(loja_id, request)
    if not entry:
        return HTTPNotFound()
    form = LojaUpdateForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(location=request.route_url('nossaslojas'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='loja_action', match_param='action=remove',
                 renderer='../templates/lojastemplate.jinja2')
def loja_delete(request):
    loja_id = int(request.params.get('id', -1))
    entry = LojasService.by_id(loja_id, request)
    if not entry:
        return HTTPNotFound()
    request.dbsession.delete(entry)
    return HTTPFound(location=request.route_url('nossaslojas'))