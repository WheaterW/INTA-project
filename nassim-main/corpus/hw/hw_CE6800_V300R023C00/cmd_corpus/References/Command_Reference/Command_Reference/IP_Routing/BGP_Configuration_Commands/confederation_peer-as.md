confederation peer-as
=====================

confederation peer-as

Function
--------



The **confederation peer-as** command configures the number of each sub-AS of a confederation.

The **undo confederation peer-as** command removes the specified sub-AS from the confederation.



By default, no sub-AS number of the confederation is configured.


Format
------

**confederation peer-as** { *as-number* } &<1-32>

**undo confederation peer-as** { *as-number* } &<1-32>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies an AS number. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x and y are integers ranging from 1 to 65535 and from 0 to 65535, respectively. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A large AS may contain a huge number of fully meshed IBGP peer relationships. In this situation, configure a confederation. To configure the number of each sub-AS of the confederation, run the confederation peer-as command.

**Prerequisites**

A confederation ID has been configured using the **confederation id** command.

**Configuration Impact**

The sub-ASs configured in this command belong to the same confederation, and devices in each sub-AS are fully meshed.

**Precautions**

The old speaker with a 2-byte AS number and the new speaker with a 4-byte AS number cannot exist in the same confederation. AS4\_Path does not support the confederation. If a 2-byte AS number and a 4-byte AS number co-exist in the same confederation, routing loops may occur, and the sub-AS numbers in the confederation may be transmitted out of the confederation.If a confederation ID is configured and the command is run, all the TCP connections of the BGP peer relationships established using the sub-AS numbers specified in the command are torn down, and the BGP peer relationships are reestablished. Therefore, exercise caution when running this command.


Example
-------

# Configure the number of each sub-AS of the confederation.
```
<HUAWEI> system-view
[~HUAWEI] bgp 1090
[*HUAWEI-bgp] confederation id 100
[*HUAWEI-bgp] confederation peer-as 1091 1092 1093

```