reset netstream cache
=====================

reset netstream cache

Function
--------



The **reset netstream cache** command forcibly ages out IPv4, IPv6, or VXLAN flows on the device.




Format
------

**reset netstream cache** { **ip** | **ipv6** | **vxlan** **inner-ip** } **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Ages IPv4 flow statistics forcibly. | - |
| **ipv6** | Ages IPv6 flow statistics forcibly. | - |
| **vxlan** | Ages VXLAN flexible flow statistics forcibly. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to forcibly age out packet statistics on the device.


Example
-------

# Forcibly age out IPv4 flows on the device.
```
<HUAWEI> reset netstream cache ip slot 1

```