netstream record vxlan inner-ip (system view)
=============================================

netstream record vxlan inner-ip (system view)

Function
--------



The **netstream record vxlan inner-ip** command creates a VXLAN flexible flow statistics template or displays the view of an existing VXLAN flexible flow statistics template.

The **undo netstream record vxlan inner-ip** command deletes a specified VXLAN flexible flow statistics template.



By default, no VXLAN flexible flow statistics template is configured.


Format
------

**netstream record** *record-name* **vxlan** **inner-ip**

**undo netstream record** *record-name* **vxlan** **inner-ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *record-name* | Specifies the name of a VXLAN flexible flow statistics template. | The value is a string of 1 to 32 case-sensitive characters without spaces. If the string is enclosed in double quotation marks (" "), the string can contain spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The original Ethernet frame information in VXLAN packets cannot be obtained from NetStream original, IPv4 flexible, or IPv6 flexible flow statistics. To obtain original Ethernet frame information in VXLAN packets, you can configure exporting of VXLAN flexible flow statistics. Before that, you need to use this command to create a VXLAN flexible flow statistics template.

**Precautions**

Each device supports a maximum of 16 flexible flow statistics templates. To configure a 17th flexible flow statistics template, run the undo netstream record vxlan inner-ip (system view) command to delete an existing one first.The template that has been applied to an interface cannot be deleted or modified. To delete such a template, run the undo netstream record vxlan inner-ip (interface view) command on the interface to cancel the flexible flow statistics template applied to the interface, and then delete or modify the template.VXLAN flexible flow statistics templates are independent of IPv4 and IPv6 flexible flow statistics templates and can have the same names as the IPv4 and IPv6 flexible flow statistics templates.


Example
-------

# Create a VXLAN flexible flow statistics template named abc1.
```
<HUAWEI> system-view
[~HUAWEI] netstream record abc1 vxlan inner-ip
[*HUAWEI-netstream-record-vxlan-abc1] match inner-ip destination-address
[*HUAWEI-netstream-record-vxlan-abc1] collect counter bytes

```