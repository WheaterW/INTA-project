radius-server authorization match-type
======================================

radius-server authorization match-type

Function
--------

The **radius-server authorization match-type** command configures the method used by a device to perform a match check between the RADIUS attribute in the received CoA or DM Request packet and user information on the device.

The **undo radius-server authorization match-type** command restores the default setting.

By default, a device performs a match check between the RADIUS attribute in the received CoA or DM Request packet and user information on the device using the any method, namely, the device performs a match check between a selected attribute in the Request packet and user information on the device.



Format
------

**radius-server authorization match-type** { **any** | **all** }

**undo radius-server authorization match-type**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **any** | Indicates that the device performs a match check between a specified attribute and user information on the device. | - |
| **all** | Indicates that the device performs a match check between all attributes and user information on the device. | - |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A device performs a match check between the RADIUS attribute in the CoA or DM Request packet and user information on the device to identify users in the following two methods:

any method: The device performs a match check between an attribute and user information on the device. The priority of identifying the RADIUS attributes used by the users is as follows: Acct-Session-ID (4)> Framed-IP-Address (8) The device searches for the attributes in the Request packet based on the priority, and performs a match check between the first found attribute and user information on the device. If the attribute is successfully matched, the device responds with an ACK packet; otherwise, the device responds with a NAK packet.all method: The device performs a match check between all attributes and user information on the device. The device identifies the following RADIUS attributes used by the users: Acct-Session-ID (4), Framed-IP-Address (8), and User-Name (1) The device performs a match check between all the preceding attributes in the Request packet and user information on the device. If all the preceding attributes are successfully matched, the device responds with an ACK packet; otherwise, the device responds with a NAK packet.

**Precautions**

When the RADIUS attribute translation function is configured in the RADIUS template using the **radius-attribute translate** command, the match will fail.



Example
-------

# Configure a device to perform a match check between all RADIUS attributes in the received CoA or DM Request packet and user information on the device.
```
<HUAWEI> system-view
[~HUAWEI] radius-server authorization match-type all

```