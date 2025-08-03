ipv4 management-interface
=========================

ipv4 management-interface

Function
--------



The **ipv4 management-interface** command sets the address and MTU for the open system management interface.

The **undo ipv4 management-interface** command cancels the address and MTU settings for the open system management interface.



By default, no management interface address is configured for an open system.


Format
------

**ipv4 management-interface** { **address** *mgmtAddress* *mgmtMask* | **mtu** *mgmtMtu* }

**undo ipv4 management-interface** { **address** *mgmtAddress* *mgmtMask* | **mtu** *mgmtMtu* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **address** *mgmtAddress* | Specifies the address of a management interface. | The value is in dotted decimal notation. |
| *mgmtMask* | Specifies the mask of the management interface address. | The value is an integer ranging from 0 to 32. |
| **mtu** *mgmtMtu* | Specifies the MTU of a management interface. | The value is an integer ranging from 68 to 9600. |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command specifies the IP address and MTU of the management interface for the open system, so that third-party Linux applications can be managed through the management interface of the device.


Example
-------

# Set the MTU of the management interface to 9600.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ipv4 management-interface mtu 9600

```

# Set the IP address of the management interface to 10.0.0.1.
```
<HUAWEI> system-view
[~HUAWEI] oas enable
[*HUAWEI] oas
[*HUAWEI-oas] ipv4 management-interface address 10.0.0.1 24

```