Verifying the Configuration
===========================

After configuring a tunnel policy and applying it to a VPN instance, you can check information about the tunnel policy applied to the VPN instance and tunnels in the system.

#### Procedure

* Run the [**display tunnel-info**](cmdqueryname=display+tunnel-info) { *tunnel-id* | **all** | **statistics** } command to check information about tunnels in the current system.
* Run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) *interface-number* command to check detailed information about a specified tunnel interface.
* Run the [**display tunnel-policy**](cmdqueryname=display+tunnel-policy) [ *tunnel-policy-name* ] command to check information about tunnel policies in the system.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** [ *vpn-instance-name* ] command to check information about the tunnel policy applied to a VPN instance.
* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) **interface** *interface-type* *interface-number* command to check the tunnel policy used by SVC VPWS.
* Run the [**display mpls l2vc interface**](cmdqueryname=display+mpls+l2vc+interface) { *interface-name* | *interface-type* *interface-number* } command to check the tunnel policy used by LDP VPWS.
* Run the [**display vpls connection**](cmdqueryname=display+vpls+connection) [ **ldp** | **vsi** *vsi-name* ] **verbose** command to check the tunnel policy used by LDP VPLS.