reset pm
========

reset pm

Function
--------



The **reset pm** command clears the performance statistics of a performance statistics task.




Format
------

**reset pm current-data** [ **instance-type** *instance-type-name* [ **measure** *measure-name* | **instance** { *vpn-instance-name* } &<1-8> ] \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **current-data** | Clears the current performance statistics of a performance statistics task. | - |
| **instance-type** *instance-type-name* | Specifies an instance type. The instance type is predefined for each feature. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |
| **measure** *measure-name* | Specifies the name of a performance counter in a performance statistics task. The performance counter is predefined for each feature. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |
| **instance** *vpn-instance-name* | Specifies an instance name of a specified instance type. The instance name format is predefined for each feature. | The value is a string of 1 to 255 case-insensitive characters. |



Views
-----

Statistics task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a large number of performance statistics have been generated, run the reset pm command to clear the current performance statistics.If no instance type, instance name, or performance counter is specified, the reset pm command clears all performance statistics.

**Precautions**

The performance statistics of a performance statistics task cannot be restored after they are cleared. Exercise caution when running this command.


Example
-------

# Clear all historical performance statistics.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[~HUAWEI-pm-statistics-huawei] reset pm current-data

```