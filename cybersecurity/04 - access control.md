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

