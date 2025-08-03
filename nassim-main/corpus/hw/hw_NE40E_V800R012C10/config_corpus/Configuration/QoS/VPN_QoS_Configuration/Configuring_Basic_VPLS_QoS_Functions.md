Configuring Basic VPLS QoS Functions
====================================

The VPN services carried over a tunnel have different resource requirements. To meet the resource requirements of VPLS services carried over a tunnel without affecting the quality of other VPN services, you need to configure VPLS QoS.

#### Usage Scenario

In an L2VPN scenario, if multiple VPN services are carried over the same tunnel, bandwidth preemption occurs among these VPN services. Non-VPN traffic also preempts the bandwidth of VPN traffic. As a result, VPN traffic cannot be forwarded strictly based on service priorities.

To solve this problem, you need to configure VPLS QoS. VPLS QoS ensures that the VPLS services carried over the tunnel have their resource requirements met without affecting the service quality of other VPNs.


#### Pre-configuration Tasks

Before configuring basic VPLS QoS functions, configure a VPLS VSI.

The VSI-based QoS configuration takes effect to all PWs in the VSI view. The VSI PW-based QoS configuration takes effect to a specified PW in an LDP VSI.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

VSI-based QoS and VSI PW-based QoS cannot be both configured in an LDP VSI.



#### Procedure

* Configure basic VPN QoS functions in the VSI view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  3. Run [**qos cir**](cmdqueryname=qos+cir) *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ]
     
     
     
     QoS parameters are configured for the VSI.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure basic VPN QoS functions in the VSI-LDP-PW view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  3. Run [**pwsignal**](cmdqueryname=pwsignal) **ldp**
     
     
     
     The LDP signaling mode is configured for the VSI, and the VSI-LDP view is displayed.
  4. Run [**pw**](cmdqueryname=pw) *pw-name*
     
     
     
     A PW is created, and the VSI-LDP-PW view is displayed.
  5. Run [**qos cir**](cmdqueryname=qos+cir) *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ]
     
     
     
     QoS parameters are configured for the VSI PW.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring basic VPLS QoS functions, verify the configuration.

* Run the [**display mpls l2vpn qos**](cmdqueryname=display+mpls+l2vpn+qos) command to check the bandwidth information about VPLS QoS.


[(Optional) Configuring VPN-based QoS Profiles](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_vpn-qos_cfg_5090a.html)

To implement QoS scheduling for VPN users, you can define various QoS profiles and apply them to VPN.