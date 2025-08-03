Configuring IGP TE (OSPF or IS-IS)
==================================

After IGP TE is configured on all LSRs in an MPLS domain, a TEDB is generated on each LSR.

#### Context

Either OSPF TE or IS-IS TE can be used:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If neither OSPF TE nor IS-IS TE is configured, LSRs do not generate TE LSAs or TE LSPs. As a result, TEDBs cannot be constructed.

TE tunnels cannot be used in inter-area scenarios. In an inter-area scenario, an explicit path can be configured, and the inbound and outbound interfaces of the explicit path must be specified, preventing a failure to establish a TE tunnel.

* OSPF TE
  
  OSPF TE uses Opaque Type 10 LSAs to carry TE attributes. The OSPF Opaque capability must be enabled on each LSR. In addition, TE LSAs are generated only when at least one OSPF neighbor is in the Full state.
* IS-IS TE
  
  IS-IS TE uses the sub-time-length-value (sub-TLV) in the IS-reachable TLV (22) to carry TE attributes. The IS-IS wide metric attribute must be configured. Its value can be wide, compatible, or wide-compatible.

#### Procedure

* Configure OSPF TE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
     
     
     
     The OSPF Opaque capability is enabled.
  4. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPF area view is displayed.
  5. Run [**mpls-te enable**](cmdqueryname=mpls-te+enable) [ **standard-complying** ]
     
     
     
     TE is enabled in the OSPF area.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure IS-IS TE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **compatible** | **wide-compatible** }
     
     
     
     The IS-IS wide metric attribute is set.
  4. Run [**traffic-eng**](cmdqueryname=traffic-eng) [ **level-1** | **level-2** | **level-1-2** ]
     
     
     
     IS-IS TE is enabled.
     
     If no level is specified when IS-IS TE is enabled, IS-IS TE is valid for both Level-1 and Level-2 routers.
  5. (Optional) Run [**te-set-subtlv**](cmdqueryname=te-set-subtlv) { **bw-constraint** *bw-constraint-value* | **lo-multiplier** *lo-multiplier-value* | **unreserve-bw-sub-pool** *unreserve-bw-sub-pool-value* } \*
     
     
     
     The type of a sub-TLV carrying DiffServ-aware Traffic Engineering (DS-TE) attributes is specified.
     
     
     
     There are no unified
     standards for sub-TLVs that carry DS-TE attributes in non-IETF mode.
     To ensure interconnection between devices of different vendors, you
     need to manually configure TLV values for these sub-TLVs. After TLV
     values are configured for these sub-TLVs, the traffic engineering
     database (TEDB) is regenerated, and then TE tunnels are reestablished.
     The sub-TLVs can be sent only after TLV values are configured for
     them.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.