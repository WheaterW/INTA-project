multicast-nat outbound
======================

multicast-nat outbound

Function
--------



The **multicast-nat outbound** command enables multicast flow translation on an outbound interface and configures multicast flow translation parameters.

The **undo multicast-nat outbound** command disables the multicast flow translation on an outbound interface and restores the initial parameters of multicast flows.



By default, the multicast flow conversion function is not configured on an outbound interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat outbound id** *outbound-id* [ **name** *outbound-name* ] [ **src-ip** *source-address* ] [ **dst-ip** *destination-address* ] [ **src-udp-port** *source-port* ] [ **dst-udp-port** *port* ]

**undo multicast-nat outbound id** *outbound-id* [ **name** *outbound-name* ] [ **src-ip** *source-address* ] [ **dst-ip** *destination-address* ] [ **src-udp-port** *source-port* ] [ **dst-udp-port** *port* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *outbound-name* | Specifies the name of an outbound interface for multicast flow translation. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |
| **src-ip** *source-address* | Specifies the post-translation source IP address of a multicast flow on an outbound interface. | The value ranges from 0.0.0.0 to 223.255.255.255, in dotted decimal notation. |
| **dst-ip** *destination-address* | Specifies the post-translation destination IP address of a multicast flow on an outbound interface. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **src-udp-port** *source-port* | Specifies the post-translation source port number of a multicast flow on an outbound interface. | The value is an integer ranging from 0 to 65535. |
| **dst-udp-port** *port* | Specifies the post-translation destination port number of a multicast flow on an outbound interface. | The value is an integer ranging from 0 to 65535. |
| **id** *outbound-id* | Specifies the multicast flow conversion ID on an outbound interface. | The value is an integer ranging from 1 to 16000. |



Views
-----

100GE interface view,25GE interface view,400GE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you need to convert the characteristics (source IP address, destination IP address, and destination UDP port number) of a multicast flow, you can specify the output multicast flow characteristics on the output interface of the multicast flow.

**Prerequisites**

Multicast NAT has been enabled globally using the **multicast-nat enable** command.

**Precautions**

The interface works in Layer 3 mode.The interface cannot be an Eth-Trunk member interface.


Example
-------

# Enable multicast stream translation on the outbound interface 100GE1/0/3.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] interface 100GE 1/0/3
[*HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] multicast-nat outbound id 1 name out1 src-ip 10.0.0.1 dst-ip 225.0.0.1 src-udp-port 20 dst-udp-port 100

```