ptp udp-egress
==============

ptp udp-egress

Function
--------

The **ptp udp-egress** command configures UDP encapsulation for 1588v2 packets sent by an interface and configures the destination MAC address, source IP address, and destination IP address for UDP-encapsulated 1588v2 packets.

The **undo ptp udp-egress** command restores the default UDP encapsulation on an interface.

By default, 1588v2 messages are encapsulated in multicast UDP mode.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp udp-egress source-ip** *source-ip* [ **destination-ip** *destination-ip* ]

**ptp udp-egress destination-mac** *destination-mac*

**ptp udp-egress source-ip** *source-ip* [ **dscp** *dscp* ] **vlan** *vlan-id* [ **priority** *priority-value* ]

**undo ptp udp-egress** { **source-ip** | **destination-ip** | **destination-mac** }

**undo ptp udp-egress** { **dscp** | **vlan** | **priority** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-ip** *source-ip* | Specifies a source IP address for UDP 1588v2 packets. | The value is in dotted decimal notation. |
| **destination-ip** *destination-ip* | Specifies a destination IP address for UDP 1588v2 packets. | The value is in dotted decimal notation. |
| **destination-mac** *destination-mac* | Specifies a destination MAC address for 1588v2 packets. | The value is in the format of H-H-H, where H is a 4-digit hexadecimal number. |
| **dscp** *dscp* | A DiffServ Code Point (DSCP) value for UDP-encapsulated 1588v2 packets. | The value is an integer ranging from 0 to 63. The default value is 56. |
| **vlan** *vlan-id* | VLAN ID that is encapsulated in the transmitted packets and identified in the receive packets. | The value is an integer ranging from 1 to 4094. |
| **priority** *priority-value* | The priority value for VLAN encapsulation packets. | The value is an integer ranging from 0 to 7. The default value is 7, indicating the highest priority. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

PTP packets can be encapsulated into Layer 2 and Layer 3 packets for transmission. Select the packet encapsulation type according to the actual networking environment, and configure the source and destination addresses and transmission priorities for packet transmission.

Before configuring the encapsulation mode of PTP packets, check the link type used for PTP packet transmission.

* For Layer 2 link transmission, run the **ptp mac-egress** command to configure the MAC encapsulation mode.
* For Layer 3 link transmission, run this command to select the UDP encapsulation mode.For unicast encapsulation, you can directly run this command to configure a destination MAC address for unicast encapsulation.

**Prerequisites**

1588v2 has been enabled on an interface using the **ptp enable** command.

**Precautions**

The higher the priority-value of multicast packets, the better the clock service. The higher the priority of multicast packets, the more timely the forwarding and processing, and the less the impact of delayed blocking of multicast packets on the clock recovery performance. The default value is the highest value and generally does not need to be changed.



Example
-------

# Encapsulate 1588v2 packets with the source IP address 192.168.2.2 and destination IP address 192.168.1.1 in UDP unicast mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp udp-egress  source-ip 192.168.2.2 destination-ip 192.168.1.1

```