display netconf session (All views)
===================================

display netconf session (All views)

Function
--------



The **display netconf session** command displays information about a NETCONF session.




Format
------

**display netconf session**


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

To view information about a NETCONF session, run the display netconf session command. The session information helps you to check failed connections or whether a maximum of sessions have been created.A maximum of 100 capabilities with 128 bytes each can be displayed for a session.

* If there are more than 100 capabilities, the system displays three dots at the end.
* If the capability length is more than 128 bytes, the system displays two dots at the end.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about NETCONF sessions.
```
<HUAWEI> system-view
[~HUAWEI] display netconf session
------------------------------------------------------------------------------------------------------------------------------------
NETCONF Session ID   : 18265
Transport            : netconf-ssh
User Name            : huawei
Host Identifier      : 10.1.1.1
Login Time           : 2019-09-17 17:37:02
Input Rpc            : 755
Input Bad Rpc        : 1
Output Rpc Error     : 12
Output Notification  : 0
------------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display netconf session (All views)** command output
| Item | Description |
| --- | --- |
| NETCONF Session ID | NETCONF session ID. |
| Transport | Transport type. |
| User Name | User Name. |
| Host Identifier | Host Identifier. |
| Login Time | Login Time. |
| Input Rpc | Counts of input RPC. |
| Input Bad Rpc | Counts of bad input RPC. |
| Output Rpc Error | Counts of output error RPC. |
| Output Notification | Counts of output notification. |