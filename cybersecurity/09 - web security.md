## intro

>[!summary] basic web infrastructure
>
>![[web-infrastructure.png|center|500]]
> Standard Client-Server model. The web browser initiates a `page request`. The web server receives it and processes it via one of two paths:
> 1. static Content (left) ⟶ the server spawns a worker to simply fetch an HTML file from storage.
> 2. dynamic content (right) ⟶ the server spawns an interpreter to execute a script. This script often queries a DB to retrieve data and generate the page content before sending the `server response` back


>[!info] URL structure
>
>![[URL-structure.png|center|500]]
>
>  the characters `:/?#[]@!$&'()*+,;=` are "not allowed" (reserved) since hey have a standardised meaning; to use them for other purposes, they have to be percent-encoded (`%` + two hexadecimal digits)

## HTTP
to see the basics of how HTTP works, see [[4 - HTTP#HTTP|HTTP]] .

### dynamic contents to HTTP requests
servers and clients use **scripting** languages to create **dynamic content** for web users
- **client-side scripting**: downloaded from the server and executed *on the client’s computer*, completely visible and readable to the user
	- can access the resources the browser is given permission to see (eg cookies or local storage)
	- e.g. javascript, VBscript, ActiveX, Ajax
- **server-side scripting**: executed entirely *on the web server*, before the final result is sent back to the client’s browser 
	- PHP, ASP.NET, Java, Perl, Ruby, Go, Python, server-side javascript like node.js

### HTTP authentication
HTTP authentication is rarely used nowadays; the process is:
1. the browser starts a request without sending any client-side credentials
2. the server replies with a status message: `401 Unauthorized`, with a specific `WWW-Authenticate` header containing information on the authentication method; the browser then prompts the user for credentials
3. the browser gets the client’s credentials, includes them in the `Authorization` header and sends it back to the server (either base64-encoded or hashed with the username, password, (other things), and a nonce (random, one-time value))

### monitoring and manipulating HTTP
HTTP payload is cleartext encapsulated in TCP packets (with default port `80`), so it's easy to monitor and manipulate
- it can be monitored through sniffing tools (eg wireshark)
- it can be manipulated through traditional browsers and extensions, via proxy, curl and more

### HTTP sessions
HTTP is stateless, so every request is independent from the previous ones; but dynamic web applications require the ability to maintain some kind of session
- HTTP sessions are implemented by web application themselves, and session information is transmitted between the client and the server via:
	- HTTP payloads `<INPUT TYPE="hidden NAME="sessionid VALUE="7456">`
	- URLs `http://www.example/com/page.php?sessionid=7456`
	- HTTP headers (eg cookies) 
```http
GET /page.php HTTP/1.1
Host: www.example.com
...
Cookie: sessionid=7456
```

(for more info, see [[4 - HTTP#cookie|cookies]])

#### session hijacking

![[session-hijacking.png|center|450]]