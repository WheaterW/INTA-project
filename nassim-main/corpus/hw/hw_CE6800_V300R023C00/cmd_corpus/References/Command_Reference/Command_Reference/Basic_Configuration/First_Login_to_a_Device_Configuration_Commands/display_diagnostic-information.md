display diagnostic-information
==============================

display diagnostic-information

Function
--------



The **display diagnostic-information** command displays diagnostic information about the current system.




Format
------

**display diagnostic-information** [ *module-name* ] &<1-8> [ **slot** *slot-id* ] *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *module-name* | Displays diagnostic file information for the specified module. | - |
| **slot** *slot-id* | Displays diagnostic file information in a specified slot. | The value displayed on the device prevails. |
| *file-name* | Specifies the name of the file that stores diagnostic information. | The value is a string of 5 to 64 characters.  By default, the file path is flash:/ and the file name extension must be .txt or .zip. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When a fault occurs in the system, if it is difficult to determine the module that causes the fault, you can use this command to collect diagnostics information for locating the fault.



**Configuration Impact**

The command output includes the output for multiple **display** commands, such as display clock, display version, and display current-configuration. Running this command is equivalent to running these **display** commands in batches.

**Precautions**

When running this command:

* Running this command may cause high CPU usage for a short period of time.
* If file-name is specified, diagnostic information is saved to a specified file.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display diagnostic information and save the result to a.txt.
```
<HUAWEI> display diagnostic-information a.txt

```