storm suppression (vlan view)
=============================

storm suppression (vlan view)

Function
--------



The **storm suppression** command configures the maximum traffic rate in a VLAN.

The **undo storm suppression** command cancels the rate limit in a VLAN.



By default, the rate of broadcast, unknown multicast, or unknown unicast traffic is not limited in VLAN view.


Format
------

**storm suppression** { **broadcast** | **multicast** | **unknown-unicast** } **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ]

**undo storm suppression** { **broadcast** | **multicast** | **unknown-unicast** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **gbps** | Specifies the CIR in the unit of Gbit/s. | - |
| **kbps** | Specifies the CIR in the unit of kbit/s. | - |
| **mbps** | Specifies the CIR in the unit of Mbit/s. | - |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the committed volume of traffic that can pass through. | The value is an integer that ranges from 1 to 4294967295, in bytes. |
| **bytes** | Specifies the CBS in the unit of bytes. | - |
| **kbytes** | Specifies the CBS in the unit of kbytes. | - |
| **mbytes** | Specifies the CBS in the unit of Mbytes. | - |
| **broadcast** | Configures broadcast packet suppression. | - |
| **multicast** | Configures unknown multicast packet suppression. | - |
| **unknown-unicast** | Configures unknown unicast packet suppression. | - |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. | The value is an integer that ranges from 1 to 4294967295, in kbit/s. |



Views
-----

VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To rate-limit broadcast, unknown multicast, or unknown unicast packets in a VLAN and prevent broadcast storms, run this command in the VLAN view to configure traffic suppression for the corresponding type of packets. After this command is run, the device rate-limits broadcast, unknown multicast, or unknown unicast packets in the specified VLAN view and discards excess packets.


Example
-------

# Set the CIR to 100 kbit/s and CBS to 18800 bytes for upstream broadcast packets in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[~HUAWEI-vlan2] storm suppression broadcast cir 100 cbs 18800

```