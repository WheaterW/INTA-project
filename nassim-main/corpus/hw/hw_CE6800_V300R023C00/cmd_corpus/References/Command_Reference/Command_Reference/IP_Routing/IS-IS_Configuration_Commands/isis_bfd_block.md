isis bfd block
==============

isis bfd block

Function
--------



The **isis bfd block** command disables an interface from dynamically establishing BFD sessions.

The **undo isis bfd block** command cancels the configuration.



By default, an interface can dynamically establish BFD sessions.


Format
------

**isis bfd block**

**undo isis bfd block**


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

BFD can provide millisecond-level fault detection, help IS-IS to detect the faults that occur on neighboring devices or links more quickly,and instruct IS-IS to recalculate routes for correct packet forwarding. To enable all IS-IS interfaces to dynamically establish BFD sessions, run the **bfd all-interfaces enable** command on the interfaces. To disable an interface from dynamically establishing BFD sessions, run the isis bfd block command.

**Prerequisites**

BFD has been enabled globally, and An IS-IS process has been created on the interface.

**Configuration Impact**

After the isis bfd block command is run on an interface, the interface is disabled from dynamically establishing BFD sessions. As a result, fast link fault detection cannot be implemented.

**Precautions**

If the **isis bfd block**, **isis bfd enable**, **isis bfd static**, and **isis bfd track session-name** commands are configured, only the last configured command takes effect.


Example
-------

# Disable 100GE1/0/1 from dynamically establishing BFD sessions.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis bfd block

```