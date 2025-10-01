# momo-app
momo-app is a collaborative project developed by the codecrafters team.
Our goal is to build an innovative mobile money application that streamlines payments, transfers, and financial tracking for users.

# What This Project Does
- How many transactions happened
- How much money moved
- What types of transactions happened
- Charts showing transaction trends

# Database Documentation
1. ERD Design

The ERD highlights clear relationships between senders, receivers, SMS messages, and transactions.
- Sender: Represents the individual sending money.
- Receiver: Represents the individual receiving money.
- SMS: Stores messages, dates, and statuses of transactions.
- Transaction: Handles financial details.
- System Logs: Handles system activity and errors.

2. Design Rationale

The design considerations ensure data integrity and cover MoMo’s key use cases.

- “Foreign key” property enforces the validity of relationships (e.g., a transaction must belong to an SMS).
- Check constraints ensure data accuracy (e.g., the amount is positive, the balance is not negative).
- The separation of sender, receiver, and SMS makes the system scalable because one SMS can trigger several transactions.
- The log table ensures system auditability, which is critical for financial systems.

# Setup Instructions

## 1. Clone the Repository

```sh
git clone https://github.com/Emmanuella00/momo-app.git
cd momo-app
```

## 2. Install Python Dependencies

If you use a virtual environment (recommended):

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# Or
source venv/bin/activate  # On Mac/Linux
```

Then install requirements (add packages to `requirements.txt` as needed):

```sh
pip install -r requirements.txt
```

## 3. Prepare Data

- Place your SMS XML file in `api/modified_sms_v2.xml`.
- Run the parser to generate transaction records:

```sh
python api/app.py
```

This will create `api/sms_records.json`.

## 4. Run the REST API Server

```sh
python api/schemas.py
```

The server will start at `http://localhost:8000`.

## 5. API Usage

See `docs/api_docs.md` for full API documentation, including authentication, endpoints, request/response examples, and error codes.

## 6. ETL Pipeline

To run the ETL pipeline (if implemented):

```sh
python etl/run.py
```

Or use the provided shell scripts in `scripts/` (edit as needed):

```sh
sh scripts/run_etl.sh
```
# Team Members
1. Anglebert Shumbusho Ishimwe
2. Faith Irakoze
3. Emmanuella Ikirezi

# Links
1. Link to Trello: https://trello.com/b/xtrQvdRf/momo-sms-project-board
2. Link to the System Architectural Design: https://drive.google.com/file/d/1Vys0YKsciS894s9Dt-00K0OC75B0JQej/view?usp=sharing

### AI Assistance
- AI was used to check SQL queries for correct syntax.
- AI was used to gather references on indexing,     constraints, and optimization.
- AI was used to review and polish our project documentation for clarity and readability.
