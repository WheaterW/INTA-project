Configuring Tunnel Load Balancing
=================================

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
   
   A tunnel policy is created and its view is displayed.
3. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   A description is configured for the tunnel policy.
4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) { **gre** | **lsp** | **cr-lsp** } \* **load-balance-number** *load-balance-number*
   
   The sequence in which each type of tunnel is selected and the number of tunnels participating in load balancing are configured.
5. Apply the tunnel policy.
   * Apply the tunnel policy to a specified BGP/MPLS IP VPN instance.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
     3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
     4. Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to apply the tunnel policy to the VPN instance IPv4 address family.
   * Apply the tunnel policy to a specified BGP/MPLS IPv6 VPN instance.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
     3. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to enter the VPN instance IPv6 address family view.
     4. Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to apply the tunnel policy to the VPN instance IPv6 address family.
   * Apply the tunnel policy to an SVC VLL.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
     3. To apply the tunnel policy to a VC of an SVC VLL, run the following commands based on interface types:
        + Ethernet interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-interworking** ] ] \*
        + ATM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] ] \*
        + TDM interface: [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | **access-port** | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | [ **rtp-header** ] ] \*
   * Apply the tunnel policy to an LDP VLL.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
     3. To apply the tunnel policy to a VC of an LDP VLL, run the following commands based on interface types:
        + Ethernet interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \*
        + ATM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **max-atm-cells** *cells-value* ] | [ **atm-pack-overtime** *time* ] | **ignore-standby-state** ] \*
        + TDM interface: [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *tnl-policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \*
   * Apply the tunnel policy to an LDP VPLS.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **auto** | **static** ] command to create a VSI.
     3. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to set the PW signaling protocol to LDP and enter the VSI-LDP view.
     4. Run the [**vsi-id**](cmdqueryname=vsi-id) *vsi-id* command to set VSI-ID.
     5. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **tnl-policy** *policy-name* command to apply the tunnel policy to a VSI peer.
   * Apply the tunnel policy to a PWE3.
     1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
     2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the AC interface view.
     3. Choose one of the following options to apply the tunnel policy to a PW.
        + For a dynamic PW, run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { **pw-template** *pw-template-name* | *ip-address* } \* *vc-id* **tunnel-policy** *policy-name* command.
        + For a static PW, run the [**mpls static-l2vc**](cmdqueryname=mpls+static-l2vc) { { **destination** *ip-address* | **pw-template** *pw-template-name* *vc-id* } \* | **destination** *ip-address* [ *vc-id* ] } **transmit-vpn-label** *transmit-label-value* **receive-vpn-label** *receive-label-value* **tunnel-policy** *tnl-policy-name* command.
6. Run [**commit**](cmdqueryname=commit).
   
   The configuration is committed.

#### Follow-up Procedure

Run the **save** command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.