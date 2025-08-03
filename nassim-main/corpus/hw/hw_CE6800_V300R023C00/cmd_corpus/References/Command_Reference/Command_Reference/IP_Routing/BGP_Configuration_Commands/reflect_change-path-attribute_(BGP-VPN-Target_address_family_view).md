reflect change-path-attribute (BGP-VPN-Target address family view)
==================================================================

reflect change-path-attribute (BGP-VPN-Target address family view)

Function
--------



The **reflect change-path-attribute** command enables an RR to modify route attributes of BGP routes through an export policy.

The **undo reflect change-path-attribute** command disables an RR from modifying route attributes of BGP routes through an export policy.



By default, an RR is disabled from modifying route attributes of BGP routes through an export policy.


Format
------

**reflect change-path-attribute**

**undo reflect change-path-attribute**


Parameters
----------

None

Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

According to standard protocols, RRs are disabled from modifying route attributes through an export policy; otherwise, routing loops may occur. Therefore, by default, an export policy cannot be configured on an RR to modify route attributes.To enable an RR to modify route attributes of BGP routes through an export policy, run the **reflect change-path-attribute** command. The route attributes that can be modified are as follows:

* The **apply as-path** command modifies the AS\_Path attribute of BGP routes.
* The **apply comm-filter delete** command deletes a community attribute from BGP routes.
* The **apply community** command modifies a community attribute of BGP routes.
* The **apply cost** command modifies the MED of BGP routes.
* The **apply ip-address next-hop** command modifies the next hop of BGP routes.
* The **apply ipv6 next-hop** command modifies the next hop of BGP4+ routes.
* The **apply local-preference** command modifies the Local\_Pref of BGP routes.
* The **apply origin** command modifies the origin attribute of BGP routes.
* The **apply extcommunity** command modifies the VPN-Target extcommunity attribute of BGP routes.
* The **apply extcommunity soo** command modifies the SoO extcommunity attribute of BGP routes.If the **undo reflect change-path-attribute** command is run, the preceding configurations on the RR do not take effect.

**Precautions**



If an export policy is configured on the current RR, the configuration does not take effect before the **reflect change-path-attribute** command is run. After the **reflect change-path-attribute** command is run, these configurations may take effect, which may affect BGP route selection. Therefore, exercise caution when running the **reflect change-path-attribute** command.Description:After the **reflect change-path-attribute** command is run on an RR, the **peer route-policy export** command takes precedence over the peer next-hop-invariable and peer next-hop-local commands.




Example
-------

# Enable an RR to modify route attributes of BGP routes through an export policy.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] reflect change-path-attribute

```