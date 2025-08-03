(Optional) Configuring an APN ID Isolation Policy
=================================================

By identifying the APN IDs of packets, you can isolate and control services.

#### Prerequisites

Basic APN6 functions have been configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**apn**](cmdqueryname=apn)
   
   
   
   The APN view is created and displayed.
3. Run [**ipv6**](cmdqueryname=ipv6)
   
   
   
   The APN IPv6 view is created and displayed.
4. Run [**isolate-group name**](cmdqueryname=isolate-group+name) *group-name*
   
   
   
   An APN isolation group is configured.
5. (Optional) Map a VPN instance with the isolation group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is mandatory only when the outbound interface is an SRv6 tunnel interface.
   
   
   
   1. Run the [**isolate-group mapping-vpn**](cmdqueryname=isolate-group+mapping-vpn) command to create and enter the view for mapping a VPN instance with an isolation group.
   2. Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* **peer-locator** *peer-locator-value* *mask-length* [**match isolate-group**](cmdqueryname=match+isolate-group) *group-name* command to map a VPN instance with the isolation group.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the APN IPv6 view.
6. Configure an APN ID isolation policy.
   1. Run the [**apn-id isolate policy**](cmdqueryname=apn-id+isolate+policy) *policy-name* command to configure an APN ID isolation policy and enter its view.
   2. (Optional) Run the [**statistics enable**](cmdqueryname=statistics+enable) command to configure the statistics collection function for the APN ID isolation policy.
   3. Run the [**index**](cmdqueryname=index) *index-value* **instance** *instance-name* **isolate-group** *group-name* **behavior** **deny** command to configure a system behavior for the traffic that belongs to the mapped APN ID instance of an isolation group.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the APN IPv6 view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the APN view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. (Optional) Add the related interface to the isolation group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is mandatory only when service traffic is isolated through different interfaces.
   
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
   2. Run the [**apn-id-ipv6 isolate-group**](cmdqueryname=apn-id-ipv6+isolate-group) *group-name* command to specify an isolation group for the interface.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
10. Apply the isolation policy.
    1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
    2. Run the [**apn-id-ipv6 isolate-policy**](cmdqueryname=apn-id-ipv6+isolate-policy) *policy-name* [**inbound**](cmdqueryname=inbound) command to apply the APN ID isolation policy to the VPN instance.
    3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
    4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.

#### Follow-up Procedure

* Run the [**display apn-id-ipv6 isolate-policy statistics**](cmdqueryname=display+apn-id-ipv6+isolate-policy+statistics) [[ **policy** *policy-name* ] [ **vpn-instance** *instance-name* ] ] command to check the traffic statistics of VPN instances mapped with isolation policies.