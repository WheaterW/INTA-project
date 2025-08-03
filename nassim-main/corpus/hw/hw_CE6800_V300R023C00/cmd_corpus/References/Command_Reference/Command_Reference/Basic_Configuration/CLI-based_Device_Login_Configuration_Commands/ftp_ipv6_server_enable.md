ftp ipv6 server enable
======================

ftp ipv6 server enable

Function
--------



The **ftp ipv6 server enable** command enables the FTP server ipv6 function on a device, allowing ipv6 FTP users to log in.

The **undo ftp ipv6 server** command disables the FTP server ipv6 function on a device, preventing ipv6 FTP users from logging in.



By default, the FTP server ipv6 function is disabled.


Format
------

**ftp ipv6 server enable**

**undo ftp ipv6 server** [ **enable** ]


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

To allow users to remotely manage files on the local client, you can run this command to enable the FTP server function, allowing the FTP users to log in.

**Configuration Impact**

* After the FTP server function is enabled, users can manage files in FTP mode.
* After the FTP server function is disabled, users cannot log in to the FTP server. The login users can perform only the quit operation.

**Precautions**

* The FTP protocol is not secure. You are advised to use the SFTP protocol, which is more secure.
* This command can be used only after the weak security algorithm/protocol feature package (WEAKEA) is installed using the **install feature-software WEAKEA** command.


Example
-------

# Enable FTP IPv6 server.
```
<HUAWEI> system-view
[~HUAWEI] ftp ipv6 server enable

```