als enable
==========

als enable

Function
--------



The **als enable** command enables ALS on an interface.

The **undo als enable** command disables ALS on an interface.



By default, ALS is disabled on an interface.


Format
------

**als enable**

**undo als enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The automatic laser shutdown (ALS) function controls the laser pulse of an optical module by detecting the Loss of Signal (LOS) on an optical interface. It provides protection for users while at the same time reducing energy consumption for users.

* If ALS is disabled and the optical fiber fails or is not properly installed, data communication is interrupted. In this case, the optical interface and the laser continue to operate, with the laser continuing to emit pulses. This wastes energy and risks damaging an operator's eyes.
* If ALS is enabled in the preceding scenario, the system automatically disables the laser from emitting pulses after detecting the LOS on the optical interface. When the system detects that the LOS is cleared after the optical fiber is installed or recovers, it enables the laser to resume emitting pulses.The constraints on ALS are as follows:
* ALS is supported only when optical interfaces are preconfigured with optical modules, optical interfaces are installed with optical modules, and COMBO interfaces are working in optical mode. Electrical interfaces do not support ALS.
* When optical interfaces transmit services unidirectionally, they do not support ALS.
* Split interfaces do not support ALS.

**Configuration Impact**

When detecting a LOS signal, the optical module disables the local laser.


Example
-------

# When detecting the LOS signal, the optical module disables the local laser.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] als enable

```