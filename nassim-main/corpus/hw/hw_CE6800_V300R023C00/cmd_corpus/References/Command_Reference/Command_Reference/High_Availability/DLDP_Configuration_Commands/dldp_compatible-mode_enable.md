dldp compatible-mode enable
===========================

dldp compatible-mode enable

Function
--------



The **dldp compatible-mode enable** command enables the DLDP-compatible mode.

The **undo dldp compatible-mode enable** command disables the DLDP-compatible mode.



By default, the DLDP-compatible mode is disabled.


Format
------

**dldp compatible-mode enable**

**undo dldp compatible-mode enable**


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

You can run the dldp compatible-mode enable command to allow Huawei devices to communicate with non-Huawei devices.

**Prerequisites**

DLDP has been enabled both globally and on interfaces.

**Precautions**

A DLDP-compatible mode must be either enabled or disabled on ports on both ends of a link on a cross-connected network.On a network where both ends are Huawei devices, the DLDP-compatible mode must also be either enabled or disabled on ports on both ends of the link.


Example
-------

# Enable the DLDP compatible mode on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] dldp enable
[*HUAWEI-100GE1/0/1] dldp compatible-mode enable

```