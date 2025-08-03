identity enable
===============

identity enable

Function
--------



The **identity enable** command enables an interface to advertise LLDP packets carrying interface identity TLVs.

The **undo identity enable** command disables an interface from advertising LLDP packets carrying interface identity TLVs.



By default, the LLDP packets advertised by an interface do not carry interface identity TLVs.


Format
------

**identity enable**

**undo identity enable**


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



To send interface identity information to a directly connected peer device, run the **identity enable** command in the interface view to enable the interface to advertise LLDP packets carrying TLVs.



**Prerequisites**



LLDP has been enabled on the involved interface by running the **undo lldp disable** command in the interface view.




Example
-------

# Enable interface 100GE1/0/1 to advertise LLDP packets carrying identity TLVs.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo lldp disable
[~HUAWEI-100GE1/0/1] identity enable

```