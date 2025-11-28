Database security has not kept pace with the increased reliance on databases.
The main reasons are:
* **imbalance of complexity** ⟶ here is a dramatic imbalance between the complexity of modern database management systems (DBMS) and the security technique used to protect these critical systems.
* **complex interaction protocol** ⟶ Structured Query Language (SQL), the interaction protocol that databases use, is complex
* **heterogeneous environments** ⟶ most enterprise environments consist of a heterogeneous mixture of database platforms, enterprise platforms, and OS platforms, creating an additional complexity hurdle for security personnel
* **cloud reliance** ⟶ increasing reliance on cloud technology to host part or all of the corporate database.
* **lack of dedicated personnel** ⟶ the typical organization lacks full-time database security personnel

Effective database security requires a strategy based on a *full understanding* of the security vulnerabilities of SQL.

## SQL injection attacks (SQLi)
SQL injection attacks represent one of the most prevalent network-based security threats. They are designed to exploit the nature of web application pages by sending **malicious SQL commands** to the database server.
- the most common attack goal is bulk *extraction of data*
- depending on the environment, it can also be exploited to *modify* or *delete* data, *execute arbitrary OS commands*, or launch *DoS attacks*

>[!summary] typical SQL injection attack
>
>![[SQL-injection.png|center|450]]

>[!bug] injection technique
> SQLi attacks typically work by **prematurely terminating** a text string and **appending a new command**.
> - since the inserted command may have additional strings appended to it before its execution, attackers terminate the injected string with a comment mark `--`, so the subsequent text is ignored at execution time

### SQL attack avenues
The main avenues for SQL attacks are:
- **user input**
- **server variables** ⟶ attackers can forge HTTP and network header values, placing data directly into them
- **second-order injection** ⟶ a malicious user could rely on data already present in the system to trigger an SQL injection attack (the input that modifies the query to cause an attack doesn't come from the user but from within the system itself)
- **cookies** ⟶ an attacker could alter cookies so that when the application server builds an SQL query based on their content, its structure and function are modified
- **physical user input** ⟶ for example through I/O mechanisms (USB sticks etc)

### inband attacks