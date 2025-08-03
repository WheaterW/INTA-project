peer allow-as-loop (BGP-VPN-Target address family view) (group)
===============================================================

peer allow-as-loop (BGP-VPN-Target address family view) (group)

Function
--------



The **peer allow-as-loop** command sets the number of local AS number repetitions.

The **undo peer allow-as-loop** command cancels the configuration.



By default, the local AS number cannot be repeated.


Format
------

**peer** *group-name* **allow-as-loop** [ *number* ]

**undo peer** *group-name* **allow-as-loop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *number* | Specifies the number of local AS number repetitions. | The value is an integer ranging from 1 to 10. The default value is 1. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Generally, BGP uses AS numbers to detect routing loops. The AS numbers in the AS\_Path of each received route are matched against the local AS number configured using the **bgp** command and the fake AS number configured using the peer fake-as command. The largest number of times any of the configured AS numbers is repeated is considered as the maximum number. In Hub-Spoke networking, if EBGP runs between the PE and CE at the Hub site, the routing information advertised by the Hub-PE to the Hub-CE carries the AS number of the local AS. When the Hub-PE receives a route update message from the Hub-CE, the route update message carries the AS number of the local AS. As a result, the Hub-PE cannot receive the route update message.To ensure correct route transmission in Hub-Spoke networking, configure the BGP peers through which the VPN routes are advertised from the Hub-CE to the Spoke-CE to allow routes with the AS number repeated once in the AS\_Path attribute to pass through.



**Prerequisites**



A peer group has been established using the **peer as-number** command.



**Configuration Impact**



If you run the command multiple times in the same peer group view, only the latest configuration takes effect.



**Precautions**



The **peer allow-as-loop** command does not take effect for IBGP peers or BGP peers in a sub-confederation. The device checks whether the routes received from EBGP peers or EBGP peers in the confederation contain the local AS number. The minimum number of repetitions is 2, and the value 1 is not displayed.Running the **peer allow-as-loop** command may cause routing loops. Therefore, exercise caution when running this command and specify the number of AS number repetitions as required.




Example
-------

# Set the number of local AS number repetitions to 2.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test allow-as-loop 2

```