from ldap3 import Server, ALL, Connection, SUBTREE, NTLM, Reader, ObjectDef

from models.User import User


def CheckUserCreds(user_name, pass_word):
    search_base = f'uid={user_name},ou=users,dc=flaskldap,dc=com'
    search_filter = '(objectclass=person)'

    server = Server('localhost:8389', get_info=ALL)
    ldap_conn = Connection(server, auto_bind=True)

    ldap_conn.search(search_base=search_base,
                     search_filter=search_filter,
                     search_scope=SUBTREE,
                     attributes=['cn', 'sn', 'uid', 'userPassword', 'givenName', 'mail'])

    results = ldap_conn.entries
    if results is None or len(results) == 0:
        return False, None

    if results[0].userPassword.values[0].decode('utf-8') != pass_word:
        return False, None

    admin_users = GetGroupMembers('admins', ldap_conn)
    develop_users = GetGroupMembers('developers', ldap_conn)

    rtn_user = User(
        dn = search_base,
        uid = results[0].uid.value,
        username = results[0].cn.value,
        email = results[0].mail.value,
        active = True)

    return True, rtn_user


def GetGroupMembers(group_name: str, ldap_conn):
    rtn_list = []
    search_base = f'cn={group_name},ou=groups,dc=flaskldap,dc=com'
    search_filter = '(objectclass=groupOfUniqueNames)'
    srch_results = ldap_conn.search(search_base=search_base,
                                    search_filter=search_filter,
                                    search_scope=SUBTREE,
                                    attributes=['uniqueMember'])
    for group_member in ldap_conn.entries[0].uniqueMember.values:
        print(f'group_member:{group_member}')
        rtn_list.append(group_member)

    return rtn_list
