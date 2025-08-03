load-balance gtp teid
=====================

load-balance gtp teid

Function
--------



The **load-balance gtp teid** command enables all Eth-Trunk interfaces on the device to perform load balancing for GTP packets based on the TEID field.

The **undo load-balance gtp teid** command disables all Eth-Trunk interfaces on the device from performing load balancing for GTP packets based on the TEID field.



By default, load balancing for GTP packets based on the TEID field is disabled on all Eth-Trunk interfaces of the device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balance gtp teid**

**undo load-balance gtp teid**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For GTP packets, you can run this command in the system view to configure whether the device performs hash calculation on the packets based on the TEID field.

**Precautions**

* This command takes effect only when the l4-src-port and l4-dst-port factors are enabled in the ip configuration command in the load balancing profile view or Eth-Trunk interface view.
* In known unicast scenarios where the device supports the enhanced load balancing mode, this command takes effect only after the enhanced load balancing mode is configured in the Eth-Trunk interface view.
* GTP packets supported by this command refer to IPv4/IPv6 packets with destination UDP port numbers 0x868 and 0x84B.
* For IPv6 GTP packets, only GTP packets whose first extension header is a UDP extension header can be load balanced based on the TEID field.
* Identification of non-tunnel-encapsulated GTP packets and tunnel-encapsulated GTP packets is supported.
* GTP fragmented packets do not support TEID-based load balancing. The first or non-first GTP fragments do not use information following the UDP port number to participate in load balancing.
* To allow tunnel-encapsulated GTP packets on a transit node to participate in load balancing based on the TEID field, configure inner packets to participate in load balancing.

Example
-------

# Enable load balancing for GTP packets based on the TEID field.
```
<HUAWEI> system-view
[~HUAWEI] load-balance gtp teid

```