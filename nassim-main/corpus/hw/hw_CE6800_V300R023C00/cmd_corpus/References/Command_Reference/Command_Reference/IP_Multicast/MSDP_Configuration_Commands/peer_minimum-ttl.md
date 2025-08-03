peer minimum-ttl
================

peer minimum-ttl

Function
--------



The **peer minimum-ttl** command sets a TTL threshold for multicast data packets that can be encapsulated in source active (SA) messages and forwarded to a specified Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer minimum-ttl** command restores the default value.



By default, the TTL threshold is 0 for multicast data packets that can be encapsulated in SA messages and forwarded to an MSDP peer.


Format
------

**peer** *peer-address* **minimum-ttl** *ttl*

**undo peer** *peer-address* **minimum-ttl**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *ttl* | Specifies a TTL threshold. | The value is an integer ranging from 0 to 255. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSDP peers exchange SA messages over TCP connections. To limit multicast data packets that can be encapsulated in SA messages, run the **peer minimum-ttl** command to set a TTL threshold for multicast data packets.After a TTL threshold is set for a specified MSDP peer, the Router checks the TTL of a multicast data packet before encapsulating the multicast data packet in an SA message. Only the multicast data packet with the TTL being greater than the threshold is encapsulated in an SA message and sent to the peer of the Router.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.


Example
-------

# In the public network instance, set the TTL threshold to 10 for multicast data packets that can be encapsulated in SA messages and forwarded to the MSDP peer 10.10.10.1, so that only multicast data packets with the TTL value being greater than 10 can be encapsulated in SA messages and forwarded to the MSDP peer.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.10.1 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.10.10.1 minimum-ttl 10

```