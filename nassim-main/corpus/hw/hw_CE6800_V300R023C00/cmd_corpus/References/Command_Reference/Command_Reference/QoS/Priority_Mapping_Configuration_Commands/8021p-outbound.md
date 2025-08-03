8021p-outbound
==============

8021p-outbound

Function
--------



The **8021p-outbound** command maps the PHB and color of outgoing VLAN packets in a DiffServ domain to the 802.1p priority.

The **undo 8021p-outbound** command restores the default mapping.



For details about default mappings from the PHBs and colors to 802.1p priorities of outgoing VLAN packets in a DiffServ domain, see "Default Settings for Priority Mapping" under "Priority Mapping Configuration" in Configuration Guide > QoS Configuration.


Format
------

**8021p-outbound** *service-class* *color* **map** *8021p-value*

**undo 8021p-outbound** [ *service-class* *color* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *service-class* | Specifies a PHB. | The value can be BE, AF1 to AF4, EF, CS6, or CS7, each of which corresponds to queues 0 to 7 respectively. |
| *color* | Indicates the color of packets. | The value can be green, yellow, and red. |
| **map** *8021p-value* | Specifies the 802.1p priority of VLAN packets. | The value is an integer that ranges from 0 to 7. A larger value indicates a higher priority. |



Views
-----

DiffServ domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After QoS scheduling is performed on VLAN packets, you can use the 8021p-outbound command to map the PHB and color of the packets in a DiffServ domain to the 802.1p priority. After the DiffServ domain is bound to the outbound direction of the VLAN packets, the downstream device implements QoS scheduling according to the 802.1p priority.

**Precautions**

If you do not specify the parameters service-class and color when running the **undo 8021p-outbound** command, the default mappings from PHBs and colors to 802.1p priorities are restored.


Example
-------

# In DiffServ domain ds1, map PHB AF1 of the outbound yellow VLAN packets to 802.1p priority 2.
```
<HUAWEI> system-view
[~HUAWEI] diffserv domain ds1
[*HUAWEI-dsdomain-ds1] 8021p-outbound af1 yellow map 2

```