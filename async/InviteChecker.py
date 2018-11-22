import aiohttp
import asyncio

class InviteChecker:
    def __init__(self, code=None, **kwargs):
        self.code = code
        for key,value in kwargs.items():
            setattr(self, key, value)

    async def is_invite_vaild(self):
        """ Checks if invite is vaild """
        async with aiohttp.ClientSession() as session:
            async with session.get('https://discordapp.com/api/v6/invite/' + self.code + '?with_counts=true') as response:
                status_code = response.status
                
                if status_code == 404:
                    return False
                elif status_code == 200:
                    return True
                else:
                    return('Unknown, try again')
            
