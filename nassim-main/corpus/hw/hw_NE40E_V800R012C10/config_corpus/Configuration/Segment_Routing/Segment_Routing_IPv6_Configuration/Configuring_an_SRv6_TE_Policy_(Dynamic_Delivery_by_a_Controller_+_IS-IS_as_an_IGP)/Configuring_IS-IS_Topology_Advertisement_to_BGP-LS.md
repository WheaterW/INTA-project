Configuring IS-IS Topology Advertisement to BGP-LS
==================================================

After IS-IS topology information is advertised to BGP-LS, BGP-LS reports the topology information to a controller for path planning.

#### Context

IS-IS collects network topology information including the link cost, latency, and packet loss rate and advertises the information to BGP-LS, which then reports the information to a controller. The controller can compute an SRv6 TE Policy based on link cost, latency, packet loss rate, and other factors to meet various service requirements.

Before the configuration, pay attention to the following points:

* If the controller computes an SRv6 TE Policy based on the link cost, no additional configuration is required.
* If the controller computes an SRv6 TE Policy based on the link latency, perform the operations described in [Configuring IS-IS Delay Information Advertisement (IPv6)](dc_vrp_isis_cfg_0094.html).
* If the controller computes an SRv6 TE Policy based on the link-specific packet loss rate, perform the operations described in [Configuring an IS-IS Process to Advertise IPv6 Packet Loss Rates](dc_vrp_isis_cfg_1063.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**ipv6 enable topology ipv6**](cmdqueryname=ipv6+enable+topology+ipv6)
   
   
   
   IPv6 is enabled for the IS-IS process.
4. Run [**cost-style**](cmdqueryname=cost-style) { **compatible** [ **relax-spf-limit** ] | **wide** | **wide-compatible** }
   
   
   
   IS-IS wide metric is configured.
5. Run [**ipv6 bgp-ls enable**](cmdqueryname=ipv6+bgp-ls+enable) [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   IS-IS IPv6 topology advertisement is enabled.
6. Run [**ipv6 advertise link attributes**](cmdqueryname=ipv6+advertise+link+attributes)
   
   
   
   The IS-IS process is enabled to advertise IPv6 link attribute TLVs in LSPs. IPv6 link attributes include the IPv6 address and interface index.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.