(Optional) Setting the DR Priority for the OSPFv3 Broadcast or NBMA Interface
=============================================================================

You can specify the Designated Router (DR) priority for each interface on a broadcast or a non-broadcast multiple access (NBMA) network for DR/Backup Designated Router (BDR) election on the network.

#### Context

When configuring broadcast networks or NBMA networks, you can specify the DR priority for each interface for DR/BDR election on the network. The greater the value, the higher the priority.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 dr-priority**](cmdqueryname=ospfv3+dr-priority) *priovalue* [ **instance** *instanceId* ]
   
   
   
   A DR priority is set for the OSPFv3 interface.
4. (Optional) Run [**ospfv3 timer wait**](cmdqueryname=ospfv3+timer+wait) *interval* [ **instance** *instanceid* ] The wait timer is set for the OSPFv3 interface.
   
   
   
   If no Backup Seen event is received within the *interval*, the designated router (DR) election starts. Setting a proper value for the wait timer can slow down changes of the DR and the backup designated router (BDR) on the network, reducing network flapping. When setting the wait timer, note the following points:
   
   * The wait timer takes effect only on broadcast and NBMA interfaces.
   * The value of the wait timer cannot be greater than the value of the dead timer.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Changing the priority leads to a DR/BDR re-election and interrupts the OSPFv3 adjacency between Routers. Therefore, changing the priority is not recommended.

You can use either of the following methods for a DR/BDR re-election:

* Restart the OSPFv3 processes on all the Routers.
* Run the [**shutdown**](cmdqueryname=shutdown) and then [**undo shutdown**](cmdqueryname=undo+shutdown) commands on the interfaces where neighbor relationships are established.