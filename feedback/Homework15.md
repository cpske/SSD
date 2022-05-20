---
title: Feedback on REST API Design
---

## Scoring

- 1 pt: Actual status codes (not a list of all HTTP status codes) documented
- 1 pt: Request headers documented
- 1 pt: Data elements, types, and values defined
- 1 pt: Example
- 1 pt: URLs and methods are complete for the application
- 2 pt: Use GET, PUT, POST, DELETE used correctly
- 3 pt: RESTful Design - URLs are resources with only ONE URL for one resource
  - OK to have special URL for services
  - Not OK to use URL for query parameters
  - Not OK to use URL like RPC (many urls for services)
    ```
    # WRONG - using url as a query
    GET /api/person/id/{id}      get by id
    GET /api/person/name/{name}  get by name
    # WRONG - urls like  remote procedure calls
    GET /api/get-book-by-title?title="sometitle"
    GET /api/get-book-by-author?author="somename"
    GET /api/get-book-by-genre?genre="something"
    ```

Important characteristics of a REST API are:

- each resource has a **single unique** URL
- for queries, use HTTP **query parameters** to send the query parameters, not URL components
  ```
  GET /registrar/api/course/{id}      course object identified by some id
  GET /registrar/api/course/search?courseNumber="01219243"   search for course
  # Not this
  GET /registrar/api/findbynumber/{coursenumber}
  ```

## Bannakorn
```
GET /api/RainbowSixSiege               get all WHAT? Not documented
GET /api/RainbowSixSiege/id/{id}       should be /api/RainbowSixSiege/character/{id}
GET /api/RainbowSixSiege/name/{name}   poor, duplicate URL for resource. Use query param.
POST /api/RainbowSixSiege/character    correct (add a new character)
PUT /api/RainbowSixSiege/character     PUT should include resource's id 
```
Similarly, URL for "DELETE" is poor.

Problems:
- using URLs like RPC
- DELETE and UPDATE return code 201 (Created).
- Missing POST response should include `Location` header.
- Missing URLs for your other domain class

## Bhokin

API is incomplete.
```
GET /api/all-jasmine-rice-sale        poor, use same hierarchy as other GET
GET /api/jasmine-rice-sale/{id}/      OK but no trailing "/"
POST /api/buy-jasmine-rice/           Not in hierarchy, body params are incomplete
```
POST should return 201 and a Location header containing the sale id.


More RESTful API:
```
GET /api/jasmine-rice-sale            get all sales, use pagination to limit
GET /api/jasmine-rice-sale/{id}       get one sale
POST /api/jasmine-rice-sale/          create a new rice sale
body: weight, cost, time, customer_id
PUT /api/jasmine-rice-sale/{id}       complete update of one rice sale
PATCH /api/jasmine-rice-sale/{id}     partial update of one rice sale
DELETE /api/jasmine-rice-sale/{id}    delete a rice sale
```

Problems:
- 500 is not returned by web service
- 202 is not returned by web service
- POST should use same path as GET
- Incomplete: No API for customer resource

## Chanunya

```
GET /api/all-artists                  poor, using separate hierarchy
GET /api/artists/{id}                 OK
POST /api/create-artist/              Wrong, should be /api/artists/
DELETE /api/remove-artist/{id}        Wrong, should be /api/artists/{id}
```

Missing:
- GET all artists should use /api/artists/
- POST should use same path as GET
- POST should return `Location` header.
- DELETE should use same path as GET
- Missing PUT or PATCH to update an artist
- No URLS for your other domain class (Song)


## Chatchawarin

- Has URLs for both GPU and Warehouse

Problems:
- Your api does not return 204, 409, 500
- URLs do not form a consistent hierarchy
- Using URLs for query instead of query parameters
- Not RESTful, just a hodge-podge of URLS for specific queries
- PUT used incorrectly
- No POST to add new GPU type
- Update stock is incomplete (GET returns a zone for each gpu, but update does not supply a zone)

Your design using lots of unrelated URLs for different kinds of queries with URL components instead of query parameters.  Since there appears to be only one warehouse, the "zone" stuff is confusing and used inconsistently.

## Chayayot

Very incomplete. Only one URL and one method (GET).


## Chonchanok

```
GET item-list/{id}                    missing starting "/"
POST /item-list/add-new-market-user   not REST, should be POST /item-list/
DELETE /item-list/{id}                OK
```

Problems
- Your API should not use 202, 204, 500
- POST URL is incorrect, should use same path as GET
- POST does not return Location header
- DELETE URL is incorrect
- No URLs for your other domain class


## Ditthapong

