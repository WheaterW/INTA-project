Setting the Dead Time of an OSPF Neighbor
=========================================

If no Hello packet is received from a neighbor within a dead interval, the neighbor is considered Down.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run [**ospf timer dead**](cmdqueryname=ospf+timer+dead) *interval*
   
   
   
   A dead timer is set for OSPF neighbor relationships.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the dead timer is shorter than 10s, the neighbor relationship may be torn down. To prevent this issue, the dead timer of 10 seconds takes effect if the value of **dead** *interval* configured for OSPF neighbor relationships is less than 10 seconds. However, if the [**ospf timer hello**](cmdqueryname=ospf+timer+hello) command is run, the **conservative** parameter is specified to enable the conservative mode for the neighbor dead timer, and the configured dead timer is less than 10s, the system still uses the configured value to determine whether a neighbor is down.
   
   Changing the network type will restore both the Hello timer and dead timer to their default values.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.