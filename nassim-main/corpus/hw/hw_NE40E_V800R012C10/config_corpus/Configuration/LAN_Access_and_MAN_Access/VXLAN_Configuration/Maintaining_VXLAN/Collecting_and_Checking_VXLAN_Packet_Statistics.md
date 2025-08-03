Collecting and Checking VXLAN Packet Statistics
===============================================

To check the network status or locate network faults, you can enable the traffic statistics function to view VXLAN packet statistics.

#### Procedure

* Enable VXLAN packet statistics collection for a BD.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     A BD is created, and the BD view is displayed.
  3. Run [**statistic enable**](cmdqueryname=statistic+enable)
     
     VXLAN packet statistics collection is enabled for the BD.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable VXLAN packet statistics collection for a specific VNI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vni**](cmdqueryname=vni) *vni-id*
     
     A VNI is created, and the VNI view is displayed.
  3. Run [**statistic enable**](cmdqueryname=statistic+enable)
     
     VXLAN packet statistics collection is enabled in the specified VNI view.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable VNI- and IPv4 VXLAN tunnel-based packet statistics collection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface nve**](cmdqueryname=interface+nve) *nve-number*
     
     An NVE interface is created, and the NVE interface view is displayed.
  3. Run [**source**](cmdqueryname=source) *ip-address*
     
     The IP address of the source VTEP is configured.
  4. Run [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list** *ip-address* &<1-10>
     
     An ingress replication list is configured for the VNI.
  5. Run [**vxlan statistics**](cmdqueryname=vxlan+statistics) **peer** *peer-ip* **vni** *vni-id* [ **inbound** | **outbound** ] **enable**
     
     VNI- and VXLAN tunnel-based packet statistics collection is enabled.
  6. Run [**vxlan statistic l3-mode**](cmdqueryname=vxlan+statistic+l3-mode) **peer** *peer-ip* **vni** *vni-id* **inbound** **enable**
     
     VNI- and VXLAN tunnel-based uplink Layer 3 traffic statistics collection is enabled.
     
     Run [**vxlan statistics l3-mode**](cmdqueryname=vxlan+statistics+l3-mode) **peer** *peer-ip* [ **vni** *vni-id* ] **outbound** **enable**
     
     VNI- and VXLAN tunnel-based downlink Layer 3 traffic statistics collection is enabled.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable VNI- and IPv6 VXLAN tunnel-based packet statistics collection.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface nve**](cmdqueryname=interface+nve) *nve-number* command to create an NVE interface and enter its view.
  3. Run the [**vxlan statistics**](cmdqueryname=vxlan+statistics) **peer** *destIpv6Addr* **vni** *vni-val* [ **inbound** | **outbound** ] **enable** command to enable VNI- and IPv6 VXLAN tunnel-based packet statistics collection.
  4. Run the [**vxlan statistics l3-mode**](cmdqueryname=vxlan+statistics+l3-mode) **peer** *destIpv6Addr* **vni** *vni-val* **inbound** **enable** command to enable VNI- and IPv6 VXLAN tunnel-based Layer 3 uplink traffic statistics collection.
  5. Run the [**vxlan statistics l3-mode**](cmdqueryname=vxlan+statistics+l3-mode) **peer** *destIpv6Addr* [ **vni** *vni-val* ] **outbound** **enable** command to enable VNI- and VXLAN tunnel-based Layer 3 downlink traffic statistics collection.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) **bd-id** **statistics** command to view VXLAN packet statistics in the BD.
* Run the [**display vxlan statistics**](cmdqueryname=display+vxlan+statistics) **vni** *vni-id* command to view VXLAN packet statistics collected by VNI.
* Run the [**display vxlan statistics**](cmdqueryname=display+vxlan+statistics) **source** *source-ip* **peer** *peer-ip* **vni** *vni-id* command to check VNI- and VXLAN tunnel-based packet statistics.
* Run the [**display vxlan statistics**](cmdqueryname=display+vxlan+statistics) **source** *source-ipv6* **peer** *peer-ipv6* **vni** *vni-val* command to check VNI- and IPv6 VXLAN tunnel-based packet statistics.
* Run the [**display vxlan statistics l3-mode**](cmdqueryname=display+vxlan+statistics+l3-mode) **source** *source-ip* **peer** *peer-ip* **local-vni** *vni-id* command to check VNI- and VXLAN tunnel-based Layer 3 uplink traffic statistics.
* Run the [**display vxlan statistics l3-mode**](cmdqueryname=display+vxlan+statistics+l3-mode) **source** *source-ip* **peer** *peer-ip* **remote-vni** *vni-id* command to check VNI- and VXLAN tunnel-based Layer 3 downlink traffic statistics.
* Run the [**display vxlan statistics l3-mode**](cmdqueryname=display+vxlan+statistics+l3-mode) **source** *source-ipv6* **peer** *peer-ipv6* **local-vni** *vni-val* command to check VNI- and IPv6 VXLAN tunnel-based Layer 3 uplink traffic statistics.
* Run the [**display vxlan statistics l3-mode**](cmdqueryname=display+vxlan+statistics+l3-mode) **source** *source-ipv6* **peer** *peer-ipv6* **remote-vni** *vni-val* command to check VNI- and IPv6 VXLAN tunnel-based Layer 3 downlink traffic statistics.