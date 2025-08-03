peer (VPN instance anycast-RP view/Public network instance Anycast-RP view)
===========================================================================

peer (VPN instance anycast-RP view/Public network instance Anycast-RP view)

Function
--------



The **peer** command configures an anycast-rendezvous point (Anycast-RP) peer address.

The **undo peer** command deletes an Anycast-RP peer address.



By default, no Anycast-RP peer address is configured.


Format
------

**peer** *peer-address* **fwd-msdp-sa** [ *acl-number* | **acl-name** *acl-name* ]

**peer** *peer-address*

**undo peer** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies an Anycast-RP peer address. | The value is in dotted decimal notation. |
| **fwd-msdp-sa** | Enables a local RP to send to Anycast-RP peers the Register messages that are encapsulated using source/group information extracted from received Multicast Source Discovery Protocol (MSDP) source active (SA) messages. | - |
| *acl-number* | Specifies the range of multicast groups to which an MSDP SA message can be forwarded. AclNum specifies an ACL number. | The value is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the range of multicast groups to which an MSDP SA message can be forwarded. AclName specifies an ACL name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VPN instance anycast-RP view,Public network instance Anycast-RP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If PIM Anycast-RP is configured, after an RP receives a Register message from a source designated router (DR), the RP checks the source address of the Register message. If the Register message is sent by the source DR, the RP forwards the Register message to Anycast-RP peers; if the Register message is sent by an Anycast RP peer, the Register message is not forwarded.When forwarding a Register message, the RP needs to replace the source address of the Register message with the local address of the Anycast RP and replace the destination address of the Register message with the address of the Anycast RP peer. In such a manner, Anycast RP peers can learn source/group information from each other. This command is used to configure an anycast RP peer address to replace the destination address of the Register message.To obtain information about the multicast source and group outside the PIM domain, use either of the following methods:

* MSDP peer relationships are set up between members of the anycast RP set and external devices.
* RPs in an anycast RP set are classified into two types: RPs that have set up MSDP peer relationships with other devices and RPs that do not set up MSDP peer relationships with other devices. When RPs that have set up MSDP peer relationships with other devices receive MSDP SA messages, they convert the messages into Register messages and send the Register messages to the RPs that have not set up MSDP peer relationships.

**Precautions**

You can specify a maximum of 16 Anycast-RP peers for each Anycast-RP.In a PIM-SM domain, an Anycast-RP peer relationship must be established between every two devices deployed with Anycast-RP to implement full connections.


Example
-------

# In the public network instance, specify 2.2.2.2 as the Anycast-RP peer address for the Anycast-RP address 3.3.3.3 , and enable the local RP to forward MSDP SA messages to its peers.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] anycast-rp 3.3.3.3
[*HUAWEI-pim-anycast-rp-3.3.3.3] peer 2.2.2.2 fwd-msdp-sa

```