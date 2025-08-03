netstream record ip (system view)
=================================

netstream record ip (system view)

Function
--------



The **netstream record ip** command creates an IPv4 flexible flow statistics template or displays the view of an existing IPv4 flexible statistics template.

The **undo netstream record ip** command deletes a specified IPv4 flexible flow statistics template.



By default, no IPv4 flexible flow statistics template exists.


Format
------

**netstream record** *record-name* **ip**

**undo netstream record** *record-name* **ip**


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

You need to create the IPv4 flexible flow statistics template before exporting flexible flow statistics.

**Precautions**



Each device supports a maximum of 16 flexible flow statistics templates. To configure a 17th flexible flow statistics template, run the **undo netstream record ip** command to delete an existing one first.The flexible flow statistics template that has been applied to an interface cannot be modified or deleted. To delete it, run the **undo netstream record ip** command on the interface and then modify or delete the template.IPv4 and IPv6 flexible flow statistics templates are independent from each other. Therefore, an IPv4 template and an IPv6 template can share the same name.




Example
-------

# Create the IPv4 flexible flow statistics template named abc1.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc1 ip

```