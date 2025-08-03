Using Ping to Check Tunnel Connectivity on an EVPN VPLS Network by Specifying a MAC Address
===========================================================================================

You can perform a ping test to check tunnel connectivity on an EVPN VPLS network by specifying a destination MAC address.

#### Prerequisites

* Before using the [**ping evpn**](cmdqueryname=ping+evpn) command to check EVPN VPLS network connectivity, ensure that the EVPN VPLS network has been correctly configured.
* If you have run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets after the previous test is complete, run the [**lspv mpls-lsp-ping echo enable**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable)/[**lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=lspv+mpls-lsp-ping+echo+enable+ipv6) command to enable the device to respond to MPLS Echo Request/MPLS Echo Request IPv6 packets before starting the current test.

#### Context

Perform the following steps in any view.


#### Procedure

* Check the connectivity of an EVPN VPLS network with the tunnel type being LDP/TE/BGP LSP/SR-MPLS BE/SR-MPLS TE/SR-MPLS TE Policy.
  
  
  
  Run the [**ping evpn**](cmdqueryname=ping+evpn) **vpn-instance** *evpn-name* **mac** *mac-address* [ **-a** *source-ip* | **-c** *count* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-nexthop** *nexthop-address* ] \* command to check the EVPN VPLS status and locate the fault.
  
  ```
  <HUAWEI> ping evpn vpn-instance evpna mac 00e0-fc12-3456 -c 3 -s 200 
    Ping vpn-instance evpna mac 00e0-fc12-3456 : 200 data bytes, press CTRL_C to break
    Tunnel-Type: MPLS; Peer-Address: 1.1.1.1
      Reply from 1.1.1.1: bytes=200 sequence=1 time = 11ms    
      Reply from 1.1.1.1: bytes=200 sequence=2 time = 10ms    
      Reply from 1.1.1.1: bytes=200 sequence=3 time = 10ms  
    --- vpn-instance: evpna 00e0-fc12-3456 ping statistics ---    
      3 packet(s) transmitted    
      3 packet(s) received    
      0.00% packet loss    
      round-trip min/avg/max = 10/10/11 ms
  ```
* Check the connectivity of an EVPN VPLS network with the tunnel type being VXLAN.
  
  Run the [**ping evpn**](cmdqueryname=ping+evpn) **bridge-domain** *bd-id* [ **vlan** *vlan-id* ] **mac** *mac-address* [ **-a** *source-ip* | **-c** *count* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-nexthop** *nexthop-address* ] \* command to check the EVPN VPLS status and roughly locate the fault.
  ```
  <HUAWEI> ping evpn bridge-domain 100 mac 00e0-fc12-3456
    Ping bridge-domain 100 mac 00e0-fc12-3456 : 110 data bytes, press CTRL_C to break
    Tunnel-Type: VXLAN; Peer-Address: 1.1.1.1
      Reply from 1.1.1.1: bytes=110 sequence=1 time < 1ms
      Reply from 1.1.1.1: bytes=110 sequence=2 time < 1ms
      Reply from 1.1.1.1: bytes=110 sequence=3 time < 1ms
      Reply from 1.1.1.1: bytes=110 sequence=4 time < 1ms
      Reply from 1.1.1.1: bytes=110 sequence=5 time < 1ms
    --- bridge-domain: 100 00e0-fc12-3456 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 1/1/1 ms
  ```
* Check the connectivity of an EVPN VPLS network with the tunnel type being SRv6 BE/SRv6 TE Policy /SRv6 TE Flow Group:
  
  
  + Run the [**ping evpn**](cmdqueryname=ping+evpn) **vpn-instance** *evpn-name* **mac** *mac-address* [ **-a** *source-ip* | **-c** *count* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-nexthop** *nexthop-address* ] \* command to check the EVPN VPLS status and locate the fault.
    ```
    <HUAWEI> ping evpn vpn-instance evpna mac 00e0-fc12-3456 -c 3 -s 200 
      Ping vpn-instance evpna mac 00e0-fc12-3456 : 200 data bytes, press CTRL_C to break
      Tunnel-Type: SRv6 TE Policy; Peer-Address: 2001:DB8:100::1:0:5F
        Reply from 2001:DB8:100::1:0:5F: bytes=200 sequence=1 time = 11ms    
        Reply from 2001:DB8:100::1:0:5F: bytes=200 sequence=2 time = 10ms    
        Reply from 2001:DB8:100::1:0:5F: bytes=200 sequence=3 time = 10ms  
      --- vpn-instance: evpna 00e0-fc12-3456 ping statistics ---    
        3 packet(s) transmitted    
        3 packet(s) received    
        0.00% packet loss    
        round-trip min/avg/max = 10/10/11 ms
    ```
  
  
  + Run the [**ping evpn**](cmdqueryname=ping+evpn) **bridge-domain** *bd-id* [ **vlan** *vlan-id* ] **mac** *mac-address* [ **-a** *source-ip* | **-c** *count* | **-m** *interval* | **-s** *packet-size* | **-t** *time-out* | **-r** *reply-mode* | **-nexthop** *nexthop-address* | { **-service-class** *classValue* | **-te-class** *teClassValue* } ]\* command to check the EVPN VPLS status and roughly locate the fault.
  
  
  ```
  <HUAWEI> ping evpn bridge-domain 100 mac 00e0-fc12-3456
    Ping bridge-domain 100 mac 00e0-fc12-3456 : 110 data bytes, press CTRL_C to break
    Tunnel-Type: SRv6 TE Policy; Peer-Address: 2001:DB8:100::1:0:5F
      Reply from 2001:DB8:100::1:0:5F: bytes=110 sequence=1 time < 1ms
      Reply from 2001:DB8:100::1:0:5F: bytes=110 sequence=2 time < 1ms
      Reply from 2001:DB8:100::1:0:5F: bytes=110 sequence=3 time < 1ms
      Reply from 2001:DB8:100::1:0:5F: bytes=110 sequence=4 time < 1ms
      Reply from 2001:DB8:100::1:0:5F: bytes=110 sequence=5 time < 1ms
    --- bridge-domain: 100 00e0-fc12-3456 ping statistics ---
      5 packet(s) transmitted
      5 packet(s) received
      0.00% packet loss
      round-trip min/avg/max = 1/1/1 ms
  ```

#### Follow-up Procedure

After the test is completed, you are advised to run the [**undo lspv mpls-lsp-ping echo enable**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable)/[**undo lspv mpls-lsp-ping echo enable ipv6**](cmdqueryname=undo+lspv+mpls-lsp-ping+echo+enable+ipv6) command to disable the device from responding to MPLS Echo Request/MPLS Echo Request IPv6 packets so as to prevent system resource occupation.