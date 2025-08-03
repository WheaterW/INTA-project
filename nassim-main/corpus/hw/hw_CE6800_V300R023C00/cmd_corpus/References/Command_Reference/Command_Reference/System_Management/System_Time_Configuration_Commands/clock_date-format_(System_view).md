clock date-format (System view)
===============================

clock date-format (System view)

Function
--------



The **clock date-format** command sets the date format on a device.

The **undo clock date-format** command restores the default date format on a device.



By default, the date format of a device is YYYY-MM-DD.


Format
------

**clock date-format** { **YYYY-MM-DD** | **MM-DD-YYYY** }

**undo clock date-format**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **YYYY-MM-DD** | Indicates that the date format is YYYY-MM-DD, standing for year-month-day. | - |
| **MM-DD-YYYY** | Indicates that the date format is MM-DD-YYYY, standing for month-day-year. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To change the date format on a device, run the clock date-format command.


Example
-------

# Set the date format to MM-DD-YYYY.
```
<HUAWEI> system-view
[~HUAWEI] clock date-format MM-DD-YYYY

```