opaque-capability enable
========================

opaque-capability enable

Function
--------



The **opaque-capability enable** command enables the opaque LSA capability.

The **undo opaque-capability** command disables the opaque LSA capability.



By default, the opaque LSA capability is disabled.


Format
------

**opaque-capability enable**

**undo opaque-capability**


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

**Usage Scenario**

Opaque LSAs provide a generic mechanism for OSPF extension:

* OSPF supports OSPF GR through Type 9 LSAs.
* OSPF supports OSPF loop detection for the imported routes through Type 11 LSAs.Before configuring OSPF GR or loop detection for the imported routes, enable the opaque LSA capability using the **opaque-capability enable** command.

**Configuration Impact**

Enabling or disabling the opaque LSA capability may delete and re-establish all sessions and instances.


Example
-------

# Enable OSPF opaque LSA capability.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] opaque-capability enable

```