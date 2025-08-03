acl ipv6 number
===============

acl ipv6 number

Function
--------



The **acl ipv6 number** command creates an ACL6 and displays the ACL6 view. If the ACL6 already exists, this command directly displays the ACL6 view.

The **undo acl ipv6 number** command deletes a created ACL6.



By default, no ACL6 is created.


Format
------

**acl ipv6** [ **number** ] *basic-acl6-number*

**acl ipv6** [ **number** ] *advance-acl6-number*

**undo acl ipv6** [ **number** ] *basic-acl6-number*

**undo acl ipv6** [ **number** ] *advance-acl6-number*

**undo acl ipv6 all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Creates a basic ACL6 with a number. | The value is an integer ranging from 2000 to 2999. |
| *advance-acl6-number* | Creates an advanced ACL6 with a number. | The value is an integer ranging from 3000 to 3999. |
| **all** | Deletes all ACL6s. | - |



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

* An interface-based ACL6 defines rules for filtering packets based on the inbound interfaces of packets.
* A basic ACL6 defines rules for filtering packets based on the source IP addresses of packets.
* Advanced ACL6s match packets based on the source IP address, destination IP address, IP protocol type, and protocol-specific configurations (for example, source and destination TCP ports and ICMPv6 protocol type and code) of the packets.

**Configuration Impact**



The **undo acl ipv6 all** command deletes all types of ACL6s on a device. If the ACL6s being deleted are applied to services, these services are interrupted. Before deleting an ACL6, ensure that the ACL6 is not referenced by services.



**Follow-up Procedure**



Run the **rule** command to configure a rule for a created ACL6. Then the ACL6 rule can be applied to match packets.Run the **description** command to configure a description for a created ACL6. The description can contain the functions of the ACL6, facilitating applications.




Example
-------

# Create a basic ACL6 numbered 2999.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 2999

```

# Create an advanced ACL6 numbered 3999.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 3999

```