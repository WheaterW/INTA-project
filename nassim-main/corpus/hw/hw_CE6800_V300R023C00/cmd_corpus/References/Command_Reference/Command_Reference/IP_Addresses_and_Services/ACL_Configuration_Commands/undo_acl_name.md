undo acl name
=============

undo acl name

Function
--------



The **undo acl name** command deletes a created ACL.



By default, no ACL is created.


Format
------

**undo acl name** *acl-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-name* | Creates an ACL with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To delete an existing ACL, run the undo acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device.If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created advanced ACL. The description can contain the functions of the advanced ACL, facilitating applications.




Example
-------

# Delete a basic ACL named basic-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name basic-acl basic
[*HUAWEI-acl4-basic-basic-acl] commit
[~HUAWEI-acl4-basic-basic-acl] quit
[*HUAWEI] undo acl name basic-acl

```