Configuring the Shortcut Function for Static SRv6 TE Flow Groups
================================================================

Enable the shortcut function for static SRv6 TE flow groups so that an IGP uses an SRv6 TE flow group that is up to perform enhanced SPF calculation.

#### Prerequisites

Before configuring the shortcut function for static SRv6 TE flow groups, complete one of the following tasks:

* [Configure an SRv6 TE Policy in manual configuration mode.](dc_vrp_srv6_cfg_all_0110.html)
* [Configure an SRv6 TE Policy in controller-based dynamic delivery mode.](dc_vrp_srv6_cfg_all_0116.html)

#### Context

An SRv6 TE flow group is a set of SRv6 TE Policies and can be used to implement DSCP-based traffic steering. It contains multiple SRv6 TE Policies with the same endpoint but different color values. During service recursion, service traffic is matched against SRv6 TE Policies in the SRv6 TE flow group according to the DSCP values carried by the traffic.

The mapping between DSCP values and SRv6 TE Policies can be statically configured in an SRv6 TE flow group and applies to both IPv4 and IPv6 services. Only an SRv6 TE Policy in the up state can be mapped to a DSCP value.

In the implementation of the shortcut function for a static SRv6 TE flow group, the SRv6 TE flow group is considered a local direct link. An IGP uses the SRv6 TE flow group as an outbound interface to perform enhanced SPF calculation. If the headend and endpoint of the SRv6 TE flow group match the ingress and egress of a physical link on the SPF tree, respectively, the IGP uses the SRv6 TE flow group to replace the physical link, implementing the shortcut function for the SRv6 TE flow group. During data forwarding, a node steers data traffic into the corresponding SRv6 TE flow group based on DSCP values, thereby meeting SLA requirements.

Although a device on which the shortcut function for SRv6 TE flow groups is enabled uses an SRv6 TE flow group as an outbound interface, it does not advertise the SRv6 TE flow group to its neighbors. As such, other devices cannot use the SRv6 TE flow group.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
3. Run the [**srv6-te flow-group**](cmdqueryname=srv6-te+flow-group)*group-name* command to enter the SRv6 flow group view.
4. Run the **[**endpoint**](cmdqueryname=endpoint)** *ipv6-address* command to configure an endpoint address for the SRv6 TE flow group.
   
   
   
   During route recursion, the device checks whether the next hop address of the route matches the endpoint address of the SRv6 TE flow group. If they match, route recursion succeeds.
5. Run the **[**igp shortcut isis**](cmdqueryname=igp+shortcut+isis)** [ **route-policy** *route-policy-name* ] command to enable the shortcut function for the SRv6 TE flow group.
   
   
   
   If the **route-policy** *route-policy-name* parameter is not configured, only 128-bit host routes can recurse to the SRv6 TE flow group by default. However, if the **route-policy** *route-policy-name* parameter is configured, the specified route-policy is used to selectively recurse routes to the SRv6 TE flow group after path calculation is complete.
6. Run the [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable)[ *instanceId* ] command to enable IS-IS IPv6 for the SRv6 TE flow group and specify the ID of the IS-IS process to be associated.
7. Run the [**match-type dscp**](cmdqueryname=match-type+dscp) command to set the mapping type of the SRv6 TE flow group to DSCP.
8. Run the [**index**](cmdqueryname=index+dscp+match)*index-value* **dscp** { { *dscpBegin* [ **to** *dscpEnd* ] } &<1-64> } **match** { **srv6-te-policy** **color** *color-value* | **native-ip** } or [**default match**](cmdqueryname=default+match){ **srv6-te-policy** **color** *color-value* | **native-ip** } command to configure the mapping between DSCP values and SRv6 TE Policies in the SRv6 TE flow group.
   
   
   
   When traffic carrying DSCP values enters an SRv6 TE flow group, it is forwarded based on the following rules:
   
   1. The traffic is first strictly matched against the SRv6 TE Policy or native IP link with the corresponding DSCP value.
   2. If no matching SRv6 TE Policy or native IP link with the corresponding DSCP value is found, the SRv6 TE Policy or native IP link with the default priority is selected.
   3. If no SRv6 TE Policy or native IP link with the default priority is configured, the SRv6 TE Policy or native IP link with the smallest DSCP value is selected.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only an SRv6 TE Policy in the up state can be mapped to a DSCP value.
   
   The mapping relationship takes effect for an SRv6 TE flow group only when it is in the up state.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display srv6-te flow-group**](cmdqueryname=display+srv6-te+flow-group) command to check SRv6 TE flow group details.
* Run the [**display srv6-te flow-group last-down-reason**](cmdqueryname=display+srv6-te+flow-group+last-down-reason) command to check the records about SRv6 TE flow group down events.
* Run the [**display srv6-te flow-group statistics**](cmdqueryname=display+srv6-te+flow-group+statistics) command to check SRv6 TE flow group statistics.
* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* ] **ipv6** [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* [ | **count** ] command to check IS-IS routing information.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] **verbose** or [**display ipv6 routing-table brief**](cmdqueryname=display+ipv6+routing-table+brief) command to check IPv6 routing table information.