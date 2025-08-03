Configuring Basic SRv6 SFC Functions
====================================

This section describes how to configure basic Service Function Chaining (SFC) functions based on SRv6 TE Policy.

#### Prerequisites

Before configuring basic SRv6 SFC functions, complete the following task:

* Configure IS-IS to ensure IPv6 connectivity between the SC, SFFs, and tail end.
* (Optional) Configure VPN instances for SRv6 nodes as needed.
* Configure basic SRv6 functions on the network, a static End SID for each SRv6 node, and End.DT4 SIDs for the IPv4 public network instances or VPN instances on the SC and tail end.

#### Context

SFC logically connects services on network devices to provide an ordered service set for the application layer. By adding service function path (SFP) information in original packets, SFC enables packets to pass through service functions (SFs) along a specified path.

By using segment lists, an SRv6 TE Policy instructs network devices to forward traffic along a specified path. This mechanism is suitable for implementing SFC. Specifically, if a data packet is steered into an SRv6 TE Policy, the headend adds the segment lists of the SRv6 TE Policy to the data packet, and other devices on the network execute the instructions embedded in the segment lists.

On the network shown in [Figure 1](#EN-US_TASK_0219099856__fig17829184811218), SF1 and SF2 are SRv6-unaware SFs. To implement SFC, SF proxy must be configured on SFF1 and SFF2, and SRv6 SIDs must be allocated to SF1 and SF2 proxies. On the SC, the SF1 Proxy SID, SF2 Proxy SID, and Tail End SID form a segment list of an SRv6 TE Policy. The SRv6 TE Policy functions as an SFP.

**Figure 1** SRv6 TE Policy-based SFC forwarding  
![](figure/en-us_image_0221084505.png "Click to enlarge")

#### Procedure

1. Manually configure an SRv6 TE Policy on the SC or use a controller to deliver an SRv6 TE Policy to the SC. The segment list of the SRv6 TE Policy consists of the SF1 Proxy SID, SF2 Proxy SID, and Tail-End SID.
2. Configure a traffic policy on the SC to redirect traffic to the SRv6 TE Policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured and its view is displayed.
   3. Run **if-match**
      
      
      
      A match condition is specified for the traffic classifier.
      
      
      
      Currently, SRv6 SFC supports only IPv4 services. Therefore, the match condition must be set based on IPv4 packets.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the traffic classifier view.
   5. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is defined and its view is displayed.
   6. Run [**redirect srv6-te policy**](cmdqueryname=redirect+srv6-te+policy) *endpoint* *color* [ **sid** *sid-ip* ]
      
      
      
      IPv4 traffic is redirected to SRv6 TE Policies.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the traffic behavior view.
   8. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is defined and its view is displayed.
   9. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      
      
      The traffic behavior is specified for the traffic classifier in the traffic policy.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the traffic policy view.
   11. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ *.subinterface-number* ]
       
       
       
       The interface view is displayed.
       
       
       
       Currently, only VBDIF interfaces are supported.
   12. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound**
       
       
       
       The traffic policy is applied to the interface.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Configure an SFF.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   4. Run [**opcode**](cmdqueryname=opcode) *func-opcode1* **end-as**
      
      
      
      An operation code (opcode) is configured for static End.AS SIDs, and the static SRv6 SFC proxy view is displayed.
   5. Run [**inner-type ipv4**](cmdqueryname=inner-type+ipv4)
      
      
      
      The type of the original packets to be sent from the SFF to an SF is configured.
      
      
      
      Currently, SRv6 SFC supports only IPv4 packets, which are required to contain only IPv4 headers and payloads.
   6. Run either of the following commands to configure the SFF-to-SF packet forwarding mode:
      
      
      
      The following commands are mutually exclusive and cannot both be configured. Select a proper packet forwarding mode and set proper parameters based on the network environment of the target SF.
      
      * To configure Layer 3 IP forwarding from the SFF to the SF, run the [**encapsulation ipv4 nexthop**](cmdqueryname=encapsulation+ipv4+nexthop)*nexthop-addr* **out-interface** { *outInfName* | *outInfType* *outInfNumber* } **in-interface** { *inInfName* | *inInfType* *inInfNumber* } [ **symmetric-index** *index-value* ] command.
        
        In the command, both **out-interface** and **in-interface** specify interfaces on the SFF, where **out-interface** is used for sending traffic to the SF and **in-interface** is used for receiving traffic from the SF. Currently, **out-interface** and **in-interface** can only be VBDIF interfaces. VBDIF interfaces usually need to be bound to VPN instances for service isolation.
      * To configure Layer 2 forwarding from the SFF to the SF, run the [**encapsulation eth out-interface**](cmdqueryname=encapsulation+eth+out-interface){ *outIntfname* | *outInfType* *outInfNum* } [ **out-vlan** *out-vlan-id* [ **ce-vid** *out-cevid* ] ] **in-interface** { *inIntfname* | *inInfType* *inInfNum* } [ **in-vlan** *in-vlan-id* [ **ce-vid** *in-cevid* ] ] [ **dest-mac** *destMac* ] command.
        
        In the command, both **out-interface** and **in-interface** specify interfaces on the SFF, where **out-interface** is used for sending traffic to the SF and **in-interface** is used for receiving traffic from the SF. Currently, **out-interface** and **in-interface** can only be EVC sub-interfaces. The VLAN IDs, including those configured using **out-vlan** *out-vlan-id* and **in-vlan** *in-vlan-id* must be the same as the VLAN IDs configured using the [**encapsulation dot1q vid**](cmdqueryname=encapsulation+dot1q+vid) command on the EVC sub-interfaces.
   7. Run [**cache source-address**](cmdqueryname=cache+source-address)*ipv6-address*
      
      
      
      A source IPv6 address is configured for the SFF to re-encapsulate this address into the SRv6 SFC packets returned from the SF.
   8. Run [**cache list**](cmdqueryname=cache+list){ *ipv6-address* } &<1-11>
      
      
      
      An SRH is configured for the SFF to re-encapsulate this SRH into the SRv6 SFC packets returned from the SF.
   9. (Optional) Run [**diffserv-mode**](cmdqueryname=diffserv-mode){ **pipe** *service-class* *color* | **uniform** }
      
      
      
      A DiffServ mode is configured for the SFC packets returned from the SF to the SFF.
   10. (Optional) Run [**ttl-mode**](cmdqueryname=ttl-mode){ **pipe** *ttl-value* | **uniform** }
       
       
       
       A TTL processing mode is configured for the SFC packets returned from the SF to the SFF.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
4. Configure the tail end.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
      
      
      
      SRv6 is enabled, and the SRv6 view is displayed.
   3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
      
      
      
      An SRv6 locator is configured, and the SRv6 locator view is displayed.
   4. Run [**opcode**](cmdqueryname=opcode)*func-opcode* **end-dt4** [ **vpn-instance** *vpn-name* ]
      
      
      
      A static End.DT4 SID's operation code (Opcode) is configured.
      
      
      
      If **vpn-instance** *vpn-name* is specified, the tail end forwards packets to the specified VPN instance. If **vpn-instance** *vpn-name* is not specified, the tail end searches the public IP routing table to forward the packets.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After completing the SRv6 SFC configuration, run the following commands to verify the configuration:

* Run the [**display segment-routing ipv6 local-sid end-as**](cmdqueryname=display+segment-routing+ipv6+local-sid+end-as) [ *sid-value* ] **forwarding** command to check the SRv6 local SID table containing End.AS SIDs.
* Run the [**display segment-routing ipv6 local-sid end-dt4**](cmdqueryname=display+segment-routing+ipv6+local-sid+end-dt4) [ *sid-value* | **vpn-instance** *vpn-name* ] **forwarding** command to check the SRv6 local SID table containing End.DT4 SIDs.