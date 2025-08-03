(Optional) Configuring MP Fragmentation
=======================================

Setting a proper size for Multilink PPP (MP) fragments improves bandwidth use efficiency.

#### Context

To improve bandwidth use efficiency on an MP link, configure MP fragmentation and set a proper size for MP fragments.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**mp statistics fragment-mode enable**](cmdqueryname=mp+statistics+fragment-mode+enable)
   
   
   
   The fragment statistical mode is configured for all MP-group interfaces and global MP-group interfaces.
3. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   The MP-Group interface view is displayed.
4. Run [**fragment-threshold**](cmdqueryname=fragment-threshold) *threshold*
   
   
   
   The maximum size of MP fragments is set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The MP fragment maximum size of 256 bytes is recommended.
5. Run [**drop-timeout**](cmdqueryname=drop-timeout) *time-number*
   
   
   
   A timeout period is set for an MP interface to reassemble upstream MP packets.
6. Perform the following steps to restart the interface:
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is shut down.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is restarted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.