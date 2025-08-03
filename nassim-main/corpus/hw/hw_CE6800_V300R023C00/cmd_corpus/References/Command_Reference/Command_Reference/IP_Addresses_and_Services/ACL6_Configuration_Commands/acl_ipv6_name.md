acl ipv6 name
=============

acl ipv6 name

Function
--------



The **acl ipv6 name** command creates an advanced ACL6 and displays the ACL6 view. If the advanced ACL6 to be created already exists, running this command directly displays the ACL6 view.



By default, no advanced ACL6 is created.


Format
------

**acl ipv6 name** *advance-acl6-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *advance-acl6-name* | Creates an advanced ACL6 with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Advanced ACL6s match packets based on the source IP address, destination IP address, IP protocol type, and protocol-specific configurations (for example, source and destination TCP ports and ICMPv6 protocol type and code) of the packets. To create an advanced ACL6, run the acl ipv6 command.



**Configuration Impact**



The **undo acl ipv6 all** command deletes all types of ACL6s on a device. If the ACL6s being deleted are applied to services, these services are interrupted. Before deleting an ACL6, ensure that the ACL6 is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created advanced ACL6. Then the ACL6 rule can be applied to match packets.Run the **description** command to configure a description for a created advanced ACL6. The description can contain the functions of the advanced ACL6, facilitating applications.




Example
-------

# Create an advanced ACL6 named advance-acl6.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name advance-acl6

```