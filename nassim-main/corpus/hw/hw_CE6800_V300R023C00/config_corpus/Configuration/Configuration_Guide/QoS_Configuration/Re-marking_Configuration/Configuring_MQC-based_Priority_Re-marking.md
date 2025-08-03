Configuring MQC-based Priority Re-marking
=========================================

Configuring MQC-based Priority Re-marking

#### Context

After re-marking is configured, the device re-marks the packets matching traffic classification rules so that the packets can be scheduled or forwarded based on re-marked priorities.

![](public_sys-resources/note_3.0-en-us.png) 

* Both [**remark 8021p**](cmdqueryname=remark+8021p) and [**remark dscp**](cmdqueryname=remark+dscp) can be bound to the same traffic policy and take effect simultaneously.
* For details about MQC-related configuration precautions, see "Configuration Precautions for MQC" in MQC Configuration.


#### Procedure

1. Configure a traffic classifier.
   
   
   
   For details about how to configure a traffic classifier, see [Configuring a Traffic Classifier](galaxy_mqc_cfg_0005.html) in "MQC Configuration".
2. Configure a traffic behavior.
   
   
   1. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Configure a traffic behavior as needed.
      * Re-marking 802.1p values of VLAN packets
        
        ```
        [remark 8021p](cmdqueryname=remark+8021p) { 8021p-value | inner-8021p }
        ```
        
        Re-marking the 802.1p value in the inner VLAN tag, that is, **inner-8021p**, is not supported by the CE6885-LL (low latency mode).
      * Re-marking DSCP values of IP packets
        
        ```
        [remark dscp](cmdqueryname=remark+dscp) { dscp-name | dscp-value }
        ```
      * Re-marking internal priorities
        
        ```
        [remark local-precedence](cmdqueryname=remark+local-precedence) { local-precedence-name | local-precedence-value } [ color ]
        ```
      * Re-marking local IDs
        
        Re-marking the local ID is not supported by the CE6885-LL (low latency mode).
        
        ```
        [remark qos-local-id](cmdqueryname=remark+qos-local-id) qos-local-id  [ inbound-match ]
        ```
      * Re-marking reserved VXLAN fields
        ```
        [remark vxlan reserved-value](cmdqueryname=remark+vxlan+reserved-value) rsv-value
        ```
        
        Re-marking reserved VXLAN fields is not supported by the CE6885-LL (low latency mode).
   3. Exit the traffic behavior view.
      ```
      [quit](cmdqueryname=quit)
      ```
   
   1. Commit the configuration.
      
      
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