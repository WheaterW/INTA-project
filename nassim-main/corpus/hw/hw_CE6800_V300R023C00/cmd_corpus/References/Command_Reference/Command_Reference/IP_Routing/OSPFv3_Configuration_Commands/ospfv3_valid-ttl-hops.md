ospfv3 valid-ttl-hops
=====================

ospfv3 valid-ttl-hops

Function
--------



The **ospfv3 valid-ttl-hops** command enables OSPFv3 GTSM and sets the TTL value to be checked.

The **undo ospfv3 valid-ttl-hops** command disables OSPFv3 GTSM.



By default, OSPFv3 GTSM is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 valid-ttl-hops** *ttl* [ **vpn-instance** *vpn-instance-name* ]

**undo ospfv3 valid-ttl-hops** [ *ttl* ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ttl* | Specifies the TTL value to be checked. | The value is an integer that ranges from 1 to 255. If you specify the parameter hops, the valid range of the TTL value in the packet to be checked is [ 255-hops+1, 255 ]. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. If this parameter is specified, it indicates that only the TTL value of the packets in the specified VPN instance needs to be checked. | The value is a string of 1 to 31 characters. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If an OSPFv3 network requires high security, you can configure GTSM to improve network security. GTSM defends against attacks through TTL detection. If an attacker continuously sends simulated OSPFv3 unicast packets to a device, the device directly sends the packets to OSPFv3 on the control plane after receiving them, without checking the validity of these packets. As a result, the control plane of the device is busy processing these packets, and the CPU usage is high. GTSM protects a device by checking whether the TTL value in the IP packet header is within a pre-defined range to enhance system security.The **ospfv3 valid-ttl-hops** command enables OSPFv3 GTSM. To check the TTL values of the packets that match the GTSM policy, you need to specify vpn-instance in the command.For example, if you run the **ospfv3 valid-ttl-hops** command, OSPFv3 GTSM is enabled on both the public network and VPNs. If the **ospfv3 valid-ttl-hops 5 vpn-instance** command is run, OSPFv3 GTSM is enabled on both the public network and VPNs, the TTL values of OSPFv3 packets in the specified VPN instance are checked, and the default action is taken on the OSPFv3 packets that do not match GTSM policies in the public network and other VPN instances.



**Precautions**



If a VPN instance is specified in the **ospfv3 valid-ttl-hops** command and the interface is bound to the VPN instance, if the configured TTL value is smaller than the actual TTL value on the network, all unicast packets sent to the interface are discarded.




Example
-------

# Enable OSPFv3 GTSM, and set the maximum number of TTL hops to 5 for the packets that can be received from the public network.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 valid-ttl-hops 5

```