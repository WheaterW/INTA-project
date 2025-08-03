display info-center
===================

display info-center

Function
--------



The **display info-center** command displays all information that information management records.




Format
------

**display info-center**


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

To view the information that information management records, run the display info-center command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information that information management records.
```
<HUAWEI> display info-center
Information Center:enabled
Log host:
        10.0.0.1, channel number 2, channel name loghost,
Console:
        channel number : 0, channel name : console
Monitor:
        channel number : 1, channel name : monitor
SNMP Agent:
        channel number : 5, channel name : snmpagent
Log buffer:
        enabled,max buffer size 10240, current buffer size 512,
current messages 506, channel number : 4, channel name : logbuffer
dropped messages 0, overwritten messages 0
Trap buffer:
        enabled,max buffer size 1024, current buffer size 256,
current messages 256, channel number:3, channel name:trapbuffer
dropped messages 0, overwritten messages 1057
logfile:
        channel number : 9, channel name : logfile, language : English
Information timestamp setting:
        log - date, trap - date, debug - date millisecond

```

**Table 1** Description of the **display info-center** command output
| Item | Description |
| --- | --- |
| Information Center | Whether information management is enabled.   * enabled. * disabled. |
| Information timestamp setting | Timestamp format of logs, traps, and debugging information:   * boot. * date. * short-date. * format-date. * none. |
| Log host | Syslog server state, including the IP address of the syslog server, the channel number used and channel name, language, syslog server level, and VPN instance number. |
| Log buffer | Usage state of the log buffer, including the enabled/disabled state, maximum size, current size, the number of current logs, channel name, channel number, the number of discarded logs, and the number of overwritten logs. |
| SNMP Agent | Usage state of the SNMP agent, including the name and number of the channel used for the SNMP agent. |
| Trap buffer | Usage state of the trap buffer, including the enabled/disabled state, maximum size, current size, the number of current traps, channel name, channel number, the number of discarded traps, and the number of overwritten traps. |
| Console | Usage state of the console interface, including the name and number of the channel used for the console interface. |
| Monitor | Usage state of the monitoring interface, including the name and number of the channel used for the monitoring interface. |
| logfile | Usage state of the information file, including the name and number of the channel through which information is output to the information file, and language. |