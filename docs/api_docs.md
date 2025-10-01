# Momo Transactions REST API Documentation

## Authentication

All endpoints require HTTP Basic Authentication.

- **Username:** `admin`
- **Password:** `secret123`

---

## Endpoints

### 1. List All Transactions

- **Endpoint:** `/transactions`
- **Method:** `GET`

#### Request Example

```http
GET /transactions HTTP/1.1
Authorization: Basic YWRtaW46c2VjcmV0MTIz
```

#### Response Example

```json
[
	{
		"id": 1,
		"transaction_type": "CREDIT",
		"amount": 5000,
		"sender": "Aime",
		"receiver": "Faith",
		"timestamp": "2023-09-30T10:00:00",
		"readable_timestamp": "30 Sep 2023 10:00:00 AM",
		"body": "..."
	},
	...
]
```

#### Error Codes

- `401 Unauthorized` – Missing or invalid credentials

---

### 2. Get Transaction by ID

- **Endpoint:** `/transactions/{id}`
- **Method:** `GET`

#### Request Example

```http
GET /transactions/1 HTTP/1.1
Authorization: Basic YWRtaW46c2VjcmV0MTIz
```

#### Response Example

```json
{
	"id": 1,
	"transaction_type": "CREDIT",
	"amount": 5000,
		"sender": "Aime",
		"receiver": "Faith",
	"timestamp": "2023-09-30T10:00:00",
	"readable_timestamp": "30 Sep 2023 10:00:00 AM",
	"body": "..."
}
```

#### Error Codes

- `401 Unauthorized`
- `404 Not Found` – Transaction does not exist
- `400 Bad Request` – Invalid ID

---

### 3. Create Transaction

- **Endpoint:** `/transactions`
- **Method:** `POST`

#### Request Example

```http
POST /transactions HTTP/1.1
Authorization: Basic YWRtaW46c2VjcmV0MTIz
Content-Type: application/json

{
	"transaction_type": "DEBIT",
	"amount": 2500,
		"sender": "Faith",
		"receiver": "Aime",
	"timestamp": "2023-09-30T11:00:00",
	"readable_timestamp": "30 Sep 2023 11:00:00 AM",
	"body": "..."
}
```

#### Response Example

```json
{
	"id": 2,
	"transaction_type": "DEBIT",
	"amount": 2500,
	"sender": "Jane Doe",
	"receiver": "John Doe",
	"timestamp": "2023-09-30T11:00:00",
	"readable_timestamp": "30 Sep 2023 11:00:00 AM",
	"body": "..."
}
```

#### Error Codes

- `401 Unauthorized`
- `404 Not Found` – Invalid endpoint

---

### 4. Update Transaction

- **Endpoint:** `/transactions/{id}`
- **Method:** `PUT`

#### Request Example

```http
PUT /transactions/1 HTTP/1.1
Authorization: Basic YWRtaW46c2VjcmV0MTIz
Content-Type: application/json

{
	"amount": 6000
}
```

#### Response Example

```json
{
	"id": 1,
	"transaction_type": "CREDIT",
	"amount": 6000,
		"sender": "Aime",
		"receiver": "Faith",
	"timestamp": "2023-09-30T10:00:00",
	"readable_timestamp": "30 Sep 2023 10:00:00 AM",
	"body": "..."
}
```

#### Error Codes

- `401 Unauthorized`
- `404 Not Found` – Transaction not found
- `400 Bad Request` – Invalid ID

---

### 5. Delete Transaction

- **Endpoint:** `/transactions/{id}`
- **Method:** `DELETE`

#### Request Example

```http
DELETE /transactions/1 HTTP/1.1
Authorization: Basic YWRtaW46c2VjcmV0MTIz
```

#### Response Example

Status: `204 No Content`

#### Error Codes

- `401 Unauthorized`
- `404 Not Found` – Transaction not found
- `400 Bad Request` – Invalid ID

---
## DSA: Search Efficiency Comparison

We compared two strategies to find a transaction by `id` using the dataset parsed from `api/modified_sms_v2.xml`:

- Linear Search: scans the list sequentially (O(n)).
- Dictionary Lookup: builds an index `id -> transaction` once, then O(1) average lookup.

How to run the benchmark:

```bash
python -m dsa.search_performance 
```
or 

```bash
python3 -m dsa.search_performance
```
Expected results: dictionary lookup is consistently faster than linear search as the list grows, because hash table access is average-case O(1), while linear search is O(n).

Potential alternatives:
- Balanced trees (e.g., B-tree, AVL, Red-Black) for ordered lookups and range queries (O(log n)).
- Skip lists with probabilistic balancing (O(log n)).
- Tries for prefix-based keys.

