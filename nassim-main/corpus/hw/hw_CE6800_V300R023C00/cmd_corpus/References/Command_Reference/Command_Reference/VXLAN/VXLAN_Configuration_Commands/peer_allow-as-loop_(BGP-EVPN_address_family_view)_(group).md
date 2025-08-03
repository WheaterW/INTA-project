peer allow-as-loop (BGP-EVPN address family view) (group)
=========================================================

peer allow-as-loop (BGP-EVPN address family view) (group)

Function
--------



The **peer allow-as-loop** command sets the number of local AS number repetitions.

The **undo peer allow-as-loop** command cancels the configuration.



By default, the local AS number cannot be repeated.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **allow-as-loop** [ *number* ]

**undo peer** *group-name* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *number* | Specifies the number of local AS number repetitions. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the **bgp** command and the fake AS number configured using the peer fake-as command. The largest number of times any of the configured AS numbers is repeated is considered as the maximum number. In Hub-Spoke networking, if EBGP runs between the PE and CE at the Hub site, the routing information advertised by the Hub-PE to the Hub-CE carries the AS number of the local AS. When the Hub-PE receives a route update message from the Hub-CE, the route update message carries the AS number of the local AS. As a result, the Hub-PE cannot receive the route update message.To ensure correct route transmission in Hub-Spoke networking, configure the BGP peers through which the VPN routes are advertised from the Hub-CE to the Spoke-CE to allow routes with the AS number repeated once in the AS\_Path attribute to pass through.

**Prerequisites**

The specified peer group has been enabled in the BGP-EVPN address family view.

**Configuration Impact**

If the **peer allow-as-loop** command is run for a peer group multiple times, the latest configuration overrides the previous one.

**Precautions**

The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.


Example
-------

# Set the number of local AS number repetitions to 2 in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group gp external
[*HUAWEI-bgp] peer 10.1.1.9 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 enable
[*HUAWEI-bgp-af-evpn] peer gp enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 group gp
[*HUAWEI-bgp-af-evpn] peer gp allow-as-loop 2

```