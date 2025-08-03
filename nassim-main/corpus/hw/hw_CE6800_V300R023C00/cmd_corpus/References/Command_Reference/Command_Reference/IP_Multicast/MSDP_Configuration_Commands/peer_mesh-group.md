peer mesh-group
===============

peer mesh-group

Function
--------



The **peer mesh-group** command adds a Multicast Source Discovery Protocol (MSDP) peer to a mesh group.

The **undo peer mesh-group** command restores the default configuration.



By default, an MSDP peer does not belong to any mesh group.


Format
------

**peer** *peer-address* **mesh-group** *name*

**undo peer** *peer-address* **mesh-group**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *name* | Specifies the name of a mesh group. | The value is a string of 1 to 32 case-sensitive characters. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If multiple MSDP peers exist on a network, source active (SA) messages may be flooded between peers. Especially when many MSDP peers are configured in the same PIM-SM domain, reverse path forwarding (RPF) rules cannot filter out useless SA messages effectively. The MSDP peer needs to perform the RPF check on each received SA message, which brings heavy workload to the system.To reduce the number of SA messages transmitted between MSDP peers and the system workload, run the **peer mesh-group** command to add MSDP peers to a mesh group.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.An MSDP peer relationship has been set up between any two members of a mesh group.

**Configuration Impact**

One MSDP peer can join only one mesh group. If an MSDP peer is configured to join different mesh groups, the latest configuration takes effect.When a member of the mesh group receives an SA message, it checks the source of the SA message:

* If the SA message is sent by an MSDP peer outside the mesh group, the member performs the RPF check on the SA message. If the SA message passes the check, the member forwards it to other members of the mesh group.
* If the SA message is sent by a member of the mesh group, the member directly accepts the message without performing the RPF check. In addition, it does not forward the message to other members in the mesh group.

**Precautions**

Before adding an MSDP peer to a mesh group using the **peer mesh-group** command, you must run the **peer connect-interface** command to set up MSDP peer relationships between this MSDP peer and all the current members of the mesh group.Commonly, the MSDP peers in the same autonomous system (AS) join the same mesh group and EBGP routes need be configured between inter-AS MSDP peers.


Example
-------

# In the public network instance, add the MSDP peer 10.10.7.6 to the mesh group named Group1.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.10.7.6 mesh-group Group1

```