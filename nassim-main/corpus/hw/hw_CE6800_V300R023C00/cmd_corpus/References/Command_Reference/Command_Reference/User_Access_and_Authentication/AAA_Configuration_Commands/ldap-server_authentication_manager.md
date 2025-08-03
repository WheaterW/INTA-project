ldap-server authentication manager
==================================

ldap-server authentication manager

Function
--------

The **ldap-server authentication manager** command configures the administrator DN and password of an LDAP authentication server.

The **undo ldap-server authentication manager** command deletes the administrator DN and password of an LDAP authentication server.

By default, no administrator DN and password of an LDAP authentication server are configured.



Format
------

**ldap-server authentication manager** *manager* *password*

**undo ldap-server authentication manager**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *manager* | Specifies the administrator DN of an LDAP authentication server. | The value is a string of 1 to 63 or 3 to 65 case-sensitive characters. |
| *password* | Specifies the administrator password of an LDAP authentication server. | The value is a string of 1 to 31 characters in plain text or a string of 148 characters in cipher text. The plain text cannot contain & or ". The system saves this string to the configuration file in cipher text. If the string consists of 1 to 16 characters, the length of the converted ciphertext is 128 bytes. If the string consists of 17 to 31 characters, the length of the converted ciphertext is 148 bytes. |




Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

To configure the administrator DN and password of an LDAP authentication server, run the **ldap-server authentication manager** command. If the **ldap-server authentication manager-anonymous enable** command has been executed to allow anonymous access to the LDAP server, this configuration will be deleted after the **ldap-server authentication manager** command is run.



Example
-------

# Set the DN of the LDAP administrator to cn=manager and password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server authentication manager cn=manager YsHsjx_202206

```