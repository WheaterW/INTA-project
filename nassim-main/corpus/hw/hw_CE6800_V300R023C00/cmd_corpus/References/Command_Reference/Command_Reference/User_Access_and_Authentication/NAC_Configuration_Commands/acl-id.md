acl-id
======

acl-id

Function
--------



The **acl-id** command binds an ACL to a service scheme.

The **undo acl-id** command unbinds an ACL from a service scheme.



By default, no ACL is bound to a service scheme.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**acl-id** *acl-number*

**undo acl-id** { *acl-number* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL bound to a service scheme. | The value is an integer ranging from 3000 to 3999. |
| **all** | Deletes the numbers of all ACLs bound to a service scheme. | - |



Views
-----

Service scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After creating a service scheme using the service-scheme (AAA view) command, you can run the acl-id command to bind an ACL to the service scheme. The user assigned with the service scheme will have the ACL rules.

**Prerequisites**

An ACL must have been created using the acl (system view) or acl name command.


Example
-------

# Bind ACL 3001 to the service scheme huawei.
```
<HUAWEI> system-view
[~HUAWEI] acl 3001
[*HUAWEI-acl-adv-3001] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] service-scheme huawei
[*HUAWEI-aaa-service-huawei] acl-id 3001

```