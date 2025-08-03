peer advertise-large-community (BGP view)
=========================================

peer advertise-large-community (BGP view)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a BGP peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its BGP peer.


Format
------

**peer** *ipv4-address* **advertise-large-community** [ **disable** ]

**undo peer** *ipv4-address* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**



Specific Large-Community values have been defined in a route-policy.




Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] peer 10.1.1.2 advertise-large-community

```