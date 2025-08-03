radius-attribute nas-ip
=======================

radius-attribute nas-ip

Function
--------

The **radius-attribute nas-ip** command sets the NAS-IP-Address attribute in a RADIUS packet sent from an NAS.

The **undo radius-attribute nas-ip** command deletes the configured NAS-IP-Address attribute.

By default, the NAS source IP address is used as the NAS-IP-Address attribute value. You can run the radius-attribute nas-ip { ip-address | ap-info } command to change the attribute value to the IP address specified on the AC or the IP address of the AP.



Format
------

**radius-attribute nas-ip** *ip-address*

**undo radius-attribute nas-ip**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the NAS-IP-Address attribute value in RADIUS packets sent by the device. | The value is a valid unicast address in dotted decimal notation. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

A RADIUS server uses the NAS-IP-Address attributes in RADIUS packets sent by NASs to identify NASs. You can run the **radius-attribute nas-ip** command in the RADIUS server template view to set the NAS-IP-Address attribute.

**Prerequisites**

A RADIUS server template has been created using the radius-server template command.

**Precautions**

If the RADIUS NAS-IP-Address attribute is set to an invalid IP address, the configuration fails and an error message is displayed.



Example
-------

# Set the NAS-IP-Address attribute value in RADIUS packets.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template temp1
[*HUAWEI-radius-temp1] radius-attribute nas-ip 10.3.3.3

```