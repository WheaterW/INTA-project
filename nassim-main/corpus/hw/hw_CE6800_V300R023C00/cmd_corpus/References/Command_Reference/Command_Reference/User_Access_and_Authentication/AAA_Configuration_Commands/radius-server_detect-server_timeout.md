radius-server detect-server timeout
===================================

radius-server detect-server timeout

Function
--------

The **radius-server detect-server timeout** command configures the timeout period for RADIUS detection packets.

The **undo radius-server detect-server timeout** command restores the default settings.

By default, the timeout period for RADIUS detection packets is 3 seconds.



Format
------

**radius-server detect-server timeout** *timeout*

**undo radius-server detect-server timeout**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *timeout* | Specifies the timeout period for RADIUS detection packets. | The value is an integer that ranges from 1 to 10, in seconds. The default value is 3. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After the automatic detection function is enabled using the **radius-server testuser** command, if the device sends a detection packet to the RADIUS server and receives a response packet from the server within the timeout period, the device sets the RADIUS server status to Up; otherwise, the device sets the RADIUS server status to Down. You can run the **radius-server detect-server timeout** command to adjust the timeout period for RADIUS detection packets based on the actual response rate of the RADIUS server.

**Precautions**

You are advised to set a timeout period for RADIUS detection packets smaller than the automatic detection interval to prevent the device from sending a detection packet again before completing processing the response packet from the RADIUS server. If the actual timeout period for RADIUS detection packets is larger than the automatic detection interval, the smaller value is the timeout period, namely:

* For the RADIUS server in Down status, the smaller one between values configured using the radius-server detect-server timeout and **radius-server detect-server interval** commands is the timeout period for detection packets.
* For the RADIUS server in Up status, the smaller one between values configured using the radius-server detect-server timeout and **radius-server detect-server up-server interval** command is the timeout period for detection packets.


Example
-------

# Set the timeout period for RADIUS detection packets to 5 seconds in the RADIUS server template acs.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template acs
[*HUAWEI-radius-acs] radius-server detect-server timeout 5

```