- Header fields not documented.
- PUT URLs are incorrect. Should use same URL as GET.
- As used, PUT should be PATCH (partial update).
- GET /api/movie should not return 404. The URL does exist!
- GET /api/imdb should not return 404. The URL does exist!
- GET /api/movie/{title} is incorrect (not 1 URL per resource)
- Missing POST method to add a new movie or review.

- URLs are missing the "/" prefix

## Jakarin

Problems:
- URLs should use "-" not `_`.
- Your app should not return 500.
- `GET /api/customer/get_all_customer` not RESTful
- `get_by_id` not RESTful
- `get_all_laptop` not RESTful
- `POST /api/add-laptop/` not RESTful
- Response to POST is not documented. Should be 201 and have Location header
- "Sign in" you can't "sign in" to a web service because there is no session. Send auth header with each request.
- No PUT (update) or DELETE


```
GET /api/customer/get_all_customer   not RESTful, use just /api/customer/
GET /api/customer/get_by_id          not RESTful
GET /api/laptop/get_all_laptop       not RESTful, use just /api/laptop/
POST /api/laptop/add-laptop/         not RESTful
```
## Kittison

Problems:
- URLs are not RESTful. Your API uses URLs like function endpoints.
- RESTful would be: `/api/station/{id}` for GET, PUT, or DELETE methods.
- Your app should not return 500
- Authorization header not clearly or accurately documented

## Krasin

- Not RESTful URLs
- Your app should not return 203, 204, or 500
- Same design error as Bannakorn

## Krittamate

- Incomplete, only GET
- Not RESTful URLs `/api/get-all-country`, `/api/get-all-athlete`

## Kul

No API.

## Nabhan

- GET RESTful. should be `GET /bicycle/{id}` not `/bicycle/get/{id}`.
- PUT not RESTful and incorrect, should use item's own URL.
- DELETE - same problem as GET.
- URLs do not represent resources.
- Rental incomplete. Has POST but no GET.
- URLs for "/rent" not RESTful.
- Header fields not documented; documentation by curl examples insufficient.
- Curl examples for "Authorization: Bearer" are missing the token.
- Nice looking document.

## Natchanon

- Has RESTful API.
- URL in table form is easy to read.
- Would be nice to have URL to GET all borrow records, with query parameters to filter what you want, such as "*only records for books still checked out*".

## Pakapop

- "bookings" api is RESTful.
- No API for users (only for bookings).

## Panitan

- Not RESTful URLS: Same design error as Bannakorn
- PUT and DELETE should return 200 (not 201 Created)

```
GET /api/Football/footballers/id/{id}  should be /api/Football/footballers/{id}
POST /api/Footballer/add_footballers   should be POST /api/Football/footballers/
PUT /api/Football/footballers          missing {id} component on URL
DELETE /api/Football/footballers/id/{id} extra "/id/" same as GET
```

## Panu

- Uses same URL for 2 different requests.  This is not RESTful and probably won't work.
- POST URL incorrect. should be `/api/character`
- Using url components instead of qauery params for queries.
- Header fields not documented.
- Response codes not documented, except 200 and 201 (by example)
- No PUT (update) or DELETE

```
GET /api/character/{CharacterID}       Get character by id
GET /api/character/{owner_id}          "Get character by Weapon ID" (really?)
POST /api/character/new                Omit "new"
```
same problem for weapons. This could work if no confusion between id
and weapon type, but makes violates 1 URL per resource rule.
```
GET /api/weapon/{id}                 Get weapon by id
GET /api/weapon/{weaponType}         Get weapons by type
```
Better:
```
GET /api/weapon/?weapontype={weaponType}  Use query parameter for filter
```

## Panuwat

- URLs not RESTful.  The URL duplicates the the HTTP method. Should be 1 URL per resource.
- PATCH incorrect
- POST incorrect
- DELETE incorrect. URL is incorrect and DELETE does not have a body.
- POST should return 201 and Location header

## Patkamon

