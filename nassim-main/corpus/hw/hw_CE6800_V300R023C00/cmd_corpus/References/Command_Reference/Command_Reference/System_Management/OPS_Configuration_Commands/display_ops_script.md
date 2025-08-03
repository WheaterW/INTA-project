display ops script
==================

display ops script

Function
--------



The **display ops script** command displays information about an OPS script.




Format
------

**display ops script** [ *dir-or-file-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dir-or-file-name* | Specifies a directory or file name. | The value is a string of 1 to 127 characters. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view information about an OPS script, run the display ops script command. The scripts that are saved in the $\_user directory are visible but cannot be modified or deleted.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about an OPS script.
```
<HUAWEI> display ops script
--------------------------------------------------------------------------------
  Index      Size(Byte)  Filename
--------------------------------------------------------------------------------
      0            6273  OPS_get_esn.py
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ops script** command output
| Item | Description |
| --- | --- |
| Index | Index of a file. |
| Size(Byte) | Size of a file. |
| Filename | File name. |