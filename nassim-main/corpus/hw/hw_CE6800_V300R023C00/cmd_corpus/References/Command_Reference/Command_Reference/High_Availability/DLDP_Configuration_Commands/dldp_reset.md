dldp reset
==========

dldp reset

Function
--------



The **dldp reset** command resets the DLDP Disable status on a port to restore DLDP detection.




Format
------

**dldp reset**


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

After DLDP detects the existence of a unidirectional link, the port enters the Disable state. In this case, DLDP prompts users to close the port or closes the port automatically. To restore DLDP detection on a port, use one of these methods to reset DLDP:

* If the port was closed using the **shutdown** command, run the **undo shutdown** command to restore the port status.
* If the port was closed automatically, you can wait for DLDP to re-open the port after DLDP detects that the link becomes bidirectional. The DLDP auto-recovery mechanism detects that the peers are reachable in both directions. Or you can run the dldp reset command to restore the port. The DLDP status after a reset depends on the physical status of the port. If the port is physically Down, its DLDP state goes to Inactive. If the port is physically Up, its DLDP state goes to Active.This command run in the system view takes effect on all ports that were Disable.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.


Example
-------

# Reset DLDP status on all ports that are Disable.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable
[*HUAWEI] dldp reset

```