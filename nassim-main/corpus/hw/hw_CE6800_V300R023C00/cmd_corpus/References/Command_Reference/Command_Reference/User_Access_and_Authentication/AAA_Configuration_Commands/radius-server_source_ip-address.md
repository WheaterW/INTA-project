radius-server source ip-address
===============================

radius-server source ip-address

Function
--------

The **radius-server source ip-address** command configures the source IP address for communication between the device and RADIUS server.

By default, no source IP address is configured for communication between the device and RADIUS server.



Format
------

**radius-server source ip-address** *source-ip-address*

**undo radius-server source ip-address** *source-ip-address*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *source-ip-address* | Specifies the source IPv4 address for communication between the device and RADIUS server. | The value is a valid unicast address in dotted decimal notation. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

You can run the **radius-server source ip-address** command to configure the source IP address for the device to communicate with a RADIUS server based on the server template. The configuration takes effect for all servers in the template.

If the source IP address of the RADIUS server is not specified in the RADIUS server template, the source IP address configured based on the RADIUS server template is used.



Example
-------

# In the view of the RADIUS server template hw, set the source IP address for communication between the device and RADIUS server to 192.168.1.1.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template hw
[*HUAWEI-radius-hw] radius-server  source ip-address 192.168.1.1

```