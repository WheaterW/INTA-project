install eva script
==================

install eva script

Function
--------



The **install eva script** command installs an EVA script.

The **uninstall eva script** command uninstalls an EVA script.




Format
------

**install eva script** *fileName* [ **inspection** ]

**uninstall eva script** *fileName*

**uninstall eva script inspection**

**install eva script** *fileName* **inspection** { **ftp** | **sftp** } { **ipv4** *ipv4Address* | **ipv6** *ipv6Address* } **port** *portNum* **username** *userName* **password** *pwd* [ **vpn-instance** *vpnInstance* ] [ **server-path** *serverPath* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *fileName* | Indicates the name of the EVA script file, which is in JSON format. | The value is a string of 1 to 63 characters. It contains the script path. The specified script name must exist on the device. If the script is in the root directory of the flash memory, you do not need to specify the path. |
| **inspection** | Indicates that a PMI script is to be installed. | - |
| **ftp** | Indicates the FTP server. | - |
| **sftp** | Indicates the SFTP server. | - |
| **ipv4** *ipv4Address* | Indicates the IPv4 address of the server. | It is in dotted decimal notation. |
| **ipv6** *ipv6Address* | Indicates the IPv6 address of the server. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **port** *portNum* | Indicates the port number of the server. | The value is an integer ranging from 1 to 65535. |
| **username** *userName* | Indicates the user name of the server. | The value is a string of 1 to 255 characters. |
| **password** *pwd* | Indicates the password of the server. | The value is a string of 1 to 255 characters. |
| **vpn-instance** *vpnInstance* | Indicates the name of the VPN instance used for logging in to the server. | The value is a string of 1 to 31 characters. |
| **server-path** *serverPath* | Indicates directory for storing files on the server. | The value is a string of 1 to 63 characters. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

EVA allows you to install user-defined scripts on devices for fault analysis and device health check. If you do not need to continue running a script, EVA allows you to uninstall the script file.When the FTP or SFTP server parameters related to PMI are specified, EVA can automatically download scripts from the specified server, install scripts, and upload script execution results.SFTP is recommended because it is more secure than FTP.

**Precautions**

1. Before the PMI script is executed or uninstalled, you are not allowed to install the PMI script again.
2. The content of a single script in the PMI script file is compressed in single-line mode. Each script must occupy one line.
3. If the specified script does not exist when you uninstall the PMI script, no error message will be reported.
4. If you specify PMI-related FTP or SFTP server parameters, you need to run the **install feature-software WEAKEA** command to install the weak security algorithm/protocol feature package (WEAKEA).


Example
-------

# Install an EVA script.
```
<HUAWEI> install eva script test.json
Starting to parse the script...

```