pim bsr-boundary
================

pim bsr-boundary

Function
--------



The **pim bsr-boundary** command configures a bootstrap router (BSR) boundary on an interface.

The **undo pim bsr-boundary** command restores the default configuration.



By default, no BSR boundary is configured on an interface.


Format
------

**pim bsr-boundary**

**pim bsr-boundary incoming**

**undo pim bsr-boundary**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **incoming** | Applies a BSR boundary only to incoming traffic.If this parameter is specified, an interface can send BSR messages but cannot receive BSR messages. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A BSR is responsible for collecting rendezvous point (RP)-set information on a PIM-SM network, encapsulating the RP-set information in a bootstrap message, and advertising the message to every PIM neighbor.Before configuring PIM-SM inter-domain multicast, run the pim bsr-boundary command to configure BSR boundaries on interfaces of edge routers to divide PIM-SM domains.Configuring BSR boundaries for a PIM-SM network and the Internet also helps isolate the PIM-SM network from the Internet.

**Prerequisites**

The multicast routing function has been enabled using the multicast routing-enable command in the public network instance view or VPN instance view.

**Configuration Impact**

If an interface is disabled from sending and receiving BSR messages through the BSR boundary configuration, BSR messages cannot pass the BSR boundary but other multicast packets can pass the BSR boundary. BSR boundaries divide a large-scale PIM-SM network into several PIM-SM domains and each BSR serves only the local PIM-SM domain and routers in another PIM-SM domain cannot participate in packet forwarding in the local domain.

**Follow-up Procedure**

Configure a BSR RP for each PIM-SM domain.Establish a Multicast Source Discovery Protocol (MSDP) peer relationship between RPs in each two PIM-SM domains and configure PIM-SM inter-domain multicast.

**Precautions**

If two PIM-SM domains are in different autonomous systems (ASs), you also need to configure BSR boundaries on edge routers.Common tunnel interfaces do not support this command. Only the GRE Tunnel interface supports this command.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure a boundary domain on a GRE tunnel interface.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface tunnel 5
[*HUAWEI-Tunnel5] tunnel-protocol gre
[*HUAWEI-Tunnel5] pim bsr-boundary

```

# Configure a BSR boundary on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim bsr-boundary

```