Configuring MP Implementations
==============================

An MP-Group interface is a logical interface used by MP applications. MP is implemented by adding multiple interfaces to an MP-Group interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   An MP-Group interface is created, and the MP-Group interface view is displayed.
3. Assign an IP address to the MP-Group interface.
   
   Perform either of the following operations to assign an IP address to the MP-Group interface:
   * To specify an IP address, run:
     
     Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   * To configure the MP-Group interface to obtain an IP address from the remote device using PPP negotiation, run:
     
     Run [**ip address ppp-negotiate**](cmdqueryname=ip+address+ppp-negotiate)
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface serial**](cmdqueryname=interface+serial) *interface-number*
   
   
   
   The interface view is displayed.
6. Run [**ppp mp mp-group**](cmdqueryname=ppp+mp+mp-group) *number*
   
   
   
   The interface is added to the MP-Group interface so that the interface works in MP mode.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The *number* value specified in this step must be the same as the *number* value specified in Step 2.
   
   Repeat Steps 5 and 6 to add multiple interfaces to the MP-Group interface.
7. (Optional) Configure authentication. For detailed information about authentication configuration, see [Configuring Unidirectional PAP Authentication](dc_ne_ppp_cfg_0011.html) or [Configuring Unidirectional CHAP Authentication](dc_ne_ppp_cfg_0015.html).
8. After completing the configuration, restart all the physical interfaces to trigger PPP negotiation so that the physical interfaces are successfully added to the MP-Group interface.
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is shut down.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is restarted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
9. (Optional) Run [**cpos mix-link-protocol enable**](cmdqueryname=cpos+mix-link-protocol+enable)
   
   
   
   The coexistence of MP-Group services and any of TDM, ATM, and IMA services on CPOS subcards is enabled.
   
   In VS mode, this command is supported only by the admin VS.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.