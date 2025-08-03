controller-ipv6
===============

controller-ipv6

Function
--------



The **controller-ipv6** command specifies the controller IPv6 address used to establish an OpenFlow connection with the device and displays the Controller-IPv6 view.

The **undo controller-ipv6** command deletes the controller IPv6 address used to establish an OpenFlow connection with the device.



By default, the controller IPv6 address used to establish an OpenFlow connection with the device is not specified.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**controller-ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address*

**undo controller-ipv6** [ **vpn-instance** *vpn-instance-name* ] *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that the controller belongs to. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *ipv6-address* | Specifies the controller IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

SDN forwarder view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To allow the device and controller to communicate with each other through the OpenFlow connection, run the **controller-ipv6** command to specify the controller IPv6 address used to establish an OpenFlow connection with the device. After this command is executed, the Controller-IPv6 view is displayed.A device can connect to one or two controllers through OpenFlow connections. When the device connects to only one controller, the controller's IPv6 address needs to be reconfigured and the OpenFlow connection must be reset up, if the controller or OpenFlow connection fails. This process requires a long time. Establishing OpenFlow connections to multiple controllers improves reliability and implements load balancing. If one controller is faulty or an OpenFlow connection fails, the device is still connected to other controllers and works normally.


Example
-------

# Set the controller IPv6 address used to establish an OpenFlow connection with the device to 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] sdn agent
[*HUAWEI-sdn-agent] controller-ipv6 2001:db8:1::1

```