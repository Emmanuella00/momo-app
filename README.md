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

# Team Members
1. Anglebert Shumbusho Ishimwe
2. Faith Irakoze
3. Emmanuella Ikirezi

# Links
1. Link to Trello: https://trello.com/b/xtrQvdRf/momo-sms-project-board
2. Link to the System Architectural Design: https://drive.google.com/file/d/1Vys0YKsciS894s9Dt-00K0OC75B0JQej/view?usp=sharing
