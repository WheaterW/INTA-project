Applying a Traffic Policy
=========================

Applying a Traffic Policy

#### Prerequisites

Before applying a traffic policy, [configure the traffic policy](galaxy_mqc_cfg_0008.html).

![](public_sys-resources/note_3.0-en-us.png) 

If a traffic policy fails to be applied due to insufficient ACL resources on the device, you are advised to delete the traffic policy configuration that fails to be applied. Otherwise, after configurations are saved and the device is restarted, the configuration of other services that are running properly cannot be restored.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Apply a traffic policy.
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
3. (Optional) Enable the device to accurately deliver the traffic policy that is applied to a VLAN, a VLANIF interface, or an Eth-Trunk.
   
   
   ```
   [traffic-policy chip-based-mode](cmdqueryname=traffic-policy+chip-based-mode)
   ```
   
   When a traffic policy is applied to a VLAN, a VLANIF interface, or an Eth-Trunk and packets match ACL rules, the traffic policy is delivered to all chips of the device. If there is no corresponding VLAN, VLANIF interface, or Eth-Trunk member interface on some chips, the traffic policy is not delivered.
   
   This command is valid only for new traffic policies. If you want to enable this function for an existing traffic policy, delete the traffic policy and re-configure it.
   
   By default, a device is not enabled to accurately deliver the traffic policy that is applied to a VLAN, a VLANIF interface, or an Eth-Trunk.
4. (Optional) Enable the function of making only one traffic policy among multiple traffic policies take effect.
   
   
   ```
   [qos traffic-policy only-one-effective](cmdqueryname=qos+traffic-policy+only-one-effective)
   ```
   
   After this command is configured, if there are multiple traffic policies in the system, only one traffic policy takes effect and the other traffic policies do not take effect.
   
   By default, the function of making only one traffic policy among multiple traffic policies take effect is disabled.
   
   This function is supported only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ .
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```