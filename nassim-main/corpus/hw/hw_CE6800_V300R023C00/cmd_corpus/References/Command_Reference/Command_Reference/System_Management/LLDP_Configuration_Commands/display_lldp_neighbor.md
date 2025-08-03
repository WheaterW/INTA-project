display lldp neighbor
=====================

display lldp neighbor

Function
--------



The **display lldp neighbor** command displays Link Layer Discovery Protocol (LLDP) neighbor information about a specific or all interfaces.




Format
------

**display lldp neighbor** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays LLDP neighbor information about a specified interface.  If this parameter is not specified, LLDP neighbor information about all interfaces is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view neighbor information on interfaces, run the display link neighbor command. The command output contains information about neighbors of a local device, the interfaces that the neighbors use to connect to the local device, and Layer 2 information about these neighbors. The command output helps check whether Layer 2 configurations of the neighbors are correct.



**Prerequisites**



LLDP has been globally enabled using the lldp enable command in the system view, and LLDP has also been enabled on interfaces using the lldp enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display LLDP neighbor information about all interfaces on a device.
```
<HUAWEI> display lldp neighbor
100GE1/0/1 has 1 neighbor(s):

Neighbor index                     :1
Chassis type                       :MAC Address
Chassis ID                         :d849-0b94-6501
Port ID subtype                    :Interface Name
Port ID                            :100GE1/0/1
Port description                   :--
System name                        :232.167                       
System description                 :Huawei Versatile Routing Platform Software
VRP (R) software, Version 8.191 (VRP )
Copyright (C) 2012-2016 Huawei Technologies Co., Ltd.
HUAWEI VRP

System capabilities supported      :bridge router
System capabilities enabled        :bridge router
Management address type            :IPv4
Management address                 :2.2.2.2
Expired time                       :96s

Port VLAN ID(PVID)                 :1
Port and Protocol VLAN ID(PPVID)   :unsupported         
VLAN name of VLAN 1                :VLAN1
Protocol identity                  :--
Auto-negotiation supported         :Yes 
Auto-negotiation enabled           :No 
OperMau                            :speed (10000) /duplex (Full)
Link aggregation supported         :Yes
Link aggregation enabled           :No
Aggregation port ID                :0
Maximum frame Size                 :9216
Port Identity                      :--
Discovered time                    :2016-12-26 09:15:43

Network Card ID                    :--

Unrecognized basic TLV
    TLV type 80                    :80 c2 03 22 22 01 32 00
    TLV type 90                    :90 c2 03 22 22 01 32 01

Unrecognized organizationally defined TLV
    TLV OUI                        : 01-02-02
    TLV subtype                    : 1
    Index                          : 1
    TLV information                : 0064
    TLV OUI                        : 01-02-02
    TLV subtype                    : 1
    Index                          : 2
    TLV information                : 0064
    TLV OUI                        : 01-02-02
    TLV subtype                    : 2
    Index                          : 1
    TLV information                : 0064
    TLV OUI                        : 01-02-03
    TLV subtype                    : 1
    Index                          : 1
    TLV information                : 0064
    TLV OUI                        : 01-02-03
    TLV subtype                    : 1
    Index                          : 2
    TLV information                : 005a
    TLV OUI                        : 01-02-04
    TLV subtype                    : 2
    Index                          : 1
    TLV information                : 0064

```

**Table 1** Description of the **display lldp neighbor** command output
| Item | Description |
| --- | --- |
| Neighbor index | Neighbor index. |
| Chassis type | ID subtype of a neighbor device:   * ChassisComponent: chassis alias. * interfaceAlias: interface alias. * portComponent: port/backplane alias. * macAddress: MAC address. * networkAddress: network address. * interfaceName: interface name. * local: local name. |
| Chassis ID | ID of an LLDP neighbor. |
| Port ID | ID of an LLDP neighbor interface. |
| Port description | Description of a neighboring interface. |
| Port VLAN ID(PVID) | ID of the VLAN to which a neighbor interface belongs. |
| Port and Protocol VLAN ID(PPVID) | ID of the protocol VLAN to which an LLDP neighbor interface belongs. |
| Port ID subtype | ID subtype of an LLDP neighbor interface:   * Interface Alias: interface alias. * Port Component: interface/backplane alias. * MAC Address: MAC address. * Network Address: network address. * Interface Name: interface name. * Agent Circuit Id: Circuit ID of a DHCP relay agent. * Local: local name. |
| Port Identity | Identity of a neighboring port. |
| System name | Name of a neighbor. |
| System description | Description of an LLDP neighbor. |
| System capabilities supported | Capabilities supported by an LLDP neighbor:   * other: other functions. * repeater: repeater function. * bridge: bridge device function. * wlanAccessPoint: wireless access point function. * router: router function. * telephone: wireless device function. * docsisCableDevice: management station function. * stationOnly: base station function. |
| System capabilities enabled | Capabilities enabled on an LLDP neighbor:   * other: other functions. * repeater: repeater function. * bridge: bridging function. * wlanAccessPoint: WLAN access point. * router: routing function. * telephone: wireless device function. * docsisCableDevice: management station function. * stationOnly: base station function. |
| Management address type | Management IP address type of an LLDP neighbor. |
| Management address | Management IP address of an LLDP neighbor. |
| Expired time | Aging time of an LLDP neighbor. |
| VLAN name of VLAN | Name of VLAN. |
| Protocol identity | Protocol type supported by the interface. |
| Auto-negotiation supported | Whether auto-negotiation is supported by a neighbor interface:   * Yes. * No. |
| Auto-negotiation enabled | Auto-negotiation status:   * Yes: Auto-negotiation is enabled. * No: Auto-negotiation is disabled. |
| OperMau | Self-adaptive rate and duplex status of a neighbor interface. |
| Link aggregation supported | Support for link aggregation by an LLDP neighbor interface:   * Yes: The LLDP neighbor interface supports link aggregation. * No: The LLDP neighbor interface does not support link aggregation. |
| Link aggregation enabled | Whether link aggregation is enabled on a neighbor interface:   * Yes: The function is enabled. * No: The function is disabled. |
| Aggregation port ID | Indicates the ID of an aggregation port. If the link aggregation function is not enabled, the value is 0. |
| Maximum frame Size | Maximum frame size supported by an LLDP neighbor interface. |
| Discovered time | Time when an LLDP neighbor is discovered. |
| Unrecognized basic TLV | Basic TLV unrecognized by the local end. |
| Unrecognized organizationally defined TLV | Organizationally defined TLV unrecognized by the local end. |
| TLV type | Basic TLV type unrecognized by the local end. |
| TLV OUI | Identifier of the organizationally defined TLV unrecognized by the local end. |
| TLV subtype | Sub-type of the organizationally defined TLV unrecognized by the local end. |
| TLV information | Information about the organizationally defined TLV unrecognized by the local end. |
| Network Card ID | Remote NIC ID. It is displayed as "--" if the packet sent from the peer end does not carry any NIC ID TLV. |
| Index | Index of the organizationally defined TLV unrecognized by the local end. |