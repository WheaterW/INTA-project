Enabling BIERv6 Network Slicing
===============================

After BIERv6 network slicing is enabled globally and slice IDs are specified, multicast packets are forwarded through specified network slices.

#### Context

In the MVPNv4 over BIERv6, MVPNv6 over BIERv6, GTMv6 over BIERv6, or GTMv4 over BIERv6 scenario, network slicing can be deployed in BIERv6 tunnels. After BIERv6 network slicing is enabled globally, you can specify a network slice instance ID for an MVPN instance or a multicast stream in an MVPN instance so that multicast service packets are forwarded through the network slice interface corresponding to the slice ID.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the **[**bier ipv6 network-slice enable**](cmdqueryname=bier+ipv6+network-slice+enable)** command to enable BIERv6 network slicing globally in NG MVPNv4/v6 over BIERv6 and GTMv4/v6 over BIERv6 scenarios.
   
   
   
   To enable a BIERv6 tunnel to support BIERv6 network slicing, perform this configuration on both the ingress and transit nodes.
3. Configure a network slice instance ID for an MVPN instance or a multicast stream in an MVPN instance on the ingress of a BIERv6 tunnel as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a network slice instance ID is configured both for an MVPN instance and for a multicast stream in the MVPN instance, the slice ID configured based on a multicast stream takes precedence over the slice ID configured based on an MVPN instance. That is, if a network slice ID is specified for a multicast stream in a VPN instance, the multicast stream is forwarded through the network slice interface corresponding to the slice ID; otherwise, multicast streams are forwarded through the network slice interface bound to the VPN instance.
   
   
   
   * MVPNv4 over BIERv6
     1. Run the **[**ip vpn-instance**](cmdqueryname=ip+vpn-instance)** **vpn-instance-name** command to enter the VPN instance view.
     2. Run the **[**ipv4-family**](cmdqueryname=ipv4-family)** command to enter the VPN instance IPv4 address family view.
     3. Run the [**mvpn**](cmdqueryname=mvpn) command to enter the VPN instance IPv4 address family MVPN view.
     4. Specify the network slice instance ID based on the MVPN instance or multicast stream as required.
        1. Run the [**bier ipv6 network-slice**](cmdqueryname=bier+ipv6+network-slice) *slice-id* command to specify a network slice instance ID for the MVPN instance.
        2. Run the [**bier ipv6**](cmdqueryname=bier+ipv6+network-slice) [ **group** *group-address* **source** *source-address* ] **network-slice** *slice-id* command to specify a network slice instance ID for a multicast stream in the MVPN instance.
   * GTMv4 over BIERv6
     1. Run the [**multicast vpn-public**](cmdqueryname=multicast+vpn-public) command to enter the public network IPv4 address family MVPN view.
     2. Specify the network slice instance ID based on the MVPN instance or multicast stream as required.
        1. Run the [**bier ipv6 network-slice**](cmdqueryname=bier+ipv6+network-slice) *slice-id* command to specify a network slice instance ID for the MVPN instance.
        2. Run the [**bier ipv6**](cmdqueryname=bier+ipv6+network-slice) [ **group** *group-address* **source** *source-address* ] **network-slice** *slice-id* command to specify a network slice instance ID for a multicast stream in the MVPN instance.
   * MVPNv6 over BIERv6
     1. Run the **[**ip vpn-instance**](cmdqueryname=ip+vpn-instance)** *vpn-instance-name* command to enter the VPN instance view.
     2. Run the **ipv6-family** command to enter the VPN instance IPv6 address family view.
     3. Run the [**mvpn**](cmdqueryname=mvpn) command to enter the VPN instance IPv6 address family MVPN view.
     4. Specify the network slice instance ID based on the MVPN instance or multicast stream as required.
        1. Run the [**bier ipv6 network-slice**](cmdqueryname=bier+ipv6+network-slice) *slice-id* command to specify a network slice instance ID for the MVPN instance.
        2. Run the [**bier ipv6**](cmdqueryname=bier+ipv6+network-slice) [ **group** *group-address* **source** *source-address* ] **network-slice** *slice-id* command to specify a network slice instance ID for a multicast stream in the MVPN instance.
   * GTMv6 over BIERv6
     1. Run the [**multicast ipv6 vpn-public**](cmdqueryname=multicast+ipv6+vpn-public) command to enter the public network IPv6 address family MVPN view.
     2. Specify the network slice instance ID based on the MVPN instance or multicast stream as required.
        1. Run the [**bier ipv6 network-slice**](cmdqueryname=bier+ipv6+network-slice) *slice-id* command to specify a network slice instance ID for the MVPN instance.
        2. Run the [**bier ipv6**](cmdqueryname=bier+ipv6+network-slice) [ **group** *group-address* **source** *source-address* ] **network-slice** *slice-id* command to specify a network slice instance ID for a multicast stream in the MVPN instance.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.