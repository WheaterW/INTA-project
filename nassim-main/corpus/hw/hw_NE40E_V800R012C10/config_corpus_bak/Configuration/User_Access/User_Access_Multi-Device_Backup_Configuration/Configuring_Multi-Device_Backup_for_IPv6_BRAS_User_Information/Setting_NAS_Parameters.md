Setting NAS Parameters
======================

By setting NAS parameters, you can ensure that the master and backup BRASs send the same information to the remote servers, which allows users to log in through the backup device without authentication again.

#### Context

Users can configure logical IP addresses, logical interfaces, and logical host names in the remote backup profile. The NAS-IP-Address, NAS-Port and Option82 information in the packets sent from two devices that back up each other to the RADIUS and DHCP servers is identical. To ensure that user traffic can be backed up in real time, perform the following operations on devices that back up each other:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP view is displayed.
3. Run [**service-type**](cmdqueryname=service-type) **bras**
   
   
   
   The RBS of BRAS user information is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**nas**](cmdqueryname=nas) { **logic-ip** *ip-address* | **logic-port** { **eth-trunk** | **ethernet** | **gigabitethernet** } *interface-name* | **logic-sysname** *host-name* }
   
   
   
   The logic IP address, logic interface, and logic host name are configured. Ensure that the devices that back up each other send the same information about NAS-IP-Address, NAS-Port, NAS-Port-ID, and Option 82 contained in the packets to the RADIUS and DHCP servers.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.