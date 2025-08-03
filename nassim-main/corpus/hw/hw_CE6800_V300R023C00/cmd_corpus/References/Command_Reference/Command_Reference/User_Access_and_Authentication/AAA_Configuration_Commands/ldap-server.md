ldap-server
===========

ldap-server

Function
--------

The **ldap-server** command configures an LDAP server template for an authentication domain.

The **undo ldap-server** command deletes an LDAP server template from an authentication domain.

By default, no LDAP server template of an authentication domain is configured.



Format
------

**ldap-server** *template-name*

**undo ldap-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of an LDAP server template. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

To perform LDAP authentication and authorization for users in a domain, bind an LDAP server template to the domain. After binding the LDAP server template to the domain, the configuration in the LDAP server template takes effect.



Example
-------

# Configure LDAP server template temp1 for authentication domain dd.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] domain dd
[*HUAWEI-aaa-domain-dd] ldap-server temp1

```