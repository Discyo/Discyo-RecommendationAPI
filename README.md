# Recommendations API

This is a [FastAPI](https://fastapi.tiangolo.com/) web app made as a part of Discyo - a cross-media recommendation platform project. In our endeavor to maintain certain proprietary aspects of our project, we've opted not to disclose the entirety of our recommendation code. However, for those interested in building upon our work, we've provided a streamlined skeleton of the Recommendations API, developed with FastAPI.

Provided API encompasses all the necessary methods required for the platform's operation. For a more in-depth understanding, we've detailed each method in an [OpenAPI](https://www.openapis.org/) specification available at `docs/recommendations-api-openapi.yaml`.

## Getting Started

The OpenAPI specification brings along a suite of valuable tools:

- **Swagger editor** - This is a space where you can upload the `docs/recommendations-api-openapi.yaml` specification for a more human-readable format.
- **Swagger codegen** - Here, one can even generate source code for both client and server-side applications.

If you'd like to use our example code, we have provided a Docker configuration that's ready to use:
```bash
docker-compose up --build
```
