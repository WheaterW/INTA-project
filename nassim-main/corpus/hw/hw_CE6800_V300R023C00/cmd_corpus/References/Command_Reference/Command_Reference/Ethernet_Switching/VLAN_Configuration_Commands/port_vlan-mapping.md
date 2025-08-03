port vlan-mapping
=================

port vlan-mapping

Function
--------



The **port vlan-mapping** command configures VLAN mapping on an interface.

The **undo port vlan-mapping** command deletes VLAN mapping on an interface.



By default, VLAN mapping is disabled on interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**port vlan-mapping vlan** *vlan-id1* **map-vlan** *vlan-id3* [ **remark-8021p** *8021p-value* ]

**port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* **map-vlan** *vlan-id3* [ **map-inner-vlan** *vlan-id4* ] [ **remark-8021p** *8021p-value* ]

**port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* **map-single-vlan** *vlan-id3*

**port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* **to** *vlan-id6* **map-vlan** *vlan-id3* [ **remark-8021p** *8021p-value* ]

**undo port vlan-mapping** { **vlan** *vlan-id1* [ **map-vlan** *vlan-id3* [ **remark-8021p** *8021p-value* ] ] }

**undo port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* [ **map-vlan** *vlan-id3* [ **map-inner-vlan** *vlan-id4* ] [ **remark-8021p** *8021p-value* ] ]

**undo port vlan-mapping all**

**undo port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* **map-single-vlan** *vlan-id3*

**undo port vlan-mapping vlan** *vlan-id1* **inner-vlan** *vlan-id5* **to** *vlan-id6* [ **map-vlan** *vlan-id3* ] [ **remark-8021p** *8021p-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id6* | Specifies the VLAN ID before mapping.  For double-tagged packets, this parameter specifies the end VLAN ID in the inner VLAN tag before mapping. | The value is an integer ranging from 1 to 4094. |
| **map-vlan** *vlan-id3* | Specifies the VLAN ID after mapping. | The value is an integer ranging from 1 to 4094. |
| **remark-8021p** *8021p-value* | Specifies the 802.1p priority in the VLAN tag to be mapped to.  If this parameter is specified, after a Layer 2 Ethernet interface receives tagged packets, it maps the VLAN tag of packets to a specified VLAN tag and uses the specified 802.1p priority.  If double-tagged packets are received, this parameter specifies the 802.1p priority in the outer VLAN tag to be mapped to. | The value is an integer ranging from 0 to 7. |
| **vlan** *vlan-id1* | Specifies a VLAN range carried in received frames.  lowVid specifies the start VLAN ID in received frames. | The value is an integer ranging from 1 to 4094. |
| **inner-vlan** *vlan-id5* | Specifies the VLAN ID before mapping.  For double-tagged packets, this parameter specifies the start inner VLAN ID before mapping. | The value is an integer ranging from 1 to 4094. |
| **map-inner-vlan** *vlan-id4* | Specifies the VLAN ID after mapping.  For double-tagged packets, this parameter specifies the inner VLAN ID after mapping. | The value is an integer ranging from 1 to 4094. |
| **map-single-vlan** *vlan-id3* | If double-tagged packets are received, this parameter specifies the single VLAN ID to be mapped to. | The value is an integer ranging from 1 to 4094. |
| **all** | Deletes all VLAN mapping configurations. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A network needs to be expanded with the growth of access users and data services, which poses the following challenges to the administrator:

* Existing and new sites assigned different VLAN IDs need to communicate.
* Inconsistent VLAN plans among sites access the public network causes VLAN ID conflicts. Therefore, VLANs at a site need to be isolated with those at another site.
* Sites that access to the public network have asymmetrical VLAN planning.To prevent these problems, you can run the **port vlan-mapping** command to configure VLAN mapping on edge devices of the public network to map the user VLAN tag to the public VLAN tag to implement inter-VLAN communication.

**Prerequisites**

The interface has been configured as a hybrid or trunk interface using the port link-type { hybrid | trunk } command.

**Configuration Impact**

VLAN mapping is implemented after packets are received on an inbound interface and before packets are sent out from an outbound interface. After VLAN mapping is enabled:

* Service VLAN IDs and user VLAN IDs change.
* Private network VLAN IDs and public network VLAN IDs change.

**Precautions**

When VLAN mapping is used to implement inter-VLAN communication, the IP addresses of the devices in the two VLANs must be on the same network segment. If the IP addresses of the devices in the two VLANs are not in the same network segment, Layer 3 routing is required for the devices to communicate with each other.


Example
-------

# Configure 2 to 2 VLAN mapping to map outer VLAN 100 and inner VLAN 200 of received packets to outer VLAN 10 and inner VLAN 20 before the packets are forwarded.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port link-type trunk
[~HUAWEI-100GE1/0/1] port vlan-mapping vlan 100 inner-vlan 200 map-vlan 10 map-inner-vlan 20

```

# Configure 2 to 1 VLAN mapping to map the outer VLAN ID 100 and inner VLAN IDs 200 to 300 of incoming packets to the outer VLAN ID 10 and transparently transmit the inner VLAN ID as data.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port link-type trunk
[~HUAWEI-100GE1/0/1] port vlan-mapping vlan 100 inner-vlan 200  to 300 map-vlan 10

```

# Configure 2 to 1 VLAN mapping to map outer VLAN 100 of received packets to outer VLAN 10 and retain inner VLAN 200 before the packets are forwarded.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port link-type trunk
[~HUAWEI-100GE1/0/1] port vlan-mapping vlan 100 inner-vlan 200 map-vlan 10

```

# Configure 2 to 1 VLAN mapping to map outer VLAN 200 and inner VLAN 100 of received packets to VLAN 20.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port link-type trunk
[~HUAWEI-100GE1/0/1] port vlan-mapping vlan 200 inner-vlan 100 map-single-vlan 20

```

# Configure 1 to 1 VLAN mapping to map VLAN 100 of received packets to VLAN 10 before the packets are forwarded.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port vlan-mapping vlan 100 map-vlan 10

```