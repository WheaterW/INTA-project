lldp management-address ipv6
============================

lldp management-address ipv6

Function
--------



The **lldp management-address ipv6** command configures an LLDP management IPv6 address.

The **lldp management-address ipv6 bind interface** command binds the LLDP management IPv6 address to a specified interface.



By default, no management IPv6 address is configured, and the management IPv6 address is not bound to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lldp management-address ipv6** *IPv6address*

**lldp management-address ipv6 bind interface** { *interface-type* *interface-number* | *interface-name* }

**undo lldp management-address ipv6** [ *IPv6address* ]

**undo lldp management-address ipv6 bind** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *IPv6address* | LLDP management IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *interface-type* | Specifies the type of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The management IPv6 address is carried in the management address TLV field of LLDP packets. It is used by the NMS to identify and manage devices. To allocate an IPv6 management address to a specified neighbor, run the **lldp management-address ipv6** command.



**Prerequisites**



The lldp enable command has been run in the system view to enable LLDP globally.



**Precautions**



Management address election:The management address configured using the lldp management-address ipv6 command has the highest priority. If no management address is configured and the lldp management-address ipv6 bind interface command is used to bind the management address to an interface, the interface address is preferentially selected as the management address. If the management address is not bound to an interface, the management address is selected based on the following algorithm:Management address selection method:The system preferentially selects the IPv6 address of a loopback interface, followed by the IPv6 address of a management interface and the IPv6 address of a VLANIF interface in turn. If there are multiple IPv6 addresses for the same type of interface, the system uses the smallest IPv6 address as the LLDP management IPv6 address.Management IPv4 and IPv6 addresses can coexist on a device, and they are selected independent. If the system fails to find a default address, the system uses the bridge MAC address as the LLDP management address. Currently, LLDP supports only global unicast IPv6 addresses.




Example
-------

# Bind the management IPv6 address to the interface.
```
<HUAWEI> system-view
[~HUAWEI] lldp management-address ipv6 bind interface 100GE 1/0/8

```

# Set the LLDP management IPv6 address of a device to 2001:db8:1::1, which is valid on the device.
```
<HUAWEI> system-view
[~HUAWEI] lldp management-address ipv6 2001:db8:1::1

```