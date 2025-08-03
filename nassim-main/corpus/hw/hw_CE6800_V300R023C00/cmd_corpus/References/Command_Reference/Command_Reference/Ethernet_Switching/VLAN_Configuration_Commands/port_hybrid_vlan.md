port hybrid vlan
================

port hybrid vlan

Function
--------



The **port hybrid vlan** command adds a hybrid port to an existing VLAN. Using the untagged/tagged command, you can specify whether the outgoing packets of a port carry VLAN tags.

The **undo port hybrid vlan** command deletes a hybrid port from a specified VLAN.



By default, a hybrid interface is added to a VLAN 1.


Format
------

**port hybrid tagged vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo port hybrid** [ **tagged** ] **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**port hybrid** { **tagged** | **untagged** } **vlan** **all**

**port hybrid untagged vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>

**undo port hybrid** [ **tagged** | **untagged** ] **vlan** **all**

**undo port hybrid** [ **untagged** ] **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the end VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **tagged** | Add a hybrid interface to a VLAN in tagged mode. | - |
| **untagged** | Add a hybrid interface to a VLAN in untagged mode. | - |
| **all** | Specifies all VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A hybrid interface can connect to either a host or a switching device. A hybrid interface allows tagged or untagged VLAN frames to pass.

* To allow a hybrid interface to send tagged VLAN frames, run the **port hybrid tagged vlan** command to add a hybrid interface to VLANs. When the hybrid interface sends frames from these VLANs, it does not remove the VLAN tags. This facilitates communication between switching devices.
* When a hybrid interface connects to a host, run the **port hybrid untagged vlan** command to configure the interface to send untagged frames because the host cannot process tagged frames.

**Prerequisites**

If the interface is not a hybrid interface, run the **port link-type** command to change the interface type to hybrid.

**Configuration Impact**

If the **port hybrid untagged vlan** command is run more than once on the same interface, all the configured VLANs take effect on the interface.

**Precautions**



The command cannot be configured on a physical interface that has been added to an Eth-Trunk interface.




Example
-------

# Add the hybrid interface 100GE1/0/1 to VLANs 2, 4, and 50 to 100. The hybrid interface removes these VLAN tags when sending the VLAN frames.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] port link-type hybrid
[*HUAWEI-100GE1/0/1] port hybrid untagged vlan 2 4 50 to 100

```