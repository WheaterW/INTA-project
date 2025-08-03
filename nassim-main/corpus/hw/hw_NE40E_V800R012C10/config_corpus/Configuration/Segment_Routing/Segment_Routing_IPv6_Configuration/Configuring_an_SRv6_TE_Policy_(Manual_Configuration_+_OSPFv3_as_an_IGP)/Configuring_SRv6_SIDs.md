Configuring SRv6 SIDs
=====================

The headend can orchestrate network paths only if SIDs are allocated to adjacencies and nodes on the network.

#### Context

An SRv6 TE Policy can contain multiple candidate paths defined using segment lists. SIDs, such as End and End.X SIDs, are mandatory for SRv6 TE Policies. The SIDs can either be configured manually or be generated dynamically using an IGP.

* In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
* In scenarios where SRv6 TE Policies are delivered dynamically by a controller, you are also advised to configure SIDs manually. Although the controller can detect SID changes through BGP-LS, SIDs that are generated dynamically using an IGP change randomly, complicating routine maintenance and fault locating.


#### Procedure

* Configure SRv6 SIDs.
  
  
  
  SRv6 paths are established based on SIDs, which can either be configured manually or be generated dynamically using OSPFv3. Use either of the following configuration methods:
  
  
  
  + Configure SIDs manually.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **ipv6-prefix** *ipv6-address* *prefix-length* specifies the locator prefix and prefix length.
       
       **static** *static-length* specifies the static segment length, which determines the number of static SIDs that can be configured in the locator.
       
       **args** *args-length* specifies the argument segment length. Arguments can be used to define flow, service, and other information for packets.
    4. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end** { **no-flavor** | **psp** | **psp-usp-usd** }An opcode for static End SIDs is configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the **no-flavor** parameter is specified, SRv6 SIDs carry only the ultimate segment POP of the SRH (USP) flavor.
       
       If the **psp** parameter is specified, SRv6 SIDs carry only the penultimate segment POP of the SRH (PSP) flavor.
       
       If the **psp-usp-usd** parameter is specified, SRv6 SIDs carry all the PSP, USP, and ultimate segment decapsulation (USD) flavors. The USD flavor is often used in SRv6 TE Policy scenarios without service SIDs (for example, a scenario where IPv4 public network services without End.DT4 SIDs are redirected to an SRv6 TE Policy). When the packets of such services are forwarded to the device identified by the last SID, the USD flavor of the SID instructs this device to decapsulate the packets.
    5. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-x** **interface** *interface-name* **nexthop** *nexthop-address* { **no-flavor** | **psp** | **psp-usp-usd** }
       
       An opcode for static End.X SIDs is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The functions of the **no-flavor**, **psp**, and **psp-usp-usd** parameters are the same as those in the [**opcode**](cmdqueryname=opcode) **end** command described in the previous step.
       
       A GRE tunnel interface can be specified using **interface** *interface-name*.
    6. Run [**quit**](cmdqueryname=quit)
       
       Exit the Segment Routing IPv6 locator view.
    7. (Optional) Run [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) *delay-time*
       
       A delay in delivering a static End.X SID to the forwarding table is configured.
       
       The [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) command is mainly used in scenarios where the outbound interface associated with a static End.X SID changes from down to up and IGP routes reconverge.
    8. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    9. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
       
       The OSPFv3 process view is displayed.
    10. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
        
        OSPFv3 SRv6 is enabled.
    11. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  + Configure OSPFv3 to dynamically generate SIDs.
    1. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **ipv6-prefix** *ipv6-address* *prefix-length* specifies the locator prefix and prefix length.
       
       **static** *static-length* specifies the static segment length, which determines the number of static SIDs that can be configured in the locator.
       
       **args** *args-length* specifies the argument segment length. Arguments can be used to define flow, service, and other information for packets.
    2. (Optional) Run [**index**](cmdqueryname=index+local-block+sid-reserve) *index-id* **local-block sid-reserve** *number-value*
       
       A range reserved for binding SIDs (BSIDs) is configured in the locator.
       
       In a scenario where a controller dynamically delivers SRv6 TE Policies, you can run this command to configure a range reserved for BSIDs. Forwarders use BGP-LS to report the range to the controller, which then allocates BSIDs within this range to SRv6 TE Policies or segment lists.
    3. Run [**quit**](cmdqueryname=quit)
       
       Exit the Segment Routing IPv6 locator view.
    4. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    5. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
       
       The OSPFv3 process view is displayed.
    6. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
       
       OSPFv3 SRv6 is enabled.
    7. (Optional) Run [**segment-routing ipv6 compatible locator-fixed-length**](cmdqueryname=segment-routing+ipv6+compatible+locator-fixed-length)
       
       A fixed length is configured for the Locator field in the SRv6 Locator TLV carried in an SRv6 Locator LSA.
       
       As defined in *draft-ietf-lsr-ospfv3-srv6-extensions-12* and later versions, the length of the Locator field in the SRv6 Locator TLV carried in an SRv6 Locator LSA is variable. To facilitate the interworking between protocols defining different lengths for the Locator field, you can run this command to configure the Locator field to be fixed at 128 bits.
    8. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.