trust upstream
==============

trust upstream

Function
--------



The **trust upstream** command applies a DiffServ domain.

The **undo trust upstream** command restores the default settings.



By default, the DiffServ domain default is applied.


Format
------

**trust upstream** { *ds-domain-name* | **none** }

**undo trust upstream**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ds-domain-name* | Specifies the name of a DiffServ domain. | The value must be the name of an existing DiffServ domain on the device. |
| **none** | Indicates that no DiffServ domain is applied, that is, packet priorities are not trusted. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Layer 2 sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To map priorities of incoming packets to PHBs and colors and map PHBs and colors of outgoing packets to priorities based on the mapping defined in a DiffServ domain, run this command to bind the DiffServ domain. The system performs PHB mapping based on the mapping in the DiffServ domain.To apply a DiffServ domain to multiple interfaces, you can perform the configuration on the port group to reduce the workload.

**Prerequisites**

A DiffServ domain has been created.

**Precautions**

* For the default mappings from 802.1p priorities to PHBs/colors, from PHBs/colors to 802.1p priorities, from DSCP priorities to PHBs/colors, from PHBs/colors to DSCP priorities, from DSCP priorities to internal DSCP priorities, and from internal DSCP priorities/colors to DSCP priorities, see the 8021p-inbound, 8021p-outbound, ip-dscp-inbound, and ip-dscp-outbound commands.
* If you run the **trust upstream** command multiple times in the same view, only the latest configuration takes effect.
* The trust upstream none and **qos phb marking 8021p disable** commands are mutually exclusive.
* The trust upstream none and **qos phb marking dscp enable** commands are mutually exclusive.
* When a packet arrives at a Layer 2 sub-interface, the local VTEP encapsulates the packet and transmits it through the VXLAN tunnel. The remote VTEP decapsulates the packet and sends it out through a Layer 2 sub-interface. After a DiffServ domain is applied to a Layer 2 sub-interface, the mapping rules for incoming packets on the Layer 2 sub-interface of the local VTEP and outgoing packets on the Layer 2 sub-interface of the remote VTEP are as follows:
* Layer 2 sub-interface of the default type:
* Inbound direction: If the trust 8021p { inner | outer } command is run on a Layer 2 sub-interface and packets do not carry VLAN tags, the device performs 802.1p mapping based on the priority configured using the **port priority priority-value** command on the main interface to which the Layer 2 sub-interface belongs and the DiffServ domain configured on the Layer 2 sub-interface. If packets carry VLAN tags, the device performs 802.1p mapping for the inner or outer 802.1p priority of packets and the DiffServ domain configured on the Layer 2 sub-interface. If trust dscp is configured on the Layer 2 sub-interface, the device performs DSCP mapping based on the DSCP priority of packets and the DiffServ domain configured on the Layer 2 sub-interface.
* Outbound direction: The device performs 802.1p or DSCP mapping based on the DiffServ domain configured on the outbound physical interface.
* Untagged Layer 2 sub-interface:
* Inbound direction: If the trust 8021p { inner | outer } command is run on a Layer 2 sub-interface, the device performs 802.1p mapping based on the priority configured using the **port priority priority-value** command on the main interface to which the Layer 2 sub-interface belongs and the DiffServ domain configured on the Layer 2 sub-interface. If trust dscp is configured on the Layer 2 sub-interface, the device performs DSCP mapping based on the DSCP priority of packets and the DiffServ domain configured on the Layer 2 sub-interface.
* Outbound direction: The device does not change the 802.1p priority of packets and performs DSCP mapping based on the DiffServ domain configured on the outbound physical interface.
* Dot1q Layer 2 sub-interface:
* Inbound direction: If the trust 8021p { inner | outer } command is run on a Layer 2 sub-interface, the device performs 802.1p mapping for the inner or outer 802.1p priority of packets and the DiffServ domain configured on the Layer 2 sub-interface. If trust dscp is configured on the Layer 2 sub-interface, the device performs DSCP mapping based on the DSCP priority of packets and the DiffServ domain configured on the Layer 2 sub-interface.
* Outbound direction: The device performs 802.1p or DSCP mapping based on the DiffServ domain configured on the outbound physical interface.
* QinQ Layer 2 sub-interface:
* Inbound direction: If the trust 8021p { inner | outer } command is run on the Layer 2 sub-interface, the device performs 802.1p mapping for the inner or outer 802.1p priority of packets and the DiffServ domain configured on the Layer 2 sub-interface. If trust dscp is configured on the Layer 2 sub-interface, the device performs DSCP mapping based on the DSCP priority of packets and the DiffServ domain configured on the Layer 2 sub-interface.
* Outbound direction: The device performs 802.1p or DSCP mapping based on the DiffServ domain configured on the outbound physical interface.


Example
-------

# Apply DiffServ domain ds1 to interface.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain ds1
[*HUAWEI-dsdomain-ds1] 8021p-inbound 7 phb be
[*HUAWEI-dsdomain-ds1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] trust upstream ds1

```