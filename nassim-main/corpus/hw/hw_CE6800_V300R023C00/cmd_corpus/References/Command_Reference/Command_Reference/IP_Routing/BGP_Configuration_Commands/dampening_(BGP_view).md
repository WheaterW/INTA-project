dampening (BGP view)
====================

dampening (BGP view)

Function
--------



The **dampening** command enabled route flapping dampening for EBGP peers or modifies route flapping dampening parameters for EBGP peers.

The **undo dampening** command cancels the dampening on the flapping of EBGP routes.

The **dampening ibgp** command enables IBGP peer route flapping dampening or modifies various IBGP peer route flapping dampening parameters.

The **undo dampening ibgp** command canceld the dampening on IBGP route flapping.



By default, BGP route flapping suppression is disabled.


Format
------

**dampening** [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* ] \* [ **update-standard** ]

**dampening ibgp** [ *half-life-reach* *reuse* *suppress* *ceiling* | **route-policy** *route-policy-name* ] \* [ **update-standard** ]

**undo dampening**

**undo dampening ibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *half-life-reach* | Specifies a half-life for reachable routes. | The value is an integer ranging from 1 to 45, in minutes. The default value is 15, in minutes. |
| *reuse* | Specifies a Reuse value. If the penalty of a route falls below the Reuse value, the route is reused. | The value is an integer ranging from 1 to 20000. The default value is 750. |
| *suppress* | Specifies a Suppress value. If the penalty value of a route exceeds the Suppress value, the route is dampened. | The value is an integer ranging from 1 to 20000 and must be greater than the value of reuse. The default value is 2000. |
| *ceiling* | Specifies a penalty ceiling. | The value is an integer ranging from 1001 to 20000. The configured value must be greater than the value of suppress. The default value is 16000. |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **update-standard** | Enables BGP to add a penalty value (500) to the route carried in each received Update message (excluding Withdraw message). | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a policy is configured for route dampening, routes are preferentially matched against the dampening parameters defined by route-policy in the command.The four parameters of the command are mutually dependent. If you configure one of the parameters, the other parameters also need to be configured in the command.BGP dampening measures route stability using a penalty value. The greater the penalty value, the less stable a route. Each time route flapping occurs (the device receives a Withdraw), BGP adds a penalty value to the route carried in the message. If a route changes from active to inactive, the penalty value increases by 1000.If the penalty value of a route exceeds the Suppress value, the route is dampened. The device does not add the route to the IP routing table or advertise any Update message to other BGP peers. BGP removes the best flag of the route. If the route is carried in an Update message, BGP adds a d flag to the route; if the route is carried in a Withdraw message, BGP adds an h flag to the route. If a route carries both a d flag and an h flag, the route is considered a deleted one. After the penalty value reaches the penalty ceiling, it does not increase any more.The penalty value of a dampened route reduces by half after a half-life period. If the route is carried in an Update message and its penalty value decreases to the Reuse value, the route becomes reusable, and BGP removes the d flag from it, adds it to the IP routing table if it is an optimal route, and advertises an Update message carrying the route to BGP peers. If the route is carried in a Withdraw message and its penalty value decreases to 0, BGP deletes this route from the BGP routing table.After BGP route dampening is configured, any parameter in the command can be used to dampen flapping routes. You can adjust the parameters as required. To increase the dampening time of flapping routes, perform any of the following operations (to reduce the dampening time, perform otherwise):

* Increase ceiling.
* Increase half-life-reach.
* Reduce reuse.

**Configuration Impact**

If the **dampening** command is run more than once, the latest configuration overrides the previous one.After the **dampening** command is run, the system dampens unstable routes. Specifically, the system does not add unstable routes to the BGP routing table or advertise them to other BGP peers.

**Precautions**

When configuring BGP route dampening, pay attention to the following points:

* The reuse, suppress, and ceiling thresholds increase in sequence.
* According to the formula MaxSuppressTime=half-life-reachÃ60Ã(ln(ceiling/reuse)/ln(2)), if the value of MaxSuppressTime is less than 1, the dampening cannot be performed. Therefore, to ensure that the value of MaxSuppressTime is greater than or equal to 1, the value of ceiling/reuse must be large enough.If **route-policy** *route-policy-name*is configured, the following items can be matched: IPv4 ACLs, AS\_Path filters, AS\_Path length filters, community filters, route costs, VPN-Target extended community filters, bandwidth extended community filters, outbound interfaces, MPLS labels, large-community filters, Next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, route priority, destination address prefix list of IP routing information, route modulo, route source IP address ACL, route source IPv6 address ACL, route source IP address prefix, route type. Route dampening parameters can be set.If the referenced policy contains unsupported attribute matching or setting behaviors, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.

Example
-------

# Enable EBGP peer route dampening and configure EBGP peer route dampening parameters.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] dampening 10 1000 2000 5000

```

# Enable IBGP peer route dampening and configure IBGP peer route dampening parameters.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] dampening ibgp 10 1000 2000 5000

```