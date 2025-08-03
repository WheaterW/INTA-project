idle-timeout (Service-RESTCONF view)
====================================

idle-timeout (Service-RESTCONF view)

Function
--------



The **idle-timeout** command sets the timeout period for disconnecting from the RESTCONF user interface. If no command is entered within the specified period, the system disconnects the current connection.

The **undo idle-timeout** command restores the default timeout period disconnecting from the RESTCONF user interface.



By default, the timeout period is 20 minutes.


Format
------

**idle-timeout** *minutes*

**undo idle-timeout**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *minutes* | Specifies the timeout period for disconnecting from the RESTCONF user interface, in minutes. | The value is an integer ranging from 1 to 60, in minutes. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

If the function is not configured after the timeout period of the RESTCONF user interface elapses, other users may fail to establish RESTCONF user interface connections when a logged-in user is in the idle state. You can run the **idle-timeout** command to configure the idle disconnection function.


Example
-------

# Set the timeout period for disconnecting from the RESTCONF user interface to 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] idle-timeout 30

```