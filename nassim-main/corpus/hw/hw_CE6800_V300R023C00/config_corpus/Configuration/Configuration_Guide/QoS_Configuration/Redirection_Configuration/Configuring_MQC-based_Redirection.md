Configuring MQC-based Redirection
=================================

Configuring MQC-based Redirection

#### Context

After redirection is configured, the device can redirect packets matching traffic classification rules to the CPU, a specified interface, a specified observing port group, and a specified next-hop address.

![](public_sys-resources/note_3.0-en-us.png) 

* For Layer 2 data traffic, you are advised to configure redirection to an interface. For Layer 3 data traffic or unicast packets that enter a VXLAN tunnel, you are advised to configure redirection to a next-hop address.
* For details about MQC-related configuration precautions, see "Configuration Precautions for MQC" in MQC Configuration.


#### Procedure

1. Configure a traffic classifier.
   
   
   
   For details about how to configure a traffic classifier, see [Configuring a Traffic Classifier](galaxy_mqc_cfg_0005.html) in "MQC Configuration".
2. Configure a traffic behavior.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   3. Configure a redirection action.
      
      
      * Redirection to a CPU
        
        ```
        [redirect cpu](cmdqueryname=redirect+cpu)
        ```
        
        The CE6885-LL (low latency mode) does not support this command.
        
        ![](public_sys-resources/notice_3.0-en-us.png) 
        
        After a traffic policy containing [**redirect cpu**](cmdqueryname=redirect+cpu) is used, the device redirects packets matching traffic classification rules to the CPU, which may decrease the CPU performance. Exercise caution when you use this command.
      * Redirection to an interface
        
        ```
        [redirect interface](cmdqueryname=redirect+interface) interface-type interface-number [ fail-action forward ]
        ```
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        Generally, if a packet needs to be redirected to the outbound interface, the outbound interface needs to be added to the VLAN corresponding to the packet.
      * Redirection to a specified GRE tunnel interface
        ```
        [redirect interface](cmdqueryname=redirect+interface) tunnel tunnel-id
        ```
        
        The CE6885-LL (low latency mode) does not support redirection to a specified GRE tunnel interface.
      * Redirection to an observing port group
        
        ```
        [redirect observe-port group](cmdqueryname=redirect+observe-port+group) group-id
        ```
      * Redirection to a single next-hop IP address
        
        For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:
        
        ```
        [redirect](cmdqueryname=redirect) [ vpn-instance vpn-instance-name ] nexthop { ip-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ fail-action discard ] [ low-precedence ]
        ```
        ```
        [redirect](cmdqueryname=redirect) ipv6 [ vpn-instance vpn-instance-name ] nexthop { ipv6-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ fail-action discard ]
        ```
        
        For the CE6885-LL (low latency mode):
        
        ```
        [redirect](cmdqueryname=redirect) [ vpn-instance vpn-instance-name ] nexthop { ip-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ fail-action discard ]
        ```
      * Redirection to multiple next-hop IP addresses
        
        ```
        [redirect load-balance](cmdqueryname=redirect+load-balance) [ vpn-instance vpn-instance-name ] nexthop { ip-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ fail-action discard ] [ low-precedence ]
        ```
        
        The CE6885-LL (low latency mode) does not support low-precedence PBR, that is, it does not support the **low-precedence** parameter.
        
        ```
        [redirect](cmdqueryname=redirect) ipv6 load-balance [ vpn-instance vpn-instance-name ] nexthop { ipv6-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ fail-action discard ]
        ```
        
        The CE6885-LL (low latency mode) does not support redirection of IPv6 packets.
      * Redirection to a remote next-hop address
        
        For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
        
        ```
        [redirect remote](cmdqueryname=redirect+remote) [ vpn-instance vpn-instance-name ] { ip-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ exact ] [ low-precedence ]
        ```
        ```
        [redirect remote](cmdqueryname=redirect+remote) [ vpn-instance vpn-instance-name ] ipv6-address &<1-16> [ exact ]
        ```
        
        For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-LL (low latency mode), CE6885-T, and CE6863E-48S8CQ:
        
        ```
        [redirect remote](cmdqueryname=redirect+remote) [ vpn-instance vpn-instance-name ] { ip-address [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ exact ] [ low-precedence ] [ local ]
        ```
        
        The CE6885-LL (low latency mode) does not support low-precedence PBR, that is, it does not support the **low-precedence** parameter.
        
        For the CE6820H, CE6820H-K, CE6820S, CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:
        
        ```
        [redirect remote](cmdqueryname=redirect+remote) ipv6 [ vpn-instance vpn-instance-name ] ipv6-address &<1-16> [ exact ] [ local ]
        ```
        
        For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-KCE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6855-LL (low latency mode), CE6885-T, and CE6863E-48S8CQ:
        
        ```
        [redirect remote](cmdqueryname=redirect+remote) multi-vpn { ip-address [ vpn-instance vpn-instance-name ] [ track nqa admin-name test-name [ reaction probe-failtimes fail-times ] ] } &<1-16> [ exact ] [ low-precedence ] [ local ]
        ```
        ```
        [redirect remote](cmdqueryname=redirect+remote) ipv6 multi-vpn { ipv6-address [ vpn-instance vpn-instance-name ] } &<1-16> [ exact ] [ local ]
        ```
        
        The CE6885-LL (low latency mode) does not support redirection of IPv6 multi-VPN instance packets.
        
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        If **low-precedence** is specified, the device does not support redirection of IPv6 packets or IP packets encapsulated in tunnel mode.
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
4. Apply the traffic policy.
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

#### Verifying the Configuration

| Operation | Command |
| --- | --- |
| Check the configured traffic classifiers. | [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] |
| Check the configured traffic behaviors. | [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] |
| Check the configured traffic policy. | [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] |
| Check the traffic policy application records. | [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) |
| Check TCAM delivery failures. | [**display system tcam fail-record**](cmdqueryname=display+system+tcam+fail-record) [ **slot** *slot-id* ] |
| Check the group indexes and rule counts occupied by different services. | [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) [ **slot** *slot-id* ]  [**display system tcam service**](cmdqueryname=display+system+tcam+service) { [**cpcar**](cmdqueryname=cpcar) [**slot**](cmdqueryname=slot) *slot-id* | *service-name* [**slot**](cmdqueryname=slot) *slot-id* [ [**chip**](cmdqueryname=chip) *chip-id* ] } |
| Check the traffic policy application records. | [**display system tcam service traffic-policy**](cmdqueryname=display+system+tcam+service+traffic-policy) |
| Check information about matched rules. | [**display system tcam match-rules**](cmdqueryname=display+system+tcam+match-rules) **slot** *slot-id* |
| Check statistics on packets that match a traffic policy. | **[**display traffic-policy statistics**](cmdqueryname=display+traffic-policy+statistics)** |
| Check statistics on packets matching hardware-based ACLs. | [**display acl hardware statistics**](cmdqueryname=display+acl+hardware+statistics)  NOTE:  The device can display only the statistics on the packets matching the hardware-based ACL referenced by MQC. To implement this, you need to first run the [**statistics enable**](cmdqueryname=statistics+enable) command in the traffic behavior view to enable traffic statistics collection. |
| Check matching fields and actions supported by a traffic policy in each view. | [**display system tcam acl group-information**](cmdqueryname=display+system+tcam+acl+group-information) |
| Check information about the resources occupied by the traffic policy to be applied to determine whether the traffic policy can be successfully applied after the configuration is committed. | [**display traffic-policy pre-state**](cmdqueryname=display+traffic-policy+pre-state) |