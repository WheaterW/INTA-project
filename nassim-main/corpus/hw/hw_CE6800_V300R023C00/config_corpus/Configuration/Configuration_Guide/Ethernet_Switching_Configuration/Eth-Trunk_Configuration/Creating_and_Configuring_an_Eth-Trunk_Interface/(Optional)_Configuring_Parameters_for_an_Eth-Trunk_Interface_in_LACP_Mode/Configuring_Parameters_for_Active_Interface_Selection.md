Configuring Parameters for Active Interface Selection
=====================================================

Configuring Parameters for Active Interface Selection

#### Context

By default, after the Actor is determined, the other end of an Eth-Trunk selects active interfaces based on the LACP interface priorities and numbers of active interfaces on the Actor. This ensures that both ends use the same active interfaces. In real-world applications, you can configure parameters for selecting active interfaces as required.

* **Mode in which active interfaces are selected**: If member interfaces of an Eth-Trunk interface work at different rates and active interfaces are selected based on interface priorities, interfaces working at a low rate may be selected. If you want interfaces working at high rates to be active interfaces, configure devices to select active interfaces based on interface rates.
* **Enabling member interfaces at different rates to forward data packets**: Ethernet interfaces working at different rates can be added to the same Eth-Trunk interface in LACP mode. To ensure that all these Ethernet interfaces can be selected to forward traffic, you can enable the interfaces to forward data packets.
* **Upper and lower thresholds for the number of active interfaces in an Eth-Trunk interface**: To ensure normal forwarding and bandwidth of an Eth-Trunk interface, set upper and lower thresholds for the number of active interfaces. This reduces the impact incurred by member link status changes.
  + When the number of active interfaces falls below the lower threshold, the Eth-Trunk interface goes down. Configuring the lower threshold for the number of active interfaces in an Eth-Trunk ensures that the Eth-Trunk has the minimum required bandwidth. Determine whether to set this parameter based on the network plan. The default value is recommended in non link-redundancy networking scenarios. By default, the lower threshold for the number of active interfaces is 1.
  + The upper threshold for the number of active interfaces can improve network reliability while assuring bandwidth. When the number of active interfaces reaches this threshold, you can keep adding new member interfaces to the Eth-Trunk interface, but the number of active interfaces will not exceed the upper threshold. In such cases, some links function as backup links until active interfaces go down.
* **Timeout period for an Eth-Trunk interface to receive LACPDUs**: If a member interface on the peer end of an Eth-Trunk link encounters a self-loop or another fault but the Eth-Trunk interface on the local end cannot detect this fault within the timeout time (the default timeout period for the local end to receive LACPDUs is 90 seconds), traffic will be lost. To ensure reliable traffic transmission between the two ends of an Eth-Trunk link, you can configure a timeout period for an Eth-Trunk interface to receive LACPDUs. If a member interface on the local end does not receive LACPDUs from the peer end within the configured timeout period, this member interface goes down immediately and stops forwarding traffic.
* **LACP preemption**: If an active link fails, the system selects the backup link with the highest priority to take its place. If the active link recovers and LACP preemption is disabled, the system does not re-select active interfaces, and the recovered link remains in backup state, despite having a higher priority than that of the new active link. LACP preemption is disabled on devices by default. If LACP preemption is enabled, the link with a higher priority will replace the link with a lower priority as an active link.
* **LACP priority of member interfaces**: By default, the member interfaces in the Actor's Eth-Trunk interface have the same LACP interface priority. The Actor selects interfaces with the smallest interface number as active interfaces. You can change the LACP interface priority to select active interfaces as needed.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. In the Eth-Trunk interface view, configure parameters for selecting active interfaces.
   
   
   
   **Table 1** Configuring parameters for selecting active interfaces in the Eth-Trunk interface view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the mode in which active interfaces in an Eth-Trunk interface are selected. | [**lacp select**](cmdqueryname=lacp+select) { **priority** | **speed** } | **priority** indicates that active interfaces are selected based on LACP interface priorities. For details about how to configure the LACP interface priority for an Eth-Trunk member interface, see [Configuring LACP Interface Priorities for Eth-Trunk Member Interfaces](#EN-US_TASK_0000001176661271__cmd8383124113714).  **speed**: indicates that active interfaces are selected based on interface rates.  To ensure normal forwarding, you are advised to set the same mode on both ends of an Eth-Trunk. |
   | Enable interfaces that work at different rates to forward data packets. | [**lacp mixed-rate link enable**](cmdqueryname=lacp+mixed-rate+link+enable) | When member interfaces of an Eth-Trunk interface work at different rates, active interfaces are selected based on LACP interface priorities and interface numbers on the Actor. To enable specified interfaces to become active, you can increase these interfaces' LACP interface priorities. For details, see [Configuring LACP Interface Priorities for Eth-Trunk Member Interfaces](#EN-US_TASK_0000001176661271__step163831415378). |
   | Configure the upper threshold for the number of active interfaces in an Eth-Trunk interface. | [**lacp max active-linknumber**](cmdqueryname=lacp+max+active-linknumber) *link-number* | To prevent an Eth-Trunk from flapping, you are advised to set the value of this parameter to be the same at both ends of the Eth-Trunk. If this parameter is configured on only one end of the Eth-Trunk, flapping may occur on the other end when all the selected active links fail. |
   | Configure the lower threshold for the number of active interfaces in an Eth-Trunk interface. | [**least active-linknumber**](cmdqueryname=least+active-linknumber) *link-number* | This parameter value can be different on local and peer devices, in which case the larger value is used. |
   | Set the timeout period for an Eth-Trunk interface to receive LACPDUs. | [**lacp timeout**](cmdqueryname=lacp+timeout) **fast** [ **user-defined** *user-defined* ] | By default, the timeout period for the local end to receive LACPDUs is 90 seconds (**slow**), and the interval for the peer end to send LACPDUs is 30 seconds.  If **fast** is specified, the timeout period for the local end to receive LACPDUs is 3 seconds, and the interval for the peer end to send LACPDUs is 1 second. If **fast** **user-defined** *user-defined* is specified, you can set the timeout period for the local end to receive LACPDUs as needed.  The two ends of an Eth-Trunk can be configured with different timeout periods; however, to facilitate maintenance, you are advised to configure the same timeout period for both ends. |
   | Configure LACP preemption on an Eth-Trunk interface. | [**lacp preempt enable**](cmdqueryname=lacp+preempt+enable) | This command enables LACP preemption on an Eth-Trunk interface. After this function is enabled, the default preemption delay is 30 seconds.  With LACP preemption enabled, the system re-selects active interfaces based on LACP interface priorities on the Actor after active interfaces recover from a failure.  To ensure that an Eth-Trunk works properly, you are advised to enable or disable LACP preemption on both ends of the Eth-Trunk. |
   | [**lacp preempt delay**](cmdqueryname=lacp+preempt+delay) *delay-time* | This command configures the LACP preemption delay. The default preemption delay is 30 seconds.  If the two ends of an Eth-Trunk link are configured with different LACP preemption delays, the longer delay takes effect. |
4. Return to the system view and enter the view of an Eth-Trunk member interface.
   
   
   ```
   quit
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Set the LACP interface priority as needed.
   
   
   ```
   [lacp priority](cmdqueryname=lacp+priority) priority
   ```
   
   
   
   LACP interface priorities affect which interfaces of an Eth-Trunk are selected as active interfaces. A smaller numerical value represents a higher priority. If interfaces have the same LACP interface priority, the system selects interfaces with the smallest interface number as active interfaces.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```