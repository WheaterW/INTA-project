ldap-server authentication manager-with-base-dn enable
======================================================

ldap-server authentication manager-with-base-dn enable

Function
--------

The **ldap-server authentication manager-with-base-dn enable** command attaches the Base DN to an administrator DN during LDAP authentication.

The undo ldap-server authentication manager-with-base-dn enable command removes the Base DN from an administrator DN during LDAP authentication.

By default, an administrator DN carries the Base DN during LDAP authentication.



Format
------

**ldap-server authentication manager-with-base-dn enable**

**undo ldap-server authentication manager-with-base-dn enable**



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

If multiple Base DNs are configured, the administrator DN automatically carries the first Base DN. Multiple Base DNs are mainly used for user authentication. During user authentication, the first Base DN is preferentially used to search for the user. If a match is found, no further searching is performed. If no match is found, the other Base DNs are used in the order of their sequence numbers.

In some cases, an administrator DN is not under the Base DN. You run the undo ldap-server authentication manager-with-base-dn enable command to remove the Base DN from the manager DN. When you run the
**ldap-server authentication manager** command to configure the administrator DN, you must enter the full path.

Example
-------

# Remove the Base DN to an administrator DN during LDAP authentication.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template temp1
[*HUAWEI-ldap-temp1] ldap-server authentication manager-with-base-dn enable

```