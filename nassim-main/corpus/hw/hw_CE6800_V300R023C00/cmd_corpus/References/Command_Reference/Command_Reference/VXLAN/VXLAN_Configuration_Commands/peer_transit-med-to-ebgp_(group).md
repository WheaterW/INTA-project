peer transit-med-to-ebgp (group)
================================

peer transit-med-to-ebgp (group)

Function
--------



The **peer transit-med-to-ebgp** command enables a device to transmit MED attributes to an EBGP peer group.

The **undo peer transit-med-to-ebgp** command disables a device from transmitting MED attributes to an EBGP peer group.



By default, a device does not forcibly transmit MED attributes to an EBGP peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **transit-med-to-ebgp**

**undo peer** *peerGroupName* **transit-med-to-ebgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of an EBGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters. The name does not contain spaces. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MED attribute is optional non-transitive. When an EBGP EVPN peer relationship is established between devices in two data centers in different BGP ASs, the devices do not transmit the MED attributes of EVPN routes to each other by default. The MED attribute needs to be transmitted to an EBGP EVPN peer in a scenario, for example, after you change a cost value to switch service flows between the active and standby gateways within a data center. You can run the peer transit-med-to-ebgp command to configure the local gateway to transmit the MED attributes of the received EVPN routes to the peer EBGP EVPN peer.

**Precautions**

MED attributes can be transmitted within an AS by default. Therefore, if you set an intra-AS peer address in this command, this command does not make sense.


Example
-------

# Enable the function to transit routes carrying the MED attribute to an EBGP EVPN peer group.
```
[*HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group gp1 external
[*HUAWEI-bgp] peer gp1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.2 enable
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.2 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 transit-med-to-ebgp

```