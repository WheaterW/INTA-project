(Optional) Enabling BGP Route Forwarding Between a CPE and BRAS for PPPoE Users
===============================================================================

(Optional) Enabling BGP Route Forwarding Between a CPE and BRAS for PPPoE Users

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172374106__fig_dc_ne_cfg_bras_001901), the CPE uses PPPoE dialup to obtain an IP address from the BRAS. By default, the CPE can use the IP address to establish a BGP connection with the BRAS, and the BRAS can learn the BGP route from the CPE. However, traffic cannot be forwarded through the BGP route. After BGP route forwarding is enabled between the CPE and BRAS, access user information is added to information about the BGP routes with the next hops being the IP addresses of PPPoE users, allowing traffic to be forwarded through the BGP route between the CPE and BRAS.

**Figure 1** Enabling BGP route forwarding between a CPE and BRAS for PPPoE users  
![](images/fig_dc_ne_cfg_bras_001901.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**bgp over pppoe enable**](cmdqueryname=bgp+over+pppoe+enable)
   
   
   
   BGP route forwarding is enabled between the CPE and BRAS.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.