export route-policy (EVPN instance view)
========================================

export route-policy (EVPN instance view)

Function
--------



The **export route-policy** command associates an EVPN instance with an export routing policy.

The **undo export route-policy** command disassociates an EVPN instance with an export routing policy.



By default, an EVPN instance is not associated with any export routing policy.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**export route-policy** *policy-name*

**undo export route-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a routing policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, an EVPN instance adds all VPN targets in the export VPN target list to EVPN routes to be advertised to its peers. To control route export more precisely, run the **export route-policy** command to associate the EVPN instance with an export routing policy and set attributes for eligible routes.

**Prerequisites**

An RD has been configured for the EVPN instance using the **route-distinguisher** command.If the export route-policy to be associated with a VPN instance IPv4 address family does not exist, configure the export route-policy first.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Associate an EVPN instance with an export routing policy named rp2.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] route-policy rp2 permit node 10
[*HUAWEI-route-policy] apply community 10:1
[*HUAWEI-route-policy] quit
[*HUAWEI] bridge-domain 100
[*HUAWEI-bd100] vxlan vni 200
[*HUAWEI-bd100] evpn
[*HUAWEI-bd100-evpn] route-distinguisher 100:1
[*HUAWEI-bd100-evpn] export route-policy rp2

```