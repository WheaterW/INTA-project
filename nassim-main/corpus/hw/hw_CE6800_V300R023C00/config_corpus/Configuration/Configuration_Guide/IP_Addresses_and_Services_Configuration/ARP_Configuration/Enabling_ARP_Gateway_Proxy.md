Enabling ARP Gateway Proxy
==========================

Enabling ARP Gateway Proxy

#### Context

To improve network security and prevent Layer 2 users in the same BD from directly communicating, enable ARP gateway proxy. After the function is enabled, traffic is diverted to the corresponding gateway. The gateway then monitors Layer 2 traffic to ensure secure traffic forwarding.

![](public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Enable ARP broadcast suppression.
   
   
   ```
   [arp broadcast-suppress enable](cmdqueryname=arp+broadcast-suppress+enable)
   ```
4. Enable ARP gateway proxy.
   
   
   ```
   [arp l2-proxy gateway-mac](cmdqueryname=arp+l2-proxy+gateway-mac)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```