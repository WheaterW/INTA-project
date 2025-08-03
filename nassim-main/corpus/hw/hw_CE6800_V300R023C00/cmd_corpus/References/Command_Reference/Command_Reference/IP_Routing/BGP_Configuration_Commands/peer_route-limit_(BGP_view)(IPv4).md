peer route-limit (BGP view)(IPv4)
=================================

peer route-limit (BGP view)(IPv4)

Function
--------



The **peer route-limit** command sets the maximum number of routes that can be received from a peer.

The **undo peer route-limit** command restores the default setting.



By default, there is no limit on the number of routes that can be accepted from a peer.


Format
------

**peer** *ipv4-address* **route-limit** [ **accept-prefix** ] *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *minutes* ]

**undo peer** *ipv4-address* **route-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **accept-prefix** | Indicates the number of routes that match the policy.   * If accept-prefix is specified and the keep-all-routes command is run, only the routes that match the policy are counted in the maximum number of routes that can be received. * If accept-prefix is specified, routes are still received and take effect after the number of received routes exceeds the limit in the alert-only scenario. | - |
| *limit* | Specifies the maximum number of routes that can be accepted from a peer. | The value is an integer ranging from 1 to 4294967295. |
| *percentage* | Specifies the proportion threshold of the number of received routes to limit.   * If the proportion reaches percentage and is less than 100%, the device sends a threshold-reaching alarm named BGP\_1.3.6.1.4.1.2011.5.25.177.1.3.1 ROUTETHRESHOLDEXCEED and properly receives routes. * If the proportion reaches 100%, the device sends a threshold-crossing alarm named BGP\_1.3.6.1.4.1.2011.5.25.177.1.3.6 ROUTEEXCEED and stops receiving routes. | The value is an integer ranging from 1 to 100. The default value is 75. |
| **alert-only** | Enables the device to send a threshold alarm or limit-exceeding alarm and stop accepting excess routes if accept-prefix is not specified and the percentage of the number of received routes to the maximum number of routes that can be accepted reaches 100%. In this case, the peer relationship is not disconnected. | - |
| **idle-forever** | Enables the device to report a threshold-crossing alarm if the percentage of the number of received routes to the maximum number of routes that can be received exceeds the specified percentage, and to tear down the peer relationship after the number of routes exceeds the upper limit without attempting to automatically re-establish it before the reset bgp command is run. Therefore, you are advised not to configure this parameter. | - |
| **idle-timeout** *minutes* | Enables the device to send an alarm if the proportion of the number of received routes to limit reaches percentage. After the number of received routes exceeds the limit, the connection is interrupted, and the device does not automatically re-establish the connection until the timer expires. | The value is an integer ranging from 1 to 1200, in minutes. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, a routing table contains a large number of routes. To prevent excessive system resources from being consumed when a large number of routes are received from peers, you can run the **peer route-limit** command to set the maximum number of routes that a BGP device can receive from a peer. This provides a mechanism for controlling the routes received from peers in addition to distribution lists, filtering lists, and route mappings.

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

# Set the maximum number of routes that can be received from a peer to 10000
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] peer 10.1.1.2 route-limit 10000

```