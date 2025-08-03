optical pn-reverse
==================

optical pn-reverse

Function
--------



The **optical pn-reverse enable** command enables SerDes polarity reversal on an interface.

The **undo optical pn-reverse enable** command disables SerDes polarity reversal on an interface.



By default, SerDes polarity reversal is disabled on an interface.


Format
------

**optical pn-reverse enable**

**undo optical pn-reverse enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 200GE interface view,200GE interface view,400GE-L2 view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



There is no IEEE standard for 100G ZR4 (80 km) optical modules. 100G ZR4 optical modules from different vendors have different data channel mapping modes. When a non-Huawei 100G ZR4 (80 km) optical module is connected to a Huawei 100G ZR4 (80 km) optical module, the ports may fail to communicate. In this case, you are advised to run this command to reverse the positive and negative electrodes of the SerDes on the corresponding port so that 100G ZR4 (80 km) optical modules from different vendors can communicate with each other, ensuring normal service running.



**Precautions**

* Only interfaces equipped with Huawei 100G ZR4 (80 km) optical modules support this command. If this command is run on an interface equipped with other media, the interface goes Down due to SerDes P/N mismatch.


Example
-------

# Enable SerDes polarity reversal on an interface.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] interface 100GE1/0/4
[~HUAWEI-100GE1/0/4] optical pn-reverse enable

```