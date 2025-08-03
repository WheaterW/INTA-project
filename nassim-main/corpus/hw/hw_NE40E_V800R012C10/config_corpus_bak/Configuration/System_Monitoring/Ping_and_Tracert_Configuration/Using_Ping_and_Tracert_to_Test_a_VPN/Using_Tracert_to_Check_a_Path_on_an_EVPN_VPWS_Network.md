Using Tracert to Check a Path on an EVPN VPWS Network
=====================================================

A tracert operation can be performed to locate a forwarding fault on an EVPN VPWS network.

#### Prerequisites

* Before running the [**tracert evpn vpws**](cmdqueryname=tracert+evpn+vpws) command to locate a forwarding fault on an EVPN VPWS network, ensure that the EVPN VPWS network has been correctly configured.
* If you have run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets after the previous test is complete, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable)/[**lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable+ipv6) command to enable the device to respond to MPLS Echo Request/MPLS Echo Request IPv6 packets before starting the current test.

#### Context

Perform the following steps in any view.


#### Procedure

* Locate a forwarding fault on an EVPN VPWS network.
  
  
  + Locate a forwarding fault on an EVPN VPWS network with the tunnel type being LDP/TE/BGP LSP/BGP Localifnet/SR-MPLS BE/SR-MPLS TE/SR-MPLS TE Policy.
    
    Run the [**tracert evpn vpws**](cmdqueryname=tracert+evpn+vpws) *local-ce-id* *remote-ce-id* [ **vpn-instance** *evpn-name* ] [ **control-word** ] [ **-a** *source-ip* | **-exp** *exp-value* | **-s** *packet-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-tc** *tc* | **backup** ] \* [ **pipe** | **uniform** ] command to check the EVPN VPWS status and locate the faulty node on the EVPN VPWS path.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In cross-domain scenarios, the **control-word** keyword must be specified, and the **-r** **4** mode is recommended.
  + Locate a forwarding fault on an EVPN VPWS network with the tunnel type being SRv6 BE/SRv6 TE Policy/SRv6 TE Flow Group:
    
    Run the [**tracert evpn vpws**](cmdqueryname=tracert+evpn+vpws) *local-ce-id* *remote-ce-id* [ **vpn-instance** *evpn-name* ] [ **end-op** *endOp* [ *prefix-length* ] [ **-a** *source-ip* | **-exp** *exp-value* | **-s** *packet-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-tc** *tc* | { **-service-class***classValue* | **-te-class** *teClassValue* } | **backup** ] \* [ **pipe** | **uniform** ] command to check the EVPN VPWS status and locate the faulty node on the EVPN VPWS path.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the local service ID is not globally unique, the **vpn-instance** *evpn-name* parameter must be specified.
  
  
  
  The following is an example:
  
  # Perform a tracert operation on an EVPN VPWS network.
  ```
  <HUAWEI> tracert evpn vpws 1 2 
    EVPN VPWS Trace Route FEC: Local Evpn Vpws Id = 100, Remote Evpn Vpws Id = 200, press CTRL_C to break.
    Tunnel-Type: SRv6 BE; Original-Nexthop: 2001:DB8:1::1; P/B: Primary
    TTL    Replier            Time    Type      Downstream
    0                                 Ingress   2001:DB8:21::1:0:0
    1      2001:DB8:20::2     2 ms    Egress  
  ```

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets so as to prevent system resource occupation.