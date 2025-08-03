display warranty
================

display warranty

Function
--------



The **display warranty** command displays information about the warranty of a device or part.




Format
------

**display warranty** [ **device** | **parts** [ **slot** *slot-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **device** | Displays information about the warranty of the entire system. | - |
| **parts** | Displays information about the warranty of a part. | - |
| **slot** *slot-id* | Displays information about the warranty in a specified slot. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

A warranty is an electronic record and copy of the service life committed to customers for products and components. To ensure that the information about the service life can be smoothly processed during the product inventory management and service process, the warranty policy must be specific to each device on the live network.You can run the **display warranty** command to view information about activated warranty policies in the system. However, you cannot view information about the warranty policy of a subcard in a specified slot.

**Precautions**

Only warranties of activated components can be queried by running the display warranty, display warranty device, or display warranty parts command. If you query inactive components, the command output is empty.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display warranty information in the system.
```
<HUAWEI> display warranty
Device information:

 chassis
  Serial number   : 210305582010JC000001_210305582010JC000001
  Start date      : 2022-07-01
  Type name       : device
  Life span       : 25 (month)
  Status          : normal
Parts information:

 MPU slot 1
  Serial number   : 391091068000297_17
  Start date      : 2021-07-08
  Type name       : part
  Life span       : 12 (month)
  Status          : normal

 FAN 32
  Serial number   : 2102120866P0EA000314
  Start date      : 2022-01-01
  Type name       : part
  Life span       : 24 (month)
  Status          : normal

 POWER slot 1
  Serial number   : 2102310QNND0D9000158
  Start date      : 2022-01-03
  Type name       : part
  Life span       : 12 (month)
  Status          : to be expired"

```

**Table 1** Description of the **display warranty** command output
| Item | Description |
| --- | --- |
| Device information | Product information. |
| Serial number | Serial number of a warranty. |
| Start date | Start date of a warranty. |
| Type name | Type of a warranty, which can be device or part. |
| Life span | Warranty period of a warranty, in months. |
| Status | Status of a warranty. |
| Parts information | Part information. |
| slot | Slot ID. |
| Info | Prompt message. |