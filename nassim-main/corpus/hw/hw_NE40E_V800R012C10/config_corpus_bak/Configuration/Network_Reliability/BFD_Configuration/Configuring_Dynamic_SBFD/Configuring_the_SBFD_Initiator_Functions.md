Configuring the SBFD Initiator Functions
========================================

The functions of the Seamless Bidirectional Forwarding Detection (SBFD) initiator can be configured, in addition to the reflector functions, implementing rapid SBFD link detection.

#### Usage Scenario

SBFD is a simplified BFD mechanism and involves the initiator and reflector:

* Initiator: functions as a detection end to implement the SBFD state machine and detection mechanism and triggers service protection.
* Reflector: only responds to SBFD packets sent by the initiator. It does not implement the state machine or detection mechanism and is not associated with services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**sbfd**](cmdqueryname=sbfd)
   
   
   
   SBFD is enabled, and the SBFD view is displayed.
5. Configure the mapping between the IP address and discriminator of the SBFD reflector.
   
   
   * (Optional) To enter the SBFD view and configure the mapping between the IPv4 address and discriminator of the SBFD reflector, run the [**destination ipv4**](cmdqueryname=destination+ipv4) *ip-address* [**remote-discriminator**](cmdqueryname=remote-discriminator) *discriminator-value* command.
   * To enter the SBFD view and configure the mapping between the IPv6 address and discriminator of the SBFD reflector, run the [**destination**](cmdqueryname=destination) **ipv6** *Ipv6Address* [**remote-discriminator**](cmdqueryname=remote-discriminator) *discriminator-value* or [**destination**](cmdqueryname=destination) **ipv6** *Ipv6Address* [**remote-discriminator**](cmdqueryname=remote-discriminator) *DiscrIpAddress* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For more information about SBFD configurations, see Segment Routing Configuration.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.