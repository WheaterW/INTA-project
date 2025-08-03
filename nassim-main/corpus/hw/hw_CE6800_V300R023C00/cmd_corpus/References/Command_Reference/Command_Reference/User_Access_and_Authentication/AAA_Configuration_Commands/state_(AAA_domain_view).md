state (AAA domain view)
=======================

state (AAA domain view)

Function
--------

The **state** command configures the state of a domain.

The **undo state** command restores the state of a domain.

By default, a domain is in active state after being created.



Format
------

**state** { **active** | **block** [ **time-range** *time-name* &<1-4> ] }

**undo state** [ **block** **time-range** [ *time-name* &<1-4> ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **active** | Sets the domain state to active. | - |
| **block** | Sets the domain state to blocking. | - |
| **time-range** *time-name* | Indicates the block time range of the domain.  time-name specifies the name of the block time range. If this parameter is not specified, the domain is always blocked. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, must start with a letter. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

If exceptions occur during service configuration, set the domain in blocking state to block access of new users. After the service configuration is complete, set the domain in active state.

**Prerequisites**

Before specifying the time-name parameter, ensure that the time range has been created using the **time-range** command.

**Precautions**

After the **state block** command is run to set the domain state to block, online users in the domain are not affected.

After the state block time-range <time-name> command is run, the specified domain state takes effect in the time specified by time-range. In buildrun information, the state block field specifies the actual state of the current domain.After the undo state block time-range <time-name> command is run to delete the last time-range configuration of the domain, the domain returns to the active state.

Example
-------

# Set the state of the domain vipdomain to blocking.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain vipdomain
[*HUAWEI-aaa-domain-vipdomain] state block

```