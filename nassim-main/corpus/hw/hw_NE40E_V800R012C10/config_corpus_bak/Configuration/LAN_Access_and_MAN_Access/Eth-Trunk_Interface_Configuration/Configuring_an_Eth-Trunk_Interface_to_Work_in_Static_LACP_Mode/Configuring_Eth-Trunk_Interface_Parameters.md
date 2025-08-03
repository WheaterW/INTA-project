Configuring Eth-Trunk Interface Parameters
==========================================

Layer 2 and Layer 3 Eth-Trunk interfaces need to be configured with different parameters as required.

#### Procedure

* Configure parameters for a Layer 2 Eth-Trunk interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Run [**portswitch**](cmdqueryname=portswitch)
     
     
     
     The Eth-Trunk interface is switched to a Layer 2 interface.
  4. Perform one or more operations shown in [Table 1](#EN-US_TASK_0172362871__tab_dc_vrp_ethtrunk_cfg_002802) as needed.
     
     
     
     **Table 1** Configuring parameters for a Layer 2 Eth-Trunk interface
     | Parameter for a Layer 2 Eth-Trunk Interface | Operation |
     | --- | --- |
     | Maximum number of up member links that determine the Eth-Trunk link bandwidth | Run the [**max bandwidth-affected-linknumber**](cmdqueryname=max+bandwidth-affected-linknumber) *link-number* command. |
     | Maximum number of up member links | Run the [**max active-linknumber**](cmdqueryname=max+active-linknumber) *link-number* command.  NOTE:  To prevent Eth-Trunk link from flapping, you are advised to configure the same upper limit for the two ends of an Eth-Trunk link. If only one end of the Eth-Trunk link is configured, flapping may occur after all the selected member links switchover is triggered. |
     | Minimum number of up member links | Run the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command. |
     | Minimum bandwidth configured for the member links that are up on an Eth-Trunk interface | Run the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command.  NOTE:  + Ensure that the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command has not been run when you run the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command because the two commands are mutually exclusive. + The minimum bandwidth configured for both ends of an Eth-Trunk must be the same to prevent the Eth-Trunk interface from flapping. + After the minimum bandwidth is configured for the member links that are up on an Eth-Trunk interface, do not run the [**max active-linknumber**](cmdqueryname=max+active-linknumber) *link-number* command to configure the maximum number of active links. That is because the Eth-Trunk interface will go down if the total bandwidth of the maximum number of active links is less than the minimum bandwidth. |
     | Eth-Trunk interface load-balancing mode | Run the [**load-balance**](cmdqueryname=load-balance) { **src-dst-mac** | **src-dst-ip** | **packet-all** } command. |
     | Mode for selecting active interfaces | Run the [**lacp selected**](cmdqueryname=lacp+selected) { **priority** | **speed** } command. |
     | LACP preemption delay | 1. Run the [**lacp preempt enable**](cmdqueryname=lacp+preempt+enable) command to enable LACP preemption. 2. Run the [**lacp preempt delay**](cmdqueryname=lacp+preempt+delay) *delay-time* command to configure an LACP preemption delay.  NOTE:     + To ensure that an Eth-Trunk works properly, you are advised to enable or disable LACP preemption on both ends.    + The two ends of an Eth-Trunk link can be configured with different LACP preemption delays. If the two ends are configured with different preemption delays, Eth-Trunk uses the greater *delay-time* value as the preemption delay. |
     | Timeout period for an Eth-Trunk interface to receive LACP packets | Run the [**lacp timeout**](cmdqueryname=lacp+timeout) { **fast** [ **user-defined** *user-defined* ] | **slow** } command.  NOTE:  The two ends of an Eth-Trunk link can be configured with different timeout periods. To facilitate maintenance, you are advised to configure the same timeout period for both ends. |
     | **CollectorMaxDelay** field value in LACPDUs to be received by an Eth-Trunk interface | Run the [**lacp collector delay**](cmdqueryname=lacp+collector+delay) *delay-dtime* command to configure the value of the CollectorMaxDelay field in an LACPDU. |
     | LACP system ID for an Eth-Trunk interface | Run the [**lacp system-id**](cmdqueryname=lacp+system-id) *mac-address* command. |
     | LACP negotiation delay for an Eth-Trunk interface | Run the [**lacp negotiate delay**](cmdqueryname=lacp+negotiate+delay) *delay-value* command. |
     | Period that an Eth-Trunk interface waits before changing its state to down | Run the [**link-state down-delay-time**](cmdqueryname=link-state+down-delay-time) *delay-value* command. |
     | LACP driving an Eth-Trunk interface to go down after a delay | Run the [**lacp trunk-down-delay enable**](cmdqueryname=lacp+trunk-down-delay+enable) command. |
     | LACP port number uniqueness for an Eth-Trunk interface | Run the [**lacp unique-port-number enable**](cmdqueryname=lacp+unique-port-number+enable) command. |
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure parameters for a Layer 3 Eth-Trunk interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
     
     
     
     The Eth-Trunk interface view is displayed.
  3. Perform one or more operations shown in [Table 2](#EN-US_TASK_0172362871__tab_dc_vrp_ethtrunk_cfg_002803) as needed.
     
     
     
     **Table 2** Configuring parameters for a Layer 3 Eth-Trunk interface
     | Parameter for a Layer 3 Eth-Trunk Interface | Operation |
     | --- | --- |
     | IP address of the Eth-Trunk interface | Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command. |
     | MAC address of the Eth-Trunk interface | Run the [**mac-address**](cmdqueryname=mac-address) *mac-address* command. |
     | MTU of the Eth-Trunk interface | Run the [**mtu**](cmdqueryname=mtu) *mtu* command. The MTU is measured in bytes.  NOTICE:  + The MTUs of two directly-connected interfaces must be the same. After using the [**mtu**](cmdqueryname=mtu) *mtu* command to change the MTU of an interface, change the MTU of the directly-connected interface on another device to ensure that the MTUs of the two ends are the same. Otherwise, services may be interrupted. + If IPv6 runs on an Eth-Trunk interface, and the MTU set by using the [**mtu**](cmdqueryname=mtu) *mtu* command on the interface is smaller than 1280 bytes, IPv6 does not properly work on this interface. To prevent such a problem, set the MTU of the interface to a value greater than or equal to 1280 when IPv6 runs on the interface. |
     | Maximum number of up member links | Run the [**max active-linknumber**](cmdqueryname=max+active-linknumber) *link-number* command.  NOTE:  To prevent Eth-Trunk link from flapping, you are advised to configure the same upper limit for the two ends of an Eth-Trunk link. If only one end of the Eth-Trunk link is configured, flapping may occur after all the selected member links switchover is triggered. |
     | Minimum number of up member links | Run the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command.  An Eth-Trunk interface is up as long as one member interface is up. |
     | Minimum bandwidth configured for the member links that are up on an Eth-Trunk interface | Run the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command.  NOTE:  + Ensure that the [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* command has not been run when you run the [**least active-bandwidth**](cmdqueryname=least+active-bandwidth) *bandwidth* command because the two commands are mutually exclusive. + The minimum bandwidth configured for both ends of an Eth-Trunk must be the same to prevent the Eth-Trunk interface from flapping. + After the minimum bandwidth is configured for the member links that are up on an Eth-Trunk interface, do not run the [**max active-linknumber**](cmdqueryname=max+active-linknumber) *link-number* command to configure the maximum number of active links. That is because the Eth-Trunk interface will go down if the total bandwidth of the maximum number of active links is less than the minimum bandwidth. |
     | Load balancing mode | Run the [**load-balance**](cmdqueryname=load-balance) { **src-dst-mac** | **src-dst-ip** | **packet-all** | **symmetric-hash** [ **complement** ] } command. |
     | Mode for selecting active interfaces | Run the [**lacp selected**](cmdqueryname=lacp+selected) { **priority** | **speed** } command. |
     | LACP preemption delay | 1. Run the [**lacp preempt enable**](cmdqueryname=lacp+preempt+enable) command to enable LACP preemption. 2. Run the [**lacp preempt delay**](cmdqueryname=lacp+preempt+delay) *delay-time* command to configure an LACP preemption delay.  NOTE:     + To ensure that an Eth-Trunk works properly, you are advised to enable or disable LACP preemption on both ends.    + The two ends of an Eth-Trunk link can be configured with different LACP preemption delays. If the two ends are configured with different preemption delays, Eth-Trunk uses the greater *delay-time* value as the preemption delay. |
     | Timeout period for an Eth-Trunk interface to receive LACP packets | Run the [**lacp timeout**](cmdqueryname=lacp+timeout) { **fast** [ **user-defined** *user-defined* ] | **slow** } command.  NOTE:  The two ends of an Eth-Trunk link can be configured with different timeout periods. To facilitate maintenance, you are advised to configure the same timeout period for both ends. |
     | **CollectorMaxDelay** field value in LACPDUs to be received by an Eth-Trunk interface | Run the [**lacp collector delay**](cmdqueryname=lacp+collector+delay) *delay-dtime* command to configure the value of the CollectorMaxDelay field in an LACPDU. |
     | An LACP system ID for an Eth-Trunk interface | Run the [**lacp system-id**](cmdqueryname=lacp+system-id) *mac-address* command. |
     | LACP negotiation delay for an Eth-Trunk interface | Run the [**lacp negotiate delay**](cmdqueryname=lacp+negotiate+delay) *delay-value* command. |
     | Period that an Eth-Trunk interface waits before changing its state to down | Run the [**link-state down-delay-time**](cmdqueryname=link-state+down-delay-time) *delay-value* command. |
     | LACP driving an Eth-Trunk interface to go down after a delay | Run the [**lacp trunk-down-delay enable**](cmdqueryname=lacp+trunk-down-delay+enable) command. |
     | LACP port number uniqueness for an Eth-Trunk interface | Run the [**lacp unique-port-number enable**](cmdqueryname=lacp+unique-port-number+enable) command. |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.