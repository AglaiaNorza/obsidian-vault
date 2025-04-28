---
created: 2025-04-28T08:23
updated: 2025-04-28T09:07
---
$P=\{ \text{persona/1, telefono/1, dipendente/1, lavora/2, diversitraloro/3, dipartimento/1} \}$
$F=\{ \text{proprietario/1, nome/1, afferisce/1, direttore/1} \}$

(in cui diversitraloro(x, y, z) equivale a $x\neq y\land y\neq z\land x\neq z$)

1) **tutte le persone hanno almeno un numero di telefono:**
$$\forall  x\,(\text{persona(x)}\implies \exists y\;(\text{telefono(y)} \land\text{ proprietario(y)}=x))$$

2) **ogni persona ha esattamente un nome:**

$$\forall x (\text{persona(x)}\implies \exists y \;(y=\text{nome(x)}))$$

3) **non ci sono dipendenti che lavorano in più di due dipartimenti.**
 
$$\forall x(\text{dipendente(x)}\implies(\neg(\exists y,\,z,\,t\,(\text{diversitraloro(y, z, t)}\land\text{lavora(x, y)}\land \text{lavora(x, z)} \land \text{lavora(x, t)})))$$
 
4) **ogni dipartimento ha esattamente un direttore**

$$\forall x(\text{dipartimento(x)}\implies \exists y\,(\text{y=direttore(x)}\land \text{persona(y)}))$$

