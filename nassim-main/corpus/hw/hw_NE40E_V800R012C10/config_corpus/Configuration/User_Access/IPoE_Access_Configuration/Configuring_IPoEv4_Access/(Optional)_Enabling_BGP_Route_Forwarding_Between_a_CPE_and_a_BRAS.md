(Optional) Enabling BGP Route Forwarding Between a CPE and a BRAS
=================================================================

(Optional) Enabling BGP Route Forwarding Between a CPE and a BRAS

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172373983__fig_dc_ne_cfg_bras_001901), a CPE uses IPoE dialup to obtain an IP address from a BRAS. By default, the CPE can use the IP address to establish a BGP connection with the BRAS, and the BRAS can learn the BGP route from the CPE. However, traffic cannot be forwarded through the BGP route. After BGP route forwarding is enabled between the CPE and the BRAS, access user information is added to information about the BGP routes with the next hops being the IP addresses of IPoE users. This allows traffic from hosts attached to the CPE or other IP addresses on the CPE to the BRAS and return traffic to be forwarded through BGP routes.

**Figure 1** Networking  
![](images/fig_dc_ne_cfg_bras_001901.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**bgp over IPoE enable**](cmdqueryname=bgp+over+IPoE+enable)
   
   
   
   BGP route forwarding is enabled between a CPE and the BRAS.