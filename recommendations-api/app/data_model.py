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
from typing import List
from pydantic import BaseModel
from datetime import datetime


class Rating(BaseModel):
    uuid: str
    value: int
    timestamp: datetime


class Interest(BaseModel):
    uuid: str
    value: bool
    timestamp: datetime


class User(BaseModel):
    country_code: str
    providers: List[str] = []
    ratings: List[Rating] = []
    interest: List[Interest] = []


if __name__ == '__main__':
    external_data = {
        'country_code': 'CZ',
        'providers': ['5257a35e-6e53-4ee3-9147-de093c4164e8', '903ca85c-2870-49eb-a85f-1120e2a90936'],
        'ratings': [{'uuid': '00017783-07cb-45ba-9a12-1de137275365', 'value': 0, 'timestamp': '2019-06-01 12:23'}, {'uuid': '000346fe-714a-4199-aded-bc7ebb07fba0', 'value': 3, 'timestamp': '2019-06-01 12:22'}],
        'interest': [{'uuid': '000443a3-f598-4fc4-9c9d-9d000021818f', 'value': False, 'timestamp': '2019-06-01 12:24'}, {'uuid': '0004b621-3a27-4aab-b5c5-9cf216350091', 'value': True, 'timestamp': '2019-06-01 12:22'}]
    }
    user = User(**external_data)
