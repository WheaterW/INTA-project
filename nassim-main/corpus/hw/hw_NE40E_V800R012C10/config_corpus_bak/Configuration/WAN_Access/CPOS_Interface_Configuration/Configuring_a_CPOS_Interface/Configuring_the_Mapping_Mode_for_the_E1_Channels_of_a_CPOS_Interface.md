Configuring the Mapping Mode for the E1 Channels of a CPOS Interface
====================================================================

CPOS interfaces support three E1 channel mapping modes:
a-mode, h-mode, and l-mode.

#### Context

Different vendors' devices have different number calculation
formulas for multiplexing CPOS E1 to STM-1.

To enable a device
to interwork with other vendors' devices using CPOS interfaces, you
must ensure that the E1 channel mapping mode on the device is the
same as that on other vendors' devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view
   is displayed.
2. Run [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number*
   
   
   
   The CPOS interface
   view is displayed.
3. Run [**mapping-mode**](cmdqueryname=mapping-mode) { **a-mode** | **h-mode** | **l-mode** }
   
   
   
   An E1 channel mapping
   mode is configured for the CPOS interface.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Before configuring the E1 channel
   mapping mode of a CPOS interface, ensure that no E1 channel is created
   on the CPOS interface.
   
   * **a-mode**:
     
     Configures the Alcatel mode (a-mode) as the E1 channel mapping mode of a CPOS interface. This mode applies when the E1 channel mapping mode of the interconnected device is the Alcatel mode. In this mode, E1 channel number = (TUG-3 number â 1) x 21 + TUG-2 number + (TU-12 number â 1) x 7.
   * **h-mode**:
     
     Configures the Huawei mode (h-mode) as the E1 channel mapping mode of a CPOS interface. This mode applies when the E1 channel mapping mode of the interconnected device is the Huawei mode. In this mode, E1 channel number = TUG-3 number + (TUG-2 number â 1) x 3 + (TU-12 number â 1) x 21.
   * **l-mode**:
     
     Configures the Lucent mode (l-mode) as the E1 channel mapping mode of a CPOS interface. This mode applies when the E1 channel mapping mode of the interconnected device is the Lucent mode. In this mode, E1 channel number = (TUG-3 number â 1) Ã 21 + (TUG-2 number â 1) x 3 + TU-12 number![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The numbers listed in the preceding formula stand for the positions in a VC-4 frame. The TUG-3 number ranges from 1 to 3; the TUG-2 number ranges from 1 to 7; the TU-12 number ranges from 1 to 3.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.