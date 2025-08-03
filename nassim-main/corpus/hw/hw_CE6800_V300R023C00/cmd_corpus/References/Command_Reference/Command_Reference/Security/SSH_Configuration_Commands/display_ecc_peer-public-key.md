display ecc peer-public-key
===========================

display ecc peer-public-key

Function
--------



The **display ecc peer-public-key** command displays information about the ECC public key configured on the remote end.




Format
------

**display ecc peer-public-key**

**display ecc peer-public-key brief**

**display ecc peer-public-key name** *key-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **brief** | Displays the brief information about the ECC public key configured on the remote end. | - |
| **name** *key-name* | Displays the name of the ECC public key configured on the remote end. | The value is a string of 1 to 40 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To display information about the public key in the ECC key pair configured on the remote end connected to the local device functioning as an SSH client, run the display **ecc peer-public-key** command. The public key enables the server to authenticate users and permits the login requests of authorized users.

**Prerequisites**

Before running the display **ecc peer-public-key** command, run the **ecc peer-public-key** command to generate the peer public key.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the brief information about all the ECC public keys.
```
<HUAWEI> display ecc peer-public-key brief
------------------------------------------
       Bits      Name
------------------------------------------
       521       sat
------------------------------------------

```

# Display the detailed information about the ECC public key named sat.
```
<HUAWEI> display ecc peer-public-key name sat
=====================================
    Key name: sat
=====================================
Key code:
    04D3B6E7 A2AC3288 99803D43 6B2596C8 4C3B986C D8902C33 F88E3026 22DC6009
    792E2544 7B4D5178 DC8054BB F38780CB 43BF6478 0C06B3EE F31338FD 74D33A7A
    26501324 DDB101EC 936405B8 CC4926E9 F1F20896 5276DC28 D0532B6E E61F219B
    DB9E5EE1 E511BC58 AC5DDF80 0BCE2033 1B6548FF F9B5B629 D21F92FF 598C72CB
    E5F465

```

**Table 1** Description of the **display ecc peer-public-key** command output
| Item | Description |
| --- | --- |
| Bits | Length of the ECC public key configured on the remote end. |
| Name | Name of the ECC public key configured on the remote end. |
| Key name | Name of the ECC public key configured on the remote end. |
| Key Code | Code of the public key in the local ECC key pair. |