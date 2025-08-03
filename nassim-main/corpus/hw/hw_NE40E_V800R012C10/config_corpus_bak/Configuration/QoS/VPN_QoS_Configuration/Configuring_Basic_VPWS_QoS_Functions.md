Configuring Basic VPWS QoS Functions
====================================

The VPNs carried over a tunnel have different resource requirements. To meet the resource requirements of a VPWS carried over a tunnel without affecting the quality of other VPN services, configure VPWS QoS.

#### Usage Scenario

In an L2VPN environment, multiple VPNs may share the same tunnel. As a result, bandwidth preemption occurs among these VPNs. This means that when VPN traffic is forwarded or discarded, the priorities of services in a VPN cannot be guaranteed. Moreover, non-VPN traffic also preempts the bandwidth of VPN traffic.

The VPNs carried over a tunnel have different resource requirements. To meet the resource requirements of a VPWS carried over a tunnel without affecting the quality of other VPNs, configure VPWS QoS.


#### Pre-configuration Tasks

Before configuring basic VPWS QoS functions, complete the following tasks:

* Configure VPWS PWs.

#### Procedure

* Configure basic VPN QoS functions in the interface view.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the AC interface view.
  3. Run the [**mpls l2vpn qos**](cmdqueryname=mpls+l2vpn+qos) **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **secondary** | **bypass** ] command to configure VPWS PW bandwidth resources.
     
     
     + **secondary**: specifies the bandwidth of the secondary VPWS PW.
     + **bypass**: specifies the bandwidth of the bypass PW.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure basic VPN QoS functions in the PW template.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**pw-template**](cmdqueryname=pw-template) *pwname* command to create a PW template and enter its view.
  3. Run the [**qos cir**](cmdqueryname=qos+cir) *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] command to configure VPWS PW bandwidth resources.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure basic VPN QoS functions in the system view.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run any of the following commands based on MS-PW types:
     
     
     + To configure basic QoS functions for a static MS-PW, run: [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address vc-id* **trans** *trans-label* **recv** *received-label* **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **between** *ip-address vc-id* **trans** *trans-label* **recv** *received-label* **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **encapsulation** *encapsulation-type* [ **control-word** | **no-control-word** ]
     + To configure basic QoS functions for a dynamic MS-PW, run: [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address* *vc-id* **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **between** *ip-address vc-id* [ **cir** *cir-value* ] [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **encapsulation** *encapsulation-type* [ **control-word-transparent** ]
     + To configure basic QoS functions for a static-dynamic MS-PW, run: [**mpls switch-l2vc**](cmdqueryname=mpls+switch-l2vc) [ **instance-name** *instance-name* ] *ip-address* *vc-id* **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **between** *ip-address* *vc-id* **trans** *trans-label* **recv** *recv-label* **cir** *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] [ **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] ] [ **oam-packet** **pop** **flow-label** ] **encapsulation** *encapsulation-type* [ **mtu** *mtu-value* ] [ **control-word** | **no-control-word** ] [ **rtp-header** ] **timeslotnum** *timeslotnum-value* [ **tdm-encapsulation** *number* ] [ **flow-label** { **both** | **send** | **receive** } ] [ ****control-word-transparent****]
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, perform the following operation to check the configuration results:

* Run the [**display mpls l2vpn qos**](cmdqueryname=display+mpls+l2vpn+qos) command to check VPWS QoS information, including bandwidth resources.


[(Optional) Configuring VPN-based QoS Profiles](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vpn-qos_cfg_5090.html)

To implement QoS scheduling for VPN users, you can define various QoS profiles and apply them to VPN.