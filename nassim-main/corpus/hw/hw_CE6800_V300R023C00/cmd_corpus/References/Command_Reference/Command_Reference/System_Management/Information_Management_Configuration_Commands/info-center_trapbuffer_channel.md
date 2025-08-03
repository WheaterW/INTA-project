info-center trapbuffer channel
==============================

info-center trapbuffer channel

Function
--------



The **info-center trapbuffer size** command sets the number of traps to be displayed.

**info-center trapbuffer channel** commands are used to configure channels for outputting trapbuffer information.

The **undo info-center trapbuffer channel** command restores the default configuration.



By default, A maximum of 256 traps can be displayed, the channel number is 3 and the channel name is trapbuffer.


Format
------

**info-center trapbuffer channel** { *channel-number* | *channel-name* } [ **size** *size* ]

**info-center trapbuffer size** *size* **channel** { *channel-number* | *channel-name* }

**undo info-center trapbuffer channel**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel-number* | Specifies the channel number. | The value is an integer ranging from 0 to 9, indicating that the system has 10 channels.  By default, a device outputs information to various destinations through channels listed in the following table.   * channel number:0, channel name:console, output destination:console. * channel number:1, channel name:monitor, output destination:remote terminal. * channel number:2, channel name:loghost, output destination:syslog server. * channel number:3, channel name:trapbuffer, output destination:trap buffer. * channel number:4, channel name:logbuffer, output destination:log buffer. * channel number:5, channel name:snmpagent, output destination:SNMP agent. * channel number:6, channel name:channel6, output destination:unspecified. * channel number:7, channel name:channel7, output destination:unspecified. * channel number:8, channel name:channel8, output destination:unspecified. * channel number:9, channel name:channel9, output destination:unspecified. |
| *channel-name* | Specifies the name of a channel, which can be the default channel name or a user-defined name. | The value is a string of 1 to 30 characters. The first character can be a letter only. The name cannot contain spaces or special characters, such as hyphens (-), slashes (/), or backslashes (\). |
| **size** *size* | Specifies the number of logbuffer. | The value is an integer ranging from 0 to 1024. |
| **trapbuffer** | Indicates the channel through which information is output to the trap buffer. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the number of traps to be output, run the info-center trapbuffer size command.To output the same information to destinations or output information from multiple channels to the same destination, run the info-center command to modify configurations about information channels. The following requirements can be met:

* Outputting the same information to destinations. For example, the information recorded by information files and the syslog server can be identical with that recorded by the trap buffer and the SNMP agent.
* Outputting information through each channel to a specific syslog server. For example, information can be output through channel 7 to a syslog server with IP address 192.168.0.1, but through channel 8 to a syslog server with IP address 192.168.0.2.

**Prerequisites**

The trap display function has been enabled. Otherwise, traps cannot be output to the trap buffer for user query.

**Configuration Impact**

If the info-center trapbuffer size command is run more than once, the latest configuration overrides the previous one.

**Precautions**



If the number of traps to be displayed is set too small, some traps cannot be queried. If the number of traps to be displayed is set too large, excessive repeated traps may be displayed. The default number of traps to be displayed is recommended.




Example
-------

# Configure the device to output information through the trap buffer.
```
<HUAWEI> system-view
[~HUAWEI] info-center trapbuffer channel trapbuffer

```

# Configure the device to send traps to the trap buffer and set the number of traps to be displayed to 30.
```
<HUAWEI> system-view
[~HUAWEI] info-center trapbuffer size 30 channel trapbuffer

```