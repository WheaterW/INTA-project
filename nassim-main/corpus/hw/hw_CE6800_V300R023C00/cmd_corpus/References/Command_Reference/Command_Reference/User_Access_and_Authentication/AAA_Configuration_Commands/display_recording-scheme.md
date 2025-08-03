display recording-scheme
========================

display recording-scheme

Function
--------



The **display recording-scheme** command displays the configuration of recording schemes.




Format
------

**display recording-scheme** [ **name** *recording-scheme-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *recording-scheme-name* | Specifies the name of a recording scheme. | The value is a string of 1 to 32 case-sensitive characters, and cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The display recording-scheme command displays the configuration of recording schemes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the recording scheme scheme0.
```
<HUAWEI> display recording-scheme name scheme0
-----------------------------------------------------------------
 Recording-scheme-name           : scheme0
 HWTACACS-template-name          : tacas-1
----------------------------------------------------------------

```

**Table 1** Description of the **display recording-scheme** command output
| Item | Description |
| --- | --- |
| Recording-scheme-name | Name of the recording scheme. To create a recording scheme, run the recording-scheme command. |
| HWTACACS-template-name | Name of the HWTACACS server template associated with the recording scheme. To associate an HWTACACS server template with a recording scheme, run the recording-mode hwtacacs command. |