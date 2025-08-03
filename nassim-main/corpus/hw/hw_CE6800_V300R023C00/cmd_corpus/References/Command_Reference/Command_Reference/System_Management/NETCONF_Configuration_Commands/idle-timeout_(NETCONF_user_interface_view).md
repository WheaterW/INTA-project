idle-timeout (NETCONF user interface view)
==========================================

idle-timeout (NETCONF user interface view)

Function
--------



The **idle-timeout** command sets a timeout period to disconnect from a NETCONF user interface. If a user does not invoke a command for a specific period of time, the connection gets disconnected.

The **undo idle-timeout** command restores the default timeout period.

The default timeout period is 10 minutes.



By default, the timeout period is 10 minutes.


Format
------

**idle-timeout** *minutes* [ *seconds* ]

**undo idle-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minutes* | Sets the time period to disconnect a user from the user interface view. | The value is an integer ranging from 0 to 35791, in minutes. |
| *seconds* | Sets the time period to disconnect a user from the user interface view. | The value is an integer ranging from 0 to 59, in seconds. |



Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If no timeout period is set for a login user and the user is in idle state for a long time, other users may fail to establish connections with the NETCONF user interface. To prevent this issue, run the **idle-timeout** command to set a timeout period. If the login user remains idle until the timeout period elapses, the user is disconnected from the NETCONF user interface.To disable the idle timeout function, specify 0 minutes and 0 seconds in the **idle-timeout** command. If an administrator does not close an operation interface due to neglect, non-administrator users may perform unauthorized operations.


Example
-------

# Set the timeout period to 1 minute and 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] idle-timeout 1 30

```