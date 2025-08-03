ipv6 (load balancing profile view)
==================================

ipv6 (load balancing profile view)

Function
--------



The **ipv6** command configures the load balancing mode for ipv6 packets in a load balancing profile.

The **undo ipv6** command deletes the specified load balancing mode or restores the default load balancing mode for ipv6 packets in a load balancing profile.



By default, ipv6 packets are load balanced based on src-ip, dst-ip, l4-src-port, and l4-dst-port.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**ipv6** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** ] \*

**undo ipv6** [ **src-ip** | **dst-ip** | **protocol** | **l4-src-port** | **l4-dst-port** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-ip** | Performs load balancing based on the source ipv6 address. | - |
| **dst-ip** | Performs load balancing based on the destination ipv6 address. | - |
| **protocol** | Performs load balancing based on the protocol type. | - |
| **l4-src-port** | Performs load balancing based on the transport-layer source port number. | - |
| **l4-dst-port** | Performs load balancing based on the transport-layer destination port number. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The ipv6 command configures the load balancing mode for ipv6 packets in a load balancing profile. The **undo ipv6** command with no parameter specified restores the default load balancing mode for ipv6 packets whereas the **undo ipv6** command with a parameter specified deletes the specified load balancing mode for ipv6 packets.

**Precautions**



If you run this command multiple times, only the latest configuration takes effect.




Example
-------

# Configure load balancing for ipv6 packets based on src-ip and protocol in the load balancing profile named abc.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile abc
[*HUAWEI-load-balance-profile-abc] ipv6 src-ip protocol

```