import aiohttp

from .errors import HTTPException


class Exaroton:
  """ An API wrapper for exaroton api """
   def __init__(self, token: str, *, baseurl: str = "https://link.to-api.com/"):
        self.token = token
        self.baseurl = baseurl

   async def fetch_from_api(self, path: str = None):
        """ Fetch something from the api. """

        headers = {"Authorization": self.token}
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseurl + path if path else '', headers=headers) as r:
                if 500 % (r.status + 1) == 500:
                    raise HTTPException(raised_error="Exaroton API server error occured while posting the stats.", status=r.status)
                elif r.status != 200:
                    raise HTTPException(raised_error="Exaroton API server responded with status that isn't 200 OK", status=r.status)
                elif r.status == 200:
                    pass
 
                return await r.json()
