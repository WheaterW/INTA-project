display warranty software
=========================

display warranty software

Function
--------



The **display warranty software** command displays software warranty information.




Format
------

**display warranty software**


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

The warranty information is preset in the software release in the packaging and building phase. You can run the **display warranty software** command to view the warranty information.Currently, only the warranty information of system software can be viewed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display software digital warranty information in the system.
```
<HUAWEI> display warranty software
 Offering Name      : NetEngin***
 Offering Version   : V800R***C**B***
 EOS Date           : 2022-01-01
 Status             : normal

```

**Table 1** Description of the **display warranty software** command output
| Item | Description |
| --- | --- |
| Offering Name | Software name. |
| Offering Version | Software version. |
| EOS Date | Service end time. |
| Status | Software digital warranty status. |