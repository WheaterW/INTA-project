multicast mib
=============

multicast mib

Function
--------



The **multicast mib** command displays the multicast MIB view.

The **undo multicast mib** command deletes all configurations in the multicast MIB view.



By default, the multicast MIB view is not displayed.


Format
------

**multicast mib**

**undo multicast mib**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Run the **undo multicast mib** command to delete all configurations in the multicast MIB view.In using the **undo multicast mib** command, you need to enter Y or N to confirm the action. This command will clear global multicast MIB configurations. So, use this command with caution.


Example
-------

# Enable multicast MIB and enter the multicast MIB view.
```
<HUAWEI> system-view
[~HUAWEI] multicast mib

```