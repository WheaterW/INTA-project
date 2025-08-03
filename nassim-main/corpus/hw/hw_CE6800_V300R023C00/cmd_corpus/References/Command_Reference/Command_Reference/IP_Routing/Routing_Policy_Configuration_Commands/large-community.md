large-community
===============

large-community

Function
--------



The **large-community** command sets Large-Community values for a BGP Large-Community list.

The **undo large-community** command deletes the Large-Community values configured for a BGP Large-Community list.



By default, no Large-Community value is configured for a BGP Large-Community list.


Format
------

**large-community** { *cmntyValue* } &<1-100>

**undo large-community** { *cmntyValue* } &<1-100>

**undo large-community all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cmntyValue* | Specifies a value of the Large-Community attribute. | The value is in the format of a:b:c. The values of a, b, and c are integers ranging from 0 to 4294967295. |
| **all** | Deletes all Large-Community values from a BGP Large-Community list. | - |



Views
-----

Large community list view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. To set Large-Community values for a BGP Large-Community list, run the **large-community** command.




Example
-------

# Set a Large-Community value to 1:2:3 in a BGP Large-Community list named abc.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-list abc
[~HUAWEI-large-community-list-abc] large-community 1:2:3

```