acl name
========

acl name

Function
--------



The **acl name** command creates an advanced ACL and displays the ACL view. If the advanced ACL to be created already exists, running this command directly displays the ACL view.



By default, no advanced ACL is created.


Format
------

**acl name** *advance-acl-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *advance-acl-name* | Creates an advanced ACL with a name. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Advanced ACLs match packets based on the source IP address, destination IP address, IP protocol type, and protocol-specific configurations (for example, source and destination TCP ports and ICMP protocol type and code) of the packets. To create an advanced ACL, run the acl command.



**Configuration Impact**



The **undo acl all** command deletes all types of ACLs on a device. If the ACLs being deleted are applied to services, these services are interrupted. Before deleting an ACL, ensure that the ACL is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created advanced ACL. Then the ACL rule can be applied to match packets.Run the **description** command to configure a description for a created advanced ACL. The description can contain the functions of the advanced ACL, facilitating applications.




Example
-------

# Create an advanced ACL named advance-acl.
```
<HUAWEI> system-view
[~HUAWEI] acl name advance-acl

```