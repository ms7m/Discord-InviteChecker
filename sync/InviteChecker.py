import requests

class InviteChecker:
    def __init__(self, code=None, **kwargs):
        self.code = code
        self.check = None
        for key,value in kwargs.items():
            setattr(self, key, value)


    def is_invite_vaild(self):
        """ Checks If Invite is vaild """
        try:
            check_discord = requests.get('https://discordapp.com/api/v6/invite/' + self.code + '?with_counts=true')
        except Exception:
            raise Exception

        if check_discord.status_code == 404:
            return False
        elif check_discord.status_code == 200:
            return True
        else:
            return("Unknown, try again.")
