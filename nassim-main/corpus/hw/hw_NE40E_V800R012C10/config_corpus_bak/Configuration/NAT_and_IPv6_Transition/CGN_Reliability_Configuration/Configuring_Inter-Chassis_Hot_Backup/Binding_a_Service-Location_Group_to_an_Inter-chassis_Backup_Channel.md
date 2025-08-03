Binding a Service-Location Group to an Inter-chassis Backup Channel
===================================================================

A dual-device inter-chassis backup channel needs to be configured in the service-location group view.

#### Context

A dual-device inter-chassis backup channel needs to be configured in the service-location group view to transmit backup packets. Perform the following operations on both the master and backup devices.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-location**](cmdqueryname=service-location) *service-location-id*
   
   
   
   A service-location group is created, and the service-location group view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Service-location IDs and the number of service-location groups configured on the master and backup devices must be the same. Otherwise, backup may fail, affecting services.
3. Run [**remote-backup interface**](cmdqueryname=remote-backup+interface) *interface-type* *interface-number* [**peer**](cmdqueryname=peer) *ip-address* [ **authentication-key** *key-value* **hash-algorithm** **hmac-sha256** ]
   
   
   
   An interface for dual-device inter-chassis backup and the IP address of the peer device are specified, and the authentication function of the backup channel is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * VRRP is usually configured on the interfaces for dual-device inter-chassis backup. The VRRP protocol is used to determine the master/backup status of the members in the dual-device inter-chassis backup group. If the interface specified by *interface-type* is a virtual Ethernet interface, the performance of the interface board may be halved.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.