undo acl ipv6 name (system view)
================================

undo acl ipv6 name (system view)

Function
--------



The **undo acl ipv6 name** command deletes a created ACL6.



By default, no ACL6 is created.


Format
------

**undo acl ipv6 name** *acl6-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-name* | Creates an ACL6 with a name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To create an ACL6, run the acl ipv6 command.

* A basic ACL6 defines rules for filtering packets based on the source IP addresses of packets.
* Advanced ACL6s match packets based on the source IP address, destination IP address, IP protocol type, and protocol-specific configurations (for example, source and destination TCP ports and ICMPv6 protocol type and code) of the packets.To delete an existing ACL6, run the undo acl command.

**Configuration Impact**



The **undo acl ipv6 all** command deletes all types of ACL6s on a device. If the ACL6s being deleted are applied to services, these services are interrupted. Before deleting an ACL6, ensure that the ACL6 is not referenced by services.




Example
-------

# Delete an advanced ACL6 named advance-acl6.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name advance-acl6
[*HUAWEI-acl6-advance-advance-acl6] commit
[~HUAWEI-acl6-advance-advance-acl6] quit
[~HUAWEI] undo acl ipv6 name advance-acl6

```