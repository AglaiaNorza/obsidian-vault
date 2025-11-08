The goal of access control is to **protect confidentiality and integrity** of information.
Controlling what a subject can do (by regulating the operations that can be executed by a subject on data and resources) can help in preventing damage to the system.
- typically, access control is provided as a part of operating systems and database management systems

>[!quote] RFC 4949
>(Access control is) a process by which use of system resources is regulated according to a *security policy* and is permitted only by *authorized entities* (users, programs, processes, or other systems) according to that policy.


>[!summary] concepts
> ![[access-control.png|center|500]]

## access control modes

### Discretionary Access Control (DAC)
Controls access based on the **identity of the requestor and its access rules**, stating what requestors are or are not allowed to do.
- an entity may be granted access rights that permit it to *enable another entity* to access some resource

The rules are often provided via **access matrix**, **access control list** (ACL) or **extended access control matrix**.

>[!info] access matrix
>
>![[access-matrix.png|center|500]]
>
>- an empty cell means that *no access rights* are granted

>[!info] Access Control Lists
>
>![[ACL.png|center|550]]
>
>- defines a list called "access control list" for each object, which enumerates the *subjects that have access* rights and, for each subject, *which rights*
>
> ACLs take a subject-centered approach to access control. 
> 
> It can also be seen this way, from the subjects' perspective:
> 
> ![[ACL-subject.png|center|450]]

>[!info] extended access control matrix
> 
> ![[extended-access-matrix.png|center|550]]
> 
> ![[extended-matrix-rule.png|center|500]]
> 
> - the extended control marix considers the ability of one subject to transfer rights, create another subject and have 'owner' access rights to it
> - it can also define a hierarchy of subjects
> - certain subjects have the authority to make specific changes to the access matrix
> 
> Access by a subject to an object is mediated by the **controller** for that object. The controller's decisions are based on the contents of the matrix. 

>[!summary]- traditional UNIX file access control
>
> ![[1 - shell, utenti, filesystem#permessi di accesso]]

Many modern UNIX systems support access control lists (Linux, FreeBSD, OpenBSD...).

When a process requests access to a file system object, the appropriate ACL is selected, and the matching entry is checked for the correct permissions.

### Mandatory Access Control (MAC)
Each subject and each object are assigned a **security class** (which often form a hierarchy and are called "security levels"). 
- a subject is said to have a **security clearance** of a given level
- an object is said to have a **security classification** of a given level
- unlike with DAC, users cannot share or change the access permissions of data they own (access is enforced by the system)
#### Multilevel Security (MLS)
The MLS model defined four **access modes**:
- **read** (read-only)
- **append** (write-only)
- **write** (both read and write)
- **execute** (neither read nor write, but execute-only)

Confidentiality is achieved if a subject at a high level cannot convey information to a subject at a lower level, unless it is thanks to an **authorised declassification**. (It is achieved through:)
- **no read up**: a subject can only read objects of $\leq$ security level
	- called the *simple security property* ('ss-property')
- **no write down**: a subject can only write into an object of $\geq$ security level
	- called the *star property* ('\*-property)

Models like this (i.e.*Bell-LaPadula* model) are limited because they cannot manage the "downgrade" of objects (they have a very rigid structure).

### Role-Based Access Control (RBAC)
Role-Based Access Control is based on the definition of **roles** and the specification of access rights for those roles, rather than for subjects directly.

>[!summary] goals
>- describing organizational access control policies
>- roles are based on job function 
>- flexibility and scalability are increased

![[RBAC-matrix.png|center|550]]

### Families of RBAC Models

![[RBAC-families.png|center|400]]

RBAC0 is the "base model", and each model implements new "features".

- **RBAC1** ⟶ **hierarchy** 
	- roles have a hierarchal structure - many operations are common to a large number of roles, so some roles subsume others, and there is **inheritance** among roles.
	- the hierarchy is based on a **partial order** (like $\leq$, so a relation that is reflective, transitive and antisymmetric) that goes from top to bottom
- **RBAC2** ⟶ **constraints**
	- constraints relating to the roles are added
	- some types include:
		- *mutually exclusive roles* 
		- *cardinality* (maximum number of roles that can be given to a user)
		- *prerequisite roles* (a user can only be assigned a role if it is already assigned to another specified role)
- **RBAC3** ⟶ **hierarchy + constraints**

### Attribute-Based Access Control (ABAC)
Authorizations can express conditions on properties of **both the resource and the subject**.
- very flexible
	- systems are capable of enforcing DAC, RBAC and MAC concepts
	- an unlimited number of attributes can be combined to satisfy any rule
- the main obstacle is it could be demanding (performance-wise) to evaluate predicates on both resources and users for each access

ABAC relies on **policies** (sets of rules and relations that govern allowable behaviour within an organisation, based on the privilege of subjects and how resources or objects are to be protected under which environment conditions) and **privileges** (authorised behaviours of a subject, defined by an authority and embodied in a policy).

The ABAC attributes can be divided into:
- **subject attributes** ⟶ define the identity and characteristics of a subject (active entity that can change the system state)
- **object attributes** ⟶ can be used to make access control decisions (objects are passive entities containing or receiving information)
- **environmnet attributes** ⟶ describe the operational/technical/situational environment or context in which the information access occurs

>[!example] ABAC policy model

#### ABA policies model
- $S$, $O$ and $E$  ⟶  subjects, objects and environments
- $SA_{k}(1\dots k\dots Kthe pre-defined attributes for subjects (they contain information about the subject)
- $OA_{m}(1\dots m\dots M)$ are the pre-defined attributes for objects (they contain information about the object)
- $EA_{n}(1\dots n\dots N)$ are the pre-defined attributes for environments (they contain information about the context under which the access attempt is made)
- the *access rule* states the decision of whether a subject $\text{can\_access}$ an object in a given environment. it is determined by a function $f$ that evaluates the collection of attributes for subject, object and environment
	- e.g.: a subject with `role` = `admin` can access a `filesecuritylevel`= `confidential` *only if* `currenttime`is in between `9am` and `5pm`
	- this is more flexible than RBAC, as it can incorporate many dynamic factors (e.g. time, location, or resource data) into access decision
$$
\text{can\_access(s,o,e)$\leftarrow$f(ATTR(s),ATTR(o), ATTR(e))}
$$



>[!bug] ABAC vs RBAC
>- In RBAC, as the number of attributes grows, the number of roles and permissions grows exponentially
>- ABAC deals with additional attributes more efficiently










