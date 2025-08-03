set license threshold
=====================

set license threshold

Function
--------



The **set license threshold** command sets an alarm threshold for a resource item registered in the system.

The **undo set license threshold** command restores the default alarm threshold of a resource item registered in the system.



The default alarm threshold of a resource item is 90%.


Format
------

**set license** *license-item* **threshold** *threshold-value*

**undo set license** *license-item* **threshold** [ *threshold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *license-item* | Specifies a resource item registered in the system. | The value is a string of 1 to 31 characters. |
| *threshold-value* | Specifies an alarm threshold for a resource item registered in the system.  When the usage of a resource item reaches the alarm threshold, an alarm is generated. The threshold can be calculated using the formula threshold-value/100. | The value is an integer ranging from 50 to 95, in percentage. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To flexibly set alarm thresholds for resource items, run the **set license threshold** command. You can be aware of resource usage in a timely manner to identify resource exhaustion risks in advance. You can run the **display license threshold** command to view the alarm thresholds of resource items registered in the system.

**Configuration Impact**

After the **set license threshold** command is run, the system performs scheduled detection based on the configured alarm threshold. When the usage of a resource item reaches the alarm threshold, the LCS\_1.3.6.1.4.1.2011.5.25.142.2.2 hwGtlResourceUsedUp alarm is generated.


Example
-------

# Set the alarm threshold of the LCRXXXX resource item to 80%.
```
<HUAWEI> system-view
[~HUAWEI] set license LCRXXXX threshold 80

```