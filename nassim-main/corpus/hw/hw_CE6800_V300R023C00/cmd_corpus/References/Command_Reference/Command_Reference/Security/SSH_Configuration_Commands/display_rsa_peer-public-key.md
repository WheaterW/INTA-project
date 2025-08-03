display rsa peer-public-key
===========================

display rsa peer-public-key

Function
--------

The **display rsa peer-public-key** command displays the specified RSA public key. If no public key is specified, all public keys are displayed.



Format
------

**display rsa peer-public-key**

**display rsa peer-public-key brief**

**display rsa peer-public-key name** *key-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **brief** | Displays the brief information about the RSA public key configured on the remote end. | - |
| **name** *key-name* | Displays the name of the RSA public key configured on the remote end. | The value is a string of 1 to 40 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To display information about the public key in the RSA key pair configured on the remote end connected to the local device functioning as an SSH client, run the display **rsa peer-public-key** command. The public key enables the server to authenticate users and permits the login requests of authorized users.

**Prerequisites**

Before running the display **rsa peer-public-key** command, run the **rsa peer-public-key** command to generate the peer public key.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the brief information about all the RSA public keys.
```
<HUAWEI> display rsa peer-public-key brief
------------------------------------------
       Bits      Name
------------------------------------------
       512       rsakey001
------------------------------------------

```

# Display the detailed RSA public key named rsakey001.
```
<HUAWEI> display rsa peer-public-key name rsakey001
=====================================
    Key name      : rsakey001
    Encoding type : DER
=====================================
Key code:
308188
  028180
    9F158EF2 6860CFC9 B3E807BB 9E235386 DF92A2B5 F5666998 38597031 BB1490C2
    6109EA0B 4F047173 0F714F18 BD525B6B 966C789F 3FDE967F E0D35361 A47A4730
    743D1038 AB23FA71 AFA66349 6E1C803F 60622F1E 33EA38FA 6DB47049 A98EF75D
    06C34B83 06F21656 3AE704A2 5D1245E3 1258E281 9025B681 6CC7FBAA 1F171DBB
  0203
    010001

```


**Table 1** Description of the
**display rsa peer-public-key** command output

| Item | Description |
| --- | --- |
| Bits | Byte length. |
| Name | Name of the public key. |
| Key name | Name of the public key. |
| Key code | Code of the public key. |
| Encoding type | Coding type of the public key. |