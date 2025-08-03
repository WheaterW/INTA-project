stp binding process (Layer 2 interface view)
============================================

stp binding process (Layer 2 interface view)

Function
--------



The **stp binding process** command adds an interface to a specified MSTP process.

The **undo stp binding process** command removes an interface from a specified MSTP process.



By default, an interface is added to MSTP process 0.


Format
------

**stp binding process** *process-id*

**undo stp binding process** *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an MSTP process. | The value is an integer ranging from 1 to 256. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After an MSTP device properly starts, each port of this device belongs to MSTP process 0 by default. The link connecting an MSTP device to an access ring is an access link. To isolate services on access rings using an MSTP process, run the stp binding process command to add an interface on an access link to a specified MSTP process.



**Prerequisites**



An MSTP process has been configured using the **stp process** command.



**Precautions**



An interface on an access link can be added to only one MSTP process. If the stp binding process command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Add an interface to MSTP process 1.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] stp binding process 1

```