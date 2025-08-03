telnet client dscp
==================

telnet client dscp

Function
--------



The **telnet client dscp** command configures a DSCP value for the Telnet packets sent by a client.

The **undo telnet client dscp** command restores the default DSCP value of the Telnet packets sent by a client.



By default, the DSCP value of Telnet packets is 48.


Format
------

**telnet client dscp** *value*

**undo telnet client dscp** *value*

**undo telnet client dscp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies a DSCP value for the Telnet packets sent by a client. | The value is an integer ranging from 0 to 63. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To change the priority of Telnet packets sent by a client, you can run this command to change the DSCP value. A larger DSCP value indicates a higher priority.
* When you run the **undo** command to restore the default value of the DSCP field, the meanings of the value parameter are as follows:
* If value is not specified, the DSCP field is restored to the default value.
* If value is set to 48, the DSCP field is restored to the default value.
* If value is set to a non-48 value, the value must be the same as that in the configuration command. Otherwise, the **undo** command will fail to be executed.
* This command takes effect only for IPv4 packets.

Example
-------

# Set the DSCP value to 10 for the Telnet packets sent by a client.
```
<HUAWEI> system-view
[~HUAWEI] telnet client dscp 10

```