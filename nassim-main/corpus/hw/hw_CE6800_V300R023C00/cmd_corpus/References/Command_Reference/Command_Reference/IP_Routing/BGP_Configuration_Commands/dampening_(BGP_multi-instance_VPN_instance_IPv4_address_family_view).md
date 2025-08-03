dampening (BGP multi-instance VPN instance IPv4 address family view)
====================================================================

dampening (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **dampening** command enables route flapping dampening for EBGP peers or modifies route flapping dampening parameters for EBGP peers.

The **undo dampening** command cancels the dampening on the flapping of EBGP routes.

The **dampening ibgp** command enables IBGP peer route flapping dampening or modifies various IBGP peer route flapping dampening parameters.

The **undo dampening ibgp** command disables IBGP route flapping dampening.



By default, BGP route flapping suppression is disabled.


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
| *ceiling* | Specifies a penalty ceiling. | The value is an integer ranging from 1001 to 20000. The configured value must be greater than the value of suppress. The default value is 16000. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **update-standard** | Enables BGP to add a penalty value (500) to the route carried in each received Update message (excluding Withdraw message). | - |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a dampening policy is configured for routes, routes preferentially match the dampening parameters of the dampening policy.If no parameter is set, the default value of each parameter is used. The four parameters of attenuation are interdependent. Therefore, if any of the preceding parameters is used, all parameters must be specified.BGP route flapping suppression measures the stability of a route by using a penalty value. The greater the penalty value, the less stable the route. Each time route flapping occurs, that is, when a device receives a Withdraw message for a route, BGP adds a penalty value (1000) to the route.When the penalty value of a route exceeds the suppression threshold, the route is suppressed. The device does not add the route to the IP routing table or advertise Update messages to other BGP peers. BGP removes the best flag of the route. If the last message received by the device is an Update message, the route is marked with the d flag. If the last message received by the device is a Withdraw message, the route is marked with the h flag. The route can have both the d and h flags. In this case, the d flag takes effect. When the penalty value reaches a certain value, the penalty value does not increase any more. This value is called the penalty upper limit.At the same time, the penalty value of the suppressed route decreases by half each time the route passes through a period of time. This period is called half-life. If the last route received by a device is an Update message, when the penalty value of the route falls below the reuse threshold, the device removes the d flag from the route. The route becomes available and is preferentially selected. Then, the device adds the route to the IP routing table and advertises an Update message to other BGP peers. If the last message received by a device is a Withdraw message and the penalty value of the route decreases to 0, the device deletes the route from the BGP routing table or BGP labeled routing table.After BGP route flapping suppression is configured, any parameter in the command can be used to suppress flapping routes. The purpose of adjusting parameters is to adjust the suppression time as required. To increase the suppression time of flapping routes, perform the following operations (or reduce the suppression time):

* The value of ceiling is increased.
* The value half-life-reach is increased.
* The value of reuse is decreased.

**Configuration Impact**



If the **dampening** command is run more than once, the latest configuration overrides the previous one.After the **dampening** command is run, the system dampens unstable routes. Specifically, the system does not add unstable routes to the BGP routing table or BGP labeled routing table or advertise them to other BGP peers.



**Precautions**

Note the following items when configuring BGP route flap dampening:

* The values of reuse, suppress, and ceiling are in ascending order.
* According to the formula MaxSuppressTime=half-life-reachÃ60Ã(ln(ceiling/reuse)/ln(2)), if the value of MaxSuppressTime is smaller than 1, dampening cannot be performed. Therefore, the value of the ceiling/reuse must be great enough so that the value of MaxSuppressTime can be equal to or greater than 1.


Example
-------

# Enable EBGP peer route dampening and configure EBGP peer route dampening parameters.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] dampening 10 1000 2000 5000

```

# Enable IBGP peer route dampening and configure IBGP peer route dampening parameters.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] dampening ibgp 10 1000 2000 5000

```