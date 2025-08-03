reset control-flap
==================

reset control-flap

Function
--------



The **reset control-flap** command deletes statistics about control-flap on an interface.




Format
------

**reset control-flap** { **penalty** | **counter** } **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **penalty** | Deletes the penalty of control-flap on an interface to release the interface from the suppressed state. | - |
| **counter** | Deletes the number of times interface flapping occurs. | - |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | The value is of the enumerated type. |
| *interface-number* | Specifies an interface number. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before collecting traffic statistics on a specific interface within a specific period of time, delete existing traffic statistics on this interface.



**Configuration Impact**



If penalty is specified in the command, the penalty of control-flap on an interface is deleted; if counter is specified in the command, the number of times interface flapping occurs are deleted.



**Precautions**



After the reset control-flap command is run, statistics about control-flap on an interface are reset to 0 using the display control-flap command. Therefore, confirm the action before you run the reset control-flap command.




Example
-------

# Delete the penalty of control-flap on 100GE 1/0/1.
```
<HUAWEI> reset control-flap penalty interface 100GE 1/0/1

```