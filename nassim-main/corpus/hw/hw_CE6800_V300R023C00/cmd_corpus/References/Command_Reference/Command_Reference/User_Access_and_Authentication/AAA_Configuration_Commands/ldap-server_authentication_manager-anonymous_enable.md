ldap-server authentication manager-anonymous enable
===================================================

ldap-server authentication manager-anonymous enable

Function
--------

The **ldap-server authentication manager-anonymous enable** command allows administrators to access an LDAP server anonymously.

The **undo ldap-server authentication manager-anonymous enable** command blocks administrators from accessing an LDAP server anonymously.

By default, administrators are prevented from accessing an LDAP server anonymously.



Format
------

**ldap-server authentication manager-anonymous enable**

**undo ldap-server authentication manager-anonymous enable**



Parameters
----------

None


Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

If the LDAP server allows anonymous access, run the **ldap-server authentication manager-anonymous enable** command. After this command is executed, the device deletes the DN and password of the administrator and removes the Base DN from the administrator DN. To prevent administrators from accessing an LDAP server anonymously, run the **undo ldap-server authentication manager-anonymous enable** command and configure an administrator DN and password. To configure the administrator DN and password, run the **ldap-server authentication manager** command.



Example
-------

# Allow administrators to access an LDAP server anonymously.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server authentication manager-anonymous enable

```