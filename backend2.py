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
desired_attrs = ['displayName'] 
group_name = 'GG-BD-Informatik'
group_to_member_list_map = session.find_members_of_group_recursive(group_name, desired_attrs)
group_to_member_list_map2 = session.find_members_of_group(group_name, desired_attrs)
print(group_to_member_list_map[0].get('ADUser[1]'))