netbios-type
============

netbios-type

Function
--------

The **netbios-type** command configures the NetBIOS node type for the DHCP client.

The **undo netbios-type** command deletes a configured NetBIOS node type.

By default, no NetBIOS node type for the DHCP client is configured.



Format
------

**netbios-type** { **b-node** | **h-node** | **m-node** | **p-node** }

**undo netbios-type**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **b-node** | Indicates a node in broadcast mode. A b-node obtains the mapping between host names and IP addresses in broadcast mode. | - |
| **h-node** | Indicates a node in hybrid mode. An h-node is a b-type node enabled with the end-to-end communication mechanism. | - |
| **m-node** | Indicates a node in mixed mode. An m-node is a p-type node with some broadcast features. | - |
| **p-node** | Indicates a node in peer-to-peer mode. A p-node obtains the mapping between host names and IP addresses by communicating with a NetBIOS server. | - |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. When a DHCP client uses NetBIOS for communication, its host name needs to be mapped to an IP address, and the NetBIOS node type needs to be specified for it using the **netbios-type** command. When a DHCP server assigns an IP address to clients, it also sends the specified NetBIOS node type to clients.

**Precautions**

To specify the NetBIOS node type for a client in the interface address pool, run the **dhcp server netbios-type** command.



Example
-------

# In the IP address pool view, set the NetBIOS node type for the DHCP client to b-node.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] netbios-type b-node

```