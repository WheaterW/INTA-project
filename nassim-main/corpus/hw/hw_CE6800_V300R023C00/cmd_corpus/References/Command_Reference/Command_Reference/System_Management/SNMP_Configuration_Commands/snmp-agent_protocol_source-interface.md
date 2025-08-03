snmp-agent protocol source-interface
====================================

snmp-agent protocol source-interface

Function
--------



The **snmp-agent protocol source-interface** command specifies a source interface for SNMP to receive and respond to requests from an NMS.

The **undo snmp-agent protocol source-interface** command restores the default configuration.

The **snmp-agent proxy protocol source-interface** command specifies a source interface for the SNMP proxy to receive and respond to requests from the CCU.

The **undo snmp-agent proxy protocol source-interface** command restores the default configuration.



By default, no source interface is specified for SNMP to receive and respond to requests from an NMS. The function that allows all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS is not enabled. No source interface is specified for the SNMP proxy to receive and respond to requests from the CCU. The function that allows all interfaces on the device to be used by the SNMP proxy to receive and respond to requests from the CCU is not enabled.


Format
------

**snmp-agent protocol source-interface** { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* }

**snmp-agent proxy protocol source-interface** { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* }

**undo snmp-agent protocol source-interface** { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* }

**undo snmp-agent proxy protocol source-interface** { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *protocol-interface-type* | Specifies the type of a source interface. | - |
| *protocol-interface-number* | Specifies the number of a source interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *protocol-interface-name* | Specifies the name of a source interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To specify a source interface for SNMP to receive and respond to requests from an NMS, run the **snmp-agent protocol source-interface** command.To allow data to be managed in a unified manner, you can specify the source interface for the SNMP proxy to receive and respond to requests from the CCU or configure the function that allows all interfaces on the device to be used by the SNMP proxy to receive and respond to requests from the CCU.



**Prerequisites**



The interface to be configured as the source interface must have been created, and a valid IP address must have been assigned to this interface. If the specified interface has not been configured, the **snmp-agent protocol source-interface** command fails to be run. If the specified interface has been created but no valid IP address is assigned to it, the command configuration does not take effect, but will take effect automatically after a valid IP address is assigned.



**Precautions**



snmp-agent protocol source-interface does not support interface association. That is, after the configured source interface is deleted or the IP address of the interface is deleted or changed, the NMS cannot communicate with the device through the original IP address of the interface.After the source interface bound to SNMP takes effect, SNMP listens only to this interface and does not receive or respond to request packets from other interfaces. The NMS uses only the IP address of the interface to communicate with the device. If the IP address of the interface changes, the NMS uses the new IP address of the interface to communicate with the device.The **snmp-agent protocol source-interface** command can be used to configure a maximum of 20 source interfaces for SNMP to receive and respond to NMS request packets.The **snmp-agent proxy protocol source-interface** command can be used to configure a maximum of 20 source interfaces for the SNMP agent to receive and respond to CCU packets.




Example
-------

# Configure loopback 1 as a source interface for SNMP to receive and respond to requests from an NMS.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] ip address 10.1.1.1 255.255.255.255
[*HUAWEI-LoopBack1] quit
[*HUAWEI] snmp-agent protocol source-interface loopback 1

```