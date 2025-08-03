sham-hello enable (OSPF view)
=============================

sham-hello enable (OSPF view)

Function
--------



The **sham-hello enable** command enables the OSPF sham-hello function.

The **undo sham-hello** command disables the OSPF sham-hello function.



By default, the OSPF sham-hello function is disabled.


Format
------

**sham-hello enable**

**undo sham-hello**


Parameters
----------

None

Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable the OSPF sham-hello function, run the **sham-hello enable** command. After the command is run, the device can maintain neighbor relationships through not only Hello packets but also LSU and LSAck packets, which strengthens OSPF neighbor relationships.


Example
-------

# Enable the OSPF sham-hello function.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] sham-hello enable

```