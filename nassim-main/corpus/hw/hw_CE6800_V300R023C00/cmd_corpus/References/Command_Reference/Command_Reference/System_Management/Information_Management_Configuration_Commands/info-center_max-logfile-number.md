info-center max-logfile-number
==============================

info-center max-logfile-number

Function
--------



The **info-center max-logfile-number** command sets the maximum number of compressed information files to be stored.

The **undo info-center max-logfile-number** command restores the default maximum number of compressed information files to be stored.



The default maximum numbers of common log files (log.log) and security log files (security.log) are both 200.


Format
------

**info-center max-logfile-number** [ **security** ] *filenumbers*

**undo info-center max-logfile-number** [ **security** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **security** | Indicates security log files. | - |
| *filenumbers* | Specifies the maximum number of compressed information files to be stored. | The value is an integer ranging from 3 to 500. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The total number of compressed files must be limited in the following cases:

* An increasing number of compressed files are generated as system actions are taken during system operations, and the excessive compressed files on a device consume plenty of disk space resources.
* Users want to view only the latest compressed files.

**Precautions**



This command only sets the maximum numbers of common and security log files. The numbers of other log file types are limited by the available storage space. To query the storage path, run the **display logfile storage-usage** command. If the number of compressed files generated exceeds the limit, the system deletes the earliest compressed files.If the number of stored compressed files is greater than the default value, system performance is much affected. Therefore, set the maximum value properly as needed. If plenty of compressed files exist, manually delete some of them or wait for the system to automatically delete them when the existing number exceeds the configured maximum value. If you do not manually delete them, CPU usage increases in a short period of time.




Example
-------

# Set the maximum number of compressed files to be stored to 100.
```
<HUAWEI> system-view
[~HUAWEI] info-center max-logfile-number 100

```