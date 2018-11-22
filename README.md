# Discord Invite Checker

Simple module to check if Discord invite is actually valid.

## Why would you use this?

* ¯\\__(ツ)_\_/¯
* Instead of just deleting all invites, known or unknown, just check if it's actually valid


***
## How to use it

Takes only the code at the end of discord.gg/

**Sync**:
```python
>> import InviteChecker
>> InviteChecker('jb').is_invite_valid()
True
```

**Aysnc** (Recommended for Discord Bots)
> Input
```python
from InviteChecker import *



async def main():
    result = await InviteChecker('jb').is_invite_vaild()
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

> Output

```python
True
```


## License
Do whatever you want