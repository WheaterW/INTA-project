hwtacacs-server template
========================

hwtacacs-server template

Function
--------

The **hwtacacs-server template** command creates an HWTACACS server template and enters the HWTACACS server template view.

The **undo hwtacacs-server template** command deletes an HWTACACS server template.

By default, no HWTACACS server template is configured.



Format
------

**hwtacacs-server template** *template-name*

**undo hwtacacs-server template** *template-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of an HWTACACS server template. | HWTACACS server template name. The name contains only digits, letters, hyphens (-), underscores (\_), and dots (.) within the specified length. The name cannot be - or --. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

You can perform HWTACACS configurations, such as the configuration of authentication servers, authorization servers, accounting servers, and shared key, only after an HWTACACS server template is created.

**Follow-up Procedure**

Configure an authentication server, accounting server, and shared key in the HWTACACS server template view, and run the **hwtacacs-server** command in the domain view to apply the HWTACACS server template.

**Precautions**

You can modify an HWTACACS server template when it is not in use.

When you run the
**undo hwtacacs-server template** command to delete an HWTACACS server template in use, a message about a deletion failure is displayed on the device.

Example
-------

# Create an HWTACACS server template template1 and enter the HWTACACS server template view.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template template1
[*HUAWEI-hwtacacs-template1]

```