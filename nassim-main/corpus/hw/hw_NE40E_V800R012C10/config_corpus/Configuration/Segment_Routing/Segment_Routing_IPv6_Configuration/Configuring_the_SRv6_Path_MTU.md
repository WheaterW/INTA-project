Configuring the SRv6 Path MTU
=============================

In a scenario where packets enter an SRv6 BE path or SRv6 TE Policy, to prevent the packets from being discarded when the packet length exceeds the MTU value of the outbound interface or to prevent the forwarding efficiency from being reduced when the fragment length is too short, you can plan an appropriate SRv6 path MTU value on the ingress of the SRv6 BE path or the headend of the SRv6 TE Policy.

#### Context

Typically, only the source and destination IPv6 nodes parse IPv6 extension headers. Transit nodes forward IPv6 packets without performing IPv6 MTU-based packet fragmentation, which is performed only on the source node. If the length of an IPv6 packet is greater than the IPv6 MTU of a device's outbound interface, the device discards the packet. The impact of the MTU must therefore be considered, because SRv6 uses IPv6 as the forwarding plane.

In addition, if original packet fragments entering an SRv6 BE path or SRv6 TE Policy are too small, the link bandwidth utilization is affected. Therefore, an appropriate SRv6 path MTU value needs to be configured to prevent packet loss and maximize link bandwidth utilization.

The SRv6 path MTU is the total length of a packet encapsulated with both the SRv6 header and IPv6 payload instead of only the IPv6 payload. For details, see [Figure 1](#EN-US_TASK_0000002100381905__en-us_task_0197097338_fig_mtu_feature_00501).

**Figure 1** SRv6 path MTU  
![](figure/en-us_image_0000002064381792.png "Click to enlarge")

To allow for the additional SRH length introduced in TI-LFA FRR, binding SID, and other scenarios, configure a reserved path MTU value on the SRv6 ingress. The configured SRv6 path MTU value minus the reserved value is called the active path MTU value. The MTU value applied to SRv6 packets is the smaller of either the active path MTU value or the IPv6 MTU value of the involved physical interface. [Figure 2](#EN-US_TASK_0000002100381905__en-us_task_0197097338_fig1950611718211) shows the relationships among the MTU values.

**Figure 2** Relationships among the MTU values  
![](figure/en-us_image_0000002100540413.png "Click to enlarge")

SRv6 path MTU configuration takes effect for packets forwarded through either an SRv6 BE path or an SRv6 TE Policy. You need to configure an appropriate SRv6 path MTU value according to the length of SRv6-encapsulated packets.

Both SRv6 TE Policy and SRv6 BE scenarios support the global configuration of a path MTU value and reserved path MTU value. If the global SRv6 path MTU value is 1600 bytes and the reserved path MTU value is 100 bytes, the active path MTU value is 1500 bytes. In this case, if the IPv6 MTU value of the involved physical interface is greater than or equal to 1500 bytes, the MTU value used by the ingress is 1500 bytes. However, if the IPv6 MTU value of the involved physical interface is less than 1500 bytes, the ingress uses this MTU value.

SRv6 TE Policies also support path MTU configuration on a per segment list basis. A path MTU value configured for a segment list overrides the global path MTU value. For example, if the global SRv6 path MTU value is 1600 bytes, the path MTU values of all segment lists are 1600 bytes by default. If the path MTU value configured for one of the segment lists is not 1600 bytes, this configured value takes precedence. The path MTU value of the segment list minus the globally reserved path MTU value is the active path MTU value of the segment list. The active path MTU value is then compared with the IPv6 MTU value of the involved physical interface. The smaller value between them is the MTU value that the headend actually uses.


#### Procedure

* Configure a path MTU value in an SRv6 BE scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
  3. Run the [**path-mtu**](cmdqueryname=path-mtu)*mtu-value* command to configure a global path MTU value for SRv6 BE.
  4. (Optional) Run the [**path-mtu reserved**](cmdqueryname=path-mtu+reserved) *reserved-value* command to configure a globally reserved path MTU value.
     
     
     
     The global path MTU value minus the reserved value is the active path MTU value, which must be greater than or equal to 1280 bytes. The ingress sends packets using the smaller value of either the active path MTU value or the IPv6 MTU value of the involved physical interface.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a path MTU value in an SRv6 TE Policy scenario.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
  3. Run the [**path-mtu**](cmdqueryname=path-mtu)*mtu-value* command to configure a global path MTU value for SRv6 TE Policy.
  4. (Optional) Run the [**path-mtu reserved**](cmdqueryname=path-mtu+reserved) *reserved-value* command to configure a globally reserved path MTU value.
     
     
     
     The global path MTU value minus the reserved value is the active path MTU value, which must be greater than or equal to 1280 bytes. The headend sends packets using the smaller value of either the active path MTU value or the IPv6 MTU value of the involved physical interface.
  5. (Optional) Configure a path MTU value for a segment list.
     
     
     
     A path MTU value configured for a segment list overrides the global path MTU value.
     
     1. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* **endpoint** *endpoint-ip* **color** *color-value* command to create an SRv6 TE Policy and enter its view.
     2. Run the [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference* command to enter the candidate path view of the SRv6 TE Policy.
     3. Run the [**segment-list**](cmdqueryname=segment-list) *list-name* **path-mtu** *mtu-value* command to configure a path MTU value for the specified segment list.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.