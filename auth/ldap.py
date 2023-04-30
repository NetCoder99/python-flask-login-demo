from ldap3 import Server, ALL, Connection, NTLM

# server = Server('localhost:8389',  get_info=ALL)
# conn   = Connection(server, auto_bind=True)
# conn.bind()
# conn.result
# conn.search('uid=bob,dc=breadcrumbdata,dc=com', '(objectclass=person)')


#ldap_url  = r'localhost'
#ldap_port = r'8389'
#base_dn = r'uid=bob,dc=breadcrumbdata,dc=com'
#server = Server('localhost:8389',  get_info=ALL)
#conn = Connection(server, user="bob", password="bobspassword", authentication=NTLM)
#conn = Connection(server, user="uid=bob,dc=breadcrumbdata,dc=com", password="bobspassword", authentication=SIMPLE)
#conn.search('uid=bob,dc=breadcrumbdata,dc=com', '(objectclass=person)')

