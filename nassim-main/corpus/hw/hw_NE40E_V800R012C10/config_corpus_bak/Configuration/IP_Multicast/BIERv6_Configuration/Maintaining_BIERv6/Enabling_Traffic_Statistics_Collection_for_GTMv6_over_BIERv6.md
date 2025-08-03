Enabling Traffic Statistics Collection for GTMv6 over BIERv6
============================================================

Enabling_Traffic_Statistics_Collection_for_GTMv6_over_BIERv6

#### Context

On a GTMv6 over BIERv6 network, multicast traffic is transmitted to multicast users through BIERv6 tunnels. After statistics collection is enabled for traffic along tunnels, the device can collect statistics such as the number of forwarded packets, number of bytes in the packets, inbound interface information, and traffic rate within 15 seconds. The traffic statistics collection function takes effect only after the function is configured on the ingress, transit, and egress nodes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (On transit and egress nodes) Run [**bier ipv6 statistics enable**](cmdqueryname=bier+ipv6+statistics+enable)
   
   
   
   Global traffic statistics collection is enabled for GTMv6 over BIERv6.
3. Enable global traffic statistics collection for GTMv6 over BIERv6 on the ingress.
   1. Run [**multicast ipv6 routing-enable**](cmdqueryname=multicast+ipv6+routing-enable)
      
      
      
      Multicast routing is enabled.
   2. Run [**multicast ipv6 vpn-public**](cmdqueryname=multicast+ipv6+vpn-public)
      
      
      
      The public network IPv6 address family MVPN view is displayed.
   3. Run [**bier ipv6 statistics**](cmdqueryname=bier+ipv6+statistics) { **all** | **group** *flow-grp-addr* **source** *flow-src-addr* }
      
      
      
      Global traffic statistics collection is enabled for GTMv6 over BIERv6, and the device is enabled to generate dynamic flow labels.
   4. (Optional) Run [**bier ipv6 group**](cmdqueryname=bier+ipv6+group) *flow-grp-address* [**source**](cmdqueryname=source) *flow-src-addr* [**flow-label**](cmdqueryname=flow-label) *flow-label-value*
      
      
      
      A static flow label is configured on the ingress in a GTMv6 over BIERv6 scenario.
      
      
      
      If no static flow label is configured, dynamically allocated flow labels are used by default.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display bier ipv6 statistics sub-domain**](cmdqueryname=display+bier+ipv6+statistics+sub-domain) *sub-domain* **bsl** *bsl* [ **flow-label** *flow-label* **source-dt** *source-address* ] command to check BIERv6 statistics.
* Run the [**display mvpn ipv6**](cmdqueryname=display+mvpn+ipv6) { **vpn-instance** *vpn-instance-name* | **all-instance** | **public** } [**ingress bier ipv6**](cmdqueryname=ingress+bier+ipv6) [ **group** *group-address* **source** *source-address* ] command to check flow information on the ingress in a GTMv6 over BIERv6 scenario.