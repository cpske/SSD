---
title: Documenting Web Services
---

## API Documentation

Web Services without accurate, detailed documentation are **useless**.

Good (but complex) examples of API documentation are

- [Twitter API](https://developer.twitter.com/) and [Reference](https://developer.twitter.com/en/docs/api-reference-index)
- [Github](https://docs.github.com/en/rest)
- ?

## Approaches to API Documentation

1. **Design First** design the services and API. Write the API contracts using OpenAPI format.  
   - Tools exist for some frameworks to generate code from the OpenAPI documentation.

2. **Code First** write the web service code based on informal design, then create the full API documentation. 
   - Django RestFramework, FastAPI, and others can automatically generate live, executable OpenAPI documentation.
   - The quality of the documentation depends on the quality of your comments in code, and usually requires extra documentation files to be useful.


## Structure of Documentation

1. Describe what the API does, what it provides, version number, URL of API servers. This is also called **Meta information**.

2. Authentication, if any. Many APIs require an *API Key* sent as header.

3. **Reusable Components** things that can be used across many endpoints, such as request parameters, headers, content types, documentation of common fields and their data types.

4. **Endpoints** - specific URLs, parameters, the allowed HTTP methods, query params, return values, status codes. For example:
   ```
   GET /orgs/{orgname}/repos

   Parameters:
   per_page    integer      query-param  Max results per page (default 30)
   page        integer      query-param  Page number of results
   ```

   NOTE:  I think this is a poor API Endpoint, because the response is 
   very long. It returns full details of all repos.

   A better API would (by default) return only brief info about the repos
   and an API link to the repository (/orgs/{orgname}/repos/{reponame}) for more detail. 

   ```
   POST /orgs/{orgname}/repos
   ```
   Create a repository.



5. **Examples** include an example for each Reusable Component and each Endpoint.

## OpenAPI

OpenAPI Specification (OAS) is a standard format for Web Service documentation,
which evolved from [Swagger][swagger].

OpenAPI provides common-format, executable documentation.

2 ways to create OpenAPI documents:

- write the web service and have the framework generate it

- write a JSON or YAML file in OpenAPI format
  - this creates more readable documentation
  - tools can create code template for Web Service from your OpenAPI file

## OpenAPI Examples

[Live Example](https://petstore.swagger.io/) Swagger Petstore. 
- The endpoint names are **poor** in my opinion.
- bad names: 
  - `/pet` should be `/pets`
  - `POST /pet/{petId}/uploadImage` definitely **bad** should be `/pets/{petId}/image`.  The URL (`image`) names a **resource** not an **action**. `POST` describes the action.
  - `/user/` hierarchy is similarly bad

[Inventory Application in Java](https://openliberty.io/guides/microprofile-openapi.html) using Java and Maven, on <https://openliberty.io>.  A bit heavy on Javaand you need Maven to build it.

[Books Example](https://betterprogramming.pub/how-to-document-your-rest-api-with-openapi-aka-swagger-b0bcc118ebe7) how to write a YAML file using OpenAPI syntax for a books collection, with screenshots of the result.


## Learning OpenAPI and References

[OpenAPI Tutorial on SmartBear](https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html)

[OpenAPI Specification](https://swagger.io/specification/) and [Guide](https://swagger.io/docs/specification/) on Swagger tells you the exact format, fields, and how to specify data types and values, with examples in JSON and YAML.

## Tools

[SwaggerEditor](https://github.com/swagger-api/swagger-editor) creates a YAML file for OpenAPI documentation. This is a "document first" approach, or when the framework your web service is built on doesn't generate OpenAPI documentation.

[SwaggerHub](https://app.swaggerhub.com/) write and deploy documentation here. Free account available.












[swagger]: https://swagger.io
