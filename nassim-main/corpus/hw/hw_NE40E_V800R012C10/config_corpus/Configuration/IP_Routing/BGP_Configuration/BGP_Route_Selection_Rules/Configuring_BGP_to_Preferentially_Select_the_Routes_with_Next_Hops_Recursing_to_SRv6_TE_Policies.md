Configuring BGP to Preferentially Select the Routes with Next Hops Recursing to SRv6 TE Policies
================================================================================================

Configuring BGP to Preferentially Select the Routes with Next Hops Recursing to SRv6 TE Policies

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001199622480__fig_dc_vrp_bgp_cfg_410401), an SRv6 TE Policy is deployed between PE1 and PE2, and an SRv6 BE tunnel is deployed between PE1 and PE3. PE1 has two routes with the same prefix but different next hops. One of the routes recurses to the SRv6 TE Policy, and the other route recurses to the SRv6 BE tunnel. If services need to be carried over the SRv6 TE Policy, you can configure this function so that BGP compares the types of SRv6 tunnels to which route next hops recurse when selecting the optimal route. Among the routes with next hops recursing to SRv6 Policies, those with next hops recursing to SRv6 TE Policies take precedence over those with next hops recursing to SRv6 BE tunnels.

**Figure 1** Configuring BGP to preferentially select the routes with next hops recursing to SRv6 TE Policies  
![](figure/en-us_image_0000001244822279.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**bestroute nexthop-recursive-priority srv6-te-policy**](cmdqueryname=bestroute+nexthop-recursive-priority+srv6-te-policy)
   
   
   
   BGP is configured to compare the types of SRv6 tunnels to which route next hops recurse when selecting the optimal route and preferentially select those with next hops recursing to SRv6 TE Policies over those with next hops recursing to SRv6 BE tunnels.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table)*network* command to check BGP route selection results.