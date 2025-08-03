acl name (basic ACL)
====================

acl name (basic ACL)

Function
--------



The **acl name** command creates a basic ACL and displays the ACL view. If the basic ACL to be created already exists, running this command directly displays the ACL view.



By default, no basic ACL is created.


Format
------

**acl name** *basic-acl-name* **basic**

**acl name** *basic-acl-name* [ **number** ] *basic-acl-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl-name* | Creates a basic ACL with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **basic** | Creates a basic ACL with a keyword. | - |
| **number** *basic-acl-number* | Creates a basic ACL with a number. | The value is an integer ranging from 2000 to 2999. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A basic ACL defines rules for filtering packets based on the source IP addresses of packets. To create a basic ACL, run the acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created basic ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created basic ACL. The description can contain the functions of the basic ACL, facilitating applications.




Example
-------

# Create a basic ACL named basic-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name basic-acl basic

```