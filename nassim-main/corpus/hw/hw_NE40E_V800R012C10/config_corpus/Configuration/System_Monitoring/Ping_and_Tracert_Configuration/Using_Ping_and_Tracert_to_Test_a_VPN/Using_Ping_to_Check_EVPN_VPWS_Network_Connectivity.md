Using Ping to Check EVPN VPWS Network Connectivity
==================================================

A ping operation can be performed to check EVPN VPWS network connectivity.

#### Prerequisites

* Before using the [**ping evpn vpws**](cmdqueryname=ping+evpn+vpws) command to check EVPN VPWS network connectivity, ensure that the EVPN VPWS network has been correctly configured.
* If you have run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets after the previous test is complete, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable)/[**lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable+ipv6) command to enable the device to respond to MPLS Echo Request/MPLS Echo Request IPv6 packets before starting the current test.

#### Context

Perform the following steps in any view.


#### Procedure

* Check the EVPN VPWS network connectivity.
  
  
  + Check the connectivity of an EVPN VPWS network with the tunnel type being LDP/TE/BGP LSP/SR-MPLS BE/SR-MPLS TE/SR-MPLS TE Policy.
    
    Run the [**ping evpn vpws**](cmdqueryname=ping+evpn+vpws) *local-ce-id* *remote-ce-id* [ **vpn-instance** *evpn-name* ] [ **control-word** ] [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-tc** *tc* | **backup** ] \* command to check the EVPN VPWS status and roughly locate the EVPN VPWS fault.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In cross-domain scenarios, the **control-word** keyword must be specified, and the **-r** **4** mode is recommended.
  + Check the connectivity of an EVPN VPWS network with the tunnel type being SRv6 BE/SRv6 TE Policy/SRv6 TE Flow Group:
    
    Run the [**ping evpn vpws**](cmdqueryname=ping+evpn+vpws) *local-ce-id* *remote-ce-id* [ **vpn-instance** *evpn-name* ] [ **end-op** *endOp* [ *prefix-length* ] [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-tc** *tc* | { **-service-class***classValue* | **-te-class** *teClassValue* } | **backup** ]\* command to check the EVPN VPWS status and roughly locate the fault.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If the local service ID is not globally unique, the **vpn-instance** *evpn-name* parameter must be specified.
  
  The following is an example:
  
  # Perform a ping operation on an EVPN VPWS network.
  ```
  <HUAWEI> ping evpn vpws 2 1 
    EVPN VPWS PING FEC: Local Evpn Vpws Id = 2, Remote Evpn Vpws Id = 1 : 100  data bytes, press CTRL_C to break
    Tunnel-Type: SRv6 BE; Original-Nexthop: 2001:DB8:1::1; P/B: Primary
      Reply from 2001:DB8:11::1:0:3F: bytes=100 Sequence=1 time=4 ms
      Reply from 2001:DB8:11::1:0:3F: bytes=100 Sequence=2 time=2 ms
      Reply from 2001:DB8:11::1:0:3F: bytes=100 Sequence=3 time=2 ms
      Reply from 2001:DB8:11::1:0:3F: bytes=100 Sequence=4 time=3 ms
      Reply from 2001:DB8:11::1:0:3F: bytes=100 Sequence=5 time=2 ms
  
    --- FEC: Local CeId = 2, Remote CeId = 1 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 1/1/2 ms
  ```

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets so as to prevent system resource occupation.