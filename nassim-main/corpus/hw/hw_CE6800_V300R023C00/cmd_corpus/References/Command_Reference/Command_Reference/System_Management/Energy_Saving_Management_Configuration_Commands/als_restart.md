als restart
===========

als restart

Function
--------



The **als restart** command manually restarts the laser of an interface.




Format
------

**als restart**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the laser of an optical module works in manual restart mode, if the faulty fiber link is recovered, you need to manually open the laser so that the laser sends one pulse to clear LOS of the optical interface. Then the data communication is recovered.The constraints on ALS are as follows:

* The ALS function is supported only when an optical module is pre-installed, an optical module is installed on an optical interface, or a combo interface works in optical mode. Electrical interfaces do not support the ALS function.
* When optical interfaces transmit services unidirectionally, they do not support ALS.
* Breakout interfaces do not support ALS.

**Prerequisites**

ALS has been enabled on the interface using the **als enable** command, and the manual restart mode has been configured using the **als restart mode** command.


Example
-------

# Restart lasers on 100GE1/0/1 manually.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] als enable
[*HUAWEI-100GE1/0/1] als restart mode manual
[*HUAWEI-100GE1/0/1] als restart

```