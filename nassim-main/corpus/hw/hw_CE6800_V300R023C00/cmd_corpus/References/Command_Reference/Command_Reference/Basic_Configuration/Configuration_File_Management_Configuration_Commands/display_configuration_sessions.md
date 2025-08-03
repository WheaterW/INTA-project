display configuration sessions
==============================

display configuration sessions

Function
--------



The **display configuration sessions** command displays session status.




Format
------

**display configuration sessions**

**display configuration sessions verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Indicates detailed information about session status. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To query information about users that have logged in to the device, you can run the display configuration sessions command to view session status.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display session status.
```
<HUAWEI> display configuration sessions
--------------------------------------------------------------------------
Session User-Intf    User                 Date                Lock
--------------------------------------------------------------------------
108                  SNMP_User            2013-02-11 17:24:09    -           
158     CON 0        anonymous            2011-01-17 10:39:47    -   
177     VTY 0        user                 2011-01-17 12:00:11    -   
179     VTY 1        user                 2011-01-17 12:04:06    -   
180 *   VTY 2        user                 2011-01-17 12:32:02    -   
14911 * VTY 0        anonymous            2013-04-19 14:46:09    -           
--------------------------------------------------------------------------

```

# Display detailed information about session status.
```
<HUAWEI> display configuration sessions verbose
--------------------------------------------------------------------------------
Session      : 60 
User-Intf    : 
User         : _SYSTEM_
Date         : 2014-08-21 13:39:06
Lock-Type    : -
Cfg-Mode     : -
Client       : NETCONF
Elapsed-Time : 1 days, 1:27:58

Session      : 168 *
User-Intf    : CON 1023
User         : 
Date         : 2014-08-22 08:34:48
Lock-Type    : -
Cfg-Mode     : -
Client       : CLI
Elapsed-Time : 0 days, 6:32:16

--------------------------------------------------------------------------------

```

**Table 1** Description of the **display configuration sessions** command output
| Item | Description |
| --- | --- |
| Session | Indicates the ID of the session that connects to the system. |
| User-Intf | Indicates the interface information that the user used to logging on. |
| User | User name.   * When a user performs operations through an NMS, SNMP\_User is displayed. * When a user performs RMON operations, RMON\_User is displayed. * After the system is started, OPS will automatically apply for an internal link that is used as a channel for the Maintenance assistant to subscribe to logs and alarms. The link user name is \_SYSTEM\_. |
| Date | Indicates the time of the logging user. |
| Lock | Indicates the lock status. |
| Lock-Type | Indicates the lock type. |
| Cfg-Mode | Indicates the configuration mode. |
| Client | Indicates the client information. |
| Elapsed-Time | Indicates the elapsed time of the logging user. |