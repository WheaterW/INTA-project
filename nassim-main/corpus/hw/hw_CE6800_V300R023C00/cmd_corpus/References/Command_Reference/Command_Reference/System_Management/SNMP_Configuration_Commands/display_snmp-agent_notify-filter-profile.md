display snmp-agent notify-filter-profile
========================================

display snmp-agent notify-filter-profile

Function
--------



The **display snmp-agent notify-filter-profile** command displays the configurations of the trap messages that are filtered.




Format
------

**display snmp-agent notify-filter-profile** [ *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the filter profile name. | The value is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the configured filter profile, run the **display snmp-agent notify-filter-profile** command. The command output includes all the configured filter profiles or the filter profile with a specified name.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display existing filter profiles.
```
<HUAWEI> display snmp-agent notify-filter-profile
   Notify-filter name: snmpv3
   Notify-filter Subtree: iso.1.2.12
   Notify-filter Subtree mask: F0(Hex)
   Notify-filter Storage-type: nonVolatile
   Notify-filter Type: included
   Notify-filter status: active

```

**Table 1** Description of the **display snmp-agent notify-filter-profile** command output
| Item | Description |
| --- | --- |
| Notify-filter name | Filter profile name. |
| Notify-filter Subtree | Trap filter subtree. |
| Notify-filter Subtree mask | Subtree mask. |
| Notify-filter Storage-type | Storage type. |
| Notify-filter Type | Whether the trap object is to be filtered. |
| Notify-filter status | Row status. |