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

### attack types
#### inband attacks
Inband attacks use the **same communication channel** for injecting SQL code and retrieving results (presented in a web page).

Examples:
- **tautology** ⟶ injects conditional statements so that they always evaluate to `true`
- **end-of-line comment** ⟶ after injecting code, legitimate code that follows is nullified by end of line comments (`--`)
- **piggybacked queries** ⟶ the attacker adds additional queries beyond the intended one, piggy-backing the attack on top of a legitimate request

#### inferential attack
There is no transfer of data, but the attacker is able to reconstruct the information by sending particular requests and observing the resulting behaviour of the website/DB.

Examples:
- **illegal/logically incorrect queries**: (preliminary, information-gathering step for other attacks) the attacker uses incorrect queries to gathers important information about the type and structure of the backend DB
- **blind SQL injections**: data is inferred bit-by-bit by observing subtle changes in the page content or response time
- **out-of-band attacks**: data is retrieved using a different channel (the outbound connectivity from the database is lax) the malicious command forces the database engine to execute a function that attemps to contact a remote server

### SQLi sinks
SQLi **sinks** are the points in a program where user-controlled data is incorporated into database queries, creating a vulnerability (sinks write results to the DB)
- the security goal is to ensure the source (the user input) *never flows unchecked* to the sink (the database execution function)

Some examples of sinks include User Input (`GET`/`POST` parameters), HTTP Headers, Cookies or the database itself in case of a second order injection.


| target                                           | description                                                                                                                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| identify **injectable params** (sources / sinks) | the attacker finds the vulnerable sources that feed into an unsafe sink, by testing inputs with simple characters like `'`                                           |
| database **footprinting**                        | find out which DBMS is in use. (SQL syntax differs betweeen systems) (can be made easy by poorly configured applications that display verbose error messages)        |
| discover **DB schema**                           | find names of important tables and the columns within them                                                                                                           |
| **data extraction**                              | stealing the information. the attacker uses techniques like `UNION` to combine malicious queries with the original one                                               |
| **data manipulation**                            | the attacker modifies the database’s integrity by changing existing records, deleting data, inserting new malicious data                                             |
| **denial of service**                            | preventing legitimate user from using the web application by flooding the database with useless queries or deleting stuff or lock tables                             |
| **authentication bypass**                        | the attacker tricks the application into authenticating them without a valid password                                                                                |
| **remote command execution**                     | (highest impact target) some DMBS allow the execution of OS commands via SQL; if the attacker reaches this target, they can run commands directly on the server’s OS |

>[!example] example: tautology
> ```SQL
> $q = "SELECT id FROM users WHERE user = '" .$user. "' AND pass = '" .$pass. "' ";
> 
> -- sent parameters:
> $user = "admin"
> $pass = "' OR '1'='1'"
> 
> -- executed query:
> $sq = " SELECT id FROM users WHERE user='admin' AND pass='' OR '1'='1' ";
> ```

## SQLi queries

### UNION query
the `UNION` construct can be used to achieve **data extraction**:

>[!example] example
>```SQL
>$q = "SELECT id, name, price, description FROM products WHERE category='" .$cat. "' ";
>
>$cat = "' 1 UNION SELECT 1, user, 1, pass FROM users --";
>
>-- query (MySQL performs a cast)
>$q = "SELECT id, name, price, description FROM products WHERE category=1 UNION SELECT 1, 1, user, pass FROM users"
>
>-- 1s are placeholders for fields we don't know/care about, so we ensure compatibility with the original query's columns
>```

>[!warning] the **number and type of the columns returned** by the two `SELECT` queries must **match**
>- in MySQL, if the types do not match, a cast is performed automatically
#### SQLi tautologies