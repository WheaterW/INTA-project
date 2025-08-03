Configuring Multicast Traffic Transmission over P2MP Tunnels
============================================================

mLDP in-band MVPN uses mLDP P2MP tunnels to carry multicast traffic.

#### Procedure

* Perform the following steps on a receiver PE:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id* command to configure an MVPN ID.
  3. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
  4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
  5. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) **route-distinguisher** command to configure an RD for the VPN instance IPv4 address family.
  6. Run the **[**vpn-target**](cmdqueryname=vpn-target)** *vpn-target* ****both**** command to associate the current instance with VPN targets.
  7. Run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command to enable multicast routing for the VPN instance IPv4 address family.
  8. Run the [**multicast inband-signaling mldp**](cmdqueryname=multicast+inband-signaling+mldp) command to enable mLDP in-band MVPN.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on a PE to be configured as a sender PE:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**multicast mvpn**](cmdqueryname=multicast+mvpn) *mvpn-id* command to configure an MVPN ID.
  3. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to enter the VPN instance view.
  4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the VPN instance IPv4 address family view.
  5. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) **route-distinguisher** command to configure an RD for the VPN instance IPv4 address family.
  6. Run the **[**vpn-target**](cmdqueryname=vpn-target)** *vpn-target* ****both**** command to associate the current instance with VPN targets.
  7. Run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command to enable multicast routing for the VPN instance IPv4 address family.
  8. (Optional) Run the [**multicast bgp-connector compatible**](cmdqueryname=multicast+bgp-connector+compatible) command to enable Connector attribute compatibility.
  9. Run the [**multicast inband-signaling mldp**](cmdqueryname=multicast+inband-signaling+mldp) [ **frr** ] command to enable mLDP in-band MVPN and dual-root protection.
  10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.