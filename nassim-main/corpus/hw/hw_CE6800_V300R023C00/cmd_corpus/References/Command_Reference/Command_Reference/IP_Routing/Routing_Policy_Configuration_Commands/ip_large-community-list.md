ip large-community-list
=======================

ip large-community-list

Function
--------



The **ip large-community-list** command sets a BGP Large-Community list and displays the Large-Community list view.

The **undo ip large-community-list** command deletes a BGP Large-Community list.



By default, no BGP Large-Community list is created.


Format
------

**ip large-community-list** *large-community-list-name*

**undo ip large-community-list** *large-community-list-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *large-community-list-name* | Specifies the name of a BGP Large-Community list. | The value is a string of 1 to 63 case-sensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The Large-Community attribute is a private attribute of BGP and can be flexibly applied to route-policies. To set a BGP Large-Community list, run the **ip large-community-list** command. The BGP Large-Community list can be used to assign values to the Large-Community attribute in BGP routes.



**Follow-up Procedure**



Run the **large-community** command in the Large-Community list view to set values for the Large-Community attribute.If no Large-community attribute is configured in the Large-community attribute list view, the filtering result of the route-policy that references the Large-community attribute list is not as expected.




Example
-------

# Create a Large-Community list named a.
```
<HUAWEI> system-view
[~HUAWEI] ip large-community-list a

```