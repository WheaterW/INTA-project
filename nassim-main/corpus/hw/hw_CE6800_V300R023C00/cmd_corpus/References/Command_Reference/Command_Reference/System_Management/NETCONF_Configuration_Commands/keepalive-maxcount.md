keepalive-maxcount
==================

keepalive-maxcount

Function
--------



The **keepalive-maxcount** command sets a keepalive maximum count for the callhome keepalive function.

The **undo keepalive-maxcount** command restores the keepalive maximum count to the default value 3.



By default, the keepalive maximum count is 3.


Format
------

**keepalive-maxcount** *maxcount*

**undo keepalive-maxcount**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maxcount* | Specify the keepalive maximum count, default is 3. | The value is an integer ranging from 1 to 30. The default value is 3. |



Views
-----

Endpoint view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an NMS does not support automatic device discovery, the NMS cannot manage devices in a timely manner. To address this issue, configure the callhome function. After the callhome function is enabled on a device, the device proactively sends a NETCONF connection request to the NMS upon login and establishes a NETCONF connection with the NMS. In this manner, users can manage the device through the NMS in a timely manner.If the callhome keepalive function is not configured, the device disconnects from the NMS when the idle time of the connection between the device and NMS exceeds the timeout period configured using the **idle-timeout** command. If you want to keep the connection alive, run the **keepalive-maxcount** command to set a keepalive maximum count. The callhome connection will be closed when the number of the keep-alive failures times exceeds the maximum count.


Example
-------

# Set a callhome maximum count.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome cc
[*HUAWEI-netconf-callhome-cc] endpoint ee
[*HUAWEI-netconf-callhome-cc-endpoint-ee] keepalive-maxcount 10

```