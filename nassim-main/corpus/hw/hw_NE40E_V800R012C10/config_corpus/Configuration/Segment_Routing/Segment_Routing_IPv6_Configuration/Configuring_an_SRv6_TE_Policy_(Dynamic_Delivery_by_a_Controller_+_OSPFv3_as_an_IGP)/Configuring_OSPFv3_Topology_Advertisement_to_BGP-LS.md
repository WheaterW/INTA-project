Configuring OSPFv3 Topology Advertisement to BGP-LS
===================================================

After OSPFv3 topology information is advertised to BGP-LS, BGP-LS reports the topology information to a controller for path planning.

#### Context

OSPFv3 collects network topology information including the link TE metric, bandwidth, SRLG, and AdminGroup information and advertises the information to BGP-LS, which then reports the information to a controller. The controller can compute an SRv6 TE Policy based on different factors to meet various service requirements.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 process view is displayed.
3. Run [**area**](cmdqueryname=area) *area-id*
   
   
   
   The OSPFv3 area view is displayed.
   
   
   
   The specified area ID can be a decimal integer or in the IPv4 address format. It is displayed as an IPv4 address regardless of its format adopted.
   
   You can run the [**description**](cmdqueryname=description) command to configure a description for the OSPF area for easier identification.
4. Run [**traffic-eng enable**](cmdqueryname=traffic-eng+enable)
   
   
   
   The TE function is enabled for the OSPFv3 area.
   
   
   
   After the TE function is enabled, the OSPFv3 area has the capability of advertising and parsing intra-area-TE-LSAs. The supported TE information includes the IPv6 LSR-IDs, SRv6 capabilities, and MSD capabilities of nodes as well as the TE metric, bandwidth, SRLG, and AdminGroup information of links. After TE information is advertised, it can be reported to the controller through BGP-LS for path computation.
5. In the OSPFv3 view, run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable)
   
   
   
   The OSPFv3 process is enabled to advertise topology information.
   
   BGP-LS is a new method of collecting topology information. It obtains topology information based on different topology identifiers and reports the information to the controller.
   
   The OSPFv3 devices in the same area have the same topology information. Therefore, you are advised to deploy BGP-LS only on two devices (with one of the devices functioning as the backup).
6. (Optional) Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier)*identifier-value*
   
   
   
   An OSPFv3 topology identifier is set.
   
   If BGP-LS is deployed on two or more devices in the same topology, *identifier-value* must be set to the same value for these devices to ensure that BGP-LS collects accurate topology information.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.