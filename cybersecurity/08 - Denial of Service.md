>[!quote] DoS attack (NIST)
>“an action that prevents or impairs the authorized use of networks, systems, or applications by exhausting resources such as CPUs, memory, bandwidth, and disk space”

DoS attacks typically target:
- network bandwidth (by hindering the capability of network links to connect to a server)
- system resources (through overloading/crashing the network handling the software)
- application resources (typically sending too many valid requests, consuming the application's resources)

## flooding attacks
Flooding attacks try to overload the network capacity on some link to a server.
They are classified based on the network protocol used.
### flooding ping (ICMP flood)
Simple attack exploiting ICMP via the `ping` command. 

- the aim of this attack is to **overwhelm the capacity** of the network connection to the target organisation ⟶ the attacker **continuously sends** a massive flood of ICMP echo request packets (`ping`s) to the target server or network (each request requires the target to process it and send back an ICMP Echo Reply back)
- as the volume of attack traffic increases and reaches the capacity limits of the victim's network or server, the device can no longer process all of it
	- eventually, the network starts **discarding** packets (both the attack packets and legitimate user traffic) - thus, service is denied

In a basic DoS attack from a single source, the originating IP address is visible in the ICMP packets, making the attacker's location traceable. However, attackers often use **IP Spoofing**, which involves falsifying the source IP address in the outgoing packets.

>[!info] spoofing
> Source Address Spoofing is the act of **falsifying the source IP address** in a network packet.
> - requires network engineers to specifically query flow information from their routers ⟶ because the source addresses are fake, simple logging of incoming IP addresses is insufficient for identifying the real attacker, external tools must be used

### SYN spoofing (SYN flood attack)
SYN flood attacks exploit the **three-way handshake** used to establish a TCP connection.

In a SYN Flood attack, the attacker sends a massive volume of SYN packets to the target server, but either:
- never sends the final ACK
- sends the SYN packets with a spoofed source IP address.

That way, the server keeps the connection entry in its **half-open queue**, waiting for the final ACK to arrive before timing out. The queue quickly fills up with these half-open (unestablished) connections.

![[SYN-spoofing.png|center|450]]

### UDP flood attack
UDP Flood aims to **saturate** the target's network bandwidth and exhaust server resources by forcing it to **generate responses**.
- the lack of a connection mechanism in UDP makes it simple for attackers to generate and send a **massive volume of UDP packets** quickly with minimal effort

The attacker sends a high volume of UDP packets, often with spoofed source IP addresses, directed toward a *wide range of random ports* on the target server.
 For every incoming UDP packet, the target server is forced to **perform a check**: it checks to see if any application is actively listening for requests at the specified destination por. Since the packets are often sent to random, unused ports, the check fails. The server then generates and **sends an ICMP Destination Unreachable packet back** to the sender (the spoofed source IP address) to inform it that the port is not available. This way, the target is saturated and the system become unaccessible to legitimate users.

## Distributed Denial of Service (DDoS)
DDoS attacks use **multiple systems** to generate attacks.

Typically, the attacker uses a flaw in operating systems or common applications to gain access and install a **zombie program** on the system. The attacker does this multiple times, gaining access to a large collection of systems that form a **botnet**.

> In many cases, attackers can launch DDoS attacks for free using
publicly available tools, or for a small fee by hiring a DDoS-as-a-service
botnet such as Moobot in the dark web.

>[!info] DDoS architecture
>
>![[DDoS.png|center|450]]

## HTTP-Based attacks

### HTTP flood
Bombards web servers with HTTP requests (typical DoS attack), thanks to tools like LOIC and HOIC.
- HTTP floods consume considerable resources
- to make traffic look more realistic, **spidering** is often used ⟶ bots start from a given HTTP page and follow all links on the website recursively

### slowloris + RUDY
A slowloris attack attemps to monopolise server resources by sending HTTP `GET` **requests that never complete**, eventually consuming the server's connection capacity.

Existing intrusion detection and prevention solutions that rely on signatures to detect attacks will generally not recognize Slowloris.

R U Dead Yet? (**RUDY**) is another example of a "low and slow" attack. It uses HTTP `POST` requests - the attacker uses the `Content-Length` header in a `POST` request to declare a large request body which is then sent at a very slow rate.

### reflection attacks
A Reflection Attack involves the attacker using a **legitimate server** on the internet (the "*reflector*" or "intermediary") to launch the actual attack traffic against the target.

- The attacker initiates the process by sending a small request packet to a publicly accessible server (the intermediary).  
- Instead of using their own IP, they use the **victim's IP address as the source address**. This way the traffic is coming from the intermediary, hiding the attacker's IP.

### DNS amplification attack
The DNS Amplification attack exploits the DNS protocol's nature to **turn a small request into a massive response**, which is directed at the victim.

- Attacker creates a series of DNS requests containing the spoofed source address of the target system

- Thanks to the Amplification Factor, an attacker can send a tiny DNS query—for example, one that asks for all records (`ANY` query) for a large domain name. The request will be very small, but the DNS server's response containing the many resource records can be hundreds or even thousands of bytes long. This allows the attacker to multiply their traffic volume by a factor of 50x or more, making the resulting flood extremely difficult to defend against.

> **Memcached** (a high-performance caching mechanism for dynamic websites made to speed up the delivery of web contents) can make this extremely more powerful -  the attacker makes a request that stores a large amount of data and then sends a spoofed request to make such data to be delivered to the victim via UDP. 
> - memcached can bring an amplification fator of 50'000

## DoS attack defenses
DoS attacks cannot be prevented entirely, since high traffic volumes may be legitimate (eg. very popular sites).

There are four lines of defense against DDoS:
- attack **prevention** and preemption
- attack **detection** and **filtering**
- attack source traceback and **identification**: ISPs could be able to trace packet flow back to source (may be difficult and time consuming)
- attack **reaction**: implementing a contingency plan (switching to alternate backup servers, commissioning new servers at a new site with new addresses)

### attack prevention
it is possible to:
- **block spoofed source addresses** ⟶ implementing filters at the edge of the network nearest the sender (the attacker's ISP) is the most effective place to stop spoofed packets before they enter the wider Internet
	- Filters must be applied to traffic before it leaves the ISP’s network or at the point of entry to their network. This practice is known as **Ingress Filtering**.
- Using **Modified TCP Connection Handling Code** (SYN Cookies)
	- primary defense against SYN Spoofing/Flood attacks
	- Instead of allocating memory for the half-open connection immediately, the server *encodes the connection's state information* into the initial sequence number of the SYN-ACK packet it sends back to the client.
		- a real client will then send the final ACK with this sequence number, allowing the server to decode the cookie, verify the connection legitimacy, and only then allocate resources.
	- As a secondary mitigation, an option is to drop an entry for an incomplete connection from the TCP connections table when it overflows (less desirable)
- Network and Service Configuration
	- **block IP directed broadcast** 
	- **block suspicious services and combinations**
- Manage application attacks with a form of graphical puzzle (captcha) to distinguish legitimate human requests
-  Use **mirrored** and **replicated servers** (redundancy) to ensure reliability-
- Good general system security practices