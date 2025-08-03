display device elabel
=====================

display device elabel

Function
--------



The **display device elabel** command displays the electronic label of the device.




Format
------

**display device elabel** [ **slot** *slotid* [ **card** *cardid* ] [ **brief** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Specifies a slot ID. | The value is a string of 1 to 30 characters. |
| **card** *cardid* | Specifies a card ID. | The value is a string of 1 to 49 characters. |
| **brief** | Indicates that the electronic label of a device does not include interface information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Electronic labels identify the hardware. You can use the display device elabel command to view electronic label information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the electronic label of the device.
```
<HUAWEI> display device elabel slot 1 brief

[1]
/$[ArchivesInfo Version]
/$ArchivesInfoVersion=3.0


[Board Properties]
BoardType=XXX
BarCode=XXX
Item=02353VLH
Description=XXX
Manufactured=2019-07-18
VendorName=Huawei
IssueNumber=00
CLEICode=
BOM=
Model=XXX
/$ElabelVersion=4.0

```

**Table 1** Description of the **display device elabel** command output
| Item | Description |
| --- | --- |
| [Slot\_n] | Electronic label of device. |
| /$ArchivesInfoVersion | Version of an electronic label. For an electronic label of version 3.0 or later, the value of this field remains 3.0. |
| BoardType | Internal model of the component. |
| BarCode | Bar code of the component. |
| Item | BOM code of the component. |
| Description | Description of the component. |
| Manufactured | Production date of a component, not the entire device. |
| VendorName | Vendor name of the component. |
| IssueNumber | Issue number of the component. |
| CLEICode | CLEI code of the component. |
| BOM | Sales BOM number of the component. |
| Model | External model of the component. There is no such information if the electronic label version is earlier than 4.0. |
| /$ElabelVersion | Electronic label version information. There is no such information if the electronic label version is earlier than 4.0. |