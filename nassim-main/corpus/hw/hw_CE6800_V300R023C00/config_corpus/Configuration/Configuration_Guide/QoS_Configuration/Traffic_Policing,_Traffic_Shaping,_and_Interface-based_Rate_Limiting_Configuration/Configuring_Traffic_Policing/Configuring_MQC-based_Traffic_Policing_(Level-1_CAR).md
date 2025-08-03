Configuring MQC-based Traffic Policing (Level-1 CAR)
====================================================

Configuring MQC-based Traffic Policing (Level-1 CAR)

#### Context

There are various services on a network. When a large amount of service traffic enters the network side, congestion may occur due to insufficient bandwidth. To control a specific type of service traffic in the inbound or outbound direction on an interface, MQC-based traffic policing (level-1 CAR) can be configured. MQC-based traffic policing uses traffic classifiers to implement differentiated services. When the receive or transmit rate of packets matching traffic classification rules exceeds the specified limit, the device discards the packets.

When both QoS CAR and MQC are used on an interface for traffic statistics collection, statistics about packets to which a QoS CAR profile is applied contain only the packets that do not match the traffic policy.

The device performs the CAR action on interfaces of the same chip centrally, and on interfaces of different chips separately. If a traffic policy containing traffic policing is applied to an Eth-Trunk, a VLAN, or the system, and interfaces of the object to which the traffic policy is applied belong to N chips, the actual rate limit is N times as large as the CAR value.

For example, assume that interface 1 and interface 2 belong to chip 0 and interface 3 and interface 4 belong to chip 1. If interfaces 1 to 4 join VLAN 10 and a traffic policy containing the rate limit of 1 Mbit/s is applied to VLAN 10, the rate limit of interface 1 and interface 2 is 1 Mbit/s and the rate limit of interface 3 and interface 4 is 1 Mbit/s. That is, the total rate limit is 2 Mbit/s after the traffic policy is applied to VLAN 10.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support this function.



#### Procedure

1. Configure a traffic classifier.
   
   
   
   For details about how to configure a traffic classifier, see [Configuring a Traffic Classifier](galaxy_mqc_cfg_0005.html) in "MQC Configuration".
2. Configure a traffic behavior.
   1. (Optional) Disable the device from counting the inter-frame gaps and preambles when the device calculates the traffic policing rate.
      
      
      ```
      [qos car ifg disable](cmdqueryname=qos+car+ifg+disable)
      ```
   2. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   3. Configure a CAR action.
      
      
      ```
      [car](cmdqueryname=car) cir cir-value [ kbps | mbps | gbps ] [ pir pir-value [ kbps | mbps | gbps ] ] [ cbs cbs-value [ bytes | kbytes | mbytes ] pbs pbs-value [ bytes | kbytes | mbytes ] ] [ share ] [ mode { color-blind | color-aware } ] [ green pass [ service-class class color color ] | yellow { discard | pass [ service-class class color color ] } | red { discard | pass [ service-class class color color ] } ] *
      ```
   4. Exit the traffic behavior view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Configure a traffic policy.
   1. Create a traffic policy and enter the traffic policy view, or enter the view of an existing traffic policy.
      
      
      ```
      [traffic policy](cmdqueryname=traffic+policy) policy-name
      ```
   2. Bind a traffic behavior and a traffic classifier to the traffic policy.
      
      
      ```
      [classifier](cmdqueryname=classifier) classifier-name behavior behavior-name [ precedence precedence-value ]
      ```
   3. Exit the traffic policy view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Apply a traffic policy.
   * Apply a traffic policy to the system.
     1. Apply a traffic policy to the system.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name global [ slot slot-id ] { inbound | outbound }
        ```
     2. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
     
     The application of a traffic policy in the outbound direction globally is not supported by the CE6885-LL (low latency mode). That is, only the **inbound** parameter is supported, and the **outbound** parameter is not supported by the CE6885-LL (low latency mode).
   * Apply a traffic policy to an interface.
     1. Enter the interface view.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        ```
     2. Apply a traffic policy to the interface.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name { inbound | outbound }
        ```
        
        The application of a traffic policy in the outbound direction globally is not supported by the CE6885-LL (low latency mode). That is, only the **inbound** parameter is supported, and the **outbound** parameter is not supported by the CE6885-LL (low latency mode).
     3. Exit the interface view.
        ```
        [quit](cmdqueryname=quit)
        ```
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Apply a traffic policy to a VLAN.
     1. Create a VLAN and enter the VLAN view.
        ```
        [vlan](cmdqueryname=vlan) vlan-id
        ```
     2. Apply a traffic policy to the VLAN.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name { inbound | outbound }
        ```
        
        The application of a traffic policy in the outbound direction globally is not supported by the CE6885-LL (low latency mode). That is, only the **inbound** parameter is supported, and the **outbound** parameter is not supported by the CE6885-LL (low latency mode).
     3. Exit the VLAN view.
        ```
        [quit](cmdqueryname=quit)
        ```
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Apply a traffic policy to a VPN instance.
     1. Create a VPN instance and enter the VPN instance view.
        ```
        [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
        ```
     2. Apply a traffic policy to the VPN instance.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name inbound
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        A traffic policy can be applied to a VPN instance only in the inbound direction.
     3. Exit the VPN instance view.
        ```
        [quit](cmdqueryname=quit)
        ```
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Apply a traffic policy to a BD.
     1. Create a BD and enter the BD view.
        ```
        [bridge-domain](cmdqueryname=bridge-domain) bd-id
        ```
     2. Apply a traffic policy to the BD.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name { inbound | outbound }
        ```
        
        After a traffic policy is applied to a BD, the traffic policy takes effect for incoming or outgoing packets that belong to the BD.
     3. Exit the BD view.
        ```
        [quit](cmdqueryname=quit)
        ```
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit) 
        ```
     
     For the CE6820H, CE6820H-K, CE6820S, and CE6885-LL (low latency mode), a traffic policy cannot be applied in the BD view.
   * Apply a traffic policy to a QoS group.
     
     If the same traffic policy needs to be applied to multiple VLANs and interfaces or multiple traffic classifiers for matching packets from different source IP addresses need to be bound to the same traffic policy, you are advised to add the VLANs, interfaces, or source IP addresses to the same QoS group and apply the traffic policy to the QoS group.
     
     1. Create a QoS group and enter the QoS group view.
        ```
        [qos group](cmdqueryname=qos+group) group-name
        ```
     2. Add a specified interface, VLAN, or source IP address to the QoS group.
        ```
        [group-member](cmdqueryname=group-member) { interface { interface-type interface-num | interface-name [ to interface-type interface-num | interface-name ] } &<1-8> | vlan { vlanid [ to vlanid ] } &<1-8> | ip source ip-address { ip-address-wildcard | ip-address-netmask } }
        ```
        
        Only one type of member can be specified.
        
        Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM and CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S support the configuration of adding a specified source IP address to a QoS group, that is, **group-member** **ip source**.
     3. Apply a traffic policy to the QoS group.
        ```
        [traffic-policy](cmdqueryname=traffic-policy) policy-name { inbound | outbound }
        ```
        
        The application of a traffic policy in the outbound direction is not supported by the CE6885-LL (low latency mode). That is, only the **inbound** parameter is supported, and the **outbound** parameter is not supported by the CE6885-LL (low latency mode).
     4. Exit the QoS group view.
        ```
        [quit](cmdqueryname=quit)
        ```
     5. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```