display ssh server-info
=======================

display ssh server-info

Function
--------

The **display ssh server-info** command displays the binding between the SSH server and the public key (RSA/DSA/ECC) that has connected or is connecting with current SSH client.



Format
------

**display ssh server-info**



Parameters
----------

None


Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After the binding between an SSH server and a public key (RSA/DSA/ECC) on an SSH client is configured, you can run the display ssh server-info command to view the binding information on the SSH client.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Get server and public key information.
```
<HUAWEI> display ssh server-info
----------------------------------------------------------------------------------------------------------------
Server Name(IP)                               Server public key name          Server public key type   State     
----------------------------------------------------------------------------------------------------------------
2001:db8:2::2                                 2001:db8:2::2                   RSA                      CONFIGURE 
10.164.39.223                                 10.164.39.223                   RSA                      CONFIGURE 
192.168.1.1                                   192.168.1.1                     RSA                      CONFIGURE 
----------------------------------------------------------------------------------------------------------------

```


**Table 1** Description of the
**display ssh server-info** command output

| Item | Description |
| --- | --- |
| Server Name(IP) | Indicates the host name of the SSH server. |
| Server public key name | Indicates the public key name of the server. |
| Server public key type | Indicates the public key type of the server. |
| State | Indicates the server key state:   * CONFIGURE: Indicates that the server public key is saved in database. * DYNAMIC: Indicates that the server public key is not saved in database. |