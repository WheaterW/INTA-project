apply large-community
=====================

apply large-community

Function
--------



The **apply large-community** command sets a value for the BGP Large-Community attribute.

The **undo apply large-community** command deletes the value set for the BGP Large-Community attribute.



By default, the BGP Large-Community attribute is not set.


Format
------

**apply large-community** { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** }

**apply large-community none**

**undo apply large-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *aa:bb:cc* | Specifies a value of the Large-Community attribute. | The value is in the format of aa:bb:cc. The values of aa, bb, and cc are integers ranging from 0 to 4294967295. |
| **additive** | Adds a value to the Large Community attribute carried in routes. | - |
| **overwrite** | Overwrites the existing values of the Large-Community attribute. | - |
| **delete** | Deletes the values of the Large-Community attribute carried in the matched routes. | - |
| **none** | Deletes all the Large-Community values set for the BGP routes to be imported. If the parameter is applied to BGP, it takes effect on the routes to be imported, not on the routes to be advertised. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. To modify or set values of the Large-Community attribute in BGP routes, run the **apply large-community** command.



**Configuration Impact**

If the **apply large-community** command is run in a route-policy, the values of the Large-Community attribute in the BGP routes filtered by the route-policy will be changed to the value in the route-policy.Assume that the Large Community attribute in the original BGP routes is set to 10:3:20 and 10:3:30. For the BGP routes that meet the filtering conditions:

* If the apply large-community 20:4:30 overwrite command has been run, the values of the Large-Community attribute are changed to 20:4:30.
* If the apply large-community 10:3:20 delete command has been run, the values of the Large-Community attribute are changed to 10:3:30.
* If the apply large-community 20:4:30 additive command has been run, the value 20:4:30 is added to the Large-Community attribute list including 10:3:20 and 10:3:30 already.
* If the apply large-community none command has been run, all the values set for the Large-Community attribute are deleted.

**Precautions**



If the **apply large-community** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Configure a route-policy named setlargecommunity to filter the routes whose AS\_Path filter is 8, and change the values of the Large-Community attribute in the matched routes to 10:3:20.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 8 permit ^10_
[*HUAWEI] route-policy setlargecommunity permit node 16
[*HUAWEI-route-policy] if-match as-path-filter 8
[*HUAWEI-route-policy] apply large-community 10:3:20 overwrite

```