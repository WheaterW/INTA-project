Optimizing the replace Operation Performance for NETCONF Configuration Packets
==============================================================================

Optimizing the replace Operation Performance for NETCONF Configuration Packets

#### Context

When NETCONF is used to deliver the replace operation to a remote device, the configuration delivery may time out, fail, or take a long time because a large number of configurations exist on the device. In this case, you can enable the function of optimizing the replace operation performance for NETCONF configuration packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**netconf**](cmdqueryname=netconf)
   
   
   
   The NETCONF user interface view is displayed.
3. Run [**config-cache enable**](cmdqueryname=config-cache+enable)
   
   
   
   The function of optimizing the replace operation performance for NETCONF configuration packets is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.