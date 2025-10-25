## symmetric encryption
Symmetric encryption (or **single-key encryption** / conventional encryption) is the universal technique for providing **confidentiality** for transmitted or stored data.

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
### block vs stream cyphers

| **block cyphers**                                 | **stream cyphers**                                                         |
| ------------------------------------------------- | -------------------------------------------------------------------------- |
| process the input one block of elements at a time | process input elements continuously (encrypt plaintext one byte at a time) |
| produce an output block for each input block      | produce output one element at a time                                       |
| can reuse keys                                    | faster to use (+ less code)                                                |
| more common                                       | pseudorandom streams are unpredictable without knowledge of the input key  |

![[block-stream-ciphers.png|center|500]]

### most known symmetric encryption algorithms
- **AES** (Advanced Encryption Standard / **Rijndael**)
	- 128-bit block cypher + 128 / 192 / 256-bit secret keys
	- most popular and widely used
- **DES** (Data Encryption Standard) (or *DEA*, Data Encryption Algorithm)
	- 64 plaintext block + 56 bit key = 64 bit cypher block
	- now considered insecure due to the shortness of the key
	- **3DES** ⟶ repeats DES threee times using either two or three unique keys
		- (168-bit key
- **RC4** (ARC4)
	- stream cipher with 40-2048-bit secret keys
	- considered insecure

### message  authentication
Message authentication is used for protection against active attacks. Received messages are verified to be authentic: contents have not been altered, 