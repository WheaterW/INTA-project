l2 (Load balancing profile view)
================================

l2 (Load balancing profile view)

Function
--------



The **l2** command configures a load balancing mode of Layer 2 packets in a load balancing profile.

The **undo l2** command deletes the load balancing mode of Layer 2 packets or restores the default load balancing mode of Layer 2 packets.



By default, Layer 2 packets are load balanced based on src-mac, dst-mac, and vlan.


Format
------

**l2** [ **src-mac** | **dst-mac** | **src-interface** | **eth-type** | **vlan** ] \*

**undo l2** [ **src-mac** | **dst-mac** | **src-interface** | **eth-type** | **vlan** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **src-mac** | Performs load balancing based on source MAC addresses in Layer 2 packets. | - |
| **dst-mac** | Performs load balancing based on destination MAC addresses in Layer 2 packets. | - |
| **src-interface** | Performs load balancing based on physical-layer source port numbers in Layer 2 packets. | - |
| **eth-type** | Performs load balancing based on the protocol types of packets. | - |
| **vlan** | Performs load balancing based on vlan. | - |



Views
-----

Load balancing profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **undo l2** command with no parameter specified restores the default load balancing mode of Layer 2 packets. The **undo l2** command with a parameter specified deletes a specified load balancing mode of Layer 2 packets.

**Precautions**

If you run the l2 command multiple times, only the latest configuration takes effect.


Example
-------

# Configure load balancing for Layer 2 packets based on eth-type in the load balancing profile named a.
```
<HUAWEI> system-view
[~HUAWEI] load-balance profile a
[*HUAWEI-load-balance-profile-a] l2 eth-type

```