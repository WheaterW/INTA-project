ip-dscp-outbound
================

ip-dscp-outbound

Function
--------



The **ip-dscp-outbound** command maps the PHB and color of outgoing IP packets in a DiffServ domain to the DSCP priority.

The **undo ip-dscp-outbound** command restores the default mapping.



For details about default mappings from the DSCP priorities to PHBs and colors of outgoing IP packets in a DiffServ domain, see "Default Settings for Priority Mapping" under "Priority Mapping Configuration" in Configuration Guide > QoS Configuration.


Format
------

**ip-dscp-outbound** *service-class* *color* **map** *dscp-value*

**undo ip-dscp-outbound** [ *service-class* *color* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *service-class* | Specifies a PHB. | The value can be BE, AF1 to AF4, EF, CS6, or CS7, each of which corresponds to queues 0 to 7 respectively. |
| *color* | Specify the color of the message mark. | The value can be green, yellow, or red. |
| **map** *dscp-value* | Specifies the DSCP priority of IP packets. | The value is an integer that ranges from 0 to 63. |



Views
-----

DiffServ domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After QoS scheduling is performed on the IP packets, you can use the ip-dscp-outbound command to map the PHB and color of IP packets in a DiffServ domain to the DSCP priority. After the DiffServ domain is bound to the outbound direction of the IP packets, the downstream device implements QoS scheduling according to the DSCP priority.

**Precautions**

If you do not specify the parameters service-class and colors when running the **undo ip-dscp-outbound** command, the default mappings from CoS values and colors to DSCP priorities are restored.


Example
-------

# In DiffServ domain ds1, map PHB AF1 of the outbound yellow IP packets to DSCP priority 8.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain ds1
[*HUAWEI-dsdomain-ds1] ip-dscp-outbound af1 yellow map 8

```