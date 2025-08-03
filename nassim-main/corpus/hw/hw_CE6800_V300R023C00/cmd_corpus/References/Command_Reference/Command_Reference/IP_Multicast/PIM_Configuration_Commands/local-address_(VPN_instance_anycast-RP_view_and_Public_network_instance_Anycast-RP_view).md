local-address (VPN instance anycast-RP view/Public network instance Anycast-RP view)
====================================================================================

local-address (VPN instance anycast-RP view/Public network instance Anycast-RP view)

Function
--------



The **local-address** command sets a local address for an anycast-rendezvous point (Anycast-RP).

The **undo local-address** command deletes the local address of an Anycast-RP.



By default, no local address is set for an Anycast-RP.


Format
------

**local-address** *local-address*

**undo local-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *local-address* | Specifies a local address for an Anycast-RP. | The value is in dotted decimal notation. This address must be a valid unicast IP address and cannot be an address on the network segment 127.0.0.0/8. |



Views
-----

VPN instance anycast-RP view,Public network instance Anycast-RP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If PIM Anycast-RP is configured, after an RP receives a Register message, it checks the source address in the Register message. If the Register message is sent by the source's designated router (DR), the RP forwards the Register message to Anycast-RP peers. If the Register message is sent by an Anycast-RP peer, it does not forward the Register message.When forwarding a PIM Register message to other Anycast-RP peers, the local RP needs to use its own IP address (called the local address) as the source address of the Register message and use the addresses of Anycast-RP peers as the destination addresses of the Register message. In such a manner, Anycast-RP peers can learn source/group information from each other. To set a local address for an Anycast-RP, run the local-address command.

**Precautions**

A local address for an Anycast-RP must be different from the Anycast RP address.Setting a loopback interface address as the local address for an Anycast-RP is recommended.


Example
-------

# In the public network instance, specify 1.1.1.1 as the local address for the Anycast-RP address 10.10.10.10.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] anycast-rp 10.10.10.10
[*HUAWEI-pim-anycast-rp-10.10.10.10] local-address 1.1.1.1

```