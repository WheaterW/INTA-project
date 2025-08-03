Configuring Route Recursion to SRv6 TE Policies
===============================================

EVPN VPWS is deployed based on the EVPN service architecture. Before configuring EVPN VPWS over SRv6 BE, you need to configure EVPN functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
   
   
   
   A value is configured for the Next Header field in an SRv6 extension header.
   
   
   
   If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled for the IPv6 forwarding plane, and the SRv6 view is displayed.
4. Run [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ]
   
   
   
   A source address is specified for SRv6 EVPN encapsulation.
5. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
   * Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
   * Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
     
     If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
6. Run [**locator**](cmdqueryname=locator) *locator-name* **ipv6-prefix** *ipv6-address* *mask-length* **static** *static-length* [ **args** *args-length* ]
   
   
   
   An SRv6 locator is configured, and its view is displayed.
7. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2** **evpl-instance** *evpl-instance-id*
   
   
   
   An opcode for static SIDs is configured.
8. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2l** **evpl-instance** *evpl-instance-id*
   
   
   
   An opcode for End.DX2L SIDs is configured. You can run this command to manually specify a SID for a bypass path.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the SRv6 locator view.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the SRv6 view.
11. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* **static-mode**
    
    
    
    The static EVPL instance view is displayed.
12. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
    
    
    
    The device is enabled to add the SID attribute to EVPN routes to be sent.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Static SRv6 EVPN VPWS supports only static SIDs. Configure a static SID for the locator specified by *locator-name*.
13. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the static EVPL instance view.
14. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
    
    
    
    The VPWS EVPN instance view is displayed.
15. Run [**segment-routing ipv6 traffic-engineer**](cmdqueryname=segment-routing+ipv6+traffic-engineer) [ **best-effort** ]
    
    
    
    The function to recurse EVPN VPWS services to SRv6 TE Policies is enabled.
    
    
    
    If an SRv6 BE path exists on the network, you can set the **best-effort** parameter, allowing the SRv6 BE path to function as a best-effort path in the case of an SRv6 TE Policy fault.
16. Run [**quit**](cmdqueryname=quit)
    
    
    
    Return to the system view.
17. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.