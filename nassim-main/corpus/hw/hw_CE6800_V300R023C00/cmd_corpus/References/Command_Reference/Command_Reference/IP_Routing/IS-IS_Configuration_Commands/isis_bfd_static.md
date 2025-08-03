isis bfd static
===============

isis bfd static

Function
--------



The **isis bfd static** command enables static BFD on an IS-IS interface.

The **undo isis bfd static** command disables static BFD from the IS-IS interface.



By default, static BFD is disabled.


Format
------

**isis bfd static**

**undo isis bfd static**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In static BFD, BFD session parameters are set manually to deliver requests for BFD session establishment, which can fast detect link faults. The isis bfd static command can be used to enable static BFD on an interface and set up a static BFD session on corresponding links.

**Prerequisites**

BFD has been enabled globally, and a specified interface has been bound to an IS-IS process using the **isis enable** command.

**Precautions**

If the isis bfd block, isis bfd enable, isis bfd static, and isis bfd track session-name commands are all configured, only the last configured command takes effect.


Example
-------

# Configure static BFD on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis bfd static

```