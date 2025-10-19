# Bus ETA API Specifications

**Source:** bus_eta_api_specifications.pdf
**Converted:** 2025-10-19

---

Real -time “Next Bus” arrival time

and related data

Citybus Limited

API Specifications

Version 2.01

July 2023

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 2 of 22

Amendment History

Version Number  Revision Details  Revision Date  Author

### 1.00 Initial Version  July 2019  DA Division, OGCIO

## ITD & OSD, CTB & NWFB

### 1.01  Amendment on Section

3 Route API  Aug 2019  DA Division, OGCIO

## ITD & OSD, CTB & NWFB

### 1.02  Amendment on Section

1 API Base URL  Dec 2021  DA Division, OGCIO

## ITD & OSD, CTB & NWFB

### 2.00  Amendment s of base

URL and items related to

franchise merger  Jun 2023 DA Division, OGCIO

## TEC,  CTB & NWFB

### 2.01  Update company info  Jul 2023  DA Division, OGCIO

## TEC,  CTB

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 3 of 22

Table of Contents

### 1. Important Notes  ................................ ................................ ................................ ...................  4

### 2. API Base URL  ................................ ................................ ................................ .......................  4

### 3. Company API  ................................ ................................ ................................ .......................  5

### 4. Route API  ................................ ................................ ................................ .............................  7

### 5. Stop API  ................................ ................................ ................................ ...............................  9

### 6. Route -Stop API  ................................ ................................ ................................ ...................  11

## 7. ETA API  ................................ ................................ ................................ ..............................  19

### 8. Error Response  ................................ ................................ ................................ ..................  22

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 4 of 22

### 1. Important Note s

(a) Starting from June 2023, the V2 API is now available for public access to real -time "Next Bus"

arrival time and related data for Citybus. To ensure uninterrupted data access in the future, it is

recommended to transition to the V2 API. Please refer to the API Specification for more details.

The V1.0 and V1.1 API versions will be discontin ued after 31st December 2023.

(b) All New World First Bus routes already  integrated into Citybus. Users can continue to use the

Citybus API  for accessing real -time "Next Bus" arrival time and related data for all routes operat ing

by Citybus, including th ose routes operated by New World First Bus  before 1 July 2023 . Data of all

routes are available under the {company_id} "CTB" in the API.

### 2. API Base URL

All APIs described in this document share the following base URL:

Base URL  https://rt.data.gov.hk/

In all the APIs, data field “generated_timestamp” has different arrangement in v1.0 and v1.1  &

V2:

V1.0

Base URL  https://rt.data.gov.hk/v1/ transport/citybus -nwfb/

Arrangement  Data field name is “generated_timestamp “ ( with  trailing space at the

end of field name)

V1.1  and V2

Base URL  https://rt.data.gov.hk/v1.1/ transport/citybus -nwfb/

https://rt.data.gov.hk/v 2/transport/citybus/

Arrangement  Data field name is “generated_timestamp“ ( without  trailing space at

the end of field name)

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 5 of 22

### 3. Company API

Description:  This API takes a  Citybus  company ID and returns the respective company

information.

HTTP Request:

Endpoint  company/{company_id}

HTTP Method  GET

Parameter  Parameter Type  Description  Required

company_id  Path  Company ID under Citybus

Valid company IDs are:

● CTB  - Citybus Limited

Sample Request:

/v2/transport/ citybus /company/ CTB

HTTP Response:

Response Format  JSON

Response Code  Response

200 Success, see sample response below

422 See message in response body

429 Processing too many requests

500 Internal Server Error

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 6 of 22

Sample Response:

"type": "Company",

"version": " 2.0",

"generated_timestamp": " 2023 -07-01T11:40:48+08:00",

