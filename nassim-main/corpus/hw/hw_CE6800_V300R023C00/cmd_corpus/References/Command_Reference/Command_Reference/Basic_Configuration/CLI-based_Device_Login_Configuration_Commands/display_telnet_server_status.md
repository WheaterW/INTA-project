display telnet server status
============================

display telnet server status

Function
--------

The **display telnet server status** command displays the current sessions information of the Telnet server.



Format
------

**display telnet server status**



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

You can view the current sessions information of the Telnet server after setting up a Telnet session. The display telnet server status command is used to display Telnet server sessions information.

**Prerequisites**

Establish a Telnet session.

If the Telnet session does not exist, this command does not display any information.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display the Telnet server status.
```
<HUAWEI> display telnet server status
Session 1: 
Source ip address : 192.168.1.1
VTY Index         : 0

Current number of sessions : 1

```


**Table 1** Description of the
**display telnet server status** command output

| Item | Description |
| --- | --- |
| Session | Display session information. |
| Source ip address | Source IP address of the telnet connection. |
| VTY Index | The absolute ID of the user interface. |
| Current number of sessions | Number of users currently connected. |