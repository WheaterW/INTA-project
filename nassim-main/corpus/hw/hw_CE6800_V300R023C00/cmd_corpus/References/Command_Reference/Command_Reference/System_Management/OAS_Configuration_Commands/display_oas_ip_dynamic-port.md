display oas ip dynamic-port
===========================

display oas ip dynamic-port

Function
--------



The **display oas ip dynamic-port** command displays the configured port range.




Format
------

**display oas ip dynamic-port**


Parameters
----------

None

Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run the display oas ip dynamic-port command to view the configured port range.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured port range.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas ip dynamic-port
--------------------------------------------------------------------------
PortRange                 UsedApplicationName
--------------------------------------------------------------------------
50020-50030              -       
--------------------------------------------------------------------------

```

**Table 1** Description of the **display oas ip dynamic-port** command output
| Item | Description |
| --- | --- |
| PortRange | Port range. |
| UsedApplicationName | Name of the app that uses the port range. |