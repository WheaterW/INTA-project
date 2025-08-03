display device board reset
==========================

display device board reset

Function
--------



The **display device board reset** command displays the reason for the board reset.




Format
------

**display device board reset** *slotid* [ *card* *cardid* ]

**display device board reset all**

**display device board reset** *slotid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slotid* | Specifies the slot number of a board or module to be displayed. | The value is a string of 1 to 51 case-insensitive characters. It cannot contain spaces. |
| *card* | Displays the reason for the reset of a subcard. | The value is a string of 1 to 4 case-insensitive characters. It cannot contain spaces. |
| *cardid* | Specifies a card ID. | The value is a string of 1 to 51 case-insensitive characters. It cannot contain spaces. |
| **all** | Indicates all reset information. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After a board is reset, this command can be used to check the reason for the board reset. The command output can be used to check whether the board is faulty.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the reason for the board reset.
```
<HUAWEI> display device board reset 1
Board 1 reset information:
-- 1. DATE:2019-03-30  TIME:16:02:03  BARCODE:210235527210D4000046  RESET Num:1
--    Reason:Board register, BarCode is 210235527210D4000046.
--    BootMode:NORMAL
--    BootCode:0x060100ff
--    Feature:DEVM
-- 2. DATE:2019-03-30  TIME:15:59:43  BARCODE:210235527210D4000046  RESET Num:1
--    Reason:Reboot board from command.(CPU Reset)
--    BootMode:NORMAL
--    BootCode:0x06010017
--    Feature:DEVM

```

# Display the reason for the subcard reset.
```
<HUAWEI> display device board reset 1 card 0
Board 1 Card 0 reset information:
-- 1. DATE:2037-01-14  TIME:11:41:28  BARCODE:TESTCARD20191104  RESET Num:1
--    Reason:Cmd reset card.
--    reset code:0x06080001
--    Feature:DEVM
-- 2. DATE:2037-01-14  TIME:10:35:46  BARCODE:TESTCARD20191104  RESET Num:0
--    Reason:Card is registered.
--    reset code:0x06080008
--    Feature:DEVM

```

# Display the reset causes of all boards.
```
<HUAWEI> display device board reset all
----------------------------------------------------------
Board 3 reset information:
-- 1. DATE:2014-10-09  TIME:11:14:34+08:00  BARCODE:ST120700006217
   RESET Num:0
--    Reason:Board register, BarCode is ST120700006217               .
--    BootMode:NORMAL
--    BootCode:0x060100ff
--    Feature:DEVM
----------------------------------------------------------
Board 4 reset information:
-- 1. DATE:2014-10-09  TIME:11:11:55+08:00  BARCODE:NULL  RESET Num:0
--    Reason:Board register, BarCode is NULL.
--    BootMode:NORMAL
--    BootCode:0x060100ff
--    Feature:DEVM
----------------------------------------------------------
......

```

**Table 1** Description of the **display device board reset** command output
| Item | Description |
| --- | --- |
| Board 1 | Slot number of the board. |
| Board X reset information | Reset information of the board in slot X. |
| RESET Num | Number of resets. |
| DATE | Reset date and time. |
| TIME | Automatic reset time. |
| BARCODE | SN of a device. |
| Reason | Reason for resetting. |
| BootMode | Reset mode. |
| BootCode | Boot code. |
| Feature | Domain to which the reset code belongs. |