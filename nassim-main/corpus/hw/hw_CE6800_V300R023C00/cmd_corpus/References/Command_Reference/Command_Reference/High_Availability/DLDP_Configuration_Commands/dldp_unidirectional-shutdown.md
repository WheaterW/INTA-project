dldp unidirectional-shutdown
============================

dldp unidirectional-shutdown

Function
--------



The **dldp unidirectional-shutdown** command configures a port shutdown mode after DLDP detects the existence of a unidirectional link.

The **undo dldp unidirectional-shutdown** command restores the default mode.



By default, the port is closed in the automatic mode after DLDP detection.


Format
------

**dldp unidirectional-shutdown** { **auto** | **manual** }

**undo dldp unidirectional-shutdown**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **auto** | Indicates that the port is closed in the automatic mode after DLDP detects the existence of a unidirectional link. | - |
| **manual** | Indicates that the port is closed in the manual mode after DLDP detects the existence of a unidirectional link. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To close the port that is Disable when DLDP detects the existence of a unidirectional link, run the dldp unidirectional-**shutdown** command to configure a shutdown mode. The port can be closed either by DLDP automatically or by a network administrator.

* Manual mode: When DLDP detects a unidirectional link, it switches to Disable state and generates an alarm, but it does not set the port status to DLDP Down. A network administrator must run the **shutdown** command to change the port status to DLDP Down. This mode is recommended when network performance is poor. Manual shutdown of a port can prevent traffic interruptions caused by DLDP automatically closing a port.
* Automatic mode: When DLDP detects a unidirectional link, it switches to Disable state, generates an alarm, and sets the port status to DLDP Down. This is the default port shutdown mode.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.

**Precautions**

When the service traffic is heavy or the CPU usage is high, the manual shutdown mode is recommended.


Example
-------

# Use the automatic mode to close the port after DLDP detects the existence of a unidirectional link.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable
[*HUAWEI] dldp unidirectional-shutdown auto

```