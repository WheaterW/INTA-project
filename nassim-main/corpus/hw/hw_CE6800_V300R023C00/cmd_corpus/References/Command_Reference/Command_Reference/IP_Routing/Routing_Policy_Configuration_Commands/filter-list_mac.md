filter-list mac
===============

filter-list mac

Function
--------



The **filter-list mac** command creates a MAC address list and displays the MAC address list view.

The **undo filter-list mac** command deletes a MAC address list.



By default, no MAC address list is created.


Format
------

**filter-list mac** *name*

**undo filter-list mac** *name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies a MAC address list name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To create a MAC address list, run the **filter-list mac** command. The MAC address list can be applied to an if-match clause to filter EVPN routes.



**Follow-up Procedure**



Run the **mac** command in the MAC address list view to add MAC addresses for the list.




Example
-------

# Create a MAC address list named mac-list.
```
<HUAWEI> system-view
[~HUAWEI] filter-list mac mac-list

```