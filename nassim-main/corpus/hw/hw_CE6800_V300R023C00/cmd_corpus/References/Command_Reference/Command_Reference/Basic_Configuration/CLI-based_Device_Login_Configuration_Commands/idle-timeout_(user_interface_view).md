idle-timeout (user interface view)
==================================

idle-timeout (user interface view)

Function
--------



The **idle-timeout** command sets a timeout period to disconnect from the user interface. If no command is entered within the specified period, the system tears down the current connection.

The **undo idle-timeout** command restores the default timeout period.



By default, the timeout period of the console user interface is 5 minutes and the timeout period of the VTY user interface is 10 minuets.


Format
------

**idle-timeout** *minutes* [ *seconds* ]

**undo idle-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minutes* | Specifies the time period in seconds to disconnect from the user interface view. | It is an integer data type. The value ranges from 0 to 35791 minutes. The timeout period for a console user ranges from 1 to 1440 minutes, and the timeout period for a VTY user ranges from 0 to 35791 minutes. |
| *seconds* | Specifies the time period in seconds to disconnect from the user interface view. | It is an integer data type. The value range is from 0 to 59 seconds. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **idle-timeout 0 0** command to disable the idle timeout function of the VTY user interface. If the administrator does not close the operation interface due to negligence, non-administrator users may perform unauthorized operations.If the idle disconnection function is not configured on the VTY or console user interface, other users may fail to obtain idle connections.


Example
-------

# Set the timeout period of vty user interface view to 1 minute and 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] idle-timeout 1 30

```

# Set the timeout period of the console user interface to 1.5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] idle-timeout 1 30

```