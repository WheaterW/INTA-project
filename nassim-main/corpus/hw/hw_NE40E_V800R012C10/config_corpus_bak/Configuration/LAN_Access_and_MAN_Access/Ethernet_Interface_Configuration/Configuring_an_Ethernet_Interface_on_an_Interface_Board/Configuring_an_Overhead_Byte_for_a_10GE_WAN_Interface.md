Configuring an Overhead Byte for a 10GE WAN Interface
=====================================================

SONET/SDH provides a variety of overhead bytes to implement monitoring at different levels.

#### Context

A 10GE WAN interface needs to adapt to SDH/SONET when processing data packets. Therefore, you need to configure an overhead byte for the interface.

Perform the following steps on the Router:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported by the following: NE40E-M2K-B.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The specified Ethernet interface view is displayed.
3. Configure an overhead byte for the 10GE WAN interface.
   
   
   
   Run any of the following commands as needed.
   
   * To configure the overhead byte j0 for the interface, run the [**flag**](cmdqueryname=flag+j0+64byte-or-null-mode) **j0** **64byte-or-null-mode** [ *64byte-value* ] or [**flag**](cmdqueryname=flag+j0+16byte-mode+1byte-mode) **j0** { **16byte-mode** [16byte-value] | **1byte-mode** [*1byte-value*] } command.
   * To configure the overhead byte j1 for the interface, run the [**flag**](cmdqueryname=flag+j1+64byte-or-null-mode) **j1** **64byte-or-null-mode** [ *64byte-value* ] or [**flag**](cmdqueryname=flag+j1+16byte-mode+1byte-mode) **j1** { **16byte-mode** [16byte-value] | **1byte-mode** [*1byte-value*] } command.
   * To configure the overhead byte c2 for the 10GE WAN interface, run the [**flag**](cmdqueryname=flag+c2) **c2** *c2-value* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.