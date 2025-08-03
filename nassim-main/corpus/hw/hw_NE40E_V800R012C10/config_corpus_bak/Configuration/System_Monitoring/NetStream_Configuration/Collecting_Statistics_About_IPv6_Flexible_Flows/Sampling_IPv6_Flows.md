Sampling IPv6 Flows
===================

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a sampling mode and sampling ratio by performing at least one of the following steps:
   
   
   * Configure a sampling mode and sampling ratio globally.
     1. Run [**ipv6 netstream sampler**](cmdqueryname=ipv6+netstream+sampler) { **fix-packets** *fix-packet-number* | **random-packets** *random-packet-number* | **fix-time** *fix-time-number* } { **inbound** | **outbound** }
        
        A sampling mode and sampling ratio are configured globally.
     2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
   * Configure a sampling mode and sampling ratio on an interface.
     1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The interface view is displayed.
     2. Run [**ipv6 netstream sampler**](cmdqueryname=ipv6+netstream+sampler) { **fix-packets** *fix-packet-number* | **random-packets** *random-packet-number* | **fix-time** *fix-time-number* } { **inbound** | **outbound** }
        
        A sampling mode and sampling ratio are configured on the interface.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        The sampling mode and sampling ratio configured in the system view apply to all interfaces on the device. The sampling mode and sampling ratio configured in the interface view take precedence over those configured in the system view.
        
        
        The [**ipv6 netstream sampler**](cmdqueryname=ipv6+netstream+sampler) command run in the system view has the same function as that run in the interface view.
        + The execution of either command takes effect on all packets, and there is no need to configure both of them. If both of them are configured, ensure that the sampling modes configured using the two commands are the same.
        + Packets are sampled at the set sampling ratio, regardless of packet types. For example, if the sampling ratio in fixed packet sampling mode is set to 1000:1, one packet will be sampled every 1000 packets, regardless of whether these packets are IPv4 or IPv6 packets.
3. Run [**ipv6 netstream**](cmdqueryname=ipv6+netstream) { **inbound** | **outbound** }
   
   
   
   NetStream is enabled on the interface. Statistics about packets' BGP next-hop information can also be collected.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For an interface bound to a VPN instance, NetStream applies to all packets of the VPN instance.
4. (Optional) Run [**ipv6 netstream statistics enable**](cmdqueryname=ipv6+netstream+statistics+enable)
   
   
   
   The traffic statistics diagnosis function is enabled so that you can compare the traffic statistics collected by the device with those restored by the NMS to determine the cause of inaccurate sampling.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.