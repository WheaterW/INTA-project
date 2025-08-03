vxlan vni (Bridge domain view)
==============================

vxlan vni (Bridge domain view)

Function
--------



The **vxlan vni** command creates a VXLAN network identifier (VNI) and maps a VNI to a bridge domain (BD) in 1:1 mode.

The **undo vxlan vni** command deletes the mapping between a VNI and a BD.

The **vxlan vni split-group** command configures a mapping VNI to be associated with a BD and specifies the split horizon group (SHG) to which the mapping VNI belongs.

The **undo vxlan vni split-group** command restores the default configuration.



By default, no VNI is created and no mapping VNI is associated with a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan vni** *vni-id* [ **split-group** *split-group-name* ]

**undo vxlan vni** *vni-id* [ **split-group** *split-group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vni-id* | Specifies the VNI ID. | The value is an integer ranging from 1 to 16777215. |
| **split-group** *split-group-name* | Specifies the ID of the mapping VNI associated with the current BD. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A virtual network (VN) on a VXLAN is a virtual broadcast domain. To allow a BD to function as a VXLAN network entity to transmit VXLAN traffic, run the **vxlan vni** command to map a VNI to a BD in 1:1 mode.To implement Layer 2 communication between hosts in different DCs in a scenario where segment VXLAN is used, run the **vxlan vni split-group** command on transit leaf nodes (edge devices interconnecting the DCs) to configure a mapping VNI to be associated with the BD. The mapping VNI is used for the VXLAN tunnel between the DCs. After this configuration is complete, a transit leaf node replaces the VNI in VXLAN packets received within the DC with the mapping VNI. This configuration decouples the VNI space for a DC's network from the VNI space for the network between DCs and isolates faults.Additionally, to prevent loops when a transit leaf node forwards BUM traffic, the split horizon group to which the mapping VNI belongs must be specified, so that devices within a DC belong to the default SHG, and transit leaf nodes between DCs belong to the specified SHG. In this manner, when a transit leaf node receives BUM traffic, it does not forward traffic to a device belonging to the same SHG, therefore preventing loops.

**Precautions**

* The command is mutually exclusive with the port vlan exclude command.
* The VNI bound to a VPN instance cannot be bound to a BD.
* A peer-link interface and VNI (4095 x N â 1) (such as VNI 4094 and VNI 8189) cannot be configured on the same device.
* For the same mapping VNI, the split-group parameter must reference the SHG name configured using the vni head-end peer-list split-group or **peer split-group** command.


Example
-------

# Configure a mapping VNI to be associated with BD 10 and specify the SHG to which the mapping VNI belongs.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 30 split-group p

```

# Associate VNI 5000 with BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] vxlan vni 5000

```