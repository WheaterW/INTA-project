netstream mpls-aware ip
=======================

netstream mpls-aware ip

Function
--------



The **netstream mpls-aware ip** command configures the mode of sampling MPLS packets.

The **undo netstream mpls-aware ip** command restores the default settings.



By default, only the IP packets encapsulated in the MPLS packets are sampled.


Format
------

**netstream mpls-aware** { **label-only** | **ip-only** | **label-and-ip** } **ip**

**undo netstream mpls-aware** [ **label-only** | **ip-only** | **label-and-ip** ] **ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **label-only** | Indicates that only labels in the MPLS packets are sampled. | - |
| **ip-only** | Indicates that only the IP packets encapsulated in the MPLS packets are sampled. | - |
| **label-and-ip** | Indicates that both labels and IP packets encapsulated in the MPLS packets are sampled. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

On an MPLS network, MPLS labels are important information that users are concerned about. The device can sample MPLS labels. If this command is not executed, the device samples only IP packets encapsulated in the MPLS packets.Currently, only original flow statistics can be collected. Flexible flow statistics cannot be collected.


Example
-------

# Configure the device to sample only MPLS labels.
```
<HUAWEI> system-view
[~HUAWEI] netstream mpls-aware label-only ip

```