peer route-limit(BGP multi-instance VPN instance IPv6 address family view)(group)
=================================================================================

peer route-limit(BGP multi-instance VPN instance IPv6 address family view)(group)

Function
--------



The **peer route-limit** command sets the maximum number of routes that can be received from a peer group.

The **undo peer route-limit** command restores the default setting.



By default, there is no limit on the number of routes that can be accepted from a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **route-limit** *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]

**undo peer** *peerGroupName* **route-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-limit** *limit* | Specifies the maximum number of routes that can be accepted from a peer. | The value is an integer ranging from 1 to 4294967295. |
| *percentage* | Specifies the proportion threshold of the number of received routes to limit.   * If the proportion reaches percentage and is less than 100%, the device sends a threshold-reaching alarm named BGP\_1.3.6.1.4.1.2011.5.25.177.1.3.1 ROUTETHRESHOLDEXCEED and properly receives routes. * If the proportion reaches 100%, the device sends a threshold-crossing alarm named BGP\_1.3.6.1.4.1.2011.5.25.177.1.3.6 ROUTEEXCEED and stops receiving routes. | The value is an integer ranging from 1 to 100. The default value is 75. |
| **alert-only** | Enables the device to send a threshold alarm or limit-exceeding alarm and stop accepting excess routes if accept-prefix is not specified and the percentage of the number of received routes to the maximum number of routes that can be accepted reaches 100%. In this case, the peer relationship is not disconnected. | - |
| **idle-forever** | Enables the device to report a threshold-crossing alarm if the percentage of the number of received routes to the maximum number of routes that can be received exceeds the specified percentage, and to tear down the peer relationship after the number of routes exceeds the upper limit without attempting to automatically re-establish it before the reset bgp command is run. Therefore, you are advised not to configure this parameter. | - |
| **idle-timeout** *times* | Enables the device to send an alarm if the proportion of the number of received routes to limit reaches percentage. After the number of received routes exceeds the limit, the connection is interrupted, and the device does not automatically re-establish the connection until the timer expires. | The value is an integer ranging from 1 to 1200, in minutes. |
| **peer** *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer route-limit** command is used to set the maximum number of routes that a BGP device is allowed to receive from its peer group. This provides a mechanism for controlling the routes received from peer group in addition to distribution lists, filtering lists, and route mappings.

**Configuration Impact**

If the **peer route-limit** command is run for a peer group, the peers of the peer group inherit the configuration.When the peer relationship between peers is Established:

* If the **peer route-limit** command is run for the first time or the upper limit is reduced and the number of routes received by the device exceeds the upper limit:
* If alert-only is specified in the command, the peer relationship is not interrupted and the received routes are not withdrawn, and for the new routes that are received, the system performs limit-exceeding processing.
* If idle-forever is specified in the command, the local device terminates the connection with its peer. To reestablish the connection, run the **reset bgp** command.
* If idle-timeout is specified in the command, the local device terminates the connection with its peer and starts the timer for automatic connection re-establishment. To re-establish the connection before the timer expires, you can run the **reset bgp** command.
* If the upper limit is increased to a value greater than the number of received routes, the device sends Refresh messages to receive routes again. If the device does not support the route-refresh capability, the device reestablishes the connection.
* If the upper limit is reduced but is still greater than the number of received routes, the device only changes the configuration parameter.If alert-only, idle-forever, or idle-timeout is not configured and the percentage of the number of received routes to the maximum number of routes that can be accepted is greater than the specified percentage, the device sends a threshold alarm. When the number of received routes exceeds the limit, the peer relationship is interrupted. After 30 seconds, the system automatically attempts to reestablish the peer relationship.
* If the upper limit remains unchanged, the device only changes the configuration parameter.
* If accept-prefix is specified, the device continues to accept excess routes in the alert-only scenario, and all received routes are valid. If accept-prefix is not specified in the alert-only scenario, the device only sends the threshold alarm or limit-exceeding alarm and does not accept excess routes. In this case, the peer relationship is not disconnected.

**Precautions**

If a specified peer has this capability and the peer relationship is interrupted because the number of routes exceeds the upper limit, the same peer relationship in all address families is affected, and the peer relationship is re-established.Adding, modifying, or deleting the peer route-limit configuration of a BGP peer may cause the BGP peer to learn a large number of routes.If idle-forever is configured, the peer relationship is interrupted after the number of routes exceeds the upper limit. In addition, the connection is not automatically re-established, which may cause network interruption and cannot be automatically restored. Therefore, configuring idle-forever is not recommended.


Example
-------

# Set the maximum number of routes that can be received from a peer group to 10000.
```
<pe> system-view
[~pe] ip vpn-instance vpna
[*pe-vpn-instance-vpna] ipv6-family
[*pe-vpn-instance-vpna-af-ipv6] quit
[*pe-vpn-instance-vpna] quit
[*pe] bgp 100 instance a
[*pe-bgp-instance-a] ipv6-family vpn-instance vpna
[*pe-bgp-instance-a-6-vpna] group b
[*pe-bgp-instance-a-6-vpna] peer b route-limit 10000

```