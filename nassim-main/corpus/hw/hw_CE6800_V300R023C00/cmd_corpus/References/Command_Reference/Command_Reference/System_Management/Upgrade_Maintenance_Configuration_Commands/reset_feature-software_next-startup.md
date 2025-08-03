reset feature-software next-startup
===================================

reset feature-software next-startup

Function
--------



The **reset feature-software next-startup** command deletes the feature package files to be used after the device restarts in batches.



By default, the feature packages that are started after the device restarts are cleared in batches or as specified.


Format
------

**reset feature-software next-startup** { *feature-file* } &<1-9>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *feature-file* | Specify the file name, in the format of [drive][path][file name]. | The value is a string of 5 to 127 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After running the **startup feature-software** command (in batches) to specify the feature package file for next startup, you can run the reset feature-software next-startup command (in batches) to clear the configuration.


Example
-------

# Clear the configuration of the feature package specified for the next startup.
```
<HUAWEI> reset feature-software next-startup XXX_Feature_a.ccx XXX_Feature_b.ccx
Info: Operating, please wait for a moment...done.
Info: Succeeded in clearing the feature package for next startup.

```