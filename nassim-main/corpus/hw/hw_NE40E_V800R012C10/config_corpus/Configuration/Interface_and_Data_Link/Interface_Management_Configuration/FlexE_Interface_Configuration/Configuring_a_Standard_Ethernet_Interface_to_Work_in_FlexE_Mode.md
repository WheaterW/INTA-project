Configuring a Standard Ethernet Interface to Work in FlexE Mode
===============================================================

The bandwidth of a standard Ethernet interface is fixed. To flexibly specify the bandwidth of an interface, you need to switch its working mode from standard Ethernet to FlexE.

#### Context

After a standard Ethernet interface is switched to the FlexE mode, the system automatically creates a FlexE physical interface and deletes the services configured on the original interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flexe enable port**](cmdqueryname=flexe+enable+port) *posStr*
   
   
   
   The working mode of the Ethernet interface is switched from standard Ethernet to FlexE.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.