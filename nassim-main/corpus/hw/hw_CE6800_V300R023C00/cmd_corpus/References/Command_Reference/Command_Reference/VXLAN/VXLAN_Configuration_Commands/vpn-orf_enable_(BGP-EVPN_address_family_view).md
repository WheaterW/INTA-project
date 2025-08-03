vpn-orf enable (BGP-EVPN address family view)
=============================================

vpn-orf enable (BGP-EVPN address family view)

Function
--------



The **vpn-orf enable** command enables EVPN ORF.

The **undo vpn-orf enable** command disables EVPN ORF.



By default, EVPN ORF is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vpn-orf enable**

**undo vpn-orf enable**


Parameters
----------

None

Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To allow two devices between which a BGP-EVPN peer relationship is established to exchange ORF routes carrying the import VPN target (IRT) of each other's EVPN instance, run the **vpn-orf enable** command to enable EVPN ORF. Upon receipt of ORF routes, a device uses the export VPN target (ERT) carried in the EVPN routes to be advertised to match the IRT in the received ORF routes so that the peer can receive only the expected routes. This relieves the pressure on the peer and reduces network load.

**Precautions**

1. This command must be used together with the ipv4-family vpn-target and peer enable (BGP-EVPN address family view) commands. If only the **vpn-orf enable** command is run, the BGP speaker in the BGP-EVPN address family view does not advertise ORF routes to its peers.
2. In a scenario where a Huawei device is connected to a non-Huawei device, VPN ORF is configured on the non-Huawei device. VPN ORF is enabled in all VPN-related address families on the non-Huawei device and enabled by address family on the Huawei device. To enable the non-Huawei device to send all required routes to the Huawei device, ensure that the import VPN targets of all VPNs are the same, or different address families are deployed over different BGP sessions.

Example
-------

# Enable EVPN ORF in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] quit
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] vpn-orf enable

```