RESTful except POST should be `POST /api/movies/` (don't need `add`).

## Pattanan

- Documentation of response codes just copied from somewhere else, includes response code that your API never returns.
- API is incomplete, just 2 GET endpoints.
- `GET /api/all_brands` should be `GET /api/brands`, and have `GET /api/brands/{id}`, etc.

## Peerasu

- Not RESTful URLs: same mistake as Bannakorn 
- Has too many URLs, not one URL for one resource
- UPDATE and DELETE should not return status code 201.
- POST should return the URL or id of the created resource
- Your app should not return status code 500

## Phakarat

- Same mistake as Bannakorn
- API doc should not include the server IP address. That is variable.
- `GET /title/` is not part of hierarchy containing other related URLs.
- Hodge podge of URLs for different types of queries, mostly using URL components instead of query parameters. Get by rating is only endpoint using query param.
- Good documentation of data fields in Episode (data dictionary) but it is **redundant** (same table 8 times!). 


## Phawit

- RESTful API (mostly)
- PATCH should use a resource's URL: `PATCH /api/book/{id}`
- DELETE should use a resource's URL: `DELETE /api/book/{id}`.
- Sending `token` as a query parameter is not RESTful and may appear in log files.  Send it as `Authorization` header instead.

## Poomtum

- "GET /staff/id/" is misdocumented. Should be "GET /staffs/{id}".
- Same for "GET /titles/id/"
- Incomplete: Only 2 GET URLs 
- Doesn't document possible return status codes
- Documentation of Authentication header is not clear. What part is variable data?

## Raweerot

- `GET /api/all_products/` should be `GET /api/products/` (same as for specific product w/o the id)
- Not RESTful: GET /api/customers/{gender}, should use query parameter
- Response does not make sense. `GET /api/customers/{gender}` example returns both male and female customer.  And case **is inconsistent**! "male" and "Female"
- Super Not RESTful: using GET to create a new customer.
- Example is nonsense. Looks like a console application.
- No POST, PUT, or DELETE.
- Object fields not documented.
- **Copying:** this is too similar to Sirawich. Same mistakes.


## Siraphop

- Documentation of request headers is poor and incorrect.
- POST URL not restful. Should be only `/api/anime`.
- PUT URL not restful. Should be `/api/anime/{id}`.
- DELETE URL not restful, same as PUT.
- Response code for POST should be documented. POST should return Location header.
- DELETE does not allow a request body (your example has request body).

## Sirapop

- Same design mistake as Bannakorn.
- Example response for "Get Character by id" is incorrect. There is one one object, not an array of objects.
- "Get by name" is not RESTful. Should use query parameter.
- POST URL not RESTful (same mistake as Bannakorn).
- PUT and DELETE URLs not RESTful.
- Same issues for "Weapons" URLs.

## Siratee

Good. Documentation is well written and nicely formatted.

## Sirawich

- "Get by gender" URL not RESTful. Use a query parameter for gender. 
- Super Not RESTful: use "GET" to create a new citizen.
- This doesn't look an API. Examples look like running a console dialog.
- **Copying:** this is too similar to Raweerot. Same mistakes.

## Sittipat

- POST URL should be same as GET (/api/records/)
- POST should return 201 and include Location header
- PATCH URL should be `/api/records/{id}`
- URLs not RESTful: you use URLs to name services, not resources

## Soravit

- No API docs in wiki

## Tanin

- Authentication by password won't work. Curl example is incorrect, too.
- Your app should not return 500, 501, 502, 503. 200 is documented twice.
- Not RESTful URLs: you use the URL to name the type of request.
- `GET /get/car/{id}` should be `GET /api/car/{id}`
- `GET /get/car/{name}` not restful, name should be query parameter.
- URLs are **poorly documented**. Reader must study the "curl" examples to get the URLs.
- POST and UPDATE URLs incorrect
- URLs do not form consistent hierarchy.

## Tawan

- Not RESTful URLs. You use urls as service request endpoints (like RPC).
- "Add a Pet" should use POST, not PUT.
- "Add new customer" should use POST, not PUT.
- Missing update using "PUT" for pets and customers.


## Thanabardi

- URLs require a number to identify provinces, so there should be a URL to get all province codes. `GET /api/provinces/`. 
- I think having a `POST /api/login/` is not secure, and username and password should not be query parameters.  Use Authentication header, preferrably with DIGEST authentication (hashes parameters).

## Thanathip

- `GET /cars/sort` is not RESTful. Use query param to request sorting.
- `GET /cars/brand/{brandname}` is not RESTful. The brandname should be query parameter (not part of URL), and having a general "search" URL would be more flexible.
- I think having a `POST /login/` is not secure, and username and password should not be query parameters.  Use Authentication header, preferrably with DIGEST authentication (hashes parameters).  But why have "login" to a web service?  Assign access tokens with scope via a web app.


## Thanatibordee

- RESTful API.
- Needs URL to add users or games (POST).
- Good documentation.

## Vitvara

- API is not RESTful. It's a collection of separate URLs for services.
- URLs are not clearly documented. User must read curl example code to get the URLs.
- URLs for "Booking Service" request URLs are buried in Python code example, and not RESTful.



