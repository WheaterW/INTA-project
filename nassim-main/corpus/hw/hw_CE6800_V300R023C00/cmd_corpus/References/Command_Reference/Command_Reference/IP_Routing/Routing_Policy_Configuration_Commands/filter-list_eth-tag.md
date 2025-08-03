filter-list eth-tag
===================

filter-list eth-tag

Function
--------



The **filter-list eth-tag** command creates an Ethernet tag list and displays the Ethernet tag list view.

The **undo filter-list eth-tag** command deletes an Ethernet tag list.



By default, no Ethernet tag list is created.


Format
------

**filter-list eth-tag** *name*

**undo filter-list eth-tag** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies an Ethernet tag list name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To create an Ethernet tag list, run the **filter-list eth-tag** command. The Ethernet tag list can be applied to an if-match clause to filter EVPN routes based on the Ethernet tags of routes.



**Follow-up Procedure**



Run the **eth-tag** command in the Ethernet tag list view to add Ethernet tag values for the list.




Example
-------

# Create an Ethernet tag list named ethtag.
```
<HUAWEI> system-view
[~HUAWEI] filter-list eth-tag ethtag

```