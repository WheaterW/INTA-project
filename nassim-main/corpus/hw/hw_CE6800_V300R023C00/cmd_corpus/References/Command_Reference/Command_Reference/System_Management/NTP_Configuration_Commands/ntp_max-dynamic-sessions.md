ntp max-dynamic-sessions
========================

ntp max-dynamic-sessions

Function
--------



The **ntp max-dynamic-sessions** command sets the maximum number of dynamic NTP sessions that a device can set up.

The **undo ntp max-dynamic-sessions** command restores the maximum dynamic NTP session to the default value.



By default, a maximum of 100 sessions are allowed to be set.


Format
------

**ntp max-dynamic-sessions** *number*

**undo ntp max-dynamic-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Sets the maximum number of dynamic NTP sessions allowed to be set up. | The value is an integer ranging from 0 to 100. The default value is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command limits the number of dynamic sessions only.

**Precautions**

* This command limits the number of only dynamic sessions, not static sessions.
* Unicast server/client mode and peer mode are configured through the command line. So, sessions between them are static. Sessions set up in the broadcast and multicast modes are dynamic.
* Using this command does not affect the NTP session that has been set up. If the number of dynamic sessions exceeds the upper limit, dynamic sessions will not be created anymore. Configure this command only on the client. The server does not record the number of NTP sessions.If this command is the first NTP configuration command, the system automatically adds the ntp server disable/ntp ipv6 server disable command to the configuration file to disable the NTP server function. To enable the NTP service, run the undo ntp server disable/undo ntp ipv6 server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable/ntp ipv6 server disable command from the configuration file when you delete this command.


Example
-------

# Set the maximum number of NTP dynamic sessions allowed to be set up to 50.
```
<HUAWEI> system-view
[~HUAWEI] ntp max-dynamic-sessions 50

```