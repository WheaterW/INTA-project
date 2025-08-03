ip-dscp-inbound
===============

ip-dscp-inbound

Function
--------



The **ip-dscp-inbound** command maps the DSCP priority of incoming IP packets in a DiffServ domain to the PHB and colors the packets.

The **undo ip-dscp-inbound** command restores the default mapping.



For details about default mappings from the DSCP priorities to PHBs and colors of incoming IP packets in a DiffServ domain, see "Default Settings for Priority Mapping" under "Priority Mapping Configuration" in Configuration Guide > QoS Configuration.


Format
------

**ip-dscp-inbound** *dscp-value* **phb** *service-class* [ *color* ]

**undo ip-dscp-inbound** [ *dscp-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscp-value* | Specifies the DSCP priority of IP packets. | The value is an integer that ranges from 0 to 63. |
| **phb** *service-class* | Specifies a PHB. | The value can be BE, AF1 to AF4, EF, CS6, or CS7, each of which corresponds to queues 0 to 7 respectively. |
| *color* | Specify the color of the message mark. | The value can be:   * green * yellow * red   The default value is green. |



Views
-----

DiffServ domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To implement QoS scheduling for incoming IP packets carrying DSCP priorities, use the ip-dscp-inbound command to configure mappings from DSCP priorities of packets to PHBs and color the packets. After a DiffServ domain is bound to the inbound direction of packets, the device forwards the packets to queues based on PHBs of the packets. Congestion management is implemented. Packets are scheduled according to their colors after a discard template is configured, avoiding congestion.



**Precautions**

* The color is used to determine whether packets are discarded during congestion avoidance, and is independent of the mapping from PHBs to queues.
* The priorities of packets are mapped to the corresponding PHBs and the packets are colored accordingly. If no mapping from DSCP priorities to PHBs is specified, the device uses the default mappings of the system.
* If you do not specify the parameter dscp-value when running the **undo ip-dscp-inbound** command, all mappings from DSCP priorities to PHBs is restored.


Example
-------

# In DiffServ domain ds1, map DSCP priority 8 of the incoming IP packets to PHB AF1 and mark the packets yellow.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain ds1
[*HUAWEI-dsdomain-ds1] ip-dscp-inbound 8 phb af1 yellow

```