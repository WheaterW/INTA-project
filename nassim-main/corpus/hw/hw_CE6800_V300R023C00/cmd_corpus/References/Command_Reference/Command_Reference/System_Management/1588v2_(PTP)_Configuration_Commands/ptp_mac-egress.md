ptp mac-egress
==============

ptp mac-egress

Function
--------

The **ptp mac-egress** command configures MAC encapsulation for PTP packets (excluding transparently transmitted packets) to be sent from an interface.

The **undo ptp mac-egress** command restores the default configuration of MAC encapsulation on an interface.

By default, MAC encapsulation in multicast mode is used, with the priority value of 7 and no VLAN ID carried.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp mac-egress destination-mac** *destination-mac*

**ptp mac-egress vlan** *vlan-id* [ **priority** *priority-value* ]

**undo ptp mac-egress destination-mac**

**undo ptp mac-egress vlan** [ **priority** ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **destination-mac** *destination-mac* | Specifies a destination MAC address for 1588v2 messages. | The value is in H-H-H format, where H is a 4-digit hexadecimal number. |
| **vlan** *vlan-id* | VLAN ID that is encapsulated in the transmitted packets and identified in the receive packets. | The value is an integer ranging from 1 to 4094. |
| **priority** *priority-value* | Specifies the priority value for PTP packets. | The value is an integer that ranges from 0 to 7. The default value is 7, indicating the highest priority. |




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

* For Layer 2 link transmission, run this command to select the MAC encapsulation mode.
* For Layer 3 link transmission, run the **ptp udp-egress** command to configure the UDP encapsulation mode.For unicast encapsulation, you can directly run this command to configure a destination MAC address for unicast encapsulation.

**Prerequisites**

PTP has been enabled on an interface using the **ptp enable** command.

**Precautions**

The higher the priority-value of multicast packets, the better the clock service. The higher the priority of multicast packets, the more timely the forwarding and processing, and the less the impact of delayed blocking of multicast packets on the clock recovery performance. The default value is the highest value and generally does not need to be changed.



Example
-------

# Configure the unicast MAC encapsulation mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp mac-egress destination-mac 00e0-fc12-3456

```

# Configure the multicast MAC encapsulation mode.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp mac-egress vlan 1 priority 2

```