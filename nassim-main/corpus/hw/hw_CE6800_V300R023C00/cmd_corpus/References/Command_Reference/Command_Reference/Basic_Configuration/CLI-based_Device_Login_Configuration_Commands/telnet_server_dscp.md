telnet server dscp
==================

telnet server dscp

Function
--------



The **telnet server dscp** command configures a DSCP value for the Telnet packets sent by a server.

The **undo telnet server dscp** command restores the default DSCP value of the Telnet packets sent by a server.



By default, the DSCP value of Telnet packets is 48.


Format
------

**telnet server dscp** *value*

**undo telnet server dscp** *value*

**undo telnet server dscp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies a DSCP value for the Telnet packets sent by a server. | The value is an integer ranging from 0 to 63. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To change the priority of the Telnet packets sent by a server, run the **telnet server dscp** command to change the DSCP value of the packets. A greater DSCP value indicates a higher priority.The priority of this command is higher than that of the **host-packet type dscp** command. If a DSCP value is configured using this command, the configured value takes effect. If a DSCP value is configured using the **host-packet type dscp** command rather than this command, the value configured using the **host-packet type dscp** command takes effect. If no DSCP value is configured using the preceding commands, the default DSCP value is used.When you run the **undo telnet server dscp** command:

* If value is not specified, the DSCP field is restored to the default value.
* If value is 48, the DSCP field is restored to the default value.
* If value is set to a non-48 value, the value must be the same as value in the **telnet server dscp** command. Otherwise, the command execution fails.The command only takes effect for IPv4 packets.

**Precautions**

The Telnet protocol has security risks. You are advised to use the SSH v2 protocol.


Example
-------

# Set the DSCP value to 10 for the Telnet packets sent by a server.
```
<HUAWEI> system-view
[~HUAWEI] telnet server dscp 10

```