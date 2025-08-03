display sm2 peer-public-key
===========================

display sm2 peer-public-key

Function
--------

The **display sm2 peer-public-key** command displays information about remote SM2 public keys.



Format
------

**display sm2 peer-public-key**

**display sm2 peer-public-key brief**

**display sm2 peer-public-key name** *key-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **brief** | Displays brief information about all remote SM2 public keys. | - |
| **name** *key-name* | Displays information about the remote SM2 public key with a specified name. | The value is a string of 1 to 40 case-insensitive characters, spaces not supported. The string can contain only letters, digits, and underscores (\_). |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To display information about the public key in the SM2 key pair configured on the remote end connected to the local device functioning as a client, run the display sm2 peer-public-key command. The public key enables the server to authenticate users and permits the login requests of authorized users.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display brief information about all remote SM2 public keys.
```
<HUAWEI> display sm2 peer-public-key brief
------------------------------------------
Bits   Name                           
------------------------------------------
256    abc                      
------------------------------------------

```

# Display detailed information about the remote SM2 public key named sm2key001.
```
<HUAWEI> display sm2 peer-public-key name sm2key001
=====================================
Key name: sm2key001
=====================================
Key Code: 
    0474F110 F90F131B B6F6D929 9A23A41E F1AB1666 AC4BE4EE EF2CD876
    2B633F80 DD5CF42F 147A722F DE527F39 247F3744 C23296BE FE3BE502
    EEF7D9EC BC28A576 7E

```


**Table 1** Description of the
**display sm2 peer-public-key** command output

| Item | Description |
| --- | --- |
| Bits | Modulus of the remote SM2 public key. |
| Name | Name of the remote SM2 public key. |
| Key name | Name of the remote SM2 public key. |
| Key Code | Code of the remote SM2 public key. |