peer tracking (BGP-VPN instance view) (group)
=============================================

peer tracking (BGP-VPN instance view) (group)

Function
--------



The **peer tracking** command enables BGP Peer Tracking. That is, you can configure BGP to fast detect the unreachable state of a peer and re-establish the connection between the local device and the peer.

The **undo peer tracking** command disables BGP Peer Tracking.



By default, BGP Peer Tracking is disabled.


Format
------

**peer** *group-name* **tracking** [ **delay** *delay-time* ]

**undo peer** *group-name* **tracking** [ **delay** *delay-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **delay** *delay-time* | Indicates the interval between when BGP detects the peer unreachable and when BGP tears down the corresponding connection. | The value is an integer that ranges from 0 to 65535, in seconds. The default value is 0 seconds. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a network where BFD is unsuitable to be deployed, you can configure BGP Peer Tracking on the local device to implement fast network convergence by rapidly detecting the unreachable state of the peer.A BGP peer is considered unreachable in either of the following situations:

* The BGP peer's IP address does not match any route in the IP routing table.
* The BGP peer's IP address matches a route with the outbound interface being a Null0 interface in the IP routing table.A proper value of delay-time can ensure network stability when a peer is detected unreachable.
* If delay-time is set to 0, BGP immediately tears down the connection between the local device and its peer after the peer is detected unreachable.
* If IGP route flapping occurs and delay-time for an IBGP peer is set to 0, the peer relationship between the local device and the peer alternates between Up and Down. Therefore, delay-time for an IBGP peer should be set to a value greater than the actual IGP route convergence time.
* When BGP neighbors successfully perform the GR negotiation, the master/slave switchover occurs on the BGP neighbors, to prevent the failure of GR, delay-time should be set to a value greater than GR convergence time. If delay-time is set to be smaller than the GR convergence time, the connection between the local device and the BGP peer will be torn down, which leads to the failure of GR.

Example
-------

# Configure BGP Peer Tracking.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test external
[*HUAWEI-bgp-instance-vpn1] peer test as-number 200
[*HUAWEI-bgp-instance-vpn1] peer test tracking delay 20

```