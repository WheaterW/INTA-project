(Optional) Configuring the Router to Comply with Route Selection Rules Defined in a Standard Protocol
=====================================================================================================

You can configure the Router to comply with the route selection rule defined in RFC 1583 or RFC 2328.

#### Context

RFC 2328 and RFC 1583 define route selection rules differently. After enabling OSPF on the Router, you can configure the device to comply with route selection rules defined in either standard protocol as required. By default, the Router complies with the route selection rules defined in RFC 1583. If you want the device to comply with the other protocol, you need to configure the device to comply with the rules defined in RFC 2328. Such configurations ensure that all OSPF-enabled devices in an AS comply with the same route selection rules defined in the same standard protocol.

If both intra-area and inter-area paths to an ASBR exist on a network, the default rules for selecting a path to the ASBR are as follows:

1. In RFC 1583 compatibility mode:
   * If the area IDs of the intra-area and inter-area paths to the ASBR are the same, intra-area paths are preferred.
   * If the area IDs of intra-area and inter-area paths to the ASBR are different, the path with the smallest cost is preferred; if their costs are the same, the path with the largest area ID is preferred.
2. In RFC 1583 non-compatibility mode:
   * If the area IDs of the intra-area and inter-area paths to the ASBR are the same and the paths belong to non-backbone areas, intra-area paths are preferred.
   * If the area IDs of the intra-area and inter-area paths to the ASBR are the same and the paths belong to the backbone area, the path with the smallest cost is preferred; if their costs are the same, load balancing is supported.
   * If the area IDs of the intra-area and inter-area paths to the ASBR are different, intra-area paths that belong to non-backbone areas are preferred; if intra-area paths belong to the backbone area, the path with the smallest cost is preferred; if their costs are the same, the path with the largest area ID is preferred.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If devices of different vendors or different series of devices of the same vendor are deployed on the same network, the rules for selecting a path to an ASBR among intra-area and inter-area paths may vary according to the mode (RFC 1583 compatibility mode or RFC 1583 non-compatibility mode). In this case, routing loops may occur. To prevent the routing loops, you can set the path selection rules to the default ones.
   
   To prevent routing loops, ensure that all devices on the network use the same path selection rules. If adjustment is performed only on some devices, the adjustment fails to meet expectations. Therefore, exercise caution when adjusting path selection rules.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. (Optional) Run [**rfc1583 compatible different-area-path prefer lower-cost**](cmdqueryname=rfc1583+compatible+different-area-path+prefer+lower-cost)
   
   
   
   The device is configured to comply with the default rules in RFC 1583 compatibility mode for selecting a path to an ASBR. That is, if the area IDs of intra-area and inter-area paths to the ASBR are different, the path with the smallest cost is preferred; if their costs are the same, the path with the largest area ID is preferred.
4. Run [**undo rfc1583 compatible**](cmdqueryname=undo+rfc1583+compatible)
   
   
   
   The device is configured to comply with the route selection rule defined in RFC 2328, rather than RFC 1583.
5. (Optional) Run [**rfc1583 non-compatible backbone-area-path prefer intra**](cmdqueryname=rfc1583+non-compatible+backbone-area-path+prefer+intra)
   
   
   
   The device is configured to comply with the default rules in RFC 1583 non-compatibility mode for selecting a path to an ASBR. That is, if the area IDs of the intra-area and inter-area paths to the ASBR are the same and the paths belong to the backbone area, intra-area paths are preferred.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.