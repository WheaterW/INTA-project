radius-server
=============

radius-server

Function
--------

The **radius-server** command applies a RADIUS server template to a domain.

The **undo radius-server** command unbinds an RADIUS server template from a domain.

By default, no RADIUS server template is bound to a configured domain.



Format
------

**radius-server** *template-name*

**undo radius-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of a RADIUS server template. | RADIUS server template's name. The name contains only digits, letters, symbols '\_', '-', and '.' within the specified length. And neither '-' nor '--' can be used as the name. The RADIUS server template must already exist. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To perform RADIUS authentication and accounting for users in a domain, apply a RADIUS server template to the domain. A RADIUS server template takes effect only after the RADIUS server template is applied to a domain.

**Prerequisites**

A RADIUS server template has been created using the **radius-server template** command.



Example
-------

# Apply the RADIUS server template template1 to the domain radius1.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] domain radius1
[*HUAWEI-aaa-domain-radius1] radius-server template1

```