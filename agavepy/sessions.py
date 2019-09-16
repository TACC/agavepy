import json
from .agave import Agave


def switch(client_name_or_key, username=None, tenant_id=None):
    # Read in current config
    try:
        current = Agave._read_current()
        # Try to inherit username and tenant from 'current' if not provided
        # This will let single-tenant switchers worry only about client_name
        if username is None:
            username = current.get('username')
        if tenant_id is None:
            tenant_id = current.get('tenantid')
    except IndexError:
        current = None

    # Read in sessions, then see if we can match to passed params
    try:
        complete_sessions = Agave._read_sessions()
        sessions = complete_sessions.get('sessions')
        if sessions is None:
            raise ValueError()
    except Exception:
        sessions = dict()
        sessions[tenant_id] = {}
        sessions[tenant_id][username] = {}
        complete_sessions = {'current': None, 'sessions': sessions}

    def resolve_client(sess, tenant_id, username, client_name_or_key):
        for k, v in sess.get(tenant_id, {}).get(username, {}).items():
            if k == client_name_or_key:
                return v
            elif v.get('apikey', None) == client_name_or_key:
                # v['client_name'] = client_name_or_key
                return v
        raise KeyError('Unable to find a matching client')

    session = resolve_client(sessions, tenant_id, username, client_name_or_key)

    print(session)

    if session.get('client_name', None) == client_name_or_key:
        if session.get('username') == current.get('username', None):
            if session.get('tenantid') == current.get('tenantid'):
                print('Current and target sessions do not differ')
                return False

    # Replace current file
    with open(Agave.tapis_current_path(), 'w') as current_file:
        # If the client was created in a client name-aware manner,
        # ensure client_name stays associated with the 'current' file
        if 'client_name' not in session or session.get('client_name') == '':
            session['client_name'] = client_name_or_key
        current_file.write(json.dumps(session))

    # Write out sessions file
    if 'client_name' not in current or current.get('client_name') == '':
        current['client_name'] = client_name_or_key
    complete_sessions['current'] = session
    complete_sessions['sessions'][tenant_id][username][
        client_name_or_key] = current

    # Write updated sessions file
    with open(Agave.tapis_sessions_path(), 'w') as sessions_file:
        sessions_file.write(json.dumps(complete_sessions))

    # They are the same - no need to switch

    # # Fetch the client from sessions.json that matches the tenant and user,
    # # plus either the client_name or the current.apikey
    # try:
    #     try:
    #         target_client = clients.get('sessions', {}).get(tenant_id, {}).get(
    #             username, {}).get(client_name_or_key, None)
    #     except KeyError:
    #         target_client = resolve_client(clients.get(
    #             'sessions', {}), tenant_id, username, client_name_or_key)
    # except KeyError:
    #     # Client did not exist in sessions cache
    #     target_client = dict()

    # # Keys arent same
    # if client['apikey'] != target_client.get('apikey', None):
    #     pass
