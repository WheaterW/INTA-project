Configuring SRv6 SIDs
=====================

The headend can orchestrate network paths only if SIDs are allocated to adjacencies and nodes on the network.

#### Context

An SRv6 TE Policy can contain multiple candidate paths defined using segment lists. SIDs, such as End and End.X SIDs, are mandatory for SRv6 TE Policies. The SIDs can either be configured manually or be generated dynamically using an IGP.

* In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
* In scenarios where SRv6 TE Policies are delivered dynamically by a controller, you are also advised to configure SIDs manually. Although the controller can detect SID changes through BGP-LS, SIDs that are generated dynamically using an IGP change randomly, complicating routine maintenance and fault locating.


#### Procedure

* Configure SRv6 SIDs in non-compression mode.
  
  
  
  SRv6 paths are established based on SIDs, which can either be configured manually or be generated dynamically using IS-IS. Use either of the following configuration methods:
  
  
  
  + Configure SIDs manually.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]An SRv6 locator is configured, and the SRv6 locator view is displayed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **ipv6-prefix** *ipv6-address* *prefix-length* specifies the locator prefix and prefix length.
       
       **static** *static-length* specifies the static segment length, which determines the number of static SIDs that can be configured in the locator.
       
       **args** *args-length* specifies the argument segment length. Arguments can be used to define flow, service, and other information for packets.
       
       **flex-algo** *flexAlgoId* specifies the Flex-Algo associated with the locator. The IGP advertises the locator together with the associated Flex-Algo through the SRv6 Locator TLV. When calculating locator routes, other nodes perform calculation based on constraints defined by the Flex-Algo.
    4. (Optional) Run [**preference**](cmdqueryname=preference) *pref-value*
       
       A preference value is configured for the locator.
    5. Configure an opcode for static SIDs.
       
       Select a SID type as needed. For details about SRv6 SIDs, see [SRv6 Segments](dc_vrp_srv6_all_feature_0030.html).
       
       - To configure an opcode for static End SIDs, run the [**opcode**](cmdqueryname=opcode) *func-opcode* **end** { **no-flavor** | **psp** | **psp-usp-usd** } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         If the **no-flavor** parameter is specified, the flavor attribute can be canceled, and SRv6 SIDs carry only the ultimate segment POP of the SRH (USP) flavor.
       - To configure an opcode for static End.X SIDs, run the [**opcode**](cmdqueryname=opcode) *func-opcode* **end-x** **interface** *intfname* **nexthop** *nexthop-address* { **no-flavor** | **psp** | **psp-usp-usd** } [ **s-flag** ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         The **s-flag** parameter is used to associate an End.X SID with a group of adjacencies.
         
         A GRE tunnel interface can be specified using **interface** *intfname*.
    6. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    7. (Optional) Run [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) *delay-time*
       
       A delay in delivering a static End.X SID to the forwarding table is configured.
       
       The [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) command is mainly used in scenarios where the outbound interface associated with a static End.X SID changes from down to up and IS-IS routes reconverge.
    8. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    9. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
       
       The IS-IS view is displayed.
    10. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
        
        IPv6 is enabled for the IS-IS process.
    11. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
        
        IS-IS wide metric is configured.
    12. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
        
        IS-IS SRv6 is enabled.
    13. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  + Configure IS-IS to dynamically generate SIDs.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **ipv6-prefix** *ipv6-address* *prefix-length* specifies the locator prefix and prefix length.
       
       **static** *static-length* specifies the static segment length, which determines the number of static SIDs that can be configured in the locator.
       
       **args** *args-length* specifies the argument segment length. Arguments can be used to define flow, service, and other information for packets.
       
       **flex-algo** *flexAlgoId* specifies the Flex-Algo associated with the locator. The IGP advertises the locator together with the associated Flex-Algo through the SRv6 Locator TLV. When calculating locator routes, other nodes perform calculation based on constraints defined by the Flex-Algo.
    4. (Optional) Run [**index**](cmdqueryname=index+local-block+sid-reserve) *index-id* **local-block sid-reserve** *number-value*
       
       A range reserved for binding SIDs (BSIDs) is configured in the locator.
       
       In a scenario where a controller dynamically delivers SRv6 TE Policies, you can run this command to configure a range reserved for BSIDs. Forwarders use BGP-LS to report the range to the controller, which then allocates BSIDs within this range to SRv6 TE Policies or segment lists.
    5. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    6. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    7. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
       
       The IS-IS view is displayed.
    8. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
       
       IPv6 is enabled for the IS-IS process.
    9. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
       
       IS-IS wide metric is configured.
    10. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
        
        IS-IS SRv6 is enabled.
    11. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
* Configure SRv6 SIDs in 32-bit compression mode.
  
  
  
  SRv6 paths are established based on SIDs, which can either be configured manually or be generated dynamically using IS-IS. Use either of the following configuration methods:
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The SRv6 SRH 32-bit compression function can be used only after the required license is loaded.
  
  
  
  + Configure SIDs manually.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* **compress** **block** *block-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **compress** **block** *block-length* specifies a block length. The NodeID length is obtained by subtracting *block-length* from *prefix-length*.
       
       To implement SRv6 SRH compression, an SRv6 SID needs to be divided using the Locator:Compression Function:Non-compression Function:Args format. For this format:
       
       The Locator field is divided into the Block and NodeID parts. The Block part indicates the address space of an SRv6 domain, in which different nodes typically have the same block. The NodeID part uniquely identifies a node in an SRv6 domain.
       
       The Function field is divided into the Compression Function and Non-compression Function parts. The NodeID and Compression Function parts form a 32-bit generalized SID (G-SID). The Compression Function part is divided into the Compression Dynamic segment and Compression Static segment. When configuring SRv6 SRH compression, you can use the **compress-static** *compress-length* parameter to specify the length of the Compression Static segment to determine the range of compression static opcodes that can be configured in the corresponding locator. During SRv6 SRH compression, an IGP dynamically allocates opcodes outside the range of the Compression Function part's Compression Static segment to ensure that no SRv6 SID conflict occurs. The Non-compression Function part also consists of a dynamic opcode segment and a static opcode segment, with the ranges of the segments changed.
       
       The relationship between the preceding fields is expressed as follows:
       
       |-Block-|-NodeID-|-Compression Dynamic-|-Compression Static-|-Dynamic-|-Static-|-Args-|
    4. Run [**opcode compress**](cmdqueryname=opcode+compress) *func-opcode* **end** { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc | coc | psp-coc** }
       
       An opcode for static End SIDs is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the **compress** parameter is specified, an opcode with the compression function is manually configured. The NodeID and opcode form a 32-bit G-SID.
       
       If the **no-flavor** parameter is specified, the flavor attribute can be canceled, and SRv6 SIDs carry only the USP flavor.
    5. Run [**opcode compress**](cmdqueryname=opcode+compress) *func-opcode* **end-x** **interface** *intfname* **nexthop** *nexthop-addr* { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc | coc | psp-coc** } [ **s-flag** ]
       
       An opcode for static End.X SIDs is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The **s-flag** parameter is used to associate an End.X SID with a group of adjacencies.
       
       A GRE tunnel interface can be specified using **interface** *intfname*.
    6. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    7. (Optional) Run [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) *delay-time*
       
       A delay in delivering a static End.X SID to an FES table is configured.
       
       The [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) command is mainly used in scenarios where the outbound interface associated with a static End.X SID changes from down to up and IGP routes reconverge.
    8. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    9. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
       
       The IS-IS view is displayed.
    10. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
        
        IPv6 is enabled for the IS-IS process.
    11. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
        
        IS-IS wide metric is configured.
    12. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
        
        IS-IS SRv6 is enabled.
    13. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  + Configure IS-IS to dynamically generate SIDs.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* **compress** **block** *block-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **compress** **block** *block-length* specifies a block length. The NodeID length is obtained by subtracting *block-length* from *prefix-length*.
       
       To implement SRv6 SRH compression, an SRv6 SID needs to be divided using the Locator:Compression Function:Non-compression Function:Args format. For this format:
       
       The Locator field is divided into the Block and NodeID parts. The Block part indicates the address space of an SRv6 domain, in which different nodes typically have the same block. The NodeID part uniquely identifies a node in an SRv6 domain.
       
       The Function field is divided into the Compression Function and Non-compression Function parts. The NodeID and Compression Function parts form a 32-bit generalized SID (G-SID). The Compression Function part is divided into the Compression Dynamic segment and Compression Static segment. When configuring SRv6 SRH compression, you can use the **compress-static** *compress-length* parameter to specify the length of the Compression Static segment to determine the range of compression static opcodes that can be configured in the corresponding locator. During SRv6 SRH compression, an IGP dynamically allocates opcodes outside the range of the Compression Function part's Compression Static segment to ensure that no SRv6 SID conflict occurs. The Non-compression Function part also consists of a dynamic opcode segment and a static opcode segment, with the ranges of the segments changed.
       
       The relationship between the preceding fields is expressed as follows:
       
       |-Block-|-NodeID-|-Compression Dynamic-|-Compression Static-|-Dynamic-|-Static-|-Args-|
    4. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    5. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    6. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
       
       The IS-IS view is displayed.
    7. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
       
       IPv6 is enabled for the IS-IS process.
    8. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
       
       IS-IS wide metric is configured.
    9. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
       
       IS-IS SRv6 is enabled.
    10. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
* Configure SRv6 SIDs in 16-bit compression mode.
  
  
  
  SRv6 paths are established based on SIDs, which can either be configured manually or be generated dynamically using IS-IS. Use either of the following configuration methods:
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The SRv6 SRH 16-bit compression function can be used only after the required license is loaded.
  
  
  
  + Configure SIDs manually.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**compress-16 enable**](cmdqueryname=compress-16+enable)
       
       The 16-bit compression mode is enabled.
    4. (Optional) Run [**csid-proportion**](cmdqueryname=csid-proportion) **global-id-block** *gib-proportion-val*
       
       The GIB number space is configured.
    5. Run [**locator**](cmdqueryname=locator) *locator-name* **compress-16** [ **ipv6-prefix** *ipv6-address* *mask-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **compress-16** specifies 16-bit compression.
       
       **compress-static** *compress-length* specifies the length of the Compression Static segment.
    6. Run [**opcode compress**](cmdqueryname=opcode+compress+end) *func-opcode* **end** { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc | coc | psp-coc** | **psp-usd-next** }
       
       An opcode for static End SIDs is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the **psp-usd-next** parameter is specified, SRv6 SIDs carry the PSP, USD, and NEXT flavors. NEXT is a new flavor related to C-SIDs. It is installed in the local SID table to identify whether the NEXT action needs to be performed for the current C-SID.
    7. Run [**opcode compress**](cmdqueryname=opcode+compress+end-x) *func-opcode* **end-x** **interface** *interface-name* **nexthop** *nexthop-addr* { **no-flavor** | **psp** | **psp-usp-usd** | **psp-usp-usd-coc | coc | psp-coc** | **psp-usd-next** | **psp-usp-usd-coc-next** } [ **s-flag** ]
       
       An opcode for static End.X SIDs is configured.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The **s-flag** parameter is used to associate an End.X SID with a group of adjacencies.
       
       A GRE tunnel interface can be specified using **interface** *interface-name*.
    8. Run [**opcode compress**](cmdqueryname=opcode+compress+bridge-domain) *func-opcode* **end-dt2u** **bridge-domain** *bd-id* { **next** | **coc-next** }
       
       An opcode for static End.DT2U SIDs is configured.
    9. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    10. (Optional) Run [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) *delay-time*
        
        A delay in delivering a static End.X SID to an FES table is configured.
        
        The [**timer end-x update-delay**](cmdqueryname=timer+end-x+update-delay) command is mainly used in scenarios where the outbound interface associated with a static End.X SID changes from down to up and IGP routes reconverge.
    11. Run [**quit**](cmdqueryname=quit)
        
        Exit the SRv6 view.
    12. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
        
        The IS-IS view is displayed.
    13. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology ipv6**
        
        IPv6 is enabled for the IS-IS process.
    14. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
        
        IS-IS wide metric is configured.
    15. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name* [ **auto-sid-disable** ]
        
        IS-IS SRv6 is enabled.
    16. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  + Configure IS-IS to dynamically generate SIDs.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
       
       The SRv6 view is displayed.
    3. Run [**compress-16 enable**](cmdqueryname=compress-16+enable)
       
       The 16-bit compression mode is enabled.
    4. (Optional) Run [**csid-proportion**](cmdqueryname=csid-proportion) **global-id-block** *gib-proportion-val*
       
       The GIB number space is configured.
    5. Run [**locator**](cmdqueryname=locator) *locator-name* **compress-16** [ **ipv6-prefix** *ipv6-address* *mask-length* [ **compress-static** *compress-length* | **static** *static-length* | **args** *args-length* | **flex-algo** *flexAlgoId* ] \* ]
       
       An SRv6 locator is configured, and the SRv6 locator view is displayed.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       **compress-16** specifies 16-bit compression.
       
       **compress-static** *compress-length* specifies the length of the Compression Static segment.
    6. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 locator view.
    7. Run [**quit**](cmdqueryname=quit)
       
       Exit the SRv6 view.
    8. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
       
       The IS-IS view is displayed.
    9. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
       
       IPv6 is enabled for the IS-IS process.
    10. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
        
        IS-IS wide metric is configured.
    11. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) **locator** *locator-name*
        
        IS-IS SRv6 is enabled.
    12. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.