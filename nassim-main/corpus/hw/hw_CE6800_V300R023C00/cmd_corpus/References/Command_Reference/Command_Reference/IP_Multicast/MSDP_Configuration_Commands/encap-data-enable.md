encap-data-enable
=================

encap-data-enable

Function
--------



The **encap-data-enable** command enables the device to encapsulate a multicast data packet into a source active (SA) message.

The **undo encap-data-enable** command disables the device from encapsulating a multicast data packet into an SA message.



By default, no multicast data packet is encapsulated into an SA message.


Format
------

**encap-data-enable**

**undo encap-data-enable**


Parameters
----------

None

Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The source's rendezvous point (RP) encapsulates the information about all active sources into many SA messages and advertises them. Each SA message can contain multiple (S, G) entries.After the encap-data-enable command is run on the source's RP, the RP encapsulates the multicast data carried in a Register message into an SA message, and then sends the SA message to Multicast Source Discovery Protocol (MSDP) peers. Only one multicast data packet can be encapsulated into an SA message.After the encap-data-enable command is run on an MSDP peer, it can transmit SA messages carrying multicast data packets to MSDP peers in other autonomous systems (ASs).


Example
-------

# Enable the device to encapsulate a multicast data packet into an SA message
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] encap-data-enable

```