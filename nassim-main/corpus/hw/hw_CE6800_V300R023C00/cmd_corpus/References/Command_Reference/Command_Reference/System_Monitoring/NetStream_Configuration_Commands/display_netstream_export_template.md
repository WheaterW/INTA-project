display netstream export template
=================================

display netstream export template

Function
--------



The **display netstream export template** command displays export template information in which the packet version is set to V9 for IPv4, IPv6, or VXLAN flow statistics.




Format
------

**display netstream export** { **ip** | **ipv6** | **vxlan** **inner-ip** } **template** **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Displays information about the template for exporting IPv4 flow statistics. | - |
| **ipv6** | Displays information about the template for exporting IPv6 flow statistics. | - |
| **vxlan** | Displays information about the template for exporting VXLAN flow statistics. | - |
| **inner-ip** | Specifies the inner packet of the IPv4 type for VXLAN packets. | - |
| **slot** *slot-id* | Specify slot to match. | The value is an integer or a character string. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When the packet version for NetStream flow statistics is set to V9, the corresponding template must be exported to the NDA. If the NMS fails to parse flow packets, this command can be used to check whether template exporting is normal.

**Precautions**

If the specified template is not exported, the command output does not contain information about this template. If none of the templates is exported, the command output is empty.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Set the packet version of original flows to V9, and check statistics in the current template.
```
<HUAWEI> display netstream export ip template slot 1
-------------------------------------------------------
TemplateName                         Success     Failed
-------------------------------------------------------
myflex11                                  45          0
myflex10                                  45          0
origin                                    45          0
-------------------------------------------------------

```

**Table 1** Description of the **display netstream export template** command output
| Item | Description |
| --- | --- |
| TemplateName | Template name. |
| Success | Number of times a template is successfully exported. |
| Failed | Number of times a template failed to be exported. |