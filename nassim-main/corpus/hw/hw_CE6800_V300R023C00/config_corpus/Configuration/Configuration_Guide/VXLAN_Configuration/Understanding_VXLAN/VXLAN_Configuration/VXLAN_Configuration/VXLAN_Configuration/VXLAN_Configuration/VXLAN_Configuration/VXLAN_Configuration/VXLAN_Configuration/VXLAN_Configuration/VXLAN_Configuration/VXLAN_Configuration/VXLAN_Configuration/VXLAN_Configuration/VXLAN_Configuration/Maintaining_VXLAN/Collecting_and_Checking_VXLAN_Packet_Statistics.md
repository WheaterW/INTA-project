Collecting and Checking VXLAN Packet Statistics
===============================================

Collecting and Checking VXLAN Packet Statistics

#### Context

To check the network status or locate network faults, you can enable packet statistics collection for a BD or VXLAN tunnel.


#### Procedure

* Enable packet statistics collection for a BD.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BD view.
     
     
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     ```
  3. Enable packet statistics collection for the BD.
     
     
     ```
     [statistics enable](cmdqueryname=statistics+enable)
     ```
     
     By default, packet statistics collection is disabled for BDs.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable VXLAN packet statistics collection for a specific VNI.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VNI view.
     
     
     ```
     [vni](cmdqueryname=vni+%28System+view%29) vni-id
     ```
  3. Enable VXLAN packet statistics collection for a specific VNI.
     
     
     ```
     [statistic enable](cmdqueryname=statistic+enable)
     ```
     
     By default, VXLAN packet statistics collection is disabled for a specific VNI.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable packet statistics collection for a VXLAN tunnel.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the NVE interface view.
     
     
     ```
     [interface nve](cmdqueryname=interface+nve) nve-number
     ```
  3. Enable packet statistics collection for a VXLAN tunnel with the specified remote VTEP IP address.
     
     
     ```
     [vxlan statistics](cmdqueryname=vxlan+statistics) peer peer-ip [ vni vni-id ] [enable](cmdqueryname=enable)
     ```
     
     By default, packet statistics collection is disabled for VXLAN tunnels.
  4. Enable packet statistics collection for a VXLAN tunnel with the specified local and remote VTEP IP addresses.
     
     
     ```
     [vxlan statistics](cmdqueryname=vxlan+statistics+enable) source srcAddr peer peer-ip [ vni vni-id ] enable
     ```
     
     By default, packet statistics collection is disabled for VXLAN tunnels.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable packet statistics collection for an IPv6 VXLAN tunnel. 
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the NVE interface view.
     
     
     ```
     [interface nve](cmdqueryname=interface+nve) nve-number
     ```
  3. Enable packet statistics collection for an IPv6 VXLAN tunnel with the specified remote VTEP IP address.
     
     
     ```
     [vxlan statistics](cmdqueryname=vxlan+statistics) peer destIpv6Addr [ vni vni-id ] [enable](cmdqueryname=enable)
     ```
     
     By default, packet statistics collection is disabled for an IPv6 VXLAN tunnel.
  4. Enable packet statistics collection for an IPv6 VXLAN tunnel with the specified local and remote VTEP IP addresses.
     
     
     ```
     [vxlan statistics](cmdqueryname=vxlan+statistics+enable) source srcIpv6Addr peer destIpv6Addr [ vni vni-id ] enable
     ```
     
     By default, packet statistics collection is disabled for an IPv6 VXLAN tunnel.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Follow-up Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) *bd-id* **statistics** command to check packet statistics of a BD.
* Run the [**display vxlan statistics**](cmdqueryname=display+vxlan+statistics) **source** *source-ip-address* **peer** *peer-ip-address* [ **vni** *vni-id* ] command to check the packet statistics of a VXLAN tunnel.
* Run the [**display vxlan statistics**](cmdqueryname=display+vxlan+statistics) **source** *source-ipv6* **peer** *peer-ipv6* [ **vni** *vni-id* ] command to check IPv6 VXLAN tunnel packet statistics.
* Run the [**display vxlan statistics vni**](cmdqueryname=display+vxlan+statistics+vni) *vni-id* command to check the VXLAN packet statistics of a VNI.
* Run the [**display fwm vxlan**](cmdqueryname=display+fwm+vxlan) { **l2subif** | **bridge-domain** | **tunnel** | **evpn** | **oam** } [**statistics**](cmdqueryname=statistics) [ **all** ] **slot** *slot-id* command to check VXLAN packet statistics on a specified board.