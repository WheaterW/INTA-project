display software info (All views)
=================================

display software info (All views)

Function
--------



The **display software info** command displays the software name and software file name of the running software package file.




Format
------

**display software info**


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

The software file name of the running software package file may have been changed. You can run this command to view the software name of the software package file to determine whether the running software package file is reliable.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display software package information, including only the current startup software package.
```
<HUAWEI> display software info
Startup software name:                    XXXXXXXXXX-XX.cc
Startup software file name:               CurrentStartup.cc

```

# Display software package information, including the current startup software package, installed independent feature package, and installed hardware package.
```
<HUAWEI> display software info
Startup software name:                                     XXXXXXXXXX-XX.cc
Startup software file name:                               CurrentStartup.cc

Startup feature software name:                        XXXXXXXXX-XXX.ccx
Startup feature software file name:                   XXXXX.ccx

Startup feature software name:                        YYYYYYYYY-YYY.ccx
Startup feature software file name:                  YYYYY.ccx

Startup extended-system software name:         Xxx_HARDWARE_001.cch
Startup extended-system software file name:   YYYYYY.cch

Startup extended-system software name:         Yyy_HARDWARE_002.cch
Startup extended-system software file name:   YYYYYY.cch

```

**Table 1** Description of the **display software info (All views)** command output
| Item | Description |
| --- | --- |
| Startup software name | Software name of the running software package file. |
| Startup software file name | Software file name of the running software package file. |
| Startup feature software name | Displays the software name of the installed independent feature package. |
| Startup feature software file name | Displays the file name of the installed independent feature package. |
| Startup extended-system software name | Displays the hardware name of the installed hardware package. |
| Startup extended-system software file name | Displays the file name of the installed hardware package. |