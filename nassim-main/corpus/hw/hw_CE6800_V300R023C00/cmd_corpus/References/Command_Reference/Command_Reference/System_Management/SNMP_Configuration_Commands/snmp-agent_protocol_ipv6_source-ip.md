snmp-agent protocol ipv6 source-ip
==================================

snmp-agent protocol ipv6 source-ip

Function
--------



The **snmp-agent protocol ipv6 source-ip** command specifies an IPv6 source address for SNMP to receive and respond to requests from an NMS.

The **undo snmp-agent protocol ipv6 source-ip** command restores the default configuration.

The **snmp-agent proxy protocol ipv6 source-ip** command specifies an IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU.

The **undo snmp-agent proxy protocol ipv6 source-ip** command restores the default configuration.



By default, no IPv6 source address is specified for SNMP to receive and respond to requests from an NMS. The function that allows all IPv6 addresses on the device to be used by SNMP to receive and respond to requests from an NMS is not enabled. No source interface is specified for SNMP to receive and respond to requests from an NMS. The function that allows all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS is not enabled. No source interface/IPv6 source address is specified for the SNMP proxy to receive and respond to requests from the CCU. The function that allows all interfaces or IPv6 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the CCU is not enabled.


Format
------

**snmp-agent protocol ipv6 source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**snmp-agent proxy protocol ipv6 source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo snmp-agent protocol ipv6 source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo snmp-agent proxy protocol ipv6 source-ip** *ip-address* [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 characters. It cannot contain spaces. |
| **source-ip** *ip-address* | Specifies an IPv6 source address for SNMP to receive and respond to requests from an NMS. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To specify an IPv6 source address for SNMP to receive and respond to requests from an NMS, run the **snmp-agent protocol ipv6 source-ip** command.To allow data to be managed in a unified manner, you can specify the IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU or configure the function that allows all IPv6 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the CCU.



**Precautions**



The **snmp-agent protocol ipv6 source-ip** command can be used to specify a maximum of 20 IPv6 source addresses for SNMP to receive and respond to requests from an NMS.The **snmp-agent proxy protocol ipv6 source-ip** command can be used to specify a maximum of 20 IPv6 source addresses for the SNMP proxy to receive and respond to requests from the CCU.




Example
-------

# Configure FC00::1 as the IPv6 source address for SNMP to receive and respond to requests from an NMS.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent protocol ipv6 source-ip FC00::1

```