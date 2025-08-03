tos-exp
=======

tos-exp

Function
--------



The **tos-exp** command sets a priority of BFD control packets for a single static BFD session.

The **undo tos-exp** command restores the default setting.



By default, the priority is 7, which is the highest priority of BFD control packets.


Format
------

**tos-exp** *tos-value*

**undo tos-exp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tos-value* | Specifies a priority for BFD control packets. | The value is an integer ranging from 0 to 7. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the system is congested, BFD control packets with a higher priority are preferentially sent. To change a priority of BFD control packets for a single static BFD session, run the **tos-exp** command.

**Prerequisites**

A BFD session has been created.

**Configuration Impact**

The priority of BFD packets changes.

**Precautions**

* If the **tos-exp** command is run in the BFD session view to set a priority and the **tos-exp** command is run in the BFD view to set a priority, the configuration of the **tos-exp** command in the BFD session view takes effect.
* If the **tos-exp** command is run in the BFD session view to set a priority to 7 (the default value) and the **tos-exp** command is run in the BFD view to set a priority to a non-default value, the configuration of the **tos-exp** command in the BFD session view takes effect.

Example
-------

# Set the priority of BFD control packets for a session named s1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-s1] tos-exp 5

```