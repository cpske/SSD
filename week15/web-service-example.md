---
title: Web Service Example
---

## [Github REST API](https://docs.github.com/en/rest)

From the [Github API Documentation](https://docs.github.com/en/rest),
view [Getting Started](https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api).

What does Getting Started show you?

- Example API call and what it returns
  ```
  curl GET https://api.github.com/
  curl GET https://api.github.com/users/defunkt   <<< sample user info
  ```

- Details of headers and response
  ```
  curl -i GET https://api.github.com/users/defunkt
  ```

- Authentication
  - Personal access tokens (for curl use the -u username:passwd syntax)
    ```
    GET https://api.github.com/user
    Authorization: Basic xxxxxx
    ```
    where xxxxxx = `b64encode(b"username:password").decode("ascii")`
    ```
    GET https://api.github.com/user
    Authorization: Token your_access_token
    ```
  - How to use authentication, with examples.

- Reference Section
  ```
  /user
  /users/{username}
  /users/{username}/hovercard
  /repos/{owner}/{repo}
  ```


### 1. No support for alternate representations

```
GET /api.github.com/
Accept: application/xml
```
Returns:
```
415 Unsupported Media Type
```


### 2. Token-based Authentication

Github API accepts a **Personal Access Token** for authentication, which you create on Github:    
**Account Settings** --> **Developer Settings** (Left side) --> **Personal access tokens**

Each token has:

1. descriptive name
2. lifetime (duration)
3. scopes - what the token is authorized to do

### Sending a Personal Access Token as Request Header

HTTP Authorization Header:

```
GET /api.github.com/user
Authorization: Token your_access_token
```

or use Basic Auth (you need to encode username:token). 
The Python Requests package will do the encoding for you,
but for the curios:

```python
import base64
bytestr = base64.b64encode(f"{username}:{token}".encode('ascii'))
```
then send:
```
GET /api.github.com/user
Authorization: Basic {bytestr.decode()}
```

To add an Authorization header to a `curl` request, use:
```
curl -u username:token https://api.github.com/user
```

A Personal Access Token has 


### 2. `/user` endpoint - info about the authenticated user

Documentation: <https://docs.github.com/en/rest/users/users>


Methods available:
* GET
  - parameters
  - response codes
  - example
* PATCH - update the authenticated user
  - parameters
  - response codes
  - example

### 3. Repositories

Exercise

