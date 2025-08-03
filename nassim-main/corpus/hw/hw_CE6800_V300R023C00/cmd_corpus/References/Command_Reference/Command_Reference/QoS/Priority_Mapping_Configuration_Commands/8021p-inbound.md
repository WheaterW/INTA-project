8021p-inbound
=============

8021p-inbound

Function
--------



The **8021p-inbound** command maps the 802.1p priority of incoming VLAN packets in a DiffServ domain to the PHB and colors the packets.

The **undo 8021p-inbound** command restores the default mapping.



For details about default mappings from the 802.1p priorities to PHBs and colors of incoming VLAN packets in a DiffServ domain, see "Default Settings for Priority Mapping" under "Priority Mapping Configuration" in Configuration Guide > QoS Configuration.


Format
------

**8021p-inbound** *8021p-value* **phb** *service-class* [ *color* ]

**undo 8021p-inbound** [ *8021p-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *8021p-value* | Specifies the 802.1p priority of VLAN packets. The value is an integer that ranges from 0 to 7. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority. |
| **phb** *service-class* | Specifies a PHB. | The value can be BE, AF1 to AF4, EF, CS6, or CS7, each of which corresponds to queues 0 to 7 respectively. |
| *color* | Indicates the color of packets. | The value can be green, yellow, and red. The default value is green. |



Views
-----

DiffServ domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To implement QoS scheduling on incoming VLAN packets, you can use the 8021p-inbound command to map the 802.1p priorities of the packets to the PHBs and colors. After a DiffServ domain is bound to the inbound direction of packets, the device forwards the packets to queues based on PHBs of the packets. Congestion management is implemented. Packets are scheduled according to their colors after a discard template is configured, avoiding congestion.



**Precautions**

* The color is used to determine whether packets are discarded during congestion avoidance, and is independent of the mapping from PHBs to queues.
* The priorities of packets are mapped to the corresponding PHBs and the packets are colored accordingly. If no mapping from 802.1p priorities to PHBs is specified, the device uses the default mappings of the system.
* If you do not specify the parameter 8021p-value when running the **undo 8021p-inbound** command, all the mapping between 802.1p priorities and PHBs is restored.


Example
-------

# In DiffServ domain ds1, map the 802.1p priority 2 of the incoming VLAN packets to PHB AF1 and mark the packets yellow.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain ds1
[*HUAWEI-dsdomain-ds1] 8021p-inbound 2 phb af1 yellow

```