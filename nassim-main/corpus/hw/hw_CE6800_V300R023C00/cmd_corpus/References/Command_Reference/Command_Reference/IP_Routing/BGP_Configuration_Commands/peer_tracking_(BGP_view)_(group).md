peer tracking (BGP view) (group)
================================

peer tracking (BGP view) (group)

Function
--------



The **peer tracking** command enables BGP Peer Tracking. That is, you can configure BGP to fast detect the unreachable state of a peer and re-establish the connection between the local device and the peer.

The **undo peer tracking** command disables BGP Peer Tracking.



By default, BGP Peer Tracking is disabled.


Format
------

**peer** *group-name* **tracking** [ **delay** *delay-time* ]

**undo peer** *group-name* **tracking**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **delay** *delay-time* | Indicates the interval between when BGP detects the peer unreachable and when BGP tears down the corresponding connection. | An integer ranging from 0 to 65535, in seconds. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a network where BFD is unsuitable to be deployed, you can configure BGP Peer Tracking on the local device to implement fast network convergence by rapidly detecting the unreachable state of the peer.A BGP peer is considered unreachable in either of the following situations:

* The BGP peer's IP address does not match any route in the IP routing table.
* The BGP peer's IP address matches a route with the outbound interface being a Null0 interface in the IP routing table.A proper value of delay-time can ensure network stability when a peer is detected unreachable.
* If delay-time is set to 0, BGP immediately tears down the connection between the local device and its peer after the peer is detected unreachable.
* If IGP route flapping occurs and delay-time for an IBGP peer is set to 0, the peer relationship between the local device and the peer alternates between Up and Down. Therefore, delay-time for an IBGP peer should be set to a value greater than the actual IGP route convergence time.
* When BGP neighbors successfully perform the GR negotiation, the master/slave switchover occurs on the BGP neighbors, to prevent the failure of GR, delay-time should be set to a value greater than GR convergence time. If delay-time is set to be smaller than the GR convergence time, the connection between the local device and the BGP peer will be torn down, which leads to the failure of GR.

**Prerequisites**



The **peer as-number** command has been run to create BGP peers or BGP peer groups.



**Precautions**



IGP GR is configured, and BGP peer relationship establishment depends on IGP routes. When a node on the network fails and an active/standby switchover is performed, IGP does not delete the route received from the node, and the BGP peer relationship established based on the route does not detect the node fault. In this case, BGP peer tracking does not take effect.After the **peer tracking** command is run on an unnumbered peer on a physical sub-interface or Eth-Trunk sub-interface of the local device, if the peer sub-interface is shut down, the local route does not change. As a result, the local device cannot detect the link fault in a timely manner and interrupt the BGP peer relationship. In this scenario, the **peer tracking** command does not take effect.




Example
-------

# Configure BGP Peer Tracking.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] peer test tracking delay 20

```