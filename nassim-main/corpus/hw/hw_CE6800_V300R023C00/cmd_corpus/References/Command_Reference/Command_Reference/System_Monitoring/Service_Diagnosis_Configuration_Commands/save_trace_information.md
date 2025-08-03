save trace information
======================

save trace information

Function
--------



The **save trace information** command saves diagnosis information in the buffer area as a file.




Format
------

**save trace information**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After you specify the parameter file file-name in the **trace object** command to save diagnosis information as files to the default root directory on the storage device, the system saves diagnosis information in the buffer area until the buffer is full. To prevent data loss, the system automatically saves diagnosis information in the buffer area as the file file-name. Before the buffer becomes full, to view real-time diagnosis information, run the **save trace information** command to save diagnosis information in the buffer area as a file.

**Prerequisites**

The device has been configured to export diagnosis information as a file using the **trace object** command.


Example
-------

# Save diagnosis information as a file.
```
<HUAWEI> system-view
[~HUAWEI] save trace information

```