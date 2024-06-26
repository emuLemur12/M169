#from ldap3 import NTLM
import os
import socket
from ms_active_directory import ADDomain, ADUser, ADGroup
hostname = socket.gethostname()
if hostname == "BDNB9571593":
    from dotenv import load_dotenv
    load_dotenv()
password = os.getenv("PASSWORD")
domain = ADDomain("BS.CH", ldap_servers_or_uris=["ldaps://bsprodsvdc01.bs.ch:636", "ldaps://bsprodsvdc02.bs.ch:636", "ldaps://bsprodsvdc03.bs.ch:636", "ldaps://bsprodsvdc04.bs.ch:636"])
session = domain.create_session_as_user('dbdsaw@bs.ch', password)
#Get Users
def get_users(group):
    password = os.getenv("PASSWORD")
    domain = ADDomain("BS.CH", ldap_servers_or_uris=["ldaps://bsprodsvdc01.bs.ch:636", "ldaps://bsprodsvdc02.bs.ch:636", "ldaps://bsprodsvdc03.bs.ch:636", "ldaps://bsprodsvdc04.bs.ch:636"])
    session = domain.create_session_as_user('dbdsaw@bs.ch', password)
    users = session.find_members_of_group(group, ['displayName'])
    usernames = []
    for user in users:
        if user.get('displayName') is not None:
            name = (user.get('displayName'))
            usernames.append(name)

        elif user.get('displayName') is None:
            users2 = session.find_members_of_group(user.get('cn'), ['displayName'])
            for user2 in users2:
                if user2.get('displayName') is not None:
                    name = (user2.get('displayName'))
                    usernames.append(name)
    return(usernames)
#    print(user.get('displayName'))
    #print(user.get('sAMAccountName'))
#    print()
    #print(user.distinguished_name)