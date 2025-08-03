hwtacacs-server
===============

hwtacacs-server

Function
--------

The **hwtacacs-server** command applies an HWTACACS server template to a domain.

The **undo hwtacacs-server** command deletes an HWTACACS server template from a domain.

By default, no HWTACACS server template is applied to a domain.



Format
------

**hwtacacs-server** *template-name*

**undo hwtacacs-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *template-name* | Specifies the name of an HWTACACS server template. | The HWTACACS server template must already exist.  The value is a string of 1 to 32 case-sensitive characters without spaces, the name contains only digits, letters, symbols '\_', '-', and '.' within the specified length. And neither '-' nor '--' can be used as the name. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To perform HWTACACS authentication, authorization, and accounting for users in a domain, configure an HWTACACS server template in the domain. After the HWTACACS server template is configured in the domain, the configuration in the HWTACACS server template takes effect.

**Prerequisites**

An HWTACACS server template has been created by using the hwtacacs-server template command.



Example
-------

# Apply the HWTACACS server template template1 to the domain tacacs1.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template template1
[*HUAWEI-hwtacacs-template1] quit
[*HUAWEI] aaa
[*HUAWEI-aaa] domain tacacs1
[*HUAWEI-aaa-domain-tacacs1] hwtacacs-server template1

```