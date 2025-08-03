isis ppp-negotiation
====================

isis ppp-negotiation

Function
--------



The **isis ppp-negotiation** command specifies PPP negotiation for the establishment of neighbor relationships.

The **undo isis ppp-negotiation** command restores the default negotiation mode.



By default, three-way handshake is adopted. Three-way handshake is backward compatible. If the neighbor supports only two-way handshake, the neighbor relationship is established through two-way handshake.


Format
------

**isis ppp-negotiation** { **2-way** | **3-way** [ **only** ] }

**undo isis ppp-negotiation**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **2-way** | Uses two-way handshake for the establishment of neighbor relationships. | - |
| **3-way** | Uses three-way handshake for the establishment of neighbor relationships. | - |
| **only** | Indicates that only three-way handshake is supported for the establishment of neighbor relationships and that three-way handshake is not backward compatible. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A reliable link layer protocol is required when IS-IS runs on a P2P link. In two-way handshake mode, once a device receives a Hello packet from its neighbor, the device declares the neighbor Up. In three-way handshake mode, a device declares its neighbor Up only when it knows that the neighbor also receives its packet. Compared with two-way handshake, three-way handshake can detect unidirectional link failures, improving the link reliability.The isis ppp-negotiation command configures the link negotiation mode.

**Prerequisites**

An IS-IS process has been created on a specified interface.

**Configuration Impact**

Running the isis ppp-negotiation command can change the link negotiation mode of an interface.

**Precautions**

For a broadcast interface, set the link type of the interface to P2P before running the isis ppp-negotiation command.


Example
-------

# Configure two-way handshake for the establishment of the neighbor relationship on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable
[*HUAWEI-100GE1/0/1] isis circuit-type p2p
[*HUAWEI-100GE1/0/1] isis ppp-negotiation 2-way

```