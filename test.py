import os

from src.kreta.mobile import endpoints, models
from src.kreta.idp import Auth_Session

username = os.getenv("username")
pwd = os.getenv("pwd")
institute_code = os.getenv("institute_code")

with Auth_Session.login(username, pwd, institute_code) as session:
    response = endpoints.get_notes(session)
    print(response)

    session.refresh() # it's automatically done when needed
    
    response = endpoints.get_device_state(session)
    print(response)
    
    session.invalidate() # invalidates the refresh token so remove if login is saved
