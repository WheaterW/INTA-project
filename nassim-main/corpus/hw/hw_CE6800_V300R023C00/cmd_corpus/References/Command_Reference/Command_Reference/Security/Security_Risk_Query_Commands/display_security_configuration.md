display security configuration
==============================

display security configuration

Function
--------



The **display security configuration** command displays security configuration in the system.




Format
------

**display security configuration** [ **feature** *feature-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **feature** *feature-name* | Display security configuration of a specified feature. | The value is a string of 1 to 31 characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can filter the security configuration by specifying the feature.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display security configuration in the system.
```
<HUAWEI> display security configuration
Feature Name  : FTPS
Security Item : ftp security configuration
Item content  : Ftp server is disabled.Ftp Ipv6 server is disabled.IP block feat
                ure is disabled.The FTP server does not bind all interface.

Feature Name  : TELNET
Security Item : telnet security configuration
Item content  : The Telnet server function is used.The TELNET server bind all in
                terface.

```

# Display security configuration of the FTP feature.
```
<HUAWEI> display security configuration feature ftp
Feature Name  : FTPS
Security Item : ftp security configuration
Item content  : Ftp server is disabled.Ftp Ipv6 server is disabled.IP block feat
                ure is disabled.The FTP server does not bind all interface.

```

**Table 1** Description of the **display security configuration** command output
| Item | Description |
| --- | --- |
| Feature Name | Feature name. |
| Security Item | Security item. |
| Item content | Item content. |