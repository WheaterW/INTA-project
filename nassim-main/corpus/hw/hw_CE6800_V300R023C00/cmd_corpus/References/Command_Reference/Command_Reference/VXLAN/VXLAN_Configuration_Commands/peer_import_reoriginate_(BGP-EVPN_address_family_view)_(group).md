peer import reoriginate (BGP-EVPN address family view) (group)
==============================================================

peer import reoriginate (BGP-EVPN address family view) (group)

Function
--------



The **peer import reoriginate** command enables a device to add a regeneration flag to the routes received from BGP EVPN peer group.

The **undo peer import reoriginate** command restores the default configuration.



By default, a device does not add a regeneration flag to the routes received from BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **import** **reoriginate**

**undo peer** *peerGroupName* **import** **reoriginate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the data center interconnect (DCI) solution, DCI-PE adds the regeneration flag to the received EVPN routes before sending the routes to the peer. By default, the function to add the regeneration flag to the routes received from the peer is disabled. Specifically, DCI-PE does not re-encapsulate the routes received from the peer. Therefore, to allow DCI-PE to re-encapsulate the EVPN routes, run the **peer import reoriginate** command to enable the function to add the regeneration flag to the routes received from the peer.

**Prerequisites**

The **peer enable** command has been run to enable the device to exchange routing information with a specified peer group.


Example
-------

# Configure the device to add the regeneration flag to the routes to be received from a BGP EVPN peer group in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 import reoriginate

```