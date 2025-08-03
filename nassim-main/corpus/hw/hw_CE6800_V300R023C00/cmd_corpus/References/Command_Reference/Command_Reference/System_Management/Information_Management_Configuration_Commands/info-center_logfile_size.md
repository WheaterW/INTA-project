info-center logfile size
========================

info-center logfile size

Function
--------



The **info-center logfile size** command sets a maximum size for each information file.

The **undo info-center logfile size** command restores the default size of each information file.



The default maximum size varies with log file types. The default maximum size is 8 MB for a common log file and 4 MB for a security log file.


Format
------

**info-center logfile** [ **security** ] **size** *size*

**undo info-center logfile** [ **security** ] **size**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **security** | Sets a maximum size for each security log file. | - |
| *size* | Specifies the maximum size of each information file. | The value is an integer, in MB   * If a log file type is not specified, size can be set to 4, 8, 16, or 32. * If security is specified, size can be set to an integer ranging from 1 to 4. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Logs generated during system operations are recorded in information files. If a single information file is too large, a large amount of disk space will be occupied. In this case, you can run this command to set the maximum size of a single information file.Information files are generated in xxx.log format. When the size of an information file exceeds the configured maximum size, the information file is compressed into a smaller file in standard log\_slot ID\_time.log.zip format.

**Configuration Impact**



When the size of an information file exceeds the configured maximum value, the information file is compressed into a smaller file in standard xxx.log.zip format.




Example
-------

# Set a maximum size for each information file to 32 MB, so that an information file is compressed into a smaller file when its size exceeds the maximum value.
```
<HUAWEI> system-view
[~HUAWEI] info-center logfile size 32

```