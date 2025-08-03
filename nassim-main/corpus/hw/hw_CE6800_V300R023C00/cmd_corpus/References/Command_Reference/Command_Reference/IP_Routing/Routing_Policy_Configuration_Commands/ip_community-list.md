ip community-list
=================

ip community-list

Function
--------



The **ip community-list** command creates a BGP community list and displays the community list view.

The **undo ip community-list** command deletes a specified BGP community list.



By default, no BGP community list is created.


Format
------

**ip community-list** *name*

**undo ip community-list** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies the name of a BGP community list. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported, the name must start with a letter. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Community attributes are BGP-specific and are used to simplify routing policy application and network maintenance and management. A community is a set of destination addresses with the same characteristics. These addresses have no physical boundary and are independent of their ASs. They share one or multiple community attributes. To create a BGP community list, run the **ip community-list** command.



**Follow-up Procedure**



Run the **community** command to configure community attributes for a BGP community list.If no community attribute is configured in the community list view, the filtering results of the route-policy that references the community list are not as expected.




Example
-------

# Create a BGP community list named community1.
```
<HUAWEI> system-view
[~HUAWEI] ip community-list community1

```