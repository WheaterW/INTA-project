ptp slaveonly
=============

ptp slaveonly

Function
--------



The **ptp slaveonly** command configures an ordinary clock (OC) to work in slave-only mode.

The **undo ptp slaveonly** command deletes the slave-only mode from the OC.



By default, an OC can work as the master clock or a slave clock and does not work in slave-only mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp slaveonly**

**undo ptp slaveonly**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An OC has only a single 1588v2 interface. Therefore, the OC can only function as the master clock to advertise clock signals to downstream devices or as a slave clock to receive clock signals from upstream devices. To enable an OC to work only as a slave clock, run the ptp slaveonly command on the OC.

**Prerequisites**

The device has been configured as an OC using the **ptp device-type oc** command.


Example
-------

# Configure the PTP-enabled interface on the OC to slaveOnly.
```
<HUAWEI> system-view
[~HUAWEI] ptp slaveonly

```