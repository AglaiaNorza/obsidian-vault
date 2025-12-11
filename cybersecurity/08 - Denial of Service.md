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

- **Incoming Processing:** The attacker sends a high volume of UDP packets, often with **spoofed source IP addresses**, directed toward a wide range of **random ports** on the target server. The attacker uses a spoofed address to hide their true location and to prevent the server's response packets from reaching them.
    
- **Resource Exhaustion (Responding):** For every incoming UDP packet, the target server is forced to perform a check:
    
    - It checks to see if any application is actively **listening** for requests at the specified destination port.
        
    - Since the packets are often sent to random, unused ports, the check fails.
        
    - The server then generates and sends an **ICMP Destination Unreachable** packet back to the sender (the spoofed source IP address) to inform it that the port is not available.