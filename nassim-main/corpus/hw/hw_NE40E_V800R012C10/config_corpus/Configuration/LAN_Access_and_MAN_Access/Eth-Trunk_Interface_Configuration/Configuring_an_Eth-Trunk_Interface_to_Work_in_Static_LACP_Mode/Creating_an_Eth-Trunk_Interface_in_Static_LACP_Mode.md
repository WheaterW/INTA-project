Creating an Eth-Trunk Interface in Static LACP Mode
===================================================

An Eth-Trunk interface must be created before you add physical interfaces to the Eth-Trunk interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lacp priority**](cmdqueryname=lacp+priority) *priority*
   
   
   
   An LACP system priority is configured.
   
   
   
   A smaller value indicates a higher priority.
   
   To configure one end as the Actor, set its LACP system priority to a value smaller than the default value. This end can serve as the Actor because the other end uses the default LACP system priority.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The LACP system priority is configured using the [**lacp priority**](cmdqueryname=lacp+priority) command in the system view, and the LACP interface priority is configured using the same command but in the interface view.
   
   A change in the LACP system priority will cause LACP renegotiation. During the renegotiation process, Eth-Trunk interfaces in LACP mode will go down until the renegotiation succeeds, which may interrupt services. If a maintenance engineer who wants to configure an LACP interface priority runs the [**lacp priority**](cmdqueryname=lacp+priority) command in the system view by mistake, an LACP system priority is configured, which may cause Eth-Trunk interface flapping. To address this problem, run the [**lacp priority-command-mode**](cmdqueryname=lacp+priority-command-mode) command so that the LACP system priority and LACP interface priority configurations require different commands.
   
   When running the [**lacp priority-command-mode**](cmdqueryname=lacp+priority-command-mode) { **default** | **system-priority** } command, note the following points:
   * If you specify **default** in the command, the LACP system priority and LACP interface priority configurations still use the same command ([**lacp priority**](cmdqueryname=lacp+priority) *priority*).
   * If you specify **system-priority** in the command, run the [**lacp system-priority**](cmdqueryname=lacp+system-priority) *priority* command to configure the LACP system priority and run the [**lacp priority**](cmdqueryname=lacp+priority) *priority* command to configure the LACP interface priority.
3. (Optional) Run **lacp ignore aggregation delay**
   
   
   
   The device is enabled to ignore the value of the **Reserved** field in received LACP packets.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * This command is not recommended if the interconnected devices are both Huawei devices.
   * When a Huawei device is connected to a non-Huawei device, if the **Reserved** field defined by other vendors in an LACP packet is different from that defined by Huawei, LACP flapping occurs, and services are interrupted. In this scenario, you are advised to configure this command.
4. Run [**interface eth-trunk**](cmdqueryname=interface+eth-trunk) *trunk-id*
   
   
   
   An Eth-Trunk interface is created, and its view is displayed.
5. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Eth-Trunk interface is switched to the Layer 2 mode.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Physical interfaces can be added to an Eth-Trunk interface regardless of whether the Eth-Trunk interface works in Layer 2 or Layer 3 mode. If the Eth-Trunk interface needs to work in Layer 3 mode, skip this step and go to the next step.
6. Run [**mode lacp-static**](cmdqueryname=mode+lacp-static)
   
   
   
   The Eth-Trunk interface is configured to work in static LACP mode.
7. (Optional) Run [**lacp backup-mode enable**](cmdqueryname=lacp+backup-mode+enable)
   
   
   
   The Eth-Trunk interface is enabled to work in static LACP master/backup negotiation mode.
   
   
   
   If not all interfaces to be added to an Eth-Trunk interface in static LACP mode reside on the same traffic manager (TM) but you want those on the same TM to negotiate first, perform this step.
8. (Optional) Run [**lacp stable-preferred disable**](cmdqueryname=lacp+stable-preferred+disable)
   
   
   
   The function to keep the selection status of ports stable is disabled for the Eth-Trunk interface in static LACP mode.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.