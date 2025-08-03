rail-group mode
===============

rail-group mode

Function
--------



The **rail-group mode** command configures an interface index allocation mode for Rail Group.

The **undo rail-group mode** command deletes the interface index allocation mode configured for Rail Group.



By default, the interface index allocation mode for Rail Group is auto.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rail-group mode** { **auto** | **manual** }

**undo rail-group mode** [ **auto** | **manual** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **auto** | Sets the interface index allocation mode for Rail Group to automatic. | - |
| **manual** | Sets the interface index allocation mode for Rail Group to manual. | - |



Views
-----

Rail group port-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure the interface index allocation mode for Rail Group.

* If the interface index allocation mode is auto, when an interface is added to a Rail Group port group, the index of this interface is automatically allocated. The interface index cannot be manually specified.
* If the interface index allocation mode is manual, you need to manually specify the index of an interface when adding this interface to a Rail Group port group.

Example
-------

# Set the interface index allocation mode for Rail Group to manual.
```
<HUAWEI> system-view
[~HUAWEI] rail-group Leaf1
[*HUAWEI-rail-group-Leaf1] rail-group mode manual

```