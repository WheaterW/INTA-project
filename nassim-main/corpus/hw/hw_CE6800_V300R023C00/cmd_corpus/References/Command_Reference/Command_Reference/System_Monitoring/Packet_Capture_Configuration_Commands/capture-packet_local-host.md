capture-packet local-host
=========================

capture-packet local-host

Function
--------



The **capture-packet local-host** command configures a packet obtaining instance for the packets to be sent to a host.

The **undo capture-packet** command deletes a packet obtaining instance.



By default, no packet capture instance is configured for the packets to be sent to the host.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**capture-packet local-host** [ **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> ] [ **acl** { *acl-number* | **name** *acl-name* } | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* **destination** { **file** *filename* | **terminal** } [ **time-out** *time-value* | **packet-num** *number* | **packet-len** *length* ] \*

**capture-packet local-host** [ **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> ] [ **acl** **ipv6** { *acl-number2* | **name** *acl-name* } | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \* **destination** { **file** *filename* | **terminal** } [ **time-out** *time-value* | **packet-num** *number* | **packet-len** *length* ] \*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**undo capture-packet** [ *capture-index* ]

For CE6885-LL (low latency mode):

**capture-packet local-host** [ **interface** { *interface-type* *interface-number* | *interface-name* } &<1-4> ] [ **acl** { *acl-number* | **name** *acl-name* } | **vlan** *vlan-id* ] \* **destination** { **file** *filename* | **terminal** } [ **time-out** *time-value* | **packet-num** *number* | **packet-len** *length* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Obtains packets on a specified interface.   * interface-type: indicates the interface type. * interface-number: indicates the interface number. | The value is a string of 1 to 128 case-insensitive characters without spaces but with spaces between type and number. |
| *interface-name* | Obtains packets on a specified interface. | The value is a string of 1 to 128 case-insensitive characters without spaces. |
| **acl** | Configures an ACL. | - |
| **ipv6** | Configures an IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *acl-number2* | Obtains packets that match a specified ACL.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 2000 to 3999. |
| **name** *acl-name* | Creates an ACL with a name. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value must start with a letter or digit, and cannot contain only digits. |
| **vlan** *vlan-id* | Obtains packets from a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):For device models in low latency mode, the value can be changed using a command. The value is in the range from 1 to 1023. |
| **destination** | Indicates the destination to which obtained packet information is sent. | - |
| **file** *filename* | Saves obtained packet information to a file. The file name extension must be .cap. | The value is a string of 5 to 64 case-sensitive characters. It cannot contain spaces and paths. It cannot contain the following special characters: ~ ? \* \ : / | < > [ ]. |
| **terminal** | Displays information about the obtained packets on the terminal. | - |
| **time-out** *time-value* | Specifies the timeout period for obtaining packets. The device stops the packet capture instance when the timeout period expires. | The value is an integer ranging from 1 to 86400, in seconds. |
| **packet-num** *number* | Specifies the number of packets to be obtained. The device stops the packet capture instance when the specified number of packets are obtained. | The value is an integer in the range from 1 to 5000. The default value is 100. |
| **packet-len** *length* | Specifies the length of obtained packets to be displayed on the terminal or stored on the storage medium. | The value is an integer in the range from 20 to 64, in bytes. The default value is 64 bytes. |
| *acl-number* | Obtains packets that match a specified ACL. | The value is an integer that ranges from 2000 to 4999 . |
| **inner-vlan** *cvlan-id* | Obtains packets with a specified inner VLAN ID.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 4094. |
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

Devices on a network transmit various services, and network administrators often need to obtain packets on devices to locate faults. The device does not support the remote packet capture function; therefore, administrators need to obtain packets onsite by connecting a PC to the switch. If packets need to be obtained on an optical interface, an optical-to-electrical converter must be installed on the interface, reducing maintenance efficiency. Running the **capture-packet local-host** command can remotely obtain the packets to be sent to the CPU and analyze the obtained packets, to greatly improve maintenance efficiency and reduce maintenance cost.

**Precautions**

The following are constraints on obtaining packets to be sent to the CPU:If the ACL and VLAN parameters as well as the specified interfaces in an instance you want to configure are the same as those in an existing instance, the device considers that this instance has been enabled.If the file for storing obtained packets is deleted during packet obtaining, contents of subsequent packets cannot be written into the file.When configuring an instance for obtaining packets, note the following two points:The device can obtain packets of protocols sent to the CPU.You can set the timeout period specified by time and the number of obtained packets specified by number. If the timeout period for obtaining packets expires or the specified number of packets are obtained, the system stops obtaining packets.When the IPv4 ACL-based packet capture function is configured, the fragment flag cannot be matched.


Example
-------

# Obtain packets sent to the CPU on 100GE1/0/1, set the timeout period to 360s and number of packets to be obtained to 100.
```
<HUAWEI> capture-packet local-host interface 100GE 1/0/1 destination file capture1.cap time-out 360 packet-num 100
Warning: The capture packet may disclosure the personal information.
Warning: Capture-packet data will be saved to flash:/logfile/capture1.cap.

```