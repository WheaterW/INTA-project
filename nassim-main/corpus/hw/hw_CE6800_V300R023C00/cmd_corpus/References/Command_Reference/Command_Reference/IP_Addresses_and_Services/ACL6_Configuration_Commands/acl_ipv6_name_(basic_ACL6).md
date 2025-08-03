acl ipv6 name (basic ACL6)
==========================

acl ipv6 name (basic ACL6)

Function
--------



The **acl ipv6 name** command creates a basic ACL6 and displays the ACL6 view. If the basic ACL6 to be created already exists, running this command directly displays the ACL6 view.



By default, no basic ACL6 is created.


Format
------

**acl ipv6 name** *basic-acl6-name* **basic**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **basic** | Creates a basic ACL6 with a keyword. | - |
| **name** *basic-acl6-name* | Creates a basic ACL6 with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A basic ACL6 defines rules for filtering packets based on the source IP addresses of packets. To create a basic ACL6, run the acl ipv6 command.



**Configuration Impact**



The **undo acl ipv6 all** command deletes all types of ACL6s on a device. If the ACL6s being deleted are applied to services, these services are interrupted. Before deleting an ACL6, ensure that the ACL6 is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created basic ACL6. Then the ACL6 rule can be applied to match packets.Run the **description** command to configure a description for a created basic ACL6. The description can contain the functions of the basic ACL6, facilitating applications.




Example
-------

# Create a basic ACL6 named basic-acl6.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name basic-acl6 basic

```