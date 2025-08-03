ipv4 source address
===================

ipv4 source address

Function
--------



The **ipv4 source address** command specifies a source address and MTU for an open system.

The **undo ipv4 source address** command cancels the configuration.



By default, no open source address is specified. If only the source address is configured, the default MTU is 1500.


Format
------

**ipv4 source address** *sourceAddress* [ **mtu** *mtuValue* ]

**undo ipv4 source address** *sourceAddress*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mtu** *mtuValue* | Specifies the MTU used by an open system for external communication. | The value is an integer ranging from 68 to 9600. |
| **address** *sourceAddress* | Specifies the source address for openness. | The value is in dotted decimal notation. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

During communication between an open system and an external device or east-west communication on a device, you need to run this command to configure the source address. A maximum of eight source addresses can be configured.


Example
-------

# Set the source IP address to 10.1.1.1 and the MTU of this IP address to 1700.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ipv4 source address 10.1.1.1 mtu 1700

```