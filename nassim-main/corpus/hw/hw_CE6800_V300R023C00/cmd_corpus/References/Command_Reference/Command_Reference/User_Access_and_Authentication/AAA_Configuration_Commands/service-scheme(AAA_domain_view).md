service-scheme(AAA domain view)
===============================

service-scheme(AAA domain view)

Function
--------

The **service-scheme** command applies a service scheme to a domain.

The **undo service-scheme** command unbinds a service scheme from a domain.

By default, no service scheme is bound to a domain.



Format
------

**service-scheme** *name*

**undo service-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *name* | Specifies the name of a service scheme. | The value is a string of 1 to 32 case-sensitive characters, and cannot contain spaces. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The authorization configuration in a service scheme takes effect only when the service scheme is applied to a domain.

**Precautions**

A service scheme has been created and configured with required parameters.



Example
-------

# Apply the service scheme srvscheme1 to the domain huawei.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] service-scheme srvscheme1
[*HUAWEI-aaa-service-srvscheme1] quit
[*HUAWEI-aaa] domain huawei
[*HUAWEI-aaa-domain-huawei] service-scheme srvscheme1

```