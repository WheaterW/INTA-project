service-address
===============

service-address

Function
--------



The **service-address** command configures the local IP address of a device in an iNOF system.

The **undo service-address** command deletes the local IP address of a device in an iNOF system.



By default, no local IP address is configured for a device in an iNOF system.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**service-address** { *ip-address* | *ipv6-address* } [ **port-id** *port-id* ]

**undo service-address** { *ip-address* | *ipv6-address* } [ **port-id** *port-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the local IPv4 address of an iNOF device. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the local IPv6 address of an iNOF device. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **port-id** *port-id* | Specifies the port number used by the local device to transmit iNOF packets. | The value is an integer ranging from 10000 to 57999. The default value is 19516. All devices in an iNOF system must be configured with the same port number. |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You need to specify the local IP address and port number for a device in an iNOF system so that the device can transmit iNOF packets.

**Precautions**

* The IPv4 address of the local device cannot be set to a non-class A/B/C or loopback address.
* The IPv6 address of the local device cannot be set to a link-local address, multicast address, unspecified address, or loopback address.

Example
-------

# Set the local IP address to 2001:DB8:1::5 and port number to 10002 for a device in the iNOF system.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] service-address 2001:DB8:1::5 port-id 10002

```

# Set the local IP address to 192.168.1.5 and port number to 10002 for a device in an iNOF system.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] service-address 192.168.1.5 port-id 10002

```