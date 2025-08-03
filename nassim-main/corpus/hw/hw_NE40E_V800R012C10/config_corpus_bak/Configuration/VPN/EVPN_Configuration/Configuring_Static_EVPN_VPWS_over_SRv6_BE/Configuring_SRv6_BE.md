Configuring SRv6 BE
===================

A PE's global redundancy mode determines whether the PE can work with other PEs in load-balancing mode.

#### Context

Before configuring static EVPN VPWS over SRv6 BE, you need to configure basic SRv6 BE functions.

Perform the following steps on PEs as required.


#### Procedure

* Configure basic SRv6 BE functions.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**evpn srv6 next-header-field**](cmdqueryname=evpn+srv6+next-header-field) { **59** | **143** }
     
     
     
     A value is configured for the Next Header field in an SRv6 extension header.
     
     
     
     If the value is 59 in earlier versions, you can perform this step to change the value to 59 to ensure compatibility with the earlier versions.
  3. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     
     
     SRv6 is enabled, and the SRv6 view is displayed.
  4. Configure a source address for SRv6 encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
     
     
     + Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to directly configure a source address for SRv6 encapsulation.
     + Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
       
       If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
  5. Run [**locator**](cmdqueryname=locator) *locator-name* **ipv6-prefix** *ipv6-address* *mask-length* **static** *static-length* [ **args** *args-length* ]
     
     
     
     An SRv6 locator is configured.
  6. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2** **evpl-instance** *evpl-instance-id*
     
     
     
     An opcode for static SIDs is configured.
  7. (Optional) Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dx2l** **evpl-instance** *evpl-instance-id*
     
     
     
     An opcode for End.DX2L SIDs is configured. You can run this command to manually specify a SID for a bypass path.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the SRv6 locator view.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the SRv6 view.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Enable IS-IS SRv6.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
     
     
     
     The IPv6 capability is enabled for the IS-IS process in the IPv6 topology.
  4. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
     
     
     
     IS-IS SRv6 is enabled.
     
     
     
     In this command, the value of *locator-name* must be the same as that specified using the [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ] command.
  5. (Optional) Run [**segment-routing ipv6 auto-sid advertise**](cmdqueryname=segment-routing+ipv6+auto-sid+advertise) { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc** | **coc** | **psp-coc** } \*
     
     
     
     The function to adjust the flavors to be carried in dynamically allocated End and End.X SIDs is enabled.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the IS-IS view.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.