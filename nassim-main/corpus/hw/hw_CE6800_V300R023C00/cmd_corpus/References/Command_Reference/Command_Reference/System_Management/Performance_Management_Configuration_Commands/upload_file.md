upload file
===========

upload file

Function
--------



The **upload file** command enables the device to upload performance statistics files to a PM server.




Format
------

**upload** *request-name* **file** { *filename* } &<1-16>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *request-name* | Specifies the name of a request for uploading performance statistics files. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| *filename* | Specifies the name of a performance statistics file.  The file name can contain the file path (absolute path or relative path). If multiple files are specified at the same time, file names are separated using blank spaces. | The value is a string of 1 to 255 case-insensitive characters, spaces not supported. |



Views
-----

Performance management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The system generates performance statistics files based on the collected performance statistics at a specified interval. To enable the device to upload performance statistics files to a PM server, run the upload file command. A maximum of 16 performance statistics files can be uploaded at a time.By default, performance statistics files are saved to the path cfcard:/PmData. You can name the performance statistics files in the specified path after running the upload command, or you can specify the path and file name in any path.



**Prerequisites**

Ensure that the configurations have been complete:

* The **ssh client first-time enable** command has been run in the system view to enable initial authentication on the SSH client.
* The **upload-config request-name server server-name** command has been run in the PM view to configure basic information about the PM server to which performance statistics files are uploaded.

**Follow-up Procedure**

View the performance statistics on the PM server.


Example
-------

# Configure the device to upload performance statistics file to a PM server.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] commit
[~HUAWEI-pm-server-a] quit
[~HUAWEI-pm] statistics enable
[*HUAWEI-pm] upload-config req1 server a
[*HUAWEI-pm] upload req1 file a20110422210001.txt

```