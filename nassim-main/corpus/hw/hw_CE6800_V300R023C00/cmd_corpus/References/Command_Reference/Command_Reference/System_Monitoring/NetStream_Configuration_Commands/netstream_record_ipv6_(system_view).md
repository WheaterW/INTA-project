netstream record ipv6 (system view)
===================================

netstream record ipv6 (system view)

Function
--------



The **netstream record ipv6** command creates an IPv6 flexible flow statistics template or displays the view of an existing IPv6 flexible flow statistics template.

The **undo netstream record ipv6** command deletes a specified IPv6 flexible flow statistics template.



By default, no IPv6 flexible flow statistics template exists.


Format
------

**netstream record** *record-name* **ipv6**

**undo netstream record** *record-name* **ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of the flexible flow statistics template. | The value is a string of 1 to 32 case-sensitive characters. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You need to create the IPv6 flexible flow statistics template before exporting flexible flow statistics.

**Precautions**

A maximum of 16 flexible flow statistics templates can be configured on a device. To configure the 17th flexible flow statistics template, run the **undo netstream record ipv6** command to delete an existing one first.The template that has been applied to an interface cannot be modified or deleted. To modify or delete the template, run the **undo netstream record ipv6** command on the interface first.IPv4 and IPv6 flexible flow statistics templates are independent from each other. Therefore, an IPv4 template and an IPv6 template can share the same name.


Example
-------

# Create an IPv6 flexible flow statistics template named abc1.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc1 ipv6

```