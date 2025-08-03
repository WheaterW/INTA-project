nacm
====

nacm

Function
--------



The **nacm** command displays the NACM view.

The **undo nacm** command deletes configuration of NACM.



By default, no NACM is created.


Format
------

**nacm**

**undo nacm**


Parameters
----------

None

Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enter the NACM view for NACM configuration, run the nacm command.


Example
-------

# Enter the NACM view.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] nacm

```

# Delete all configuration of NACM.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] undo nacm

```