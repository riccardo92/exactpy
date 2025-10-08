# ExactPy

A modern, highly configurable Python interface to the Exact Online API based on Pydantic.

## Why?

Currently available packages aren't configurable in such a way that they are usable to me. This package attempts to fix that.

## Sample usage

### Initial oauth token request

This initial token request theoretically needs to be done once. An access token and requets token will be available after this. If the access token is refreshed in time (refresh token is valid for 30 days max), no log in has to be performed.

```python
from exactpy.client import Client

client = Client(
    client_id="xxx",
    client_Secret="xxx,
    verbose=True,
)

# this can literally be anything, but it needs to be valid
# so that redirects can happen
redirect_url = "https://some_website"
print(client.get_authorization_url(redirect_url=redirect_url)

# Now, open the url that was printed, log in to exactonline and copy the response url
response_url = "<paste_url_here>"

# Now retrieve the access token and refresh token
client.retrieve_token(response_url=response_url)
client.cache_credentials()
```

If your cache callable was not set to `None`, your credentials should now have been saved. In the default case, they're saved in `creds.json` (plain text).

Now you can use the client like below:

```python
from exactpy.client import Client

client = Client(
    client_id="xxx",
    client_Secret="xxx,
    verbose=True,
)

client.load_credentials()
client.check_token_validity()
client.cache_credentials()

# Every request you do, will trigger a token
# check as well. In the default case, auto-caching is done
# This means that the current access token and refresh token
# (after a optional refresh) are cached. This is only true
# if cache_callable was not set to None.
# To disable this behaviour, either set cache_callable to None
# or set autocache_enabled to False.
accounts = client.accounts.all()
```
