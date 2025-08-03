Locking a NAT Address Segment
=============================

Locking an address segment that is faulty or needs to be reclaimed can prevent user offline. This function is applicable to both the centralized and distributed scenarios.

#### Context

The function of locking an address segment allows reclaiming of useless IP addresses and prevents new users from using these IP addresses. The IP addresses in the locked address segment are reclaimed after all the old users go offline. In distributed scenarios, after an address segment is locked, the CGN device does not allocate IP addresses from the address segment after it is associated with online users. In centralized scenarios, after an address segment is locked, the CGN device does not allocate IP addresses from the address segment after a user table is created.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Lock NAT address segments in a specific scenario.
   1. Local an address segment in a global static address pool.
      
      
      1. Run the [**nat ip-pool**](cmdqueryname=nat+ip-pool) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] [ **slave** ] command to enter the global static address pool view.
      2. Run the [**section**](cmdqueryname=section) *section-id* **lock** command to lock an address segment in the global static address pool.
      3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   2. Local an address segment in a NAT address pool.
      
      
      1. Run the [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ] command to enter the NAT instance view.
      2. Run the [**nat address-group**](cmdqueryname=nat+address-group) *address-group-name* [ **group-id** *id* ] command to enter the NAT address pool view.
      3. Run the [**section**](cmdqueryname=section) *section-num* **lock** command to lock an address segment in the address pool.
      4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   
   
   
   IP addresses in the locked address segment cannot be allocated to users any more. To restore this address segment, run the [**undo section lock**](cmdqueryname=undo+section+lock) command.