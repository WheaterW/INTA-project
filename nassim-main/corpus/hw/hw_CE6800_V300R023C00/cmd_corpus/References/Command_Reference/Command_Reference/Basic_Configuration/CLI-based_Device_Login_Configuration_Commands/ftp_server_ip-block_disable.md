ftp server ip-block disable
===========================

ftp server ip-block disable

Function
--------



The **ftp server ip-block disable** command disables an FTP server from locking client IPv4 and IPv6 addresses.

The **undo ftp server ip-block disable** command enables an FTP server to lock client IPv4 or IPv6 addresses.



By default, an FTP server is enabled to lock client ipv4 and ipv6 addresses.


Format
------

**ftp server ip-block disable**

**undo ftp server ip-block disable**


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

* If an FTP server is enabled to lock client IP addresses, a client IP address is locked when the number of FTP authentication failures reaches the upper limit in a specific period of time. Client IPv4 and IPv6 addresses being locked fail the authentication and are displayed in the **display ftp server ip-block list** command output.
* If an FTP server is disabled from locking client IP addresses, the **display ftp server ip-block list** command does not display any client IP address that is locked because of authentication failures.
* IP addresses being locked are unlocked immediately after the FTP server is disabled from locking client IP addresses.

**Precautions**

* The FTP protocol has security risks. You are advised to use the SFTP protocol.
* To improve security, you are advised to enable the FTP server to lock client IP addresses.

Example
-------

# Disable an FTP server from locking client IP addresses.
```
<HUAWEI> system-view
[~HUAWEI] ftp server ip-block disable

```