display snmp-agent mib modules
==============================

display snmp-agent mib modules

Function
--------



The **display snmp-agent mib modules** command displays MIB file information.




Format
------

**display snmp-agent mib modules**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The SNMP MIB resource files can be loaded and unloaded dynamically. To view MIB file information, run the display snmp-agent mib modules command.

**Prerequisites**

The SNMP agent function has been enabled using the **snmp-agent** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the loaded MIB file information.
```
<HUAWEI> display snmp-agent mib modules
BGP4-MIB:
    resource : allmibs_mib.bin
    mib      : bgp4-mib.mib

ENTITY-MIB:
    resource : allmibs_mib.bin
    mib      : entity-mib.mib

HUAWEI-AAA-MIB:
    resource : allmibs_mib.bin
    mib      : huawei-aaa-mib.mib

```

**Table 1** Description of the **display snmp-agent mib modules** command output
| Item | Description |
| --- | --- |
| mib | MIB file name. |
| resource | BIN file name. |
| MIB | MIB module name. |