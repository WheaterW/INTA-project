Using Tracert to Check a PW Path on a VPLS Network
==================================================

After configuring a VPLS network, you can use tracert to check a PW path on the network.

#### Prerequisites

Before you run the [**tracert vpls**](cmdqueryname=tracert+vpls) command to check PW connectivity, ensure that the VPLS network has been configured correctly.


#### Context

Perform the following steps on a PE of a VPLS network:


#### Procedure

1. To locate the faulty node on the VPLS network, run either of the following commands as required:
   
   
   * In BGP mode, run the [**tracert vpls**](cmdqueryname=tracert+vpls) [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ] \* **vsi** *vsi-name* *local-site-id* *remote-site-id* [ **full-lsp-path** ] [ **detail** ] [ **bypass** **-si** *interface-type* *interface-number* ] command.
   * In LDP mode, run the [**tracert vpls**](cmdqueryname=tracert+vpls) [ **-exp** *exp-value* | **-f** *first-ttl* | **-m** *max-ttl* | **-r** *reply-mode* | **-t** *timeout-value* | **-g** ] \* **vsi** *vsi-name* **peer** *peer-address* [ **negotiate-vc-id** *vc-id* ] [ **full-lsp-path** ] [ **control-word** ] [ **pipe** | **uniform** ] [ **detail** ] [ **bypass** **-si** *interface-type* *interface-number* ] command.
   
   
   
   Run the [**tracert vpls**](cmdqueryname=tracert+vpls) command to locate VPLS network faults.
   
   ```
   <HUAWEI>tracert vpls vsi test 10 10 full-lsp-path  
   PW Trace Route FEC: L2 VPN ENDPOINT. Sender VEID = 10, Remote VEID = 20, press CTRL_C to break 
   TTL    Replier            Time    Type      Downstream 
   0                                 Ingress   10.1.1.2/[294929 32894 32888 ] 
   1      10.1.1.2           93 ms   Transit   10.2.1.2/[32925 3 ] 
   2      10.2.1.2           1 ms    Transit   10.3.1.2/[32881 ] 
   3      4.4.4.4            2 ms    Egress 
   ```
   
   The preceding command output contains information about each node along the PW and the response time of each hop.