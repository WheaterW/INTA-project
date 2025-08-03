display ssh server status
=========================

display ssh server status

Function
--------

The **display ssh server status** command displays the global configuration of the SSH server.



Format
------

**display ssh server status**



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

**Usage Scenario**

After configuring the SSH attributes, you can run the display ssh server status command to view the global configuration.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display SSH server status.
```
<HUAWEI> display ssh server status
SSH Version                                : 2.0
SSH authentication timeout (Seconds)       : 60
SSH authentication retries (Times)         : 3
SSH server key generating interval (Hours) : 0
SSH version 1.x compatibility              : Enable
SSH server keepalive                       : Disable
SFTP IPv4 server                           : Disable
SFTP IPv6 server                           : Disable
STELNET IPv4 server                        : Enable
STELNET IPv6 server                        : Enable
SNETCONF IPv4 server                       : Enable
SNETCONF IPv6 server                       : Enable
SNETCONF IPv4 server port(830)             : Disable
SNETCONF IPv6 server port(830)             : Disable
SCP IPv4 server                            : Enable
SCP IPv6 server                            : Enable
SSH port forwarding                        : Disable
SSH IPv4 server port                       : 22
SSH IPv6 server port                       : 22
ACL name                                   :
ACL number                                 :
ACL6 name                                  : 
ACL6 number                                :
SSH server ip-block                        : Enable

```


**Table 1** Description of the
**display ssh server status** command output

| Item | Description |
| --- | --- |
| SSH Version | Indicates the version of the SSH server. |
| SSH authentication timeout (Seconds) | Indicates the timeout period of SSH authentication in seconds. |
| SSH authentication retries (Times) | Indicates the number of SSH authentication retries. |
| SSH server key generating interval (Hours) | Indicates the interval of SSH server key generation in hours. |
| SSH version 1.x compatibility | Indicates the status of SSH version 1.x compatibility. It can be any one of the following:   * Enable. * Disable. |
| SSH server keepalive | Indicates the status of SSH server keep alive feature. It can be any one of the following:   * Enable. * Disable. |
| SSH IPv4 server port | Indicates the IPv4 port number of SSH server. |
| SSH IPv6 server port | Indicates the IPv6 port number of SSH server. |
| SSH server ip-block | Indicates the status of SSH server from locking client IP addresses. It can be any one of the following:   * Enable: SSH server is enabled to lock client IP addresses. * Disable: SSH server is disabled to lock client IP addresses. |
| SSH port forwarding | Indicates the SSH port forwarding status. It can be any one of the following:  -Enable.  -Disable. |
| SFTP IPv4 server | Indicates the IPv4 status of SFTP server. It can be any one of the following:   * Enable: The SFTP server is enabled. * Disable: The SFTP server is disabled. |
| SFTP IPv6 server | Indicates the IPv6 status of SFTP server. It can be any one of the following:   * Enable: The SFTP server is enabled. * Disable: The SFTP server is disabled. |
| STELNET IPv4 server | Indicates the IPv4 status of STelnet server. It can be any one of the following:   * Enable: The STelnet server is enabled. * Disable: The STelnet server is disabled. |
| STELNET IPv6 server | Indicates the IPv6 status of STelnet server. It can be any one of the following:   * Enable: The STelnet server is enabled. * Disable: The STelnet server is disabled. |
| SNETCONF IPv4 server | Indicates the IPv4 status of SNETCONF server. It can be any one of the following:   * Enable: The SNETCONF server is enabled. * Disable: The SNETCONF server is disabled. |
| SNETCONF IPv6 server | Indicates the IPv6 status of SNETCONF server. It can be any one of the following:   * Enable: The SNETCONF server is enabled. * Disable: The SNETCONF server is disabled. |
| SNETCONF IPv4 server port(830) | Indicates the IPv4 status of the well-known port on the SSH server. It can be any one of the following:   * Enable. * Disable.   The protocol inbound ssh port 830 command configures well-known port 830 to establish an NETCONF connection. |
| SNETCONF IPv6 server port(830) | Indicates the IPv6 status of the well-known port on the SSH server. It can be any one of the following:   * Enable. * Disable.   The protocol inbound ssh port 830 command configures well-known port 830 to establish an NETCONF connection. |
| SCP IPv4 server | Indicates IPv4 the status of SCP server. It can be any one of the following:   * Enable. * Disable. |
| SCP IPv6 server | Indicates IPv6 the status of SCP server. It can be any one of the following:   * Enable. * Disable. |
| ACL name | Indicates the configured ACL name. |
| ACL number | Indicates the configured ACL number. |
| ACL6 name | Indicates the configured IPv6 ACL name. |
| ACL6 number | Indicates the configured IPv6 ACL number. |