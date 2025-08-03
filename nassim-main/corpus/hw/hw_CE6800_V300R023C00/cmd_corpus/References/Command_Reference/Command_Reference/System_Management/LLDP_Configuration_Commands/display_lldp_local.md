display lldp local
==================

display lldp local

Function
--------



The **display lldp local** command displays Link Layer Discovery Protocol (LLDP) information about a specific or all interfaces.




Format
------

**display lldp local** [ **interface** { *interface-name* | *ifType* *ifNum* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** | Specifies an interface. | - |
| *interface-name* | Specifies the interface name. | - |
| *ifType* | Specifies an interface type. | - |
| *ifNum* | Specifies an interface number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view statistics about neighbors learned by a local device and LLDP information on a local device, run the display lldp local command.If interface parameter is specified, displays LLDP information about a specified interface.If interface parameter is not specified, LLDP information about all interfaces is displayed.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display LLDP information about all interfaces on a device.
```
<HUAWEI> display lldp local
System information
--------------------------------------------------------------------------
Chassis type                       :MAC Address
Chassis ID                         :00e0-fc21-1220
System name                        :HUAWEI                        
System description                 :Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.191 (CE8800, 6800 V300R023C00)
Copyright (C) 2012-2015 Huawei Technologies Co., Ltd.
CE8800, 6800 V300R023C00

System capabilities supported      :bridge router 
System capabilities enabled        :bridge router 
LLDP Up time                       :2015/04/23 02:24:44

System configuration
--------------------------------------------------------------------------
LLDP Status                        :enabled              (default is disabled)         
LLDP Message Tx Interval           :15                   (default is 30s)              
LLDP Message Tx Hold Multiplier    :4                    (default is 4)                
LLDP Refresh Delay                 :3                    (default is 2s)               
LLDP Tx Delay                      :1                    (default is 2s)               
LLDP Notification Interval         :5                    (default is 5s)               
LLDP Notification Enable           :enabled              (default is enabled)          
Management Address                 :IPv4: 1.2.3.4                                
LLDP Fast Message Count            :3                    (default is 4)                

Remote Table Statistics:
--------------------------------------------------------------------------
Remote Table Last Change Time      :5 days,1 hours, 06 minutes,50 seconds
Remote Neighbors Added             :1
Remote Neighbors Deleted           :0
Remote Neighbors Dropped           :0
Remote Neighbors Aged              :0
Total Neighbors                    :1

Port information:
--------------------------------------------------------------------------
Interface 100GE1/0/8:
LLDP Enable Status                 :txAndRx              (default is disabled)
Total Neighbors                    :1

Port ID subtype                    :interfaceName
Port ID                            :100GE1/0/1
Port description                   :HUAWEI, 100GE1/0/8 Interface

Port and Protocol VLAN ID(PPVID)   :unsupported
Port VLAN ID(PVID)                 :1
VLAN name of VLAN 1                :1
Protocol identity                  :LACP 
Auto-negotiation supported         :Yes 
Auto-negotiation enabled           :No 
OperMau                            :speed (10000) /duplex (Full)
Link aggregation supported         :Yes
Link aggregation enabled           :No
Aggregation port ID                :0
Maximum frame Size                 :9216
Port Identity                      :abc

```

**Table 1** Description of the **display lldp local** command output
| Item | Description |
| --- | --- |
| System information | Information about a local device. |
| System name | Name of a local device. |
| System description | Description of a local device. |
| System capabilities supported | Capabilities supported by a local device:   * other: other functions. * repeater: repeater function. * bridge: bridging function. * wlanAccessPoint: WLAN access point. * router: routing function. * telephone: wireless device function. * docsisCableDevice: management station function. * stationOnly: base station function. |
| System capabilities enabled | Capabilities enabled on a local device:   * other: other functions. * repeater: repeater function. * bridge: bridging function. * wlanAccessPoint: WLAN access point. * router: routing function. * telephone: wireless device function. * docsisCableDevice: management station function. * stationOnly: base station function. |
| System configuration | Configuration of a local device. |
| Chassis type | ID subtype of a local device:   * ChassisComponent: chassis alias. * interfaceAlias: interface alias. * portComponent: interface/backplane alias. * macAddress: MAC address. * networkAddress: network address. * InterfaceName: interface name. * local: local name. |
| Chassis ID | Chassis ID of a local device. |
| LLDP Up time | Date and time when LLDP was enabled on a local device. |
| LLDP Status | LLDP status on the local device:   * Enabled. * Disabled. |
| LLDP Message Tx Interval | Interval (in seconds) at which LLDP packets are sent. |
| LLDP Message Tx Hold Multiplier | Time multiplier of local device information held on neighboring nodes. |
| LLDP Refresh Delay | Delay for initializing LLDP on interfaces of a local device. |
| LLDP Tx Delay | Delay (in seconds) for sending LLDP packets on a local device. |
| LLDP Notification Interval | Delay (in seconds) for sending alarms about neighbor information changes from a local device to an NMS. |
| LLDP Notification Enable | LLDP notification status on the local device:   * Enabled. * Disabled. |
| LLDP Fast Message Count | Number of LLDP packets quickly sent by the local device to neighbors. |
| LLDP Enable Status | LLDP status on a local interface:   * txOnly: LLDP packets can only be received. * rxOnly: LLDP packets can only be sent. * txAndRx: LLDP packets can be sent and received. * disabled: LLDP is not enabled. |
| Management Address | Management IP address of the local device. |
| Remote Table Statistics | Statistics about LLDP neighbors. |
| Remote Table Last Change Time | Time that has elapsed since the data on an LLDP neighbor is last changed. |
| Remote Neighbors Added | Number of added LLDP neighbors. |
| Remote Neighbors Deleted | Number of deleted LLDP neighbors. |
| Remote Neighbors Dropped | Number of LLDP neighbors dropped due to insufficient memory. |
| Remote Neighbors Aged | Number of LLDP neighbors deleted due to aged information. |
| Total Neighbors | Total number of LLDP neighbors. |
| Port information | Information about a local interface. |
| Port ID subtype | ID subtype of a local interface:   * interfaceAlias: interface alias. * portComponent: interface/backplane alias. * macAddress: MAC address. * networkAddress: network address. * InterfaceName: interface name. * agentCircuitId: circuit ID of a DHCP relay agent. * local: local name. |
| Port ID | ID of a local interface. |
| Port description | Description of a local interface. |
| Port and Protocol VLAN ID(PPVID) | ID of the protocol VLAN to which a local interface belongs. |
| Port VLAN ID(PVID) | ID of the VLAN to which a local interface belongs. |
| Port Identity | Identity of a local port. |
| Port and Protocol VLAN supported | Whether protocol VLANs are supported. |
| Port and Protocol VLAN enabled | Whether protocol VLANs are enabled. |
| Protocol identity | Protocol type supported by the interface. |
| VLAN name of VLAN | VLAN name. |
| Auto-negotiation supported | Support for auto-negotiation:   * Yes: Auto-negotiation is supported. * No: Auto-negotiation is not supported. |
| Auto-negotiation enabled | Auto-negotiation status:   * Yes: Auto-negotiation is enabled. * No: Auto-negotiation is disabled. |
| OperMau | Self-adaptive rate and duplex status of a local interface. |
| Link aggregation supported | Support for link aggregation by a local interface:   * Yes: The local interface supports link aggregation. * No: The local interface does not support link aggregation. |
| Link aggregation enabled | Link aggregation status on a local interface:   * Yes: Link aggregation is enabled. * No: Link aggregation is disabled. |
| Aggregation port ID | ID of an aggregated interface.  Value 0 indicates that link aggregation is not enabled. |
| Maximum frame Size | Maximum frame size supported by a local interface. |