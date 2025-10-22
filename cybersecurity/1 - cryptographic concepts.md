## symmetric encryption
Symmetric encryption (or **single-key encryption**/conventional encryption) is the universal technique for providing **confidentiality** for transmitted or stored data.

Two requirements need to be met for secure use:
1) a strong **encryption algorithm**
2) sender and receiver must have obtained copies of the secret key in a secure fashion, and must **keep the key secure**

>[!summary] simplified model
>
>![[sym-enc.png|center|550]]

### attacks
There are two kinds of attacks used on symmetric encryption:
- **cryptoanalytic attacks** ⟶ rely on the nature of the algorithm, knowledge of the general characteristics of the plaintext, or some plaintext-ciphertext pairs
	- they exploit the *characteristics* of an algorithm to attempt to deduce a plaintext or a key (if successful, all future and past messages encrypted with that key are compromised)
	- these types of attacks are mainly used to reduce the dictionary of a possible brute-force attacks, but they have become outdated due to the new standards of encryption
- **brute-force attacks** ⟶ all possible keys are tried until an intelligible translation into plaintext is obtained (on average, half of all possible keys must be tried)

### most known symmetric encryption algorithms
