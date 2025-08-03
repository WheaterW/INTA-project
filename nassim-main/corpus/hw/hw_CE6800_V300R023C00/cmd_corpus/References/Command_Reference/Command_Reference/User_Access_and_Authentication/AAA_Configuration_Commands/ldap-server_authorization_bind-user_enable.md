ldap-server authorization bind-user enable
==========================================

ldap-server authorization bind-user enable

Function
--------

The **ldap-server authorization bind-user enable** command configures user binding during LDAP authorization.

The **undo ldap-server authorization bind-user enable** command cancels user binding during LDAP authorization.

By default, user binding is performed during LDAP authorization.



Format
------

**ldap-server authorization bind-user enable**

**undo ldap-server authorization bind-user enable**



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

By default, user binding is performed during LDAP authorization. During the authorization, the device sends the user names and passwords of authenticated users to the LDAP server for re-authentication. If a user name has the same password on an authentication server and an LDAP server, user binding is required. If a user name has different passwords on an authentication server and an LDAP server, run the **undo ldap-server authorization bind-user enable** command to cancel user binding; otherwise, user authentication will fail on the LDAP server and authorization fails.



Example
-------

# Cancel user binding during LDAP authorization.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] undo ldap-server authorization bind-user enable

```