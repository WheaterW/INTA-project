display radius-attribute translate
==================================

display radius-attribute translate

Function
--------



The **display radius-attribute translate** command displays the RADIUS attribute translation configuration.




Format
------

**display radius-attribute** [ **template** *template-name* ] **translate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **template** *template-name* | Displays the RADIUS attribute translation configuration of a specified RADIUS server template. template-name specifies the name of the RADIUS server template that is created using the radius-server template command.  If this parameter is not specified, the disabled RADIUS attributes translation configuration in all the RADIUS server templates are displayed. | The value must be an existing RADIUS server template name. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After running the **radius-attribute translate** command to configure the device to translate RADIUS attributes, run the **display radius-attribute translate** command to check the configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the RADIUS attribute translation configuration.
```
<HUAWEI> display radius-attribute translate
Packet-Type: Type of the RADIUS packets to be modified. 1 indicates valid; 0 indicates invalid. Bit 1 to bit 4 indicate the authentication request, authentication accept, accounting request, and accounting response packets.   

Server-template-name: t1                                                       
--------------------------------------------------------------------------------
Source-Vendor-ID Source-Sub-ID Dest-Vendor-ID Dest-Sub-ID  Direct    Packet-Type
--------------------------------------------------------------------------------
0                6             0              40           receive    0 0 0 0   
--------------------------------------------------------------------------------
Server-template-name: t2                                                       
--------------------------------------------------------------------------------
Source-Vendor-ID Source-Sub-ID Dest-Vendor-ID Dest-Sub-ID  Direct    Packet-Type
--------------------------------------------------------------------------------
234567           123           2011           20           --         0 1 0 1   
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display radius-attribute translate** command output
| Item | Description |
| --- | --- |
| Source-Vendor-ID | Vendor ID of the source attribute. |
| Source-Sub-ID | ID of the source attribute's sub-attribute. |
| Dest-Vendor-ID | Vendor ID of the destination attribute. |
| Dest-Sub-ID | ID of the destination attribute's sub-attribute. |
| Direct | Direction in which the attribute is translated.   * receive: The RADIUS attributes of received packets are translated. * send: The RADIUS attributes of sent packets are translated. |
| Packet-Type | Type of RADIUS packets.   * 0: The RADIUS attributes of this type of packets are not translated. * 1: The RADIUS attributes of this type of packets are translated. |
| Server-template-name | RADIUS server template name. |