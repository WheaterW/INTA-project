reset counters peak-rate interface
==================================

reset counters peak-rate interface

Function
--------



The **reset counters peak-rate interface** command clears the displayed peak rate and peak rate time of a specified physical interface and records the peak rate from the current measurement period.




Format
------

**reset counters peak-rate interface** { **all** | *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all interfaces. | - |
| *interface-type* | Specifies an interface type. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-num* | Specifies an interface number. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| **interface** *interface-name* | Specifies an interface. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The device saves the historical peak rates of interfaces. If the subsequent peak rates are all lower than the saved peak rates, the saved peak rates will not be updated. To obtain the subsequent peak rates, run the **reset counters peak-rate interface** command to reset the saved peak rates.


Example
-------

# Clear the peak rates of all interfaces.
```
<HUAWEI> system-view
[~HUAWEI] reset counters peak-rate interface all

```