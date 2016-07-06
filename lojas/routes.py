def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('nossaslojas', '/lojas/all')
    config.add_route('loja_action', '/loja/{action}')
