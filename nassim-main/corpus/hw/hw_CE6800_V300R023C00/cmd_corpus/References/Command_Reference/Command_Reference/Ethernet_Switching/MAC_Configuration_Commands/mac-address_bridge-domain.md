mac-address bridge-domain
=========================

mac-address bridge-domain

Function
--------



The **mac-address static bridge-domain** command configures a static MAC address entry based on a bridge domain (BD).

The **undo mac-address static bridge-domain** command deletes a static MAC address entry in a BD.



By default, no static MAC address entry is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-address static** *mac-address* { *interface-type* *interface-number* | *interface-name* } **bridge-domain** *bd-id* [ **vid** *pe-vid* ]

**undo mac-address** { *mac-address* **bridge-domain** *bd-id* | **bridge-domain** *bd-id* | **static** { **bridge-domain** *bd-id* | *mac-address* { *interface-type* *interface-number* | *interface-name* } **bridge-domain** *bd-id* } }

**undo mac-address static** *mac-address* { *interface-type* *interface-number* | *interface-name* } **bridge-domain** *bd-id* [ **vid** *pe-vid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a MAC address. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| *interface-type* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | - |
| **bridge-domain** *bd-id* | Specifies the ID of a bridge domain to which an outbound interface belongs. | The value is an integer ranging from 1 to 16777215. |
| **vid** *pe-vid* | Specifies the outer tag carried in packets that an outbound interface. receives. | The value is an integer ranging from 1 to 4094. |
| **static** *mac-address* | Indicates a static entry. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device learns MAC addresses and adds MAC address entries to a MAC address table, the device cannot identify whether packets are from authorized users or hackers, which brings security threats. If hackers spoof authorized users by changing the source MAC address of packets and access a device through different interfaces from authorized users' access interfaces, the device learns incorrect MAC address entries. As a result, the packets that should be forwarded to authorized users are forwarded to hackers.To improve interface security, run the **mac-address static bridge-domain** command to add a specified user MAC address to a MAC address table so that a user device is bound to a local device interface, which prevents hackers from accessing the local device and obtaining data.

**Configuration Impact**

The configured static MAC address entry cannot age. After a device receives a frame with the specified static MAC address, the device forwards the frame through the specified outbound interface. The configured static MAC address entry will not be lost even if the device is reset or a board on the device is hot swapped.

**Precautions**

The manually added MAC address entries (static MAC address entries) take precedence over automatically generated MAC address entries. Static MAC address entries cannot be overwritten by dynamic MAC address entries, but dynamic MAC address entries can be overwritten by static MAC address entries.


Example
-------

# Add a blackhole entry with MAC address 00e0-fc12-3456 to BD 10. When packets with destination MAC address 00e0-fc12-3456 and belonging to BD 10 are received, the packets are discarded.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] mac-address blackhole 00e0-fc12-3456 bridge-domain 10

```

# Enable a device to forward packets destined for MAC address 00e0-fc12-3456 through outbound interface 100GE1/0/1.1 in bridge domain 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] bridge-domain 10
[*HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 10
[*HUAWEI-100GE1/0/1.1] quit
[*HUAWEI] mac-address static 00e0-fc12-3456 100GE1/0/1.1 bridge-domain 10

```