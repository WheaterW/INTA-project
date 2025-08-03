ssh client dscp
===============

ssh client dscp

Function
--------



The **ssh client dscp** command configures a DSCP value for the SSH packets sent by a client.

The **undo ssh client dscp** command restores the default DSCP value of the SSH packets sent by a client.



By default, the DSCP value of SSH packets is 48.


Format
------

**ssh client dscp** *value*

**undo ssh client dscp** *value*

**undo ssh client dscp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies a DSCP value for the SSH packets sent by a client. | The value is an integer ranging from 0 to 63. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To change the priority of the SSH packets sent by a client, run the ssh client dscp command to change the DSCP value of the packets. A greater DSCP value indicates a higher priority.
* When you run the undo ssh client dscp command:
* If value is not specified, the DSCP field is restored to the default value.
* If value is 48, the DSCP field is restored to the default value.
* If value is set to a non-48 value, the value must be the same as value in the telnet server dscp command. Otherwise, the command execution fails.
* The command only takes effect for IPv4 packets.

Example
-------

# Set the DSCP value to 10 for the SSH packets sent by a client.
```
<HUAWEI> system-view
[~HUAWEI] ssh client dscp 10

```