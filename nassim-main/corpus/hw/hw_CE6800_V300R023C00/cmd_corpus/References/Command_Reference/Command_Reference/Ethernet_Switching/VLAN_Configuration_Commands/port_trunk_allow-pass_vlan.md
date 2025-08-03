port trunk allow-pass vlan
==========================

port trunk allow-pass vlan

Function
--------



The **port trunk allow-pass vlan** command adds a trunk interface to a VLAN.

The **undo port trunk allow-pass vlan** command deletes a trunk interface from a VLAN.



By default, a trunk interface is added to a VLAN 1.


Format
------

**port trunk allow-pass vlan** { { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-40> } | **all** }

**undo port trunk allow-pass vlan** { { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-40> } | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vlan-id2* | Specifies the end VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer in the range from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
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

A trunk interface can be added to multiple VLANs and is generally used to connect network devices. If frames with one or more VLAN tags need to pass through a trunk interface, run the **port trunk allow-pass** command to add the trunk interface to the VLAN(s). In this manner, the trunk interface forwards these frames without removing the VLAN tags.

**Prerequisites**



An interface has been configured as a trunk interface using the **port link-type** command.



**Precautions**



The trunk interface to be added to VLANs must be a Layer 2 interface. If the interface is a Layer 3 interface, run the **portswitch** command to change the interface to a Layer 2 interface.If you run the **port trunk allow-pass** command more than once on the same interface, all the configured VLANs take effect on the interface.Running the **undo port trunk allow-pass vlan** command on an interface deletes the MAC address entries of the interface.




Example
-------

# Add the trunk interface 100GE1/0/1 to VLANs 2 to 10, 100, and 200.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 2 to 10 100 200

```