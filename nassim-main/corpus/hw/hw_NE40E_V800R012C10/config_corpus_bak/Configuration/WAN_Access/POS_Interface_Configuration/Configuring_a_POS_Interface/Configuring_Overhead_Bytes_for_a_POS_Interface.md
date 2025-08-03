Configuring Overhead Bytes for a POS Interface
==============================================

SONET/SDH provides a variety of overhead bytes to implement
monitoring at different levels.

#### Context

C2, the path signal label byte, is contained in the higher-order
path overhead. C2 is used to specify the multiplexing structure and
the attributes of the information payload in a VC frame.

J0, the regenerator section trace byte, is contained in the section
overhead. J0 is used to check the continuity between two ports at
the section layer.

J1, the higher-order VC-N path trace byte, is used to check the continuity
between two ports at the path layer.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

C2, J0, and J1 of the receiver must be the same as those of the
transmitter; otherwise, the two ends cannot communicate.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The POS interface
   view is displayed.
3. Configure the overhead byte for the POS interface.
   
   
   
   Run the following command as required.
   
   * Run [**flag**](cmdqueryname=flag) **j0** **64byte-or-null-mode** [ *j0-value* ] or [**flag**](cmdqueryname=flag) **j0** { **16byte-mode** | **1byte-mode** } *j0-value* or [**flag**](cmdqueryname=flag) **j0** **peer**
     
     The overhead byte J0 is configured for the interface.
   * Run [**flag**](cmdqueryname=flag) **j1** **64byte-or-null-mode** [ *j1-value* ] or [**flag**](cmdqueryname=flag) **j1** { **16byte-mode** | **1byte-mode** } *j1-value* or [**flag**](cmdqueryname=flag) **j1** **peer**
     
     The overhead byte J1 is configured for the interface.
   * Run [**flag**](cmdqueryname=flag) **c2** *c2-value*
     
     The overhead byte C2 is configured
     for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.