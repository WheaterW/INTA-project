set configuration operation cpu-limit
=====================================

set configuration operation cpu-limit

Function
--------



The **set configuration operation cpu-limit** command reduces the rate to some extent in response to the CPU overhigh caused by NMS data collection.

The **undo set configuration operation cpu-limit** command deletes the threshold configured for CPU rate decreasing.



By default, no threshold is configured for CPU rate decreasing.


Format
------

**set configuration operation cpu-limit** { *percent-value* **access-type** **snmp** | *ncf-percent-value* **access-type** **netconf** }

**undo set configuration operation cpu-limit** [ { **access-type** **snmp** | **access-type** **netconf** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *percent-value* | Specifies a threshold for CPU rate decreasing in SNMP access mode. | The value is an integer ranging from 30 to 100. |
| **access-type** | Specifies a protocol access type. | - |
| **snmp** | Specifies the access type protocol is snmp. | - |
| *ncf-percent-value* | Specifies a threshold for CPU rate decreasing in NETCONF access mode. | The value is an integer ranging from 30 to 100. |
| **netconf** | Specifies the access type protocol is netconf. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Data collection by an NMS consumes many CPU resources. To ensure that other service runs properly, the device must reserve some resources for other services. To resolve this issue, run the set configuration operation cpu-limit command to configure a threshold for CPU rate decreasing. If the CPU usage reaches the configured threshold, the device reduces CPU resources allocated to the NMS when the NMS collects data. In this case, CPU pressure can be relieved to some extent.

**Precautions**



The default values of <percent-value> and <ncf-percent-value> are customized on the product side. You can run the **display this include-default** command to view the current default values.




Example
-------

# Set a threshold to 50 for CPU rate decreasing in SNMP access mode.
```
<HUAWEI> system-view
[~HUAWEI] set configuration operation cpu-limit 50 access-type snmp

```