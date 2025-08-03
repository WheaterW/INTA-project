group-member interface(Rail group port-group view)
==================================================

group-member interface(Rail group port-group view)

Function
--------



The **group-member interface** command adds a specified interface to a Rail Group port group.

The **undo group-member interface** command deletes a specified interface from a Rail Group port group.



By default, no interface is added to a Rail Group port group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**group-member interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ] &<1-32>

**group-member interface** { *interface-name* | *interface-type* *interface-number* } **index** *index-value*

**undo group-member interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ] &<1-32>

**undo group-member interface** { *interface-name* | *interface-type* *interface-number* } **index** *index-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface to be added to a Rail Group port group. | - |
| *interface-type* | Specifies the type of an interface to be added to a Rail Group port group. | - |
| *interface-number* | Specifies the number of an interface to be added to a Rail Group port group. | - |
| **to** | Specifies an interface range that includes all interfaces between the two interfaces. | - |
| **index** *index-value* | Specifies the index of an interface to be added to a Rail Group port group. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 0 to 255.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer in the range from 0 to 1023. |



Views
-----

Rail group port-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to add members to a Rail Group port group.

**Precautions**

* If you run this command multiple times, all the configurations take effect.
* Only physical interfaces can be added to a Rail Group port group.
* A physical interface that has been added to an Eth-Trunk interface cannot be added to a Rail Group port group.
* When the interface index allocation mode for Rail Group is auto, the indexes of the interfaces in the Rail Group port group are automatically allocated after this command is run. The index-value parameter cannot be configured.
* When the interface index allocation mode for Rail Group is manual, you must specify index-value when running this command to manually specify the index of an interface in the Rail Group port group. It is recommended that index-value be consecutive numbers starting from 0 for interfaces in the same Rail Group port group. Otherwise, load imbalance may occur.
* When running this command, pay attention to the following points when using the keyword to:
  + The two interfaces before and after to must be of the same type and have the same attribute. For example, they are both interfaces resulting from a split. If they are interfaces resulting from a split, they must belong to the same physical interface.
  + If the keyword to is not used, ignore the preceding points.

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:A Rail Group port group can contain a maximum of 256 members.For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:A Rail Group port group can contain a maximum of 1024 members.



Example
-------

# Add 100GE1/0/1 through 100GE1/0/4 to Rail Group port group Leaf1.
```
<HUAWEI> system-view
[~HUAWEI] rail-group Leaf1
[*HUAWEI-rail-group-Leaf1] group-member interface 100GE 1/0/1 to 100GE 1/0/4

```