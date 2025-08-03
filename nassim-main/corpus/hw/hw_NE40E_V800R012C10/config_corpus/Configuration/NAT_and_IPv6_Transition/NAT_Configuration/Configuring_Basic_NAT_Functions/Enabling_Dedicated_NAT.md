Enabling Dedicated NAT
======================

Using the VSUPA-100 board for NAT is also called dedicated NAT. NAT must be enabled on the board before NAT is performed.

#### Context

By default, a device uses the on-board NAT mode, in which NAT is performed by the device's main control board. If a dedicated board is also installed on the device and needs to be used for NAT, NAT must be first enabled on this board.

This configuration process is supported only by the admin-VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsm on-board-mode disable**](cmdqueryname=vsm+on-board-mode+disable)
   
   
   
   Dedicated NAT is enabled for the device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.