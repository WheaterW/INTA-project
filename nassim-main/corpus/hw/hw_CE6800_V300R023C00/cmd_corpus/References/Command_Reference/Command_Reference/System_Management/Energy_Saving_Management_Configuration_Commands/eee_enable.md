eee enable
==========

eee enable

Function
--------



The **eee enable** command enables the Energy Efficient Ethernet (EEE) function on an electrical interface.

The **undo eee enable** command disables the EEE function on an electrical interface.



By default, EEE is disabled on an electrical interface.


Format
------

**eee enable**

**undo eee enable**


Parameters
----------

None

Views
-----

Layer 2 10GE interface view,10GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The system provides power for each interface. Even though an interface is idle, it consumes the same power as working interfaces. The **eee enable** command enables the system to reduce the power on an interface when the interface is idle and restore the power when the interface starts to transmit data. This reduces system power consumption.



**Prerequisites**



If an electrical interface works in non-auto negotiation mode, run the **undo negotiation disable** command to enable auto-negotiation.



**Precautions**

* The EEE function can be configured only on a combo interface working in electrical mode or on an electrical interface (except the management interface).
* After the **eee enable** command is run on an interface in the Up state, the interface alternates between Up and Down states.


Example
-------

# Enable the EEE function on a 10GE electrical port.
```
<HUAWEI> system-view
[~HUAWEI] interface 10GE1/0/1
[~HUAWEI-10GE1/0/1] eee enable

```

# Disable the EEE function on a 10GE electrical interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 10GE1/0/1
[~HUAWEI-10GE1/0/1] undo eee enable

```