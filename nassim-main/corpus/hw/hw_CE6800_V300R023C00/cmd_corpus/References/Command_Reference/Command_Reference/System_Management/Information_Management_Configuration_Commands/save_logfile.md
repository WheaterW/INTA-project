save logfile
============

save logfile

Function
--------



The **save logfile** command saves logs in the log buffer into information files.




Format
------

**save logfile**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The system records what happens to a device during device operations as logs. To reduce the times of writing the storage, the device caches logs in memory before writing them into information files. The device immediately writes logs cached in the memory into information files when the log buffer is full or a timer expires.If the log buffer is not full or the timer does not expire, run the **save logfile** command to manually write logs in the memory into information files.



**Prerequisites**



Logs must be generated before this command is run to effectively save logs. If new logs are not generated in the system or logs are just saved, null information is saved with this command.



**Configuration Impact**

After the **save logfile** command is run, logs are saved into information files. The size of each information file is 8 MB by default.

**Follow-up Procedure**

Run the **display logfile** command to view log details.

**Precautions**

The cached data for information files and the cached log data displayed with the **display logfile** command are independent of each other and do not affect each other.NOTE:

* After the command is run, logs in the log file are sorted based on the log generation time.
* After the command is run, the system displays whether logs are successfully saved without displaying whether logs are successfully sorted. To check whether logs are successfully sorted, run the **display info-center log-server sort-result** command.


Example
-------

# Save logs in the log buffer into information files.
```
<HUAWEI> save logfile
Info: Save log file successfully.

```