startup feature-software
========================

startup feature-software

Function
--------



The **startup feature-software** command configures feature packages for the next startup in batches.



By default, feature packages for next startup are specified in batches or separately.


Format
------

**startup feature-software** { *name* } &<1-9>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifying feature software. | The value is a string of 5 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In a feature software upgrade or downgrade scenario, you can run this command to configure the feature package for the next startup in batches.

**Follow-up Procedure**

Run the **reboot** command to restart the device.

**Precautions**

After specifying the feature software file for next startup, restart the device.The system must have been installed with a feature software file of the same feature.


Example
-------

# Specify the feature software to be configured for next startup.
```
<HUAWEI> startup feature-software V300R023C00-XXX_Feature1.ccx V300R023C00-XXX_Feature2.ccx
Info: Operating, please wait for a moment...........done.
Info: Succeeded in setting the software package for next startup.

```