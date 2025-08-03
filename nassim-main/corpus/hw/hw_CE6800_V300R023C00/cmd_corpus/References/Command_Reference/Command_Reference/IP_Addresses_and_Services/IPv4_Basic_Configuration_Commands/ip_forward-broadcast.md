ip forward-broadcast
====================

ip forward-broadcast

Function
--------



The **ip forward-broadcast** command enables an interface to receive and forward directed broadcast packets destined for its direct network segment.

The **undo ip forward-broadcast** command disables an interface from receiving or forwarding directed broadcast packets destined for its direct network segment.



By default, an interface is disabled from receiving or forwarding directed broadcast packets destined for its direct network segment.


Format
------

**ip forward-broadcast** [ **acl** { *acl-number* | **name** *acl-name* } ]

**undo ip forward-broadcast**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **acl** *acl-number* | Specifies an ACL number. | The value is an integer ranging from 2000 to 3999.   * A basic ACL number ranges from 2000 to 2999. * An advanced ACL number ranges from 3000 to 3999. |
| **name** *acl-name* | Specifies an ACL name. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A directed broadcast packet is broadcast to a specific network. In the destination IP address of such a packet, the network ID field contains the network ID of a specific network, and the host ID field contains all 1s.Directed broadcast packets can be used by attackers to attack the network system, bringing security risks. However, the device interfaces may need to receive or forward directed broadcast packets in some scenarios. For example, when an interface is configured as a UDP helper, it converts broadcast packets into unicast packets and sends them to a specific server. To allow this, enable the interface to receive and forward directed broadcast packets destined for its direct network segment.An ACL can be referenced in this command to implement this function. For example, to use a basic ACL rule to implement this function, run the acl (system view) command to create a basic ACL and then the rule (ACL view) command in the basic ACL rule to create a rule with permit defined for the directed broadcast packets to be received and forwarded. Then run the **ip forward-broadcast** command with the ACL specified.


Example
-------

# Disable an interface from receiving or forwarding directed broadcast packets destined for its direct network segment.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] undo ip forward-broadcast

```