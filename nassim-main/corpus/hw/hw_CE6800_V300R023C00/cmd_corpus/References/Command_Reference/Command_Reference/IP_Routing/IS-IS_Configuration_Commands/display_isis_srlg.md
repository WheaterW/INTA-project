display isis srlg
=================

display isis srlg

Function
--------



The **display isis srlg** command displays shared risk link group (SRLG) information.




Format
------

**display isis** [ *process-id* ] **srlg** { *srlgGroupId* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| *srlgGroupId* | Specifies an SRLG ID. | The value is an integer ranging from 0 to 4294967295. |
| **all** | Indicates all SRLGs. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After interfaces are added to SRLGs, you can run the display isis srlg command to check the SRLG information. If neither IS-IS process ID nor SRLG number is specified, the command displays the information about all SRLGs.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display SRLG information.
```
<HUAWEI> display isis srlg all
Total SRLG supported : 4000
Total SRLG configured : 3

                           SRLG for ISIS(1)
                   --------------------------------
 SRLG          10:      100GE1/0/1       100GE1/0/2       100GE1/0/3

```

**Table 1** Description of the **display isis srlg** command output
| Item | Description |
| --- | --- |
| Total SRLG supported | Maximum number of supported SRLGs. |
| Total SRLG configured | Number of configured SRLGs. |
| SRLG 10 | Interfaces in the SRLG. |