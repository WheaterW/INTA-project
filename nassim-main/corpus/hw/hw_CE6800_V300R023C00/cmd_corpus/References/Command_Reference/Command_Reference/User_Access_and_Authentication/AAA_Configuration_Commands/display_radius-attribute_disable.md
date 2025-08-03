display radius-attribute disable
================================

display radius-attribute disable

Function
--------



The **display radius-attribute disable** command displays the disabled RADIUS attributes.




Format
------

**display radius-attribute** [ **template** *template-name* ] **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **template** *template-name* | Displays the disabled RADIUS attributes in a specified RADIUS server template.  If this parameter is not specified, the disabled RADIUS attributes in all the RADIUS server templates are displayed. | The value must be an existing RADIUS server template name. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can use the **display radius-attribute disable** command to view the RADIUS attributes disabled by using the **radius-attribute disable** command.To enable a RADIUS attribute, run the **undo radius-attribute disable** command in the RADIUS server template view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the disabled RADIUS attributes on the device.
```
<HUAWEI> display radius-attribute disable
Packet-Type: Type of the RADIUS packets to be modified. 1 indicates valid; 0 ind
icates invalid. Bit 1 to bit 4 indicate the authentication request, authenticati
on accept, accounting request, and accounting response packets.                 
                                                                                
Server-template-name: d                                                         
--------------------------------------------------------------------------------
Source-Vendor-ID Source-Sub-ID Dest-Vendor-ID Dest-Sub-ID  Direct    Packet-Type
--------------------------------------------------------------------------------
0                7             0              0            send       0 0 0 0   
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display radius-attribute disable** command output
| Item | Description |
| --- | --- |
| Source-Vendor-ID | Vendor ID of the source attribute. |
| Source-Sub-ID | ID of the source attribute's sub-attribute. |
| Dest-Vendor-ID | Vendor ID of the destination attribute. |
| Dest-Sub-ID | ID of the destination attribute's sub-attribute. |
| Direct | Direction in which the attribute is translated.   * receive: Translates RADIUS attributes for received packets. * send: Translates RADIUS attributes for sent packets. |
| Packet-Type | Type of RADIUS packets.   * 0: The RADIUS attributes of this type of packets are not translated. * 1: The RADIUS attributes of this type of packets are translated. |
| Server-template-name | RADIUS server template name. |