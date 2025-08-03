display ssh user-information
============================

display ssh user-information

Function
--------

The **display ssh user-information** command displays the configuration of all the SSH users.



Format
------

**display ssh user-information** [ *user-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies the name of an SSH user. | The value is a string of 1 to 253 case-insensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

All views



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If a user uses SSH to log in to a device and RSA or DSA or ECC mode for authentication, you can run the display ssh user-information command to check whether the user information is correct, including the user name, password, RSA or DSA or ECC public key, and service type.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the configuration of the SSH user client001.
```
<HUAWEI> display ssh user-information client001
--------------------------------------------------------------------------------
User Name             : client001
Authentication type   : password-ecc
User public key name  : --
User public key type  : --
Sftp directory        : --
Service type          : stelnet | sftp | snetconf
--------------------------------------------------------------------------------

```

# Display the configurations of all the SSH users.
```
<HUAWEI> display ssh user-information
----------------------------------------------------
User Name               : client001
Authentication type     : password-ecc
User public key name    : --
User public key type    : --
Sftp directory          : --
Service type            : stelnet | sftp | snetconf

User Name               : client002
Authentication type     : rsa
User public key name    : --
User public key type    : --
Sftp directory          : --
Service type            : --
----------------------------------------------------
Total 2, 2 printed

```


**Table 1** Description of the
**display ssh user-information** command output

| Item | Description |
| --- | --- |
| User Name | Name of SSH users. |
| User public key name | Peer public key assigned to the SSH user. |
| User public key type | Public key type allocated to SSH users. |
| Authentication type | Authentication mode of the SSH user. |
| Sftp directory | SFTP service directory of an SSH user. |
| Service type | Service type for an SSH user.   * snetconf: indicates that the service type of an SSH user is SNETCONF. * stelnet: indicates that the service type of an SSH user is stelnet. * sftp: indicates that the service type of the SSH user is SFTP. * -: indicates that no service type is specified for the SSH user. |