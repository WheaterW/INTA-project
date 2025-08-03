ipv6 mtu
========

ipv6 mtu

Function
--------



The **ipv6 mtu** command sets the maximum transfer unit (MTU) value for an interface to send IPv6 packets.

The **undo ipv6 mtu** command restores the default MTU value for an interface to send IPv6 packets.



The default MTU value varies according to the hardware and interface. For details, see the parameter description field.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 mtu** *mtu*

**undo ipv6 mtu**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mtu* | Specifies the MTU for an interface to send IPv6 packets. | The value is an integer. The value ranges and default values of common interfaces are as follows:   * Ethernet interface and its sub-interface: The value is an integer ranging from 1280 to 9600, in bytes. The default value is 1500. * Tunnel interface: The value is an integer ranging from 1280 to 9600, in bytes. The default value is 1500. * Eth-Trunk interface and its sub-interfaces: The value is an integer ranging from 1280 to 9600, in bytes. The default value is 1500. * VBDIF interface: The value is an integer ranging from 1280 to 9600, in bytes. The default value is 1500. * VLANIF interface: The value is an integer ranging from 1280 to 9600, in bytes. The default value is 1500.   The preceding values are for reference only. The value ranges and default values vary according to hardware and interfaces. The supported interface types, value ranges, and default values depend on the actual device. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the traffic capability on a link between the source and destination ends changes, this ipv6 mtu command is used to set the MTU value for sending IPv6 packets. If the packet length is greater than the IPv6 MTU of the interface, the system fragments the packet based on the set MTU value before forwarding the packet.

**Configuration Impact**

The dynamic PMTU of the system is set based on the IPv6 MTU of the interface.The PMTU mechanism specifies the minimum MTU of all interfaces on the path from the source to the destination.When sending a packet, an interface fragments the packet based on the smaller value between the path MTU (PMTU) and the IPv6 MTU configured using this command.

**Precautions**

When using this command to set the IPv6 MTU of an interface, ensure that the IPv6 MTUs of the directly connected interfaces are the same.For OSPFv3:

* By default, MTU check is enabled on an OSPFv3 interface. The interface fills in the MTU value when sending DD packets. In addition, the device checks whether the MTU carried in the DD packet from the neighbor exceeds the MTU of the local device. If the MTU exceeds the MTU of the local device, the OSPF neighbor relationship is not established. If the IPv6 MTU of the interface is changed, the OSPF neighbor relationship is re-established. If the MTUs are different, the OSPF neighbor relationship cannot be established.
* After the **ospfv3 mtu-ignore** command is run on an OSPFv3 interface and MTU check is disabled, the MTU value is 0 when the interface sends DD packets. If the MTUs at both ends of a link are different, an OSPF neighbor relationship can be established. Changing the IPv6 MTU of an interface does not reestablish an OSPF neighbor relationship. However, packets whose length exceeds the local MTU sent by the peer end may be discarded, and routes carried in the packets cannot be learned. As a result, services may be interrupted.


Example
-------

# Set the IPv6 MTU value to 1400 for an Eth-Trunk interface.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 mtu 1400

```

# Set the IPv6 MTU value to 1400 for 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 mtu 1400

```