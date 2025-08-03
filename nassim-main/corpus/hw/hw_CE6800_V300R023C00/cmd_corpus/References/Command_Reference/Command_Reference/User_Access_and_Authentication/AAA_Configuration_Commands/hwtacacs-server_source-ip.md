hwtacacs-server source-ip
=========================

hwtacacs-server source-ip

Function
--------

The **hwtacacs-server source-ip** command specifies the source IPv4 address used by a device to communicate with an HWTACACS server.

The **undo hwtacacs-server source-ip** command cancels the configuration.

By default, the device uses the IP address of the actual outbound interface as the source IP address of HWTACACS packets.



Format
------

**hwtacacs-server source-ip source-loopback** *interface-number*

**hwtacacs-server source-ip** *ip-address*

**hwtacacs-server source-ip source-vlanif** *interface-number1*

**undo hwtacacs-server source-ip**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IP address. | The value is in dotted decimal notation. |
| **source-vlanif** *interface-number1* | Specifies the IP address of a VLANIF interface as the source address for communication between the device and HWTACACS server. | The VLANIF interface must already exist. |
| **source-loopback** *interface-number* | Specifies the IP address of a loopback interface as the source address for communication between the device and HWTACACS server. | The loopback interface must exist. |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

You can configure all HWTACACS packets sent by the device to use the same source IPv4 address using the **hwtacacs-server source-ip** command. In this way, an HWTACACS server uses only one IPv4 address to communicate with the device.

If you run this command multiple times, only the latest configuration takes effect.

Example
-------

# Specify the source IPv4 address 10.1.1.1 for communication between the device and HWTACACS server.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server source-ip 10.1.1.1

```