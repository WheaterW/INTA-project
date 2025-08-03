isis bfd track session-name
===========================

isis bfd track session-name

Function
--------



The **isis bfd track session-name** command binds an IS-IS interface to a link-bundle BFD session.

The **undo isis bfd track session-name** command unbinds an IS-IS interface from a link-bundle BFD session.



By default, BFD for IS-IS is disabled on an IS-IS interface.


Format
------

**isis bfd track session-name** *bfd-session-name*

**undo isis bfd track session-name** *bfd-session-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bfd-session-name* | Specifies the link-bundle BFD session to be bound to an IS-IS interface. The BFD session needs to be manually configured. | The value is a string of 1 to 64 case-sensitive characters. |



Views
-----

100ge sub-interface view,100GE interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An IS-IS interface can be bound to a link-bundle BFD session by specifying a session name. The BFD session needs to be manually configured to quickly detect link faults. To enable the track BFD function on a specified interface and bind a link-bundle BFD session to the interface, run the isis bfd track session-name <bfd-session-name> command.

**Prerequisites**

BFD has been enabled globally, and a specified interface has been bound to an IS-IS process using the **isis enable** command.

**Precautions**

If the isis bfd block, isis bfd enable, isis bfd static, and isis bfd track session-name <bfd-session-name> commands are configured at the same time, only the last configured command takes effect.


Example
-------

# Enable the track BFD function on the interface.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] isis 1
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] quit
[*HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] bfd atob bind link-bundle peer-ip 10.10.0.2 interface Eth-Trunk1 source-ip 10.10.0.1
[*HUAWEI-bfd-session-atob] quit
[*HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] isis enable 1
[*HUAWEI-Eth-Trunk1] isis bfd track session-name AtoB

```