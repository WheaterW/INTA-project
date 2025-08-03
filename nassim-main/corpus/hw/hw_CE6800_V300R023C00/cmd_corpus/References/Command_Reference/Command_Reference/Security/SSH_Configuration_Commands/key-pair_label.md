key-pair label
==============

key-pair label

Function
--------



The **key-pair label** command creates the key-pairs with specified label name.

The **undo key-pair label** command deletes the key-pairs with specified label name.



By default, a device does not have local key pairs or server key pairs.


Format
------

**dsa key-pair label** *label-name* [ **modulus** *modulus-bits* ]

**ecc key-pair label** *label-name* [ **modulus** *modulus-bits* ]

**sm2 key-pair label** *label-name*

**undo** { **dsa** | **ecc** } **key-pair** **label** *label-name*

**undo sm2 key-pair label** *label-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *label-name* | Specifies the label name of the key pair. | The value is a string of 1 to 35 case-insensitive characters, spaces not supported. The string can contain only letters, digits, and underscores (\_). |
| **modulus** *modulus-bits* | Specifies the key-pair modulus bit value. | The value is an integer that can be 256, 384, or 521, in bits. The default value is 521 bits.  The greater the modulus of a key pair, the higher the security. However, it takes longer time to generate and use key pairs of a greater modulus. |
| **ecc** | Specifies to generate the ECC key-pairs. | - |
| **sm2** | Specifies to generate the SM2 key-pairs. | - |
| **dsa** | Specifies to generate the DSA key-pairs. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

DSA/ECC/SM2 keys are common key algorithms used for user authentication in SSH to ensure user authentication security.After this command is executed, a new key pair is created and stored with the specified label name. The **undo key-pair label** command deletes a specified key pair from the database.

**Configuration Impact**

On execution of the **dsa key-pair label** command, a new DSA key-pair is generated and stored with the given label name. On execution of the **undo dsa key-pair label** command, the DSA key-pair with the given label name is deleted from the database.On execution of the **ecc key-pair label** command, a new ECC key-pair is generated and stored with the given label name. On execution of the **undo ecc key-pair label** command, the ECC key-pair with the given label name is deleted from the database.On execution of the **sm2 key-pair label** command, a new SM2 key-pair is generated and stored with the given label name. On execution of the **undo sm2 key-pair label** command, the SM2 key-pair with the given label name is deleted from the database.


Example
-------

# Generate an ECC key-pair with the label name ecc\_key\_pair and modulus 521.
```
<HUAWEI> system-view
[~HUAWEI] ecc key-pair label ecc_key_pair modulus 521

```

# Create an SM2 key pair named sm2key001.
```
<HUAWEI> system-view
[~HUAWEI] sm2 key-pair label sm2key001

```