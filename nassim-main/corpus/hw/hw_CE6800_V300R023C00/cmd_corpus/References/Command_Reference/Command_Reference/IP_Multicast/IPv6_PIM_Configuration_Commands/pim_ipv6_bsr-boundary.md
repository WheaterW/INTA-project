pim ipv6 bsr-boundary
=====================

pim ipv6 bsr-boundary

Function
--------



The **pim ipv6 bsr-boundary** command configures a BootStrap router (BSR) boundary on an interface.

The **undo pim ipv6 bsr-boundary** command restores the default configuration.



By default, no BSR boundary is configured on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 bsr-boundary**

**undo pim ipv6 bsr-boundary**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A BSR is a core of a PIM-SM network responsible for collecting Rendezvous Point (RP)-Set information on the network, encapsulating the RP-Set information in a Bootstrap message, and advertising the message to every PIM neighbor.Prior to configuring PIM-SM inter-domain multicast, you need to configure BSR boundaries on interfaces of edge Router to divide PIM-SM domains.Configuring BSR boundaries for a PIM-SM network and the Internet also helps isolate the PIM-SM network from the Internet.


Example
-------

# Configure a BSR boundary on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 bsr-boundary

```