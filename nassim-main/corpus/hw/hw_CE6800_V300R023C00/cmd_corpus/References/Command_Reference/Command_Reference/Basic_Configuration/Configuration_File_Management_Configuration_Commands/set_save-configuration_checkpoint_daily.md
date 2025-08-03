set save-configuration checkpoint daily
=======================================

set save-configuration checkpoint daily

Function
--------



The **set save-configuration checkpoint daily** command enables or sets the time for periodically generating configuration rollback points.

The **undo set save-configuration checkpoint daily** command disables the function of periodically generating configuration rollback points.



By default, the system does not periodically generate configuration rollback points.


Format
------

**set save-configuration checkpoint daily time** *time*

**undo set save-configuration checkpoint daily time** [ *time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **time** *time* | Specifies the time when configuration rollback points are automatically generated. | The value is in the hh:mm format. hh specifies the hour, which is an integer ranging from 0 to 23. mm specifies the minute, which is an integer ranging from 0 to 59. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enable the system to generate a configuration rollback point on each day, run the set save-configuration checkpoint daily command. The configuration rollback point files help perform device rollback.


Example
-------

# Set the time when configuration rollback points are periodically generated to 3:00.
```
<HUAWEI> system-view
[~HUAWEI] set save-configuration checkpoint daily time 3:00

```