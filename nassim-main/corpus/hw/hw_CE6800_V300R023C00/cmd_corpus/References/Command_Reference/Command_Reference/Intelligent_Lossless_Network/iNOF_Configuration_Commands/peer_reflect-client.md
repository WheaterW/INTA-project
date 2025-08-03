peer reflect-client
===================

peer reflect-client

Function
--------



The **peer reflect-client** command specifies the IP address of a client on an iNOF reflector.

The **undo peer reflect-client** command deletes the IP address of a client from an iNOF reflector.



By default, no client IP address is specified on an iNOF reflector.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**peer** { *peer-address* | *peer-ipv6-address* } **reflect-client**

**undo peer** { *peer-address* | *peer-ipv6-address* } **reflect-client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IPv4 address of a client. | The value is in dotted decimal notation. |
| *peer-ipv6-address* | Specifies the IPv6 address of a client. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

iNOF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to specify the IP address of a client on an iNOF reflector. In this way, iNOF packets containing the zone management configuration can be transmitted between the iNOF reflector and client.

**Precautions**

* An iNOF reflector supports a maximum of 256 IPv4 client addresses and 256 IPv6 client addresses.
* The IPv4 address of a specified client cannot be set to a non-class A/B/C or loopback address.
* The IPv6 address of a specified client cannot be set to a link-local address, multicast address, unspecified address, or loopback address.

Example
-------

# Set the client IP address to 192.168.1.8 on an iNOF reflector.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] peer 192.168.1.8 reflect-client

```

# Set the client IP address to 2001:DB8:1::8 on an iNOF reflector.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] peer 2001:DB8:1::8 reflect-client

```