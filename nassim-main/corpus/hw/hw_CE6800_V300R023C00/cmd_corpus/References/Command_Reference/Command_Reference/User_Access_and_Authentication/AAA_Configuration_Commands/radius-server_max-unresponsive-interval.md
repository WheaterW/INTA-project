radius-server max-unresponsive-interval
=======================================

radius-server max-unresponsive-interval

Function
--------

The **radius-server max-unresponsive-interval** command configures the longest unresponsive interval for a RADIUS server.

The **undo radius-server max-unresponsive-interval** command restores the default settings.

By default, the longest unresponsive interval for a RADIUS server is 300 seconds.



Format
------

**radius-server max-unresponsive-interval** *max-unresponsive-interval*

**undo radius-server max-unresponsive-interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-unresponsive-interval* | Specifies the longest unresponsive interval for a RADIUS server. | The value is an integer that ranges from 10 to 7200, in seconds. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

If the user access frequency is low and the device receives only a few authentication request packets sourced from users, the device cannot detect the RADIUS server status by periodically detecting authentication request packets. In this case, you can configure the mechanism of marking the RADIUS server status as Down if no response is received from the server for a long period of time to ensure that users can obtain escape authorization. If the interval for sending two consecutive RADIUS Access-Request packets is greater than the value of max-unresponsive-interval, the device marks the RADIUS server status as Down.



Example
-------

# Set the longest unresponsive interval for a RADIUS server to 100 seconds.
```
<HUAWEI> system-view
[~HUAWEI] radius-server max-unresponsive-interval 100

```