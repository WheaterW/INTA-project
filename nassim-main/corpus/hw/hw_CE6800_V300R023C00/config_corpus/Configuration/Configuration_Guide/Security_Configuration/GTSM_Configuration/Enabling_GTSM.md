Enabling GTSM
=============

Enabling GTSM

#### Context

Without GTSM enabled on a device, the device sends protocol packets directly to the control plane. After GTSM is enabled for a protocol:

* If a protocol packet matches a GTSM policy, the device checks whether the TTL value in the packet is within the specified range. If so, the device sends the packet to the control plane. If not, the device drops the packet.
* If a protocol packet does not match the GTSM policy, the device sends the protocol packet to the control plane if the default action of "pass" is used or drops the packet if the action is set to "drop." For detailed configurations, see [(Optional) Configuring an Action to Process Packets That Do Not Match a GTSM Policy](vrp_gtsm_cfg_0004.html).

[Table 1](#EN-US_TASK_0000001130781840__table2020194613253) describes the protocols that support GTSM.

**Table 1** Protocols supporting GTSM
| Protocol | Matching Granularity of a GTSM Policy | Configuration Reference |
| --- | --- | --- |
| RIP | Public network instance or VPN instance | IP Routing Configuration > RIP Configuration > Improving RIP Network Security > Configuring RIP GTSM |
| OSPF/OSPFv3 | Public network instance or VPN instance | IP Route Configuration > OSPF Configuration > Configuring OSPF GTSM  IP Route Configuration > OSPFv3 Configuration > Configuring OSPFv3 GTSM |
| BGP/BGP4+ | Public network instance or VPN instance  Peer IP address or peer group name | IP Route Configuration > BGP Configuration > Configuring BGP GTSM  IP Route Configuration > BGP4+ Configuration > Configuring BGP4+ GTSM |

The following uses RIP as an example to describe how to enable RIP GTSM.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable RIP GTSM and configure a TTL value range and GTSM policy.
   
   
   ```
   [rip valid-ttl-hops](cmdqueryname=rip+valid-ttl-hops) valid-ttl-hops-value [ vpn-instance vpn-instance-name ]
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The value range is [255 â *valid-ttl-hops-value* + 1, 255].
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.
* Run the [**reset gtsm statistics**](cmdqueryname=reset+gtsm+statistics) { *slot-id* | **all** } command to clear GTSM statistics.