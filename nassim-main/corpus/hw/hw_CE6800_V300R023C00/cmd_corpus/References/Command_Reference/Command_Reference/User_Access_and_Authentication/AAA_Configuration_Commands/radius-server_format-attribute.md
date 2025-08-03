radius-server format-attribute
==============================

radius-server format-attribute

Function
--------

The **radius-server format-attribute** command configures the format of the NAS-Port attribute.

The **undo radius-server format-attribute** command deletes the configured attribute format.

By default, the format of the NAS-Port attribute is new.



Format
------

**radius-server format-attribute nas-port** *nas-port-string*

**undo radius-server format-attribute nas-port**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **nas-port** *nas-port-string* | Specifies the format of the NAS-Port attribute. In the nas-port-string parameter in binary format:  The keywords s, t, p, o, and i indicate slot, subslot, port, out-vlan (qinqvlan)/vpi, and vlan (user-vlan)/vci respectively. The keywords n and z are used as paddings. The keyword n indicates 1 and the keyword z indicates 0.  The keywords s, t, p, o, and i must be followed by numbers, and the numbers must range from 1 to 32. The keywords s, t, p, o, and i can appear in the format string only once.  The keywords s, t, p, o, i, n, and z must range from 1 to 9.  n and z can appear multiple times at any position. They are followed by numbers. For example, n12 indicates that this position is filled in with twelve 1s, and z12 indicates that this position is filled in with twelve 0s.  The character string must contain 32 bits.  The format string must start with s, t, p, o, i, n, or z and end with a number.  If no VLAN exists, you can add n or z before o or i to indicate whether this position is filled in with 0s or 1s. That is, n and z can be followed by numbers, o, or i in this case, and the numbers must range from 1 to 32.  To specify the format string, determine the interface type, and then determine the encapsulation type of the interface. If the format string does not contain o or i, the NAS-Port attribute does not contain the QinQ VLAN or user VLAN field. If the format string contains o or i but no outer VLAN exists, the outer VLAN field is filled in with 0s. If n is added before o or i, this field is filled in with 1s when no outer VLAN or inner VLAN exists. | The value is a string of 1 to 32 characters. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

The NAS port format affects the information about the physical port. The NAS port format can be used by the RADIUS server to process services, such as binding the user name and port. This attribute is developed by Huawei, which is used to ensure connectivity and service cooperation among Huawei devices.

If the radius-server nas-port-format command sets the format of the NAS-Port attribute to new (the default format is new), the device will check whether the radius-server format-attribute nas-port command configuration exists. If yes, the device will assemble the NAS-Port attribute in the format configured by the radius-server format-attribute nas-port command. If no, the device will assemble the NAS-Port attribute in the new format. If the radius-server nas-port-format command sets the format of the NAS-Port attribute to old, the device will assemble the NAS-Port attribute in the old format, regardless of whether the radius-server format-attribute nas-port command configuration exists.

Example
-------

# Configure the format of the NAS-Port attribute to s2t2p6no10ni12. That is, the NAS-Port attribute consists of a 2-bit slot field, a 2-bit subslot field, a 6-bit port field, a 10-bit outer VLAN field, and a 12-bit inner VLAN field. If the outer VLAN does not exist, this field is filled by ten 1s. If the inner VLAN does not exist, this field is filled by twelve 1s. Therefore, the NAS-port attribute contains 32 bits.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template template1
[*HUAWEI-radius-template1] radius-server format-attribute nas-port s2t2p6no10ni12

```