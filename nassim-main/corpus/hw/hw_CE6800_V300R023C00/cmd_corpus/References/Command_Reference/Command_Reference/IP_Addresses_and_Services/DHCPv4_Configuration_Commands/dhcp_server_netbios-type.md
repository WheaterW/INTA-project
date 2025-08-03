dhcp server netbios-type
========================

dhcp server netbios-type

Function
--------

The **dhcp server netbios-type** command specifies the NetBIOS node type for a DHCP client connecting to an interface.

The **undo dhcp server netbios-type** command deletes the specified NetBIOS node type of a DHCP client connecting to an interface.

By default, no NetBIOS node type is specified for a DHCP client connecting to an interface.



Format
------

**dhcp server netbios-type** { **b-node** | **h-node** | **m-node** | **p-node** }

**undo dhcp server netbios-type**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **b-node** | Indicates a node in broadcast mode. A b-node obtains the mapping in broadcast mode. | - |
| **h-node** | Indicates a node in hybrid mode. An h-node is a b-node enabled with the end-to-end communication mechanism. | - |
| **m-node** | Indicates a node in mixed mode. An m-node is a p-node with some broadcast features. | - |
| **p-node** | Indicates a node in peer-to-peer mode. A p-node obtains mappings by communicating with the NetBIOS server. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. When DHCP clients use NetBIOS on the WAN to communicate, their host names and IP addresses need to be mapped. You can run the **dhcp server netbios-type** command to configure the NetBIOS node type for an interface address pool. When assigning an IP address to the client, the DHCP server also sends the specified NetBIOS node type to the client.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

To specify the NetBIOS node type for a client in the global address pool, run the **netbios-type** command.



Example
-------

# Set the NetBIOS node type for a client in the address pool on
100GE
1/0/1 to p-node.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server netbios-type p-node

```