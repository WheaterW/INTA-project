load-balance l2
===============

load-balance l2

Function
--------



The **load-balance l2** command configures a load balancing mode for Layer 2 packets.

The **undo load-balance l2** command deletes the specified load balancing mode or restores the default load balancing mode of Layer 2 packets.



By default, Layer 2 packets are load balanced based on src-mac, dst-mac, and vlan.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**load-balance l2** [ **vlan** | **src-mac** | **dst-mac** | **eth-type** | **src-interface** ] \*

**undo load-balance l2** [ **vlan** | **src-mac** | **dst-mac** | **eth-type** | **src-interface** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** | Configures an Eth-Trunk interface to load balance traffic based on the VLAN. | - |
| **src-mac** | Configures an Eth-Trunk interface to load balance traffic based on the source MAC address. | - |
| **dst-mac** | Configures an Eth-Trunk interface to load balance traffic based on the destination MAC address. | - |
| **eth-type** | Configures an Eth-Trunk interface to load balance traffic based on the protocol type. | - |
| **src-interface** | Configures an Eth-Trunk interface to load balance traffic based on the source port. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **load-balance l2** command to configure a load balancing mode for Layer 2 packets so that the device can obtain specified fields from Layer 2 packets for hash calculation to achieve even load balancing.


Example
-------

# Configure Eth-Trunk 1 to perform load balancing for Layer 2 packets based on dst-mac.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] load-balance l2 dst-mac

```