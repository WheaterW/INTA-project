info-center loghost source
==========================

info-center loghost source

Function
--------



The **info-center loghost source** command configures the source interface of the device through which information is output to a syslog server.

The **undo info-center loghost source** command cancels the settings about deletes the source interface of the device through which information is output to a syslog server.

The source interface of the information sent by a device is the interface on which the information is sent by default.



By default, the source interface is the interface that sends information from a device.


Format
------

**info-center loghost source** { *interface-name* | *interface-type* *interface-number* }

**undo info-center loghost source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If different source interfaces are configured for multiple devices, when these devices send information to the syslog server, the syslog server can determine the device from which the information is sent based on the source interface address. In this way, the syslog server can search for the received information.

**Prerequisites**



An IP address has been assigned to the source interface to be set.



**Precautions**

After a source interface is configured using this command, the source interface is automatically bound to the VPN to which the source interface belongs. When the VPN of the log host is the same as that of the source interface, the IP address of the source interface is used as the source address. When the VPN of the log host is different from that of the source interface, the IP address of the outbound interface is used as the source address.If an independent source IP address is configured for the log host, the source IP address of the log host is used.


Example
-------

# Configure the IP address of the interface loopback0 as the source interface address in information packets.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback 0
[*HUAWEI-loopback0] ip address 1.1.1.1 255.255.255.0
[*HUAWEI-loopback0] quit
[*HUAWEI] info-center loghost source loopback 0

```