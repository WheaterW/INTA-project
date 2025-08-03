advertise prefix-attributes flags
=================================

advertise prefix-attributes flags

Function
--------



The **advertise prefix-attributes flags** command enables an IS-IS process to advertise the extended prefix attribute flag.

The **undo advertise prefix-attributes flags** command disables an IS-IS process from advertising the extended prefix attribute flag.



By default, an IS-IS process does not advertise the extended prefix attribute flag.


Format
------

**advertise prefix-attributes flags**

**undo advertise prefix-attributes flags**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To view information about the origin of routes in the LSDB, run this command. After the command is run, the IS-IS process advertises the extended prefix attribute flag (IPv4 Extended Reachability Attribute Flags) to carry related information in the LSDB.


Example
-------

# Enable an IS-IS process to advertise the extended prefix attribute flag.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] advertise prefix-attributes flags

```