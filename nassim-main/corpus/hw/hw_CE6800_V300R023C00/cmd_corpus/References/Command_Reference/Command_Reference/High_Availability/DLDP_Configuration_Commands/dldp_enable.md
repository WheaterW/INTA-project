dldp enable
===========

dldp enable

Function
--------



The **dldp enable** command enables DLDP.

The **undo dldp enable** command disables DLDP.



By default, DLDP is disabled globally and on all ports.


Format
------

**dldp enable**

**undo dldp enable**


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

A unidirectional link may exist in an actual networking scenario. A unidirectional link problem occurs when a local device receives packets from a peer device, but the peer device cannot receive packets from the local device. A unidirectional link may result in problems such as loops in an STP-enabled network.DLDP monitors the link status of devices connected by optical fibers. If DLDP detects a unidirectional link, it automatically closes the port on the unidirectional link or instructs you to close the port. Closing the port prevents a traffic interruption.To enable DLDP on the interface, run the dldp enable command to enable DLDP globally, and then run the dldp enable command on the interface to enable DLDP.

**Prerequisites**

The network devices have been connected properly by optical fibers because DLDP detection can be performed only after the link is working properly at the physical level.

**Configuration Impact**

If DLDP is disabled in the system view, DLDP functions on all interfaces are disabled and all DLDP configurations are deleted, which cannot be restored.

**Precautions**

After running the dldp enable command in the system view, you must run the command on interfaces so that DLDP functions can be enabled and DLDPDUs can be transmitted.


Example
-------

# Enabled DLDP globally.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable

```