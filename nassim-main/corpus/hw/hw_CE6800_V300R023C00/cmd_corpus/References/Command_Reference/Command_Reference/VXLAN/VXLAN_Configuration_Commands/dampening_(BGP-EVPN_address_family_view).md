dampening (BGP-EVPN address family view)
========================================

dampening (BGP-EVPN address family view)

Function
--------



The **dampening** command enables EVPN route dampening or modifies EVPN route damping parameters.

The **undo dampening** command disables EVPN route dampening.



By default, BGP route flapping suppression is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dampening** [ *half-life-reach* *reuse* *suppress* *ceiling* | [ **route-policy** *route-policy-name* ] ] \* [ **update-standard** ]

**dampening ibgp** [ *half-life-reach* *reuse* *suppress* *ceiling* | [ **route-policy** *route-policy-name* ] ] \* [ **update-standard** ]

**undo dampening**

**undo dampening ibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *half-life-reach* | Specifies the half life of a reachable route. | The value is an integer ranging from 1 to 45, in minutes. The default value is 15. |
| *reuse* | Specifies a Reuse value. If the penalty value of a route falls below the Reuse value, the route is reused. | The value is an integer ranging from 1 to 20000. The default value is 750. |
| *suppress* | Specifies a Suppress value. If the penalty value of a route exceeds the Suppress value, the route is dampened. | The value is an integer ranging from 1 to 20000 and must be greater than the value of reuse. The default value is 2000. |
| *ceiling* | Specifies a penalty ceiling. | The value is an integer ranging from 1001 to 20000. The configured value must be greater than that of suppress. The default value is 16000. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **update-standard** | Enables BGP to add the standard penalty value to the route carried in each received Update message (excluding Withdraw message). | - |
| **ibgp** | Enables IBGP route flap damping. | - |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a policy is configured for route dampening, routes are preferentially matched against the dampening parameters defined by route-policy in the command.The four parameters of the command are mutually dependent. If you configure one of the parameters, the other parameters also need to be configured in the command.EVPN dampening measures route stability using a penalty value. The greater the penalty value, the less stable a route. Each time route flapping occurs (the device receives a Withdraw), EVPN adds a penalty value to the route carried in the message. If a route changes from active to inactive, the penalty value increases by 1000.If the penalty value of a route exceeds the Suppress value, the route is dampened. The device does not add the route to the IP routing table or advertise any Update message to other EVPN peers. EVPN removes the best flag of the route. If the route is carried in an Update message, EVPN adds a d flag to the route; if the route is carried in a Withdraw message, EVPN adds an h flag to the route. If a route carries both a d flag and an h flag, the route is considered a deleted one. After the penalty value reaches the penalty ceiling, it does not increase any more.The penalty value of a dampened route reduces by half after a half-life period. If the route is carried in an Update message and its penalty value decreases to the Reuse value, the route becomes reusable, and EVPN removes the d flag from it, adds it to the IP routing table if it is an optimal route, and advertises an Update message carrying the route to EVPN peers. If the route is carried in a Withdraw message and its penalty value decreases to 0, EVPN deletes this route from the EVPN routing table.After EVPN route dampening is configured, any parameter in the command can be used to dampen flapping routes. You can adjust the parameters as required. To increase the dampening time of flapping routes, perform any of the following operations (to reduce the dampening time, perform otherwise):

* Increase ceiling.
* Increase half-life-reach.
* Reduce reuse.

**Prerequisites**



Run the **evpn-overlay enable** command to enable EVPN as the VXLAN control plane.



**Configuration Impact**

If the **dampening** command is run more than once, the latest configuration overrides the previous one.After the **dampening** command is run, the system dampens unstable routes. Specifically, the system does not add unstable routes to the EVPN routing table or advertise them to other EVPN peers.

**Precautions**

When configuring EVPN route flapping suppression, pay attention to the following points:

* The reuse, suppress, and ceiling thresholds increase in sequence.
* According to the formula MaxSuppressTime = half-life-reach x 60 x (ln(ceiling/reuse)/ln(2)), if the value of MaxSuppressTime is less than 1, the suppression cannot be performed. Therefore, to ensure that the value of MaxSuppressTime is greater than or equal to 1, the value of ceiling/reuse must be large enough.When **route-policy** *route-policy-name*is configured, the following items can be specified: IPv4 ACL, AS\_Path filter, AS\_Path length filter, community filter, route cost, IPv6 route destination address, VPN target extended community filter, outbound interface, MPLS label, Large-community filter, next-hop address ACL of routing information, next-hop address ACL of IPv6 routing information, next-hop address prefix list based on routing information, next-hop address prefix list based on IPv6 routing information, route priority, destination address prefix list of IP routing information, destination address prefix list of IPv6 routing information, route modulo, route source IP address ACL, route source IPv6 address ACL, route source IP address prefix list, route source IPv6 address prefix list, route type, and route dampening parameters.If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.

Example
-------

# Enable EVPN route dampening and configure EVPN route dampening parameters.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] dampening 10 1000 2000 5000

```