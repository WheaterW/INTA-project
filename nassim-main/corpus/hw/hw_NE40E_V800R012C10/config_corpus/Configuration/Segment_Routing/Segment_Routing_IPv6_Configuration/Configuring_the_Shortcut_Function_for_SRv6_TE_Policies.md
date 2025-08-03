Configuring the Shortcut Function for SRv6 TE Policies
======================================================

Enable the shortcut function for SRv6 TE Policies so that an IGP uses an SRv6 TE Policy that is up to perform enhanced SPF calculation.

#### Prerequisites

Before configuring the shortcut function for SRv6 TE Policies, complete one of the following tasks:

* [Configure an SRv6 TE Policy in manual configuration mode.](dc_vrp_srv6_cfg_all_0110.html)
* [Configure an SRv6 TE Policy in controller-based dynamic delivery mode.](dc_vrp_srv6_cfg_all_0116.html)

#### Context

Currently, SRv6 TE Policies are mainly deployed in specific network areas for purposes such as traffic acceleration and load balancing. Sometimes, traffic traversing network areas cannot be effectively steered into the desired SRv6 TE Policy, resulting in an SLA guarantee failure.

An IGP uses an SRv6 TE Policy as a local direct link to perform enhanced SPF calculation. If the headend and endpoint of the SRv6 TE Policy match the ingress and egress of a physical link on the SPF tree, respectively, the IGP uses the SRv6 TE Policy to replace the physical link, implementing the shortcut function for the SRv6 TE Policy.

Although a device on which the shortcut function for SRv6 TE Policies is enabled uses an SRv6 TE Policy as an outbound interface, it does not advertise the SRv6 TE Policy to its neighbors. As such, other devices cannot use the SRv6 TE Policy.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
3. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* **endpoint** *endpoint-ip* **color** *color-value* command to enter the SRv6 TE Policy view.
4. Run the [**encapsulation-mode**](cmdqueryname=encapsulation-mode) { **encaps** | **insert-encaps** } command to configure an SRv6 TE Policy encapsulation mode.
   
   
   
   When forwarded data enters an SRv6 TE Policy, new SID stack encapsulation is required. If no service SID is available, the SRv6 TE Policy needs to use the **encaps** encapsulation mode. Otherwise, the endpoint cannot remove the SRv6 encapsulation. The headend of the SRv6 TE Policy encapsulates IPv6 header and SRH information into data when the data enters the SRv6 TE Policy, and the endpoint implements the USD flavor to remove the encapsulated IPv6 header and SRH information.
   
   The shortcut function of SRv6 TE Policies does not support the Insert mode.
5. Run the **igp shortcut isis** [ **route-policy** *route-policy-name* ] command to enable the shortcut function for the SRv6 TE Policy.
   
   
   
   If the **route-policy** *route-policy-name* parameter is not configured, only 128-bit host routes can recurse to SRv6 TE Policies by default. However, if the **route-policy** *route-policy-name* parameter is configured, the specified route-policy is used to selectively recurse routes to SRv6 TE Policies after path calculation is complete.
6. Run the [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable)[ *instanceId* ] command to enable IS-IS IPv6 for the SRv6 TE Policy and specify the ID of the IS-IS process to be associated.
7. (Optional) Run the [**igp metric**](cmdqueryname=igp+metric){ **relative** *relativeValue* | **absolute** *absoluteValue* } command to configure an IGP metric value for the SRv6 TE Policy used for SPF calculation.
   
   
   
   Configure an appropriate IGP metric value for the SRv6 TE Policy to ensure that the SRv6 TE Policy can be correctly advertised and used. For example, the metric value of an SRv6 TE Policy should be less than the metric value of the IGP route that is not expected to be used by traffic.
8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* ] **ipv6** [ **topology** *topology-name* ] [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \* [ | **count** ] command to check IS-IS routing information.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] **verbose** or [**display ipv6 routing-table brief**](cmdqueryname=display+ipv6+routing-table+brief) command to check IPv6 routing table information.