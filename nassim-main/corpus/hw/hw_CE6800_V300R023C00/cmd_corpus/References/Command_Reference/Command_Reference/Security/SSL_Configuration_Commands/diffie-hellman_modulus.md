diffie-hellman modulus
======================

diffie-hellman modulus

Function
--------



The **diffie-hellman modulus** command sets the modulus of the Diffie-Hellman key exchange algorithm.



By default, the modulus of the Diffie-Hellman key exchange algorithm is 3072.


Format
------

**diffie-hellman modulus** *modulus-val*

**undo diffie-hellman modulus**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *modulus-val* | Specifies the modulus of the Diffie-Hellman key exchange algorithm. | The value can be 2048, 3072 or 4096. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command can set the modulus of the Diffie-Hellman key exchange algorithm.

**Precautions**



If the minimum value of the Diffie-hellman modulus is 2048 bits, security risks exist. You need to run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package (WEAKEA) before using the Diffie-hellman modulus. You are advised to set the minimum length to 3072 bits.




Example
-------

# Set the modulus of the Diffie-Hellman key exchange algorithm.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy a
[~HUAWEI-ssl-policy-a] diffie-hellman modulus 4096

```