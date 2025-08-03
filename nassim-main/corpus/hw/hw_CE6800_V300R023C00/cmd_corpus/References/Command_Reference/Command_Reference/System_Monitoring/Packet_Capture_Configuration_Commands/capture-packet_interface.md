capture-packet interface
========================

capture-packet interface

Function
--------



The **capture-packet interface** command configures an instance for obtaining hardware-forwarded packets.

The **undo capture-packet** command deletes an instance for obtaining hardware-forwarded packets.



By default, no instance for obtaining hardware-forwarded packets is configured.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**capture-packet** { { **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> } | { **acl** { *acl-number* | **name** *acl-name* } } } \* [ **vxlan** [ **vni** *vni-id* ] | [ **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* ] [ **clear** **payload** ] **destination** { **file** *filename* | **terminal** } [ **time-out** *time* | **packet-num** *number* | **packet-len** *length* ] \* [ **inbound** | **outbound** ]

**capture-packet** { { **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> } | { **acl** **ipv6** { *acl-number2* | **name** *acl-name* } } } \* [ **vxlan** [ **vni** *vni-id* ] | [ **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* ] [ **clear** **payload** ] **destination** { **file** *filename* | **terminal** } [ **time-out** *time* | **packet-num** *number* | **packet-len** *length* ] \* [ **inbound** | **outbound** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**undo capture-packet** [ *capture-index* ]

For CE6885-LL (low latency mode):

**capture-packet** { { **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> } | **acl** { *acl-number* | **name** *acl-name* } } \* [ **vlan** *vlan-id* ] \* [ **clear** **payload** ] **destination** { **file** *filename* | **terminal** } [ **time-out** *time* | **packet-num** *number* | **packet-len** *length* ] \* **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Obtains packets on a specified interface.   * interface-type: indicates the interface type. * interface-number: indicates the interface number. | - |
| *interface-name* | Obtains·packets·on·a·specified·interface. | - |
| **acl** | Configures an ACL. | - |
| **ipv6** | Configures an IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *acl-number2* | Obtains packets that match a specified ACL.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 2000 to 3999. |
| **name** *acl-name* | Creates an ACL with a name. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| *acl-number* | Obtains packets that match a specified ACL. | The value is an integer ranging from 2000 to 4999. |
| **vlan** *vlan-id* | Obtains packets from a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value can be changed from 1 to 1023 using commands. |
| **inner-vlan** *cvlan-id* | Obtains packets with a specified inner VLAN ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |
| **clear** | Sets the data content in obtained packets to 0.  The data content of only the TCP and UDP packets can be set to 0. | - |
| **payload** | Indicates the data content in obtained packets. | - |
| **destination** | Indicates the destination to which obtained packet information is sent. | - |
| **file** *filename* | Saves obtained packet information to a file. The file name extension must be .cap. | The value is a string of 5 to 64 case-sensitive characters. It cannot contain spaces and paths. It cannot contain the following special characters: ~ ? \* \ : / | < > [ ]. |
| **terminal** | Displays information about the obtained packets on the terminal. | - |
| **time-out** *time* | Specifies the timeout period for obtaining packets. The device stops the packet capture instance when the timeout period expires. | The value is an integer that ranges from 1 to 86400, in seconds. The default value is 60 seconds. |
| **packet-num** *number* | Specifies the number of packets to be obtained. The device stops the packet capture instance when the specified number of packets are obtained. | The value is an integer in the range from 1 to 5000. The default value is 100. |
| **packet-len** *length* | Specifies the length of obtained packets to be displayed on the terminal or stored on the storage medium. | The value is an integer ranging from 20 to 64, in bytes. The default value is 64 bytes. (After the packet capture feature package is installed, the value is in the range from 20 to 9500, and the default value is still 64 bytes.) |
| **inbound** | Obtains incoming packets. | - |
| **outbound** | Obtains outgoing packets.  If inbound and outbound are not specified, the device obtains packets in both directions by default.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vxlan** | Obtains packets from a specified VXLAN.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vni** *vni-id* | Specifies the VNI ID of the VXLAN.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |
| *capture-index* | Deletes the packet capture instance with a specified index. | The value is an integer ranging from 1 to 8. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an exception occurs when the hardware forwards traffic, for example, the traffic status does not match the traffic model, you are advised to configure the device to obtain hardware-forwarded packets for analysis. In this way, you can process invalid packets in a timely manner to ensure correct transmission of network data.When configuring parameters for packet capture, set the parameter values based on the traffic volume on the target interface. If the interface forwards many packets, specify a small value for the time parameter and a large value for the number parameter. If the interface forwards a few packets, specify a large value for the time parameter and a small value for the number parameter.

**Precautions**

* After the function of hardware-forwarded packet obtaining is configured, the device performance may be affected. Therefore, exercise caution when using this function.
* You can set parameters such as time (timeout period) and number (number of captured packets) for a packet obtaining instance. If the specified timeout time expires or the device obtains the specified number of packets, the device stops obtaining packets.
* If the packet saving file is deleted during packet obtaining, subsequent packet contents cannot be written into the file.
* When IPv4 ACLs are configured to obtain packets, fragment flags cannot be matched.

Example
-------

# Obtain packets on 100GE1/0/1 matching ACL 2000 and save obtained packet information in the capture.cap file.
```
<HUAWEI> capture-packet interface 100GE 1/0/1 acl 2000 destination file capture.cap

```