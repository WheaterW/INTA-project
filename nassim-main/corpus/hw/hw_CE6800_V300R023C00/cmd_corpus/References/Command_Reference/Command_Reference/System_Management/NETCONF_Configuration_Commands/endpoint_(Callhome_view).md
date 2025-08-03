endpoint (Callhome view)
========================

endpoint (Callhome view)

Function
--------



The **endpoint** command creates a NETCONF connection instance and then displays the NETCONF connection instance view or displays the view of an existing NETCONF connection instance directly.

The **undo endpoint** command deletes existing NETCONF connection instance.



By default, no NETCONF connection instance is created.


Format
------

**endpoint** *endpoint-name*

**undo endpoint** *endpoint-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *endpoint-name* | Specifies the name of a NETCONF connection instance. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

Callhome view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an NMS does not support automatic device discovery, it cannot manage devices in time. To address this problem, you can configure proactive NETCONF registration for a device to send a NETCONF connection request to the NMS when the device goes online so that the NMS can manage the device.When configuring proactive NETCONF registration, you need to create a NETCONF connection instance using the **endpoint** command in the callhome template view and configure the IP address and TCP port number of the NMS with which the device is to establish a NETCONF connection using the **peer-ip** command.

**Precautions**



A maximum of 20 IPv4 NETCONF connection instances and 20 IPv6 NETCONF connection instances can be created on the device, but only one NETCONF connection instance can be used for connection.




Example
-------

# Create a NETCONF connection instance named huawei and enter the NETCONF connection instance view.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome root
[*HUAWEI-netconf-callhome-root] endpoint huawei
[*HUAWEI-netconf-callhome-root-endpoint-huawei]

```