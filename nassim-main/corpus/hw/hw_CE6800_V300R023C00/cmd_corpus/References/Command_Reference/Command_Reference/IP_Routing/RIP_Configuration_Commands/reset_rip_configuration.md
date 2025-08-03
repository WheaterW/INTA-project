reset rip configuration
=======================

reset rip configuration

Function
--------



The **reset rip configuration** command resets the configuration parameters of the specific RIP process. When the RIP process is initiated, the default configuration parameters are restored to the default value.




Format
------

**reset rip** { *process-id* | **all** } **configuration**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the RIP process ID. | The value is an integer ranging from 1 to 4294967295. |
| **all** | Resets all RIP processes. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **reset rip configuration** command resets system parameters for a specified RIP process. When a RIP process starts, all the parameters of the process retain their default values.

**Precautions**

Restarting RIP processes may interrupt services. Therefore, exercise caution when running the reset rip command.After being restarted, all RIP processes adopt default configurations.


Example
-------

# Reset the configuration parameters of RIP process 100.
```
<HUAWEI> reset rip 100 configuration

```