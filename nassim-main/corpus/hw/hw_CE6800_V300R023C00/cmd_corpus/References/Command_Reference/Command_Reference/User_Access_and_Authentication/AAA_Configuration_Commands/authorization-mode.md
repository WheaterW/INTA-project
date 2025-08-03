authorization-mode
==================

authorization-mode

Function
--------

The **authorization-mode** command configures an authorization mode for an authorization scheme.

The **undo authorization-mode** command restores the default authorization mode in an authorization scheme.

By default, local authorization is used.



Format
------

**authorization-mode none**

**authorization-mode** { **hwtacacs** | **if-authenticated** | { **local** | **local-case** } | **ldap** } \* [ **none** ]

**undo authorization-mode**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hwtacacs** | Indicates that the user is authorized by an HWTACACS server. | - |
| **if-authenticated** | Indicates that only the user who succeeds in authentication is authorized.  The configuration of if-authenticated authorization does not take effect in RADIUS authentication. | - |
| **local** | Authenticates users locally and sets local user names to case-insensitive. | - |
| **local-case** | Authenticates users locally and sets local user names to case-sensitive. | - |
| **none** | Indicates non-authorization. | - |
| **ldap** | Indicates that the user is authorized by an LDAP server. | - |




Views
-----

Authorization scheme view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

To authorize users, configure an authorization mode in an authorization scheme.

You can configure multiple authorization modes in an authorization scheme to reduce the chance of authorization failures.After the
**authorization-mode hwtacacs local** command is used, if it fails to connect to the HWTACACS authentication server and HWTACACS authorization cannot be performed, the device starts local authorization.

Example
-------

# Configure the authorization scheme named scheme1 to apply HWTACACS authorization.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authorization-scheme scheme1
[*HUAWEI-aaa-author-scheme1] authorization-mode hwtacacs

```