"""
Copyright (C) 2023  Petr Buchal, Vladimír Jeřábek, Martin Ivančo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import uvicorn
from fastapi import FastAPI, Header, Request

from data_model import User

app = FastAPI(title="Recommendations API", docs_url="/", version="1.0")


@app.get('/shows/init', tags=["shows"])
@app.get('/movies/init', tags=["movies"])
def get_initial_content(request: Request):

    # your recommendation code

    response_example = [
      "27fe8750-38a9-4c88-8382-670134953db5",
      "2b931fcd-84e7-4469-88f2-74ff7ee2efdf",
      "da12b912-65ab-434a-8e47-9c17c0fd9d7e"
    ]
    return response_example


@app.put('/shows/recommendations', tags=["shows"])
@app.put('/movies/recommendations', tags=["movies"])
def get_recommendations(request: Request, user: User, recommendations_count: int = Header(16), sophisticated: bool = False):

    # your recommendation code

    response_example = [
      "27fe8750-38a9-4c88-8382-670134953db5",
      "2b931fcd-84e7-4469-88f2-74ff7ee2efdf",
      "da12b912-65ab-434a-8e47-9c17c0fd9d7e"
    ]
    return response_example


@app.get('/shows/similar/{wapitch_id}', tags=["shows"])
@app.get('/movies/similar/{wapitch_id}', tags=["movies"])
def get_similar(request: Request, wapitch_id, provider_id=None, country_code=None, count: int = 10):

    # your recommendation code

    response_example = {
                        "page": 0,
                        "total_count": 3,
                        "items": [
                          {
                            "id": "3306fd55-d2a3-4c3d-8a61-47ddf5200ee4",
                            "tmdb_id": 546554
                          },
                          {
                            "id": "087ec9dc-00e6-463f-b6af-e3ad030db082",
                            "tmdb_id": 537116
                          },
                          {
                            "id": "c3cc7b0b-7edd-468b-8ea9-ac970fdd8409",
                            "tmdb_id": 438631
                          }
                        ]
                      }
    return response_example


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
