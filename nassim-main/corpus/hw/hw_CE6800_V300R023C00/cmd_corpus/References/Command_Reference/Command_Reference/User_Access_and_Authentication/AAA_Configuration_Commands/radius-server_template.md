radius-server template
======================

radius-server template

Function
--------

The **radius-server template** command creates a RADIUS server template and displays the RADIUS server template view.

The **undo radius-server template** command deletes a RADIUS server template.

By default, there is no RADIUS server template on the device.



Format
------

**radius-server template** *template-name*

**undo radius-server template** *template-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of a RADIUS server template. | The value is a string of 1 to 32 case-sensitive characters, including letters (case-sensitive), numerals (0 to 9), periods (.), hyphens (-), and underscores (\_). The value cannot be - or --. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Creating a RADIUS server template is the prerequisite for configuring RADIUS authentication and accounting. You can perform RADIUS configurations, such as the configuration of authentication servers, accounting servers, and shared key only after a RADIUS server template is created.

**Follow-up Procedure**

Configure an authentication server, an accounting server, and shared key in the RADIUS server template view, and then run the radius-server command to apply the RADIUS server template.



Example
-------

# Create a RADIUS server template template1 and enter the RADIUS server template view.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1]

```