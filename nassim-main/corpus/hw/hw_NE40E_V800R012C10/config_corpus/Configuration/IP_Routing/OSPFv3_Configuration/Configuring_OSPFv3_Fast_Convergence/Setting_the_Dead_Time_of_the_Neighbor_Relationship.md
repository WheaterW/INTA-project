Setting the Dead Time of the Neighbor Relationship
==================================================

If a device does not receive a Hello packet from its neighbor within the dead interval, the device considers the neighbor Down.

#### Context

Perform the following steps on the OSPFv3 router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 timer dead**](cmdqueryname=ospfv3+timer+dead) *interval* [ **instance** *instance-id* ]
   
   
   
   A dead timer is configured for the neighboring Router.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the dead timer is shorter than 10s, the neighbor relationship may be torn down. To prevent this issue, the dead timer of 10 seconds takes effect if the value of **dead** *interval* is less than 10 seconds. However, if the [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) command is run, the **conservative** parameter is specified to enable the conservative mode for the neighbor dead timer, and the configured dead timer is less than 10s, the system still uses the configured value to determine whether a neighbor is down.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.