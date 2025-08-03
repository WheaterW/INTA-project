display device elabel brief
===========================

display device elabel brief

Function
--------



The **display device elabel brief** command displays the serial numbers of all slots in a device.




Format
------

**display device elabel brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the serial numbers of boards, subcards, fans, and power modules in all slots, run the display device elabel brief command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the serial numbers of boards, fans, and power supplies on the device.
```
<HUAWEI> display device  elabel brief
Equipment SN(ESN): BARCODETEST2019**** 
License ESN: --
-------------------------------------------------------------------------------
SlotID     Sub    Type                  SN                       P/N
-------------------------------------------------------------------------------
1          --     CE6866-48S8CQ-P         BARCODETEST2019****      02353EGM
           FAN1   --                    --                       --
           FAN2   --                    --                       --
           FAN3   --                    --                       --
           FAN4   --                    --                       --
           PWR1   PAC600S12-CB          2102312FFUBTM100****     02312FFU
           PWR2   PAC600S12-CB          2102312FFUBTKB01****     02312FFU
------------------------------------------------------------------------------

```

**Table 1** Description of the **display device elabel brief** command output
| Item | Description |
| --- | --- |
| Equipment SN(ESN) | Device serial number. |
| License ESN | License serial number. |
| SlotID | Slot ID. |
| Sub | If it is a subcard, the subcard slot is displayed.  In other cases, the hardware type is displayed. |
| Type | Type of an electronic label. |
| SN | Serial number, which corresponds to the value of Barcode in the electronic label. |
| P/N | Part number, which corresponds to the value of Item in the electronic label. |