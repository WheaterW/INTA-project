ldap-server server-type
=======================

ldap-server server-type

Function
--------

The **ldap-server server-type** command sets the LDAP server type.

The **undo ldap-server server-type** command restores the default LDAP server type.

The default server type of LDAP server templates that the device creates is AD LDAP.



Format
------

**ldap-server server-type** { **ad-ldap** | **ibm-tivoli** | **open-ldap** | **sun-one** }

**undo ldap-server server-type**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ad-ldap** | Sets the LDAP server type to AD LDAP. | - |
| **ibm-tivoli** | Sets the LDAP server type to IBM Tivoli LDAP. | - |
| **open-ldap** | Sets the LDAP server type to OPEN LDAP. | - |
| **sun-one** | Sets the LDAP server type to Sun ONE LDAP. | - |




Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

You need to set the LDAP server type based on the type of the peer LDAP server.



Example
-------

# Set the LDAP server type to AD-LDAP.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server server-type ad-ldap

```