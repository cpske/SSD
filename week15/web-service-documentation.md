---
title: Document Web Services
---

Web Services without accurate, useful documentation are **useless**.

A standard format for Web Service documentation is OpenAPI Specification
(OAS), which evolved from [Swagger][swagger].

OpenAPI provides common-format, executable documentation.


## Approaches to API Documentation

1. **Design First** design the services and API. Write the API contracts using OpenAPI format.  
   - Tools exist for some frameworks to generate code from the OpenAPI documentation.

2. **Code First** write the web service code based on informal design, then create the full API documentation. 
   - Django RestFramework, FastAPI, and others can automatically generate live, executable OpenAPI documentation.
   - The quality of the documentation depends on the quality of your comments in code, and usually requires extra documentation files to be useful.


## OpenAPI Guide

[OpenAPI Guide](https://swagger.io/docs/specification/about/) on swagger.io has explanation and examples of elements in OpenAPI.

[Live Example](https://petstore.swagger.io/) Swagger Petstore. 
- The endpoint names are **poor** in my opinion.
- bad names: 
  - `/pet` should be `/pets`
  - `POST /pet/{petId}/uploadImage` definitely **bad** should be `/pets/{petId}/image`.  The URL (`image`) names a **resource** not an **action**. `POST` describes the action.
  - `/user/` hierarchy is similarly bad

[OpenAPI Tutorial on SmartBear](https://support.smartbear.com/swaggerhub/docs/tutorials/openapi-3-tutorial.html)

[Example with Code](https://openliberty.io/guides/microprofile-openapi.html) using Java and Maven, for an inventory application.  On <https://openliberty.io>.  A bit heavy on Java.


[Books Example](https://betterprogramming.pub/how-to-document-your-rest-api-with-openapi-aka-swagger-b0bcc118ebe7) how to write a YAML file using OpenAPI syntax for a books collection, with screenshots of the result.


## Tools

[SwaggerEditor](https://github.com/swagger-api/swagger-editor) creates a YAML file for OpenAPI documentation. This is a "document first" approach, or when the framework your web service is built on doesn't generate OpenAPI documentation.













[swagger]: https://swagger.io
