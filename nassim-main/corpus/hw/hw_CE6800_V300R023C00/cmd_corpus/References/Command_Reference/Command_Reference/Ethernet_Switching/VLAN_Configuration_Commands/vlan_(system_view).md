vlan (system view)
==================

vlan (system view)

Function
--------



The **vlan** command creates a VLAN and displays the VLAN view. If the VLAN already exists, the VLAN view is displayed.

The **undo vlan** command deletes the VLAN.



By default, VLAN 1 exists.


Format
------

**vlan** *vlan-id*

**undo vlan** *vlan-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Specifies a VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To reduce broadcast domains and enhance security on a complex network, VLANs can be created on the network to isolate the devices that do not need to communicate with each other.

**Precautions**

The **vlan** command creates a VLAN and displays the VLAN view. If a VLAN has been created, the VLAN view is displayed after this command is used. If you run the **vlan** command more than once, all the created VLANs take effect. If a VLAN has been created, using this command does not create the same VLAN or modify the VLAN configuration. After a VLAN is created, both the vlan and vlan batch configurations exist in the configuration file.


Example
-------

# Create VLAN 2. If it already exists, display the VLAN 2 view.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2

```