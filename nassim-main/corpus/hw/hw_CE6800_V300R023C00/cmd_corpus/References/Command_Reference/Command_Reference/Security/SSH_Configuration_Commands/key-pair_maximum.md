key-pair maximum
================

key-pair maximum

Function
--------



The **key-pair maximum** command configures the maximum number of allowed key-pairs.

The **undo key-pair maximum** command resets the value of the key-pair to its default value.



By default, you can configure 20 key-pairs.


Format
------

**rsa key-pair maximum** *max-keys*

**dsa key-pair maximum** *max-keys*

**ecc key-pair maximum** *max-keys*

**undo rsa key-pair maximum**

**undo dsa key-pair maximum**

**undo ecc key-pair maximum**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-keys* | Specifies the maximum number for key-pairs. | The value is an integer ranging from 1 to 20. |
| **dsa** | Specifies to generate the DSA key-pairs. | - |
| **ecc** | Specifies to generate the ECC key-pairs. | - |
| **rsa** | Specifies to generate the RSA key-pairs. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Storing key-pairs consumes system memory and file resources. You can run the key-pair maximum command to set the maximum number of allowed key-pairs to prevent excess key pairs from exhausting system resources.


Example
-------

# Set the maximum number of allowed ECC key-pairs to 15.
```
<HUAWEI> system-view
[~HUAWEI] ecc key-pair maximum 15

```

# Set the rsa key-pair maximum value as 15.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair maximum 15

```