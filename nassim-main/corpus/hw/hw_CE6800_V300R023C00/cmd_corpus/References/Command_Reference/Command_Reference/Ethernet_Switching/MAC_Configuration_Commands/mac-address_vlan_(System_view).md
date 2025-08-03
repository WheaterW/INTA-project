mac-address vlan (System view)
==============================

mac-address vlan (System view)

Function
--------



The **mac-address blackhole** command configures a static blackhole MAC address entry.

The **undo mac-address blackhole** command deletes a static blackhole MAC address entry.

The **mac-address static vlan** command configures static MAC address entries for a VLAN to direct data forwarding.

The **undo mac-address static vlan** command deletes static MAC address entries for a VLAN.



By default, no static blackhole MAC address entry or VLAN-based static MAC address entry is configured.


Format
------

**mac-address blackhole** *mac-address* **vlan** *vlan-id*

**mac-address static** *mac-address* { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id*

**undo mac-address** *mac-address* **vlan** *vlan-id*

**undo mac-address** { { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* | **vlan** *vlan-id* [ *interface-type* *interface-number* | *interface-name* ] }

**undo mac-address blackhole** [ *mac-address* ] **vlan** *vlan-id*

**undo mac-address static** { { *mac-address* { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* } | { { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* | **vlan** *vlan-id* [ *interface-type* *interface-number* | *interface-name* ] } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a destination MAC address entry. | The value is in the H-H-H format. H is a 4-digit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **vlan** *vlan-id* | Specifies the ID of a VLAN to which the outbound interface belongs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **static** *mac-address* | Indicates a static MAC address entry. | The value is in the H-H-H format. H is a 4-digit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **blackhole** *mac-address* | Indicates a blackhole entry. | The value is in the H-H-H format. H is a 4-digit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* MAC address table capacity attackThe attack source sends packets with different source MAC addresses to a network device. After receiving these packets, the network device learns the source MAC addresses. Since the capacity of a MAC address table is limited, when the number of the MAC addresses in the MAC address table reaches the limit, the source MAC addresses of valid packets cannot be learned. These packets sent from the attack source are also broadcast in the VLAN, consuming lots of bandwidth on the network. This may also affect the hosts attached to the network device.
* MAC address entry attackWhen a device learns source MAC addresses and creates a MAC address table, the system cannot identify whether the packets are from authorized users or hackers. This brings security threats. If hackers send attack packets with forged source MAC addresses and access a device through other interfaces, the device will learn incorrect MAC address entries. As a result, the packets that should be forwarded to authorized users are forwarded to hackers.To improve interface security, a network administrator can run the **mac-address static** command to add specific MAC address entries to the MAC address table. User devices are bound to interfaces to prevent unauthorized users from obtaining data.

**Configuration Impact**



After static MAC address entries are configured, when receiving a frame with a specific MAC address, a device directly forwards the frame through the corresponding outbound interface. Static MAC address entries will not be aged and they will not be lost after the system resets or the board is hot-swapped.The device that has MAC flapping enabled will send its received packets through all interfaces except the interface that receives the packets. This ensures that the silent host receives the packets.



**Precautions**



Manually configured MAC address entries take precedence over automatically generated entries. Static and static blackhole MAC address entries that are configured by users will not be overwritten by dynamic MAC address entries. Dynamic MAC address entries, however, can be overwritten by static and blackhole MAC address entries.The network administrator is familiar with the MAC addresses of the network devices that need to use static MAC address entries for communication; otherwise, the configuration will interrupt authorized users' communication.




Example
-------

# Configure a static MAC address entry with the outbound interface belonging to a specified VLAN.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] quit
[*HUAWEI] vlan 20
[*HUAWEI-vlan20] quit
[*HUAWEI] interface 100GE 1/0/3
[*HUAWEI-100GE1/0/3] portswitch
[*HUAWEI-100GE1/0/3] port default vlan 10
[*HUAWEI-100GE1/0/3] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 20
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] mac-address static 00e0-fc12-3457 100GE 1/0/3 vlan 10
[*HUAWEI] mac-address static 00e0-fc12-3456 100GE 1/0/1 vlan 20

```

# Configure a static MAC address entry based on a specified interface and VLAN.
```
<HUAWEI> system-view
[~HUAWEI] vlan 40
[*HUAWEI-vlan40] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 40
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] mac-address static 1-1-1 100GE 1/0/1 vlan 40

```