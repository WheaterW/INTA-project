info-center logbuffer channel
=============================

info-center logbuffer channel

Function
--------



The **info-center logbuffer channel** command allocates a channel for cached logs.

The **info-center logbuffer size** command sets the number of logs to be displayed.

The **undo info-center logbuffer channel** command deletes the channel allocated for cached logs.



A maximum of 512 logs are displayed by default.


Format
------

**info-center logbuffer channel** { *channel-number* | *channel-name* } [ **size** *logbuffersize* ]

**info-center logbuffer size** *logbuffersize* **channel** { *channel-number* | *channel-name* }

**undo info-center logbuffer channel**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel-number* | Specifies a channel number. | The value is an integer ranging from 0 to 9.  By default, a device outputs information to various destinations through channels listed in the following table.   * channel number:0, channel name:console, output destination:console. * channel number:1, channel name:monitor, output destination:remote terminal. * channel number:2, channel name:loghost, output destination:syslog server. * channel number:3, channel name:trapbuffer, output destination:trap buffer. * channel number:4, channel name:logbuffer, output destination:log buffer. * channel number:5, channel name:snmpagent, output destination:SNMP agent. * channel number:6, channel name:channel6, output destination:unspecified. * channel number:7, channel name:channel7, output destination:unspecified. * channel number:8, channel name:channel8, output destination:unspecified. * channel number:9, channel name:channel9, output destination:unspecified. |
| *channel-name* | Specifies a channel name. | The value is a string of 1 to 30 case-insensitive characters, spaces not supported. It cannot contain special characters, such as hyphens (-), slashes (/), or backslashes (\). |
| **size** *logbuffersize* | Specifies the number of logbuffer. | The value is an integer ranging from 0 to 10240. |
| **logbuffer** | Indicates the channel through which information is output to the log buffer. | - |
| **channel** | Specifies an information channel. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the number of logs to be displayed, run the info-center logbuffer size command.

**Configuration Impact**

If this command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Configure the channel through which information is output to the log buffer.
```
<HUAWEI> system-view
[~HUAWEI] info-center logbuffer channel logbuffer

```