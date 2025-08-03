start dynamic-integrity-measurement right-now
=============================================

start dynamic-integrity-measurement right-now

Function
--------



The **start dynamic-integrity-measurement right-now** command configures the DIM function to be triggered immediately.




Format
------

**start dynamic-integrity-measurement right-now**


Parameters
----------

None

Views
-----

Trust environment management


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to immediately trigger the DIM function to check whether the memory of processes in running state is tampered with in real time.


Example
-------

# Trigger the DIM function immediately.
```
<HUAWEI> system-view
[~HUAWEI] trustem
[~HUAWEI-trustem] start dynamic-integrity-measurement right-now
Info: Operating, please wait for a moment......................
Info: Operation succeeded.

```

**Table 1** Description of the **start dynamic-integrity-measurement right-now** command output
| Item | Description |
| --- | --- |
| Info: Operation succeeded | Operation succeeded. |