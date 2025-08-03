display eva inspection history
==============================

display eva inspection history

Function
--------



The **display eva inspection history** command displays the execution history of the PMI script.




Format
------

**display eva inspection history**


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

You can run this command to query the execution history of the PMI script.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Query the execution history of the PMI script.
```
<HUAWEI> display eva inspection history
------------------------------------------------------------------------------------------------------------------------
RegisterTime            FileName       ServerType IpAddress            Port   UserName        Status    ResultFileName
----------------------------------------------------------------------------------------------------------------
2022-02-26 14:51:08   test_ftp.json    SFTP       192.168.1.1         22     admin           Running     -     
2022-02-26 16:28:48   test_ftp.json    SFTP       192.168.2.1        22     admin           Complete  1021900406271_
eva_inspection_20220226162859.zip
2022-02-26 14:51:08   test_ftp.json    -          -                    -      -               -     -         
------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display eva inspection history** command output
| Item | Description |
| --- | --- |
| RegisterTime | Time when a PMI script is registered and parsed. |
| FileName | Name of a PMI script file. |
| ServerType | Type of the server where the script is located.   * FTP: indicates that the script is automatically downloaded from the FTP server. * SFTP: indicates that the script is automatically downloaded from the SFTP server. * -: indicates that the script is manually downloaded from the server to the device. |
| IpAddress | IP address of the server where the script is located.   * -: indicates that the script is manually downloaded from the server to the device. |
| Port | Port number of the server where the script is located.   * -: indicates that the script is manually downloaded from the server to the device. |
| UserName | User name of the server where the script is located.   * -: indicates that the script is manually downloaded from the server to the device. |
| Status | Running status of the PMI script.   * Running: The script is running. * Complete: The script execution is complete. * Unconnected: The server fails to be connected. * NonExistence: The file does not exist on the server. * DownloadError: The file fails to be downloaded from the server. * UploadError: The device fails to upload the file to the server. * ScriptInvalid: The script content is invalid. * Uninstalled: The script is uninstalled before the script execution is complete. |
| ResultFileName | Name of the running result file. |