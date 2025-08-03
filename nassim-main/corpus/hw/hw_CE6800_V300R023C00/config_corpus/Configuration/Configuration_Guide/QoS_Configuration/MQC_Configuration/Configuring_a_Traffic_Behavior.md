Configuring a Traffic Behavior
==============================

Configuring a Traffic Behavior

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
   
   
   ```
   [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
   ```
3. Define actions in the traffic behavior. You can configure multiple non-conflicting actions in a traffic behavior.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For details about precautions for each action, see the corresponding commands in the Command Reference.
   
   The device supports a maximum of 2048 traffic behaviors.
   
   
   
   | Action | Command |
   | --- | --- |
   | Packet filtering | See [Packet Filtering Configuration](galaxy_qos_filtering_cfg_0001.html). |
   | Traffic statistics collection | See [Traffic Statistics Collection Configuration](galaxy_qos_statistics_cfg_0001.html). |
   | MQC-based re-marking | See [Re-marking Configuration](galaxy_qos_remark_cfg_0001.html). |
   | MQC-based redirection | See [Redirection Configuration](galaxy_qos_redirect_cfg_0001.html). |
   | MQC-based traffic policing | See [Configuring MQC-based Traffic Policing (Level-1 CAR)](galaxy_qos_trafficpolicy_trafficshaping_cfg_0031.html) in **Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting Configuration**. |
   | Hierarchical traffic policing | [**car**](cmdqueryname=car) *car-name* **share**  See [Configuring Traffic Policing (Level-2 CAR)](galaxy_qos_trafficpolicy_trafficshaping_cfg_0032.html) in **Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting Configuration**.  This command is not supported by the CE6885-LL (low latency mode). |
   | MQC-based flow mirroring | [**mirroring observe-port**](cmdqueryname=mirroring+observe-port) *observe-port-index*  [**mirroring observe-port**](cmdqueryname=mirroring+observe-port) **group** *group-id*  For details, see "Configuring Flow Mirroring" in Configuration Guide > System Monitoring Configuration > Mirroring Configuration. |
   | Disabling MAC address learning | [**mac-address learning disable**](cmdqueryname=mac-address+learning+disable)  For details, see "Disabling MAC Address Learning" in Configuration Guide > Ethernet Switching Configuration > MAC Configuration. |
   | MQC-based VLAN mapping | [**vlan-mapping**](cmdqueryname=vlan-mapping) { **vlan** *vlan-id* | **inner-vlan** *inner-vlan-id* }  For details, see "Configuring VLAN Mapping" in Configuration Guide > Ethernet Switching Configuration > VLAN Configuration. |
   | MQC-based selective QinQ | [**vlan-stacking**](cmdqueryname=vlan-stacking) **vlan** *vlan-id*  For details, see "Configuring QinQ" in Configuration Guide > Ethernet Switching Configuration > VLAN Configuration. |
   | Disabling URPF check | [**ip urpf disable**](cmdqueryname=ip+urpf+disable)  For details, see "URPF Configuration" in Configuration Guide > Security Configuration.  This command is not supported by the CE6885-LL (low latency mode). |
   | Enabling AnyFlow | [**any-flow enable**](cmdqueryname=any-flow+enable)  This function is supported only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM.  For details, see "AnyFlow Configuration" in Configuration Guide > System Monitoring Configuration. |
   | Enabling intelligent traffic analysis | [**traffic-analysis enable**](cmdqueryname=traffic-analysis+enable)  This function is supported only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM and CE6885-LL (low latency mode).  For details, see "Intelligent Traffic Analysis Configuration" in Configuration Guide > System Monitoring Configuration. |
   | Binding a multicast NAT instance to a traffic behavior | [**multicast-nat bind instance**](cmdqueryname=multicast-nat+bind+instance) **id** *instance-id* [ **name** *instance-name* ]  This function is supported only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM and CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.  For details, see "Multicast NAT Configuration" in Configuration Guide > IP Multicast Configuration. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```