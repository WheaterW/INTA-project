service-scheme (aaa view)
=========================

service-scheme (aaa view)

Function
--------

The **service-scheme** command creates a service scheme and displays the service scheme view.

The **undo service-scheme** command deletes a service scheme.

By default, no service scheme is configured.



Format
------

**service-scheme** *service-scheme-name*

**undo service-scheme** *service-scheme-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *service-scheme-name* | Specifies the name of a service scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or the following symbols: /, \, :, \*, ?, ", <, >, and |. The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A service scheme is used to manage user authorization information in a unified manner.

**Follow-up Procedure**

Run the service-scheme (AAA domain view) command to apply the service scheme to a domain.

**Precautions**

If the service scheme to be configured does not exist, the service-scheme (AAA view) command creates a service scheme and displays the service scheme view. If the service scheme to be configured already exists, the service-scheme (AAA view) command displays the service scheme view.

To delete or modify the service scheme applied to a domain, run the undo service-scheme (AAA domain view) command to unbind the service scheme from the domain.

Example
-------

# Create a service scheme srvscheme1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] service-scheme srvscheme1

```