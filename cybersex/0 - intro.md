>[!quote] definition of cybersecurity (by NIST)
>prevention of damage to, protection of, and restoration of computers, electronic communication systems, electronic communications services, wire communication, and electronic communication, including information contained therein, to ensure its **availability**, **integrity**, **authentication**, **confidentiality**, and **nonrepudiation**

>[!info] computer security
>Computer security is made up of the measures and controls that ensure **confidentiality**, **integrity** and **availability** of information system assets, including hardware, software, firmware and information that is being processed, stored and communicated.

## C.I.A.
The key concepts of security are united under the C.I.A. acronym, and they are:
### confidentiality

>[!info] confidentiality
> Preserving **authorised restrictions** on **information access** and disclosure, including means for protecting personal privacy and proprietary information
> (avoiding unauthorised disclosure of information).

Confidentiality includes two related concepts:
- **data confidentiality** ⟶ assures that private information is not made available to unauthorised individuals
- **privacy** ⟶ assures that individuals control what information related to them can be collected and stored and by whom
#### tools for confidentiality
- **encryption** ⟶ the transformation of information via a secret ("*encryption key*"), so that it can only be read using another secret ("*decryption key*")
- **access control** ⟶ rules and policies that limit access to a confidential piece of information to those systems on a "need to know" basis
- **authentication** ⟶ determination of someone's identity or role 
- **authorization** ⟶ determining whether a system is allowed access to resources, based on access control policy
- **physical security** ⟶ establishment of physical barriers to limit access to protected computational resources (es. locks, windowless rooms, copper meshes that stop electromagnetic signals from entering)

### integrity
>[!info] integrity
> Guarding against improper information modification or destruction (including ensuring information nonrepudiation and authenticity).

Integrity includes two related concepts:
- **data integrity** ⟶ assures that information and programs are changed only in a specific and authorized manner
- **system integrity** ⟶ assures that a system can perform its intented function free from unauthorised manipulation

#### tools for integrity
- **backups** ⟶ periodic archival of data
- **checksums** ⟶ computation of a function that maps contents of a file to a numerical value; a checksum depends on the entire content of a file and even a small change is highly likely to generate a different output value
- **data-correcting codes** ⟶ methods for storing data so that small changes can be easily detected and corrected (automatically)

### availability
>[!info] availability
> Ensuring timely and reliable access to / use of information.

#### tools for availability
- **physical protections** ⟶ infrastructure meant to keep information available even in the event of physical challenges
- **computational redundancies** ⟶ computers and storage devices that serve as fallbacks in case of failures

## other security concepts
There are other very important security concepts, such as:

### authenticity
>[!info] authenticity
>The ability to determine that statements, policies and permissions issued by people or systems are genuine

Primary tool: **digital signatures** ⟶ cryptographic computations that allow someone to commit to the authenticity of their documents in a way that achieves non-repudiation (authentic statements issued by some person or system cannot be denied).

### accountability
>[!info] accountability
>The requirement for an entity's actions to be traced uniquely to that entity.

- Accountability supports non-repudiation, deterrence, fault isolation, intrusion detection and prevention, after-action recovery and legal action.
- Systems must keep records of their activities to permit forensic analyses to trace security breaches / to aid in transaction disputes

### anonimity
>[!info] anonimity
> The property that certain records or transactions are not to be attributable to any individual.

Tools:
- **aggregation** ⟶ the combining of data from many individuals so that disclosed sums or averages canno be tied to a specific individual
- **mixing** ⟶ the intertwining of transactions, information, or communications in a way that cannot be traced to any individual
- **proxies** ⟶ trusted agents that are willing to engage in actions for an individual in a way that cannot be traced back to that person
- **pseudonyms** ⟶ fictional identities that can fill in for real identities in communications and transactions, but are otherwise known only to a trusted entity

## security and attacks

