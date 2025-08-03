rollback configuration
======================

rollback configuration

Function
--------



The **rollback configuration** command rolls the system configuration back to a preceding configuration.




Format
------

**rollback configuration** { **to** **commit-id** *commit-id* | **last** *number-of-commits* | **to** **label** *label* | **to** **file** *file-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** | The system will be rolled back to the configurations when the configuration rollback point is generated. | - |
| **commit-id** *commit-id* | Specifies the ID of the configuration rollback point to which the system configuration is expected to roll back. | The value is an integer that is generated automatically and ranging from 1000000001 to 1999999999, the value of periodical configuration rollback point is ranging from 2000000001 to 2999999999. |
| **last** *number-of-commits* | Specifies the number of the last configuration rollback point to which the system rolls back. | The value is an integer ranging from 1 to 80. |
| **label** *label* | Specifies a user label for a configuration rollback point. A specified user label indicates the historical configuration state to which the system configuration is expected to roll back. | The value is a string of 1 to 256 case-sensitive characters. It can be any visible ASCII character except for the space. However, the string can contain spaces if it is enclosed with double quotation marks (" "). The string cannot start with a digit or be a hyphen (-). |
| **file** *file-name* | Rolls back the current configuration to the configuration in the specified configuration file. After the rollback, the configuration on the device is the same as that in the specified configuration file. | The value is a string of 5 to 64 case-sensitive characters in the format of \*.zip, \*.cfg, or \*.dat, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When an error occurs or the configuration procedure has an unexpected impact on services, run the **rollback configuration** command to roll the system configuration back to a specified configuration.Assume that a user has committed four configurations and four consecutive rollback points (A, B, C, and D) are generated. If an error is found in configurations committed at rollback point B and the system must be rolled back, configuration rollback allows the system to roll back to the configurations at rollback point A. Additionally, configuration rollback point E is generated and specially marked with a Rollback flag, indicating that this point is generated because of configuration rollback.If a configuration rollback error is detected, system configurations can be rolled back to what they were before the configuration rollback operation was performed and the new configuration rollback point is specially marked.


Example
-------

# Roll the system configuration back to configuration rollback label test.
```
<HUAWEI> rollback configuration to label test
Warning: This operation will revert configuration changes to the previous status. During the rollback configuration process, some configurations involving differences may be temporarily invalid. Continue? [Y/N]:y
Checking changes...
Loading rollback changes
Committing
Check rollback result
Configuration rollback succeeded.
Please use 'display configuration commit changes last 1' to view the changes.

```

# Roll back the system to the historical configuration state of the test.cfg file.
```
<HUAWEI> rollback configuration to file test.cfg
Warning: This operation will revert configuration changes to the file test.cfg. During the rollback configuration process, some configurations involving differences may be temporarily invalid. The time required for this operation depends on the configuration delivery time and configuration difference amount. If the configuration difference amount is large, this operation will take a long time. Continue? [Y/N]:y
Checking changes...
Loading rollback changes
Committing
Check rollback result
Configuration rollback succeeded.
Please use 'display configuration commit changes last 1' to view the changes.

```