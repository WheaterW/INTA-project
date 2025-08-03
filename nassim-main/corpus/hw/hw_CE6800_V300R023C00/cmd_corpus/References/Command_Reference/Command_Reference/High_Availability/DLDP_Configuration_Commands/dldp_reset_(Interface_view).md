dldp reset (Interface view)
===========================

dldp reset (Interface view)

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

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DLDP detects the existence of a unidirectional link, the port enters the Disable state. In this case, DLDP prompts users to close the port or closes the port automatically. To restore DLDP detection on a port, use one of these methods to reset DLDP:

* If the port was closed using the **shutdown** command, run the **undo shutdown** command to restore the port status.
* If the port was closed automatically, you can wait for DLDP to re-open the port after DLDP detects that the link becomes bidirectional. The DLDP auto-recovery mechanism detects that the peers are reachable in both directions. Or you can run the dldp reset command to restore the port. The DLDP status after a reset depends on the physical status of the port. If the port is physically Down, its DLDP state goes to Inactive. If the port is physically Up, its DLDP state goes to Active.This command run in the interface view takes effect only on a specific interface.

**Prerequisites**

DLDP has been enabled globally and on a specific interface using the **dldp enable** command before you run the dldp reset command in the interface view.


Example
-------

# Reset the DLDP status of 100GE 1/0/1 that is disabled.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] dldp reset

```