> [!summary]- computer security challenges
> 1. Computer security is not as simple as it might first appear to the novice
> 2. In developing a particular security mechanism or algorithm, one must always consider *potential attacks* on it
> 3. Procedures used to provide particular services are ofter *counterintuitive*
> 4. *Physical and logical placement* needs to be detected
> 5. Security mechanisms typically involve more than a particular algorithm or protocol and also require that participants be in possession of some *secret information* which raises questions about the creation, distribution and protection of that secret information
> 6. Attackers only need to find a single weakness, while the designer must find and *eliminate all weaknesses* to achieve protect security
> 7. Security is still too ofter an afterthought to be incorporated into a system after the design is complete, rather than being an *integral part* of the design process
> 8. Security requires regular and constant *monitoring*
> 9. There is a natural tendency on the part of the users and system managers to perceive little benefit from security until a security failure occurs
> 10. Many users and even security administrators view strong security as in impediment to efficient and user-friendly operation of an information system or use of information

> [!info] security concepts and relationships
> 
> ![[concepts-security.png|center|450]]
> 
> categories of vulnerabilities:
> - **corrupted** ⟶ loss of integrity
> - **leaky** ⟶ loss of confidentiality
> - **unavailable** or very slow ⟶ loss of availability
> 
> categories of attacks:
> - **passive** ⟶ attempt to learn or make use of information that does not affect system resources
> - **active** ⟶ attempt to alter system resources or affect their operation (involve some modification of data streams or creation of false streams) 
> 
> they can be inside attacks (by an "insider" who has access to system resources) or outside attacks (from outside the perimeter, by an unauthorised user)
> 
> **threat agents** ⟶ those who have the intent to conduct detrimental activities
> 

## threat consequences
- **unauthorised disclosure** is a threat to *confidentiality*
	- an entity gains access to data for which it's not authorised 
- **deception** is a threat to *system and/or data integrity*
	- an authorised entity receives false data and believes it to be true
- **disruption** is a threat to *availability or system integrity*
	- the correct operation of system services and functions is interrupted or prevented
- **usurpation** is a threat to *system integrity*
	- an unauthorised entity takes control of system services or functions

## threats and attacks
- **interception** ⟶ eavesdropping of information intended for someone else during its transmission over a communication channel
- **inference** (/correlation/traceback) ⟶ integration of multiple data sources and information flows to determine the source of a particular data stream or piece of information
- **masquerading** ⟶ fabrication of information appearing to be from someone who is not actually the author
- **falsification** ⟶ unauthorised modification of information
- **repudiation** ⟶ denial of a commitment or data receipt (attempt to back out of a contract or protocol that requires the different parties to provide receipts acknowledging that the data has been received)
- **incapacitation** ⟶ prevents or interrupts system operation by disabling a system component
- **corruption** ⟶ undesirably alters system operation by adversely modifying system functions or data
- **obstruction** ⟶ interrupts delivery of system services by hindering system operation
- **denial-of-service** (DOS) ⟶ obstruction or degradation of a data service or information access
- **misappropriation** ⟶ an entity assumes unauthorised logical or physical control of a system resource
- **misuse** ⟶ causes a system component to perform a function or service that is detrimental to system security

## attack surfaces
>[!info] attack surfaces
> Reachable and exploitable vulnerabilities in a system.

Divided into three categories:
- **network attack surface** ⟶ vulnerabilities over an enterprise netwoek, wide-area network or the Internet 
	- includes network protocol vulnerabilities (eg those used for a DOS attack), disruption of communication links and intruder attacks
- **software attack surface** ⟶ vulnerabilities in application, utility or operating system code 
- **human attack surface** ⟶ vulnerabilities created by personnel or outsiders (social engineering, human error)

## computer security strategy
- **security policy** ⟶ formal statement of rules and practices that specify or regulate how a system or organization provides security services to protect sensitive and critical system resources
- **security implementation** ⟶ made up of
	- prevention
	- detection
	- response
	- recovery
- **assurance** ⟶ attribute of an information system that provides grounds for having confidence that the system's security policy is enforced
- **evaluation** ⟶ examining a computer product with respect to certain criteria