ftp server enable
=================

ftp server enable

Function
--------



The **ftp server enable** command enables the FTP server function on a device, allowing FTP users to log in.

The **undo ftp server** command disables the FTP server function on a device, preventing FTP users from logging in.



By default, the FTP server function is disabled.


Format
------

**ftp server enable**

**undo ftp server** [ **enable** ]


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

To ensure that users can remotely manage files on the local client, run the **ftp server enable** command to enable the FTP server function, allowing the FTP users to log in.

**Configuration Impact**

* After the FTP server function is enabled, users can manage files in FTP mode.
* After the FTP server function is disabled, users cannot log in to the FTP server. The login users can perform only the quit operation.
* The command ftp server enable enables the only the IPv4 function.

**Precautions**

* In addition to running the **ftp server enable** command, you need to run the **ftp server source** command to enable the FTP server function on the device.
* Use SFTP because FTP is not secure.
* This command is available only after the weak security algorithm/protocol feature package (WEAKEA) command has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Enable FTP server.
```
<HUAWEI> system-view
[~HUAWEI] ftp server enable

```