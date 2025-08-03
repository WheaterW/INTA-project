info-center loghost domain
==========================

info-center loghost domain

Function
--------



The **info-center loghost domain** command configures a device to output logs to a syslog server.

The **undo info-center loghost domain** command disables a device from outputting logs to a syslog server.



A device does not output logs to any syslog server by default.


Format
------

**info-center loghost domain** *domain-name* [ { **local-time** | **utc** } | **channel** { *channel-number* | *channel-name* } | { **public-net** | **vpn-instance** *vpn-instance-name* } | **source-ip** *source-ip-address* | **facility** *local-num* | **level** *level-num* | **port** *server-port* | **transport** { **udp** | **tcp** { [ **version** **rfc6587** ] [ **ssl-policy** *policy-name* [ [ **security** ] | [ **verify-dns-name** *dns-name* ] ] \* ] } } | **brief** ] \*

**undo info-center loghost domain** *domain-name* [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **local-time** | Specifies the local time. If this parameter is not specified, the UTC time is used by default. | The default value is UTC. |
| **utc** | Specifies the UTC time. If this parameter is not specified, the UTC time is used by default. | - |
| **channel** | Specifies a channel number. | - |
| *channel-number* | Specifies a channel number. | The value is an integer ranging from 0 to 9.   * 0: console * 1: monitor * 2: loghost * 3: trapbuffer * 4: logbuffer * 5: snmpagent * 6: channel6 * 7: channel7 * 8: channel8 * 9: channel9 |
| *channel-name* | Specifies a channel name. | The value is a string:   * console: console * monitor: remote terminal * loghost: syslog server * trapbuffer: trap buffer * logbuffer: log buffer * snmpagent: SNMP agent * channel6: unspecified * channel7: unspecified * channel8: unspecified * channel9: information file |
| **public-net** | Indicates the logs sent to a syslog server over the public network. | - |
| **vpn-instance** *vpn-instance-name* | Specifies name of a virtual private network (VPN) instance of a syslog server. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **source-ip** *source-ip-address* | Specifies the source IPv4 address of packets to be sent to a syslog server. | The value is in dotted decimal notation. |
| **facility** *local-num* | Specifies a syslog server facility that is used to identify the log information source. You can use this parameter to plan a local value for the log information of a specified device, so that the syslog server can handle received log information based on the parameter. | The value is of the enumerated type and can be local0, local1, local2, local3, local4, local5, local6, or local7. The default value is local7. |
| **level** *level-num* | Specifies a log level. | The value is an enumerated type:   * emergencies: an emergency error. * alert: an error that needs to be corrected immediately * critical: a major error * error: a minor error * warning: a potential error * notification: information that needs to be noticed * informational: an informational message * debugging: detailed information for debugging use |
| **port** *server-port* | Specifies the destination port number of packets to be sent to a syslog server. | The value is an integer ranging from 1 to 65535.   * If UDP is used, the default port number is 514. * If the transmission mode is TCP, the default port number is 601. * If the TCP-based SSL encryption mode is used, the default port number is 6514. |
| **transport** | Specifies the information transmission mode. If this parameter is not specified, the default transmission mode is UDP. | - |
| **udp** | Indicates that the information transport mode is UDP. | - |
| **tcp** | Indicates that the information transport mode is TCP. | - |
| **version** | Specifies an RFC version. | - |
| **rfc6587** | Specifies RFC 6587. If this parameter is specified, TCP packets are sent in RFC 6587 format and carry packet length information. If this parameter is not specified, TCP packets are sent in RFC 5424 format by default and do not carry packet length information. | - |
| **ssl-policy** *policy-name* | Specifies the name of a Secure Sockets Layer (SSL) policy when packets are transmitted using TCP.  SSL encrypted transmission provides high security. If packets are transmitted on insecure networks, configure SSL encrypted transmission by specifying ssl-policy policy-name. If packets are transmitted on secure networks, configure UDP transmission mode by specifying udp or TCP transmission mode by specifying tcp. | The value is a string of 1 to 23 characters that can contain case-insensitive letters, underscores (\_), and digits. |
| **security** | Specifies a security log host.  If the security parameter is set, the system sends only security logs to the log host. | - |
| **verify-dns-name** *dns-name* | Specifies the DNS server certificate name for the logging host. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| **brief** | Sends logs to a log host in brief mode. | - |
| **domain** *domain-name* | Specifies the DNS domain name of a log host. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a device to output logs to a syslog server, run the **info-center loghost** command. The system logs information about device operations in real time. These logs can be output to the syslog servers for storage and query. If a problem occurs, you can check the logs to learn about what happened to the device during device operation and analyze fault causes.You can choose whether to set brief as needed:

* When brief is not set, logs are sent to the log host in non-brief mode. The log content is displayed in the format of timestamp/host name/module name/log level/summary/log details.
* When brief is set, logs are sent to the log host in brief mode. The log content contains only details output by each module and is displayed in the format of timestamp/host name/log details.For example:
* When brief is not set, the log content is displayed as follows:May 15 2016 21:48:33 223.171 %%01SSH/5/SSH\_USER\_LOGIN\_FAIL(s):CID=0x80932723; The SSH user failed to login. (ServiceType=\*\*, FailedReason=Client requested disconnection, UserName=u2000test, IPAddress=22.22.23.23, VPNInstanceName=\_public\_.)
* When brief is set, the log content is displayed as follows:May 15 2016 21:48:33 223.171 : The SSH user failed to login. (ServiceType=\*\*, FailedReason=Client requested disconnection, UserName=u2000test, IPAddress=22.22.23.23, VPNInstanceName=\_public\_.)

**Prerequisites**

Information management has been enabled using info-center enable, and the IP address of a syslog server is reachable.

**Configuration Impact**

Logs record information about users' operations on an existing device (such as command configuration operation) and specific events (such as a network connection failure). After the **info-center loghost** command is run, an existing device outputs generated logs to the specified syslog server.

**Precautions**

Rules for a single host to select a VPN

* Rule 1: If the **info-center loghost** command is run with vpn-instance specified, the specified VPN is used as the host's VPN. Otherwise, refer to rule 2.
* Rule 2: If the **set net-manager vpn-instance** command is run to configure a global VPN, the global VPN is used as the host's VPN. Otherwise, refer to rule 3.
* Rule 3: The public network is used to send logs.


Example
-------

# Configure a device to output logs to the syslog server
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] info-center loghost 3.3.3.3 level critical
Warning: The configured loghost level does not take effect on security logs.
[~HUAWEI] info-center loghost domain www.huawei.com level critical
Warning: The configured loghost level does not take effect on security logs.

```

# Configure a device to output logs to the syslog server with the domain name www.huawei.com.
```
<HUAWEI> system-view
[~HUAWEI] info-center loghost domain www.huawei.com vpn-instance vrf1
Warning: There is security risk as this operation enables a non secure syslog protocol.

```