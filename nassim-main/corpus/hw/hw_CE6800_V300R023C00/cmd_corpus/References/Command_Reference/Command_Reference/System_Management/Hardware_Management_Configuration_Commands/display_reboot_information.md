display reboot information
==========================

display reboot information

Function
--------



The **display reboot information** command displays reset information about a device.




Format
------

**display reboot information slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot number of a board or module to be displayed. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the system restarts, you can run this command to check the system reset cause. You can determine whether a fault occurs in the system according to the displayed information.The following table lists common restart causes.

| Common Device Restart Cause | Meaning | Handling Suggestion |
| --- | --- | --- |
| Power off board for energy-saving | The board is powered off for energy saving. | No action is required. |
| Reboot board from command | The board is restarted using a command. | No action is required. |
| Board button reset | The board is restarted by pressing the button. | No action is required. |
| Board is absent, and reset board | The board is removed and then reset. | No action is required. |
| Board register | The board is registered. | No action is required. |
| Power off board from command | The board is powered off using a command. | No action is required. |
| The board was reset due to kernel panic | The board is restarted unexpectedly due to kernel exceptions. | Contact technical support. |
| NP initialize failed, and reset board | Failed to start the NP. | Contact technical support. |
| The heartbeat lost and reset board | The board is restarted due to heartbeat loss. | Contact technical support. |
| Reset board from watchdog | The board restarts from the watchdog. | Contact technical support. |
| Board no enough Memory,and reset board | The board restarts due to insufficient memory. | Check the memory usage. |
| Board type is incompatible with software and reset board | The board restarts due to mismatch between the board and software. | Contact technical support. |
| Board temperature is too high, and power off board | The board is powered off due to high temperature. | Contact technical support. |
| Board temperature is too high, and reset board | The board restarts due to high temperature. | Contact technical support. |
| HPP link down, and reset board | The board restarts due to HPP link down. | Contact technical support. |
| Board cold reset | The board is powered off and then powered on using a command. | No action is required. |



Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the reason for the system reboot.
```
<HUAWEI> display reboot information slot 1
Board 1 reset information:
-- 1. DATE:2019-03-30  TIME:16:02:03  BARCODE:BARCODETEST20190718 
--    Reason:Board register BarCode is BARCODETEST20190718.
--    BootMode:NORMAL
--    BootCode:0x060100ff
--    Feature:DEVM
-- 2. DATE:2019-03-30  TIME:15:59:43  BARCODE:BARCODETEST20190718
--    Reason:Reboot board from command. BarCode is BARCODETEST20190718.
--    BootMode:NORMAL
--    BootCode:0x06010017
--    Feature:DEVM

```

**Table 1** Description of the **display reboot information** command output
| Item | Description |
| --- | --- |
| Board | Specified board. |
| BarCode | SN of a device. |
| DATE | Reset date. |
| TIME | Reset time. |
| Reason | Reset reason. |
| BootMode | Boot mode. |
| BootCode | Boot code. |
| Feature | Field which the reset reason belongs to. |