"data": {

"co": "CTB",

"name_tc" : "城巴有限公司 ",

"name_en": "Citybus Limited",

"name_sc": "城巴有限公司 ",

"url": "http s://www.citybus.com.hk",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

Note: Refer to the data dictionary on description and specifications on the returned fields.

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 7 of 22

### 4. Route API

Description:  This API takes a Citybus  company ID and the company’s operating bus route

number and returns the respective route information.

Important N ote: All New World First Bus routes already  integrated into Citybus. Data of all

routes are available under the {company_id} "CTB".

HTTP Request:

Endpoint  route/{company_id}/{route}

HTTP Method  GET

Parameter  Parameter Type  Description  Required

company_id  Path  Company ID under Citybus .

Valid company IDs are:

● CTB  - Citybus Limited  Y

route  Path  Optional: The route number of the

respective bus company specified

above.

If the route parameter is not

provided, the complete route list of

the respective company will be

returned.

Sample Request:

/v2/transport/ citybus  /route/CTB/107

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 8 of 22

HTTP Response:

Response Format  JSON

Response Code  Response

200 Success, see sample response below

422 See message in response body

429 Processing too many requests

500 Internal Server Error

Sample Response:

"type": "Route",

"version": " 2.0",

"generated_timestamp": " 2023 -07-01T11:40:48+08:00",

"data": {

"co": "CTB",

"route": "107",

"orig_en": "Wah Kwai Estate",

"orig_tc": "華貴邨 ",

"orig_sc": "华贵邨",

"dest_en": "Kowloon Bay",

"dest_tc": "九龍灣 ",

"dest_sc": "九龙湾",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

Note: Refer to the data dictionary on description and specifications on the returned fields.

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 9 of 22

### 5. Stop API

Description:  This API takes a 6 -digit bus stop ID and returns the respective bus stop

information.

(Remark:  To find the  corresponding bus stop ID, user can  query the " Route -Stop API ")

HTTP  Request:

Endpoint  stop/{stop_id}

HTTP Method  GET

Parameter  Parameter Type  Description  Required

stop_id  Path  ● 6-digit representation of a bus

stop  Y

Sample Request:

/v2/transport/ citybus /stop/00 2737

HTTP Response:

Response Format  JSON

Response Code  Response

200 Success, see sample response below

422 See message in response body

429 Processing too many requests

500 Internal Server Error

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 10 of 22

Sample Response:

"type": "Stop",

"version": "2 .0",

"generated_timestamp": "2023 -07-01T11:40:48+08:00 ",

"data": {

"stop": "002737",

"name_tc": " 砵典乍街 , 德輔道中 ",

"name_en": "Pottinger Street, Des Voeux Road Central",

"name_sc": " 砵典乍街 , 德辅道中 ",

"lat": 22.283948,

"long": 114.156309,

"data_timestamp": "2023 -07-01T11:40:00+08:00 "

Note: Refer to the data dictionary on description and specifications on the returned fields.

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 11 of 22

### 6. Route -Stop API

Description:  This API takes a Citybus  company ID, route direction and the company’s

operating bus route number and returns the stop information of the respective route.

Important N ote: All New World First Bus routes already  integrated into Citybus. Data of all

routes are available under the {company_id} "CTB".

HTTP Request:

Endpoint  route -stop/{company_id}/{route}/{direction}

HTTP Method  GET

Parameter  Parameter Type  Description  Required

company_id  Path  Company ID under Citybus .

Valid company IDs are:

● CTB  - Citybus Limited

route  Path  The route number of the respective

bus company specified above.  Y

direction  Path  The direction of the route number as

specified above.

Valid directions are:

● inbound - direction towards

origin

● outbound - direction towards

destination

Sample Request:

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 12 of 22

/v2/transport/ citybus /route -stop/CTB/1/inbound

HTTP Response:

Response Format  JSON

Response Code  Response

200 Success, see sample response below

422 See message in response body

429 Processing too many requests

500 Internal Server Error

Sample Response:

"type": "Route",

"version": " 2.0",

"generated_timestamp": " 2023 -07-01T11:40:48+08:00",

"data": [

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 1,

"stop": "002403",

"data_timestamp": " 2023 -07-01T11:40:00+08 :00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 2,

"stop": "002402",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 13 of 22

"route": "1",

"dir": "I",

"seq": 3,

"stop": "002492",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 4,

"stop": "002493",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 5,

"stop": "002453",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 6,

"stop": "002552",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 7,

"stop": "002553",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 8,

"stop": "002467",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 14 of 22

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 9,

"stop": "002566",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 10,

"stop": "002537",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 11,

"stop": "002446",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 12,

"stop": "002449",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 13,

"stop": "001140",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 15 of 22

"seq": 14,

"stop": "001142",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 15,

"stop": "001054",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 16,

"stop": "001056",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 17,

"stop": "001175",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 18,

"stop": "001040",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 19,

"stop": "001066",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 16 of 22

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 20,

"stop": "001067",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 21,

"stop": "001068",

"data_ti mestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 22,

"stop": "001069",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 23,

"stop": "001070",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 24,

"stop": "001082",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 25,

"stop": "001083",

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 17 of 22

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 26,

"stop": "001005",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 27,

"stop": "001164",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 28,

"stop": "001165",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 29,

"stop": "001166",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 30,

"stop": "001167",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 18 of 22

"dir": "I",

"seq": 31,

"stop": "001168",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

"co": "CTB",

"route": "1",

"dir": "I",

"seq": 32,

"stop": "001186",

"data_timestamp": " 2023 -07-01T11:40:00+08:00"

Note: Refer to the data dictionary on description and specifications on the returned fields.

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 19 of 22

## 7. ETA API

Description:  This API takes a Citybus  company ID, bus stop ID  and the company’s operating

bus route number ; then it returns the “estimated time of arrival” (ETA) information of the

respective route  at that stop .

(Remark: May return 1 or 2 ETA data and a t most 3 ETA data will be provided.)

Important N ote: All New World First Bus routes already  integrated into Citybus. Data of all

routes are available under the {company_id} "CTB".

HTTP Request:

Endpoint  eta/{company_id}/{stop_id}/{route}

HTTP Method  GET

Parameter  Parameter Type  Description  Required

company_id  Path  Company ID under Citybus .

Valid company IDs are:

● CTB  - Citybus Limited

stop_id  Path  ● 6-digit representation of a bus

stop  Y

route  Path  The route number of the respective

bus company specified above.  Y

Sample Request:

/v2/transport/ citybus /eta/CTB/001145/11

HTTP Response:

Response Format  JSON

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 20 of 22

Response Code  Response

200 Success, see sample response below

422 See Error Response below

429 Processing too many requests

500 Internal Server Error

Sample Response:

"type": "ETA",

"version": " 2.0",

"generated_timestamp": " 2023 -07-01T15:45:00+08:00",

"data": [

"co": "CTB",

"route": "11",

"dir": "O",

"seq": 1,

"stop": "001145",

"dest_tc": " 渣甸山 ",

"dest_sc": " 渣甸山 ",

"dest_en": "Jardine's Lookout",

"eta_seq": 1,

"eta": " 2023 -07-01T15:48:00+08:00",

"rmk_tc": "",

"rmk_sc": "",

"rmk_en": "",

"data_timestamp": " 2023 -07-01T15:44:33+08:00"

"co": "CTB",

"route": "11",

"dir": "O",

"seq": 1,

"stop": "001145",

"dest_tc": " 渣甸山 ",

"dest_sc": " 渣甸山 ",

"dest_en": "Jardine's Lookout",

"eta_seq": 2,

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 21 of 22

"eta": " 2023 -07-01T16:00:00+08:00",

"rmk_tc": "",

"rmk_sc": "",

"rmk_en": "",

"data_timestamp": " 2023 -07-01T15:44:33+08:00"

"co": "CTB",

"route": "11",

"dir": "O",

"seq": 1,

"stop": "001145",

"dest_tc ": "渣甸山 ",

"dest_sc": " 渣甸山 ",

"dest_en": "Jardine's Lookout",

"eta_seq": 3,

"eta": " 2023 -07-01T16:12:00+08:00",

"rmk_tc ": "",

"rmk_sc": "",

"rmk_en ": "",

"data_timestamp": " 2023 -07-01T15:44:33+08:00"

Real -time “Next Bus” arrival time and related data  of Citybus  - API Specifications  07.2023

Copyright ©  202 3  Citybus Limited.  All Rights Reserved  Page 22 of 22

### 8. Error Response

In case of API execution error , a corresponding HTTP response code will be returned along

with the same response  code and an error message in the JSON body .

HTTP Response:

Response Format  JSON

Sample Response:

"code": "422",

"message": "Invalid company code"

