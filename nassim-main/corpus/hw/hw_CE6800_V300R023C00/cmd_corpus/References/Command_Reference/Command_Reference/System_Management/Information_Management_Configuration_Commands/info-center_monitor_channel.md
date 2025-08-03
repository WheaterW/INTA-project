info-center monitor channel
===========================

info-center monitor channel

Function
--------



The **info-center monitor channel** command configures channels for outputting information to monitor destinations.

The **undo info-center monitor channel** command restores the default settings.



By default, channel number:1, channel name:monitor.


Format
------

**info-center monitor channel** { *channel-number* | *channel-name* }

**undo info-center monitor channel**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel-number* | Specifies the channel number. | The value is an integer ranging from 0 to 9, indicating that the system has 10 channels.  By default, a device outputs information to various destinations through channels listed in the following table.   * channel number:0, channel name:console, output destination:console. * channel number:1, channel name:monitor, output destination:remote terminal. * channel number:2, channel name:loghost, output destination:syslog server. * channel number:3, channel name:trapbuffer, output destination:trap buffer. * channel number:4, channel name:logbuffer, output destination:log buffer. * channel number:5, channel name:snmpagent, output destination:SNMP agent. * channel number:6, channel name:channel6, output destination:unspecified. * channel number:7, channel name:channel7, output destination:unspecified. * channel number:8, channel name:channel8, output destination:unspecified. * channel number:9, channel name:channel9, output destination:unspecified. |
| *channel-name* | Specifies the name of a channel, which can be the default channel name or a user-defined name. | The value is a string of 1 to 30 characters. The first character can be a letter only. The name cannot contain spaces or special characters, such as hyphens (-), slashes (/), or backslashes (\). |
| **monitor** | Indicates the channel through which information is output to a remote terminal. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To output the same information to destinations or output information from multiple channels to the same destination, run the info-center command to modify configurations about information channels. The following requirements can be met:

* Outputting the same information to destinations. For example, the information recorded by information files and the syslog server can be identical with that recorded by the trap buffer and the SNMP agent.
* Outputting information through each channel to a specific syslog server. For example, information can be output through channel 7 to a syslog server with IP address 192.168.0.1, but through channel 8 to a syslog server with IP address 192.168.0.2.

Example
-------

# Configure the channel through which information is output to a syslog server.
```
<HUAWEI> system-view
[~HUAWEI] info-center monitor channel monitor

```