Using Tracert to Check a Path on an EVPN VPLS Network by Specifying a MAC Address
=================================================================================

You can perform a tracert test to locate the forwarding fault on an EVPN VPLS network by specifying a destination MAC address.

#### Prerequisites

* Before running the [**tracert evpn**](cmdqueryname=tracert+evpn) command to locate a forwarding fault on an EVPN VPLS network, ensure that the EVPN VPLS network has been correctly configured.
* If you have run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets after the previous test is complete, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable)/[**lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable+ipv6) command to enable the device to respond to MPLS Echo Request/MPLS Echo Request IPv6 packets before starting the current test.

#### Context

Perform the following steps in any view.


#### Procedure

* Locate a forwarding fault on an EVPN VPLS network with the tunnel type being LDP/TE/BGP LSP/SR-MPLS BE/SR-MPLS TE/SR-MPLS TE Policy.
  
  
  
  Run the [**tracert evpn**](cmdqueryname=tracert+evpn) **vpn-instance** *evpn-name* **mac** *mac-addr* [ **-a** *source-ip* | **-s** *pkt-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-nexthop** *next-hop* ]\* [ **pipe** | **uniform** ] [ **detail** ] command to check the EVPN VPLS status and locate exceptions on a node along the EVPN VPLS path.
  
  ```
  <HUAWEI> tracert evpn vpn-instance evrf1 mac 00e0-fc12-3456
    Tracert vpn-instance evrf1 mac 00e0-fc12-3456 : 30 hops max, press CTRL_C to break
    Tunnel-Type: MPLS; Peer-Address: 3.3.3.9
    TTL    Replier            Time    Type      Hit   Downstream
    0                                 Ingress   N     10.1.1.2/[48061 48060 ]
    1      10.1.1.2           5 ms    Transit   N     10.3.1.2/[3 ]
    2      3.3.3.9            3 ms    Egress    Y   
  ```
* Locate a forwarding fault on an EVPN VPLS network with the tunnel type being SRv6 BE/SRv6 TE Policy/SRv6 TE Flow Group:
  
  
  + Run the [**tracert evpn**](cmdqueryname=tracert+evpn) **vpn-instance** *evpn-name* **mac** *mac-addr* [ **-a** *source-ip* | **-s** *pkt-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-nexthop** *next-hop* ] \* [ **pipe** | **uniform** ] [ **detail** ] command to check the EVPN VPLS status and locate exceptions on a node along the EVPN VPLS path.
    ```
    <HUAWEI> tracert evpn vpn-instance evrf1 mac 00e0-fc12-3456
      Tracert vpn-instance evrf1 mac 00e0-fc12-3456 : 30 hops max, press CTRL_C to break
      Tunnel-Type: SRv6 TE Policy; Peer-Address: 2001:DB8:3::3
      TTL    Replier                                 Time    Type      Hit   Downstream
      0                                                      Ingress   N     2001:DB8:21::1:0:0
      1      2001:DB8:20::2                          6 ms    Transit   N     2001:DB8:31::1:0:0
      2      2001:DB8:31::1:0:22                     4 ms    Egress    Y  
    ```
  
  
  + Run the [**tracert evpn**](cmdqueryname=tracert+evpn) **bridge-domain** *bd-id* [ **vlan** *vlan-id* ] **mac** *mac-address* [ **-a** *source-ip* | **-s** *pkt-size* | **-t** *timeout* | **-h** *max-ttl* | **-r** *reply-mode* | **-nexthop** *next-hop* | { **-service-class** *classValue* | **-te-class** *teClassValue* } ] \* [ **pipe** | **uniform** ] [ **detail** ] command to check the EVPN VPLS status and locate a faulty node along the EVPN VPLS path.
    ```
    <HUAWEI> tracert evpn bridge-domain 10 mac 00e0-fc12-3456 
      Tracert bridge-domain 10 mac 00e0-fc12-3456 : 30 hops max, press CTRL_C to break
      Tunnel-Type: SRv6 TE Policy; Peer-Address: 2001:DB8:3::3
      TTL    Replier                                 Time    Type      Hit   Downstream
      0                                                      Ingress   N     2001:DB8:21::1:0:0
      1      2001:DB8:20::2                          6 ms    Transit   N     2001:DB8:31::1:0:0
      2      2001:DB8:31::1:0:22                     4 ms    Egress    Y    
    ```

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets so as to prevent system resource occupation.