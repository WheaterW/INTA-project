Creating an Eth-Trunk Interface in Manual 1:1 Master/Backup Mode
================================================================

Before bundling physical interfaces into an Eth-Trunk interface, create this Eth-Trunk interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   An Eth-Trunk interface is created, and its view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Eth-Trunk interface is switched to Layer 2 mode.
4. Run [**mode manual backup**](cmdqueryname=mode+manual+backup)
   
   
   
   The Eth-Trunk interface is configured to work in manual 1:1 master/backup mode.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.