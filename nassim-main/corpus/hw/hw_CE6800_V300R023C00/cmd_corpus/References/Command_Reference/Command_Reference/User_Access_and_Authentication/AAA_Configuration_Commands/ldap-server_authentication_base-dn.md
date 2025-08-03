ldap-server authentication base-dn
==================================

ldap-server authentication base-dn

Function
--------

The **ldap-server authentication base-dn** command configures the Base DN of an LDAP authentication server.

The **undo ldap-server authentication base-dn** command restores the default Base DN of an LDAP authentication server.

By default, no Base DN of an LDAP server is configured.



Format
------

**ldap-server authentication base-dn** *base-dn*

**undo ldap-server authentication base-dn** *base-dn*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *base-dn* | Specifies the Base DN of an LDAP authentication server. | The value is a string of 1 to 127 characters, excluding question marks (?). If the character string contains spaces, it must be enclosed in double quotation marks (""). The length ranges from 3 to 129 characters and cannot contain only spaces. |




Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

To add multiple Base DNs, repeat this command.



Example
-------

# Configure the Base DN of an LDAP authentication server named cn.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server authentication base-dn cn

```