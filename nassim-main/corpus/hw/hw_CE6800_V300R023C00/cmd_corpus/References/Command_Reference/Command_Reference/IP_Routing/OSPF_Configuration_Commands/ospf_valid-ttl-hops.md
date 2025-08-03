ospf valid-ttl-hops
===================

ospf valid-ttl-hops

Function
--------



The **ospf valid-ttl-hops** command enables OSPF GTSM and sets the TTL value to be checked.

The **undo ospf valid-ttl-hops** command disables OSPF GTSM.



By default, OSPF GTSM is disabled.


Format
------

**ospf valid-ttl-hops** *ttl* [ **nonstandard-multicast** ] [ **vpn-instance** *vpn-instance-name* ]

**undo ospf valid-ttl-hops** [ *ttl* ] [ **nonstandard-multicast** ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ttl* | Specifies the TTL value to be checked. | The value is an integer that ranges from 1 to 255. If you specify the parameter hops, the valid range of the TTL value in the packet to be checked is [ 255-hops+1, 255 ]. |
| **nonstandard-multicast** | Specifies the GTSM configuration is also valid for multicast packets. When the.  nonstandard-multicast parameter is configured:   * The TTL values of the multicast packets which will be sent are set to 255. * Received multicast packets are not checked. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network requiring high security, you can configure GTSM to improve the security of the OSPF network. GTSM defends against attacks through TTL detection. If an attacker continuously sends simulated OSPF unicast packets to a device, the device receives these packets and finds that they are local packets. Then, the device directly sends the packets to OSPF on the control plane for processing, without checking the validity of these packets. As a result, the control plane of the device is busy processing these packets, and the CPU usage is high. GTSM protects a device by checking whether the TTL value in the IP packet header is within a pre-defined range to enhance system security.This command can be used to enable OSPF GTSM and check the TTL value.

* After the **ospf valid-ttl-hops** command is run, OSPF GTSM can be enabled, regardless of whether the public network or private network is used.
* If vpn-instance is specified, only the TTL values of OSPF packets in a specified VPN instance are checked, and the default action (configured using the **gtsm default-action** command) for the packets that do not match GTSM policies is taken on the OSPF packets in the public network instance and other VPN instances. If vpn-instance is not specified, only the TTL values of OSPF packets in the public network instance are checked, and the default action for the packets that do not match GTSM policies is taken on OSPF packets in VPN instances.

**Precautions**

* If a VPN instance is specified in the **ospf valid-ttl-hops** command and an interface is bound to the VPN instance, all the OSPF unicast packets sent to this interface are discarded when the set TTL value is smaller than the actual TTL value on the network.
* If a virtual link or sham link is configured, the configured TTL value must be the same as the actual TTL value. That is, the number of devices that the virtual link or sham link passes through is counted. Otherwise, packets sent from neighbors over the virtual link or sham link are discarded.
* The default TTL value of OSPF packets sent by a device is 1. After the **ospf valid-ttl-hops** command is run, the TTL value of OSPF packets sent by the device changes to 255. If the **ospf valid-ttl-hops** command is run only on one end, OSPF unicast packets may fail to be forwarded. Although the established OSPF neighbor relationship is not affected, the new OSPF neighbor relationship cannot go Up.
* After the **ospf valid-ttl-hops hops** command is run, the valid TTL range of the detected packet changes to [255-hops+1, 255]. For example, if the value of hops is 5, the received OSPF packet is valid only when the TTL value of the packet ranges from 251 to 255.


Example
-------

# Enable OSPF GTSM, and set the maximum number of TTL hops to 5 for the packets that can be received from the public network.
```
<HUAWEI> system-view
[~HUAWEI] ospf valid-ttl-hops 5

```