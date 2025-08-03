Configuring a PHY Number for a FlexE Physical Interface
=======================================================

To ensure normal communication between interconnected devices, you need to configure the same PHY number for the FlexE physical interfaces on both of them.

#### Context

Different FlexE physical interfaces can be configured with the same PHY number. However, the FlexE physical interfaces with the same PHY number cannot be added to the same FlexE group, and a FlexE physical interface can be added to only one FlexE group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The FlexE physical interface view is displayed.
3. Run [**phy-number**](cmdqueryname=phy-number) *phyNum*
   
   
   
   A PHY number is configured for the FlexE physical interface.
4. (Optional) Run [**management-channel mode**](cmdqueryname=management-channel+mode) { **union** | **section** | **shim-to-shim** | **shim-to-shim-op2** }
   
   
   
   A management channel mode is configured for the FlexE physical interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command is not supported on the NE40E-M2E and NE40E-M2F.
5. (Optional) Run [**down-filter disable**](cmdqueryname=down-filter+disable)
   
   
   
   Down interrupt suppression is disabled on the FlexE physical interface.
6. (Optional) Run [**switch-mode**](cmdqueryname=switch-mode) { **manual** | **auto** }
   
   
   
   A switching mode is configured for the FlexE physical interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be run only on port 0 of a 2x50GE subcard.
   
   This command is not supported on the NE40E-M2E and NE40E-M2F.
7. (Optional) Run [**port-speed**](cmdqueryname=port-speed) { **50GE** | **100GE** }
   
   
   
   A rate mode is configured for the FlexE physical interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be run only on port 0 of a 2x50GE subcard.
   
   This command is not supported on the NE40E-M2E and NE40E-M2F.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.