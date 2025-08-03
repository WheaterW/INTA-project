display ftp client
==================

display ftp client

Function
--------



The **display ftp client** command views the current configuration status of FTP client.




Format
------

**display ftp client**


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

After setting the source IP address of an FTP client, you can run the display ftp client command to view the configuration. If ftp client source is not specified, the source IP address of FTP client is 0.0.0.0 by default.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the source IP address of the FTP client.
```
<HUAWEI> display ftp client
SrcIPv4Addr         : 10.18.26.233

```

# Display the source interface of the FTP client.
```
<HUAWEI> display ftp client
Interface Name      : LoopBack0

```

**Table 1** Description of the **display ftp client** command output
| Item | Description |
| --- | --- |
| SrcIPv4Addr | Indicates the source IPv4 address of the FTP client. |
| Interface Name | Indicates the source interface of the FTP client. |