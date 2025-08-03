snmp-agent protocol source-status all-interface
===============================================

snmp-agent protocol source-status all-interface

Function
--------



The snmp-agent protocol ipv6 source-ip command specifies an IPv6 source address for SNMP to receive and respond to requests from an NMS.

The undo snmp-agent protocol ipv6 source-ip command restores the default configuration.

The snmp-agent protocol source-status ipv6 all-interface command allows all IPv6 addresses on the device to be used by SNMP to receive and respond to requests from an NMS.

The undo snmp-agent protocol source-status ipv6 all-interface command restores the default configuration.

The snmp-agent protocol source-interface command specifies a source interface for SNMP to receive and respond to requests from an NMS.

The undo snmp-agent protocol source-interface command restores the default configuration.

The snmp-agent protocol source-status all-interface command allows all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS.

The undo snmp-agent protocol source-status all-interface command restores the default configuration.

The snmp-agent proxy protocol source-interface command specifies a source interface for the SNMP proxy to receive and respond to requests from the CCU.

The undo snmp-agent proxy protocol source-interface command restores the default configuration.

The snmp-agent proxy protocol source-status all-interface allows all interfaces on the device to be used by the SNMP proxy to receive and respond to requests from the CCU.

The undo snmp-agent proxy protocol source-status all-interface command restores the default configuration.

The snmp-agent proxy protocol ipv6 source-ip command specifies an IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU.

The undo snmp-agent proxy protocol ipv6 source-ip command restores the default configuration.

The snmp-agent proxy protocol source-status ipv6 all-interface allows all IPv6 source addresses on the device to be used by the SNMP proxy to receive and respond to requests from the CCU.

The undo snmp-agent proxy protocol source-status ipv6 all-interface restores the default configuration.



By default, no IPv6 source address is specified for SNMP to receive and respond to requests from an NMS. The function that allows all IPv6 addresses on the device to be used by SNMP to receive and respond to requests from an NMS is not enabled. No source interface is specified for SNMP to receive and respond to requests from an NMS. The function that allows all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS is not enabled. No source interface/IPv6 source address is specified for the SNMP proxy to receive and respond to requests from the CCU. The function that allows all interfaces or IPv6 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the CCU is not enabled.


Format
------

**snmp-agent protocol source-status** [ **ipv6** ] **all-interface**

**snmp-agent proxy protocol source-status** [ **ipv6** ] **all-interface**

**undo snmp-agent protocol source-status** [ **ipv6** ] **all-interface**

**undo snmp-agent proxy protocol source-status** [ **ipv6** ] **all-interface**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To allow all IPv6 addresses on the device to be used by SNMP to receive and respond to requests from an NMS, run the **snmp-agent protocol source-status ipv6 all-interface** command.To allow all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS, run the **snmp-agent protocol source-status all-interface** command.To allow data to be managed in a unified manner, you can specify the source interface/IPv6 source address for the SNMP agent to receive and respond to requests from the CCU or configure the function that allows the SNMP agent to receive and respond to any CCU IPv4/IPv6 packets.



**Precautions**



After the **snmp-agent protocol source-status ipv6 all-interface** command is run, all IPv6 addresses on the device can be used by SNMP to receive and respond to requests from an NMS, which brings security risks. Therefore, a risk message will be displayed when you run the **snmp-agent protocol source-status ipv6 all-interface** command.After the **snmp-agent protocol source-status all-interface** command is run, all interfaces on the device can be used by SNMP to receive and respond to requests from an NMS, which brings security risks. Therefore, a risk message will be displayed when you run the **snmp-agent protocol source-status all-interface** command.A risk message will be displayed when you run the **snmp-agent proxy protocol source-status all-interface** command.A risk message will be displayed when you run the **snmp-agent proxy protocol source-status ipv6 all-interface** command.




Example
-------

# Enable the function that allows all IPv6 addresses on the device to be used by SNMP to receive and respond to requests from an NMS.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent protocol source-status ipv6 all-interface
Warning: It will allow all accessible network to access the device.

```