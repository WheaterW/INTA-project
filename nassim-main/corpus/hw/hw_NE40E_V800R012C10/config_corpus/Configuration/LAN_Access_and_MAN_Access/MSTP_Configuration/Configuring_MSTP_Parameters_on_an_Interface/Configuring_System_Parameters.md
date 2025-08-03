Configuring System Parameters
=============================

Multiple Spanning Tree Protocol (MSTP) parameters that may affect network convergence include the network diameter, hello time, and timeout period for waiting for Bridge Protocol Data Units (BPDUs) from the upstream (3 x hello time x time factor). Configure proper MSTP parameters to implement rapid network convergence.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**stp process**](cmdqueryname=stp+process) *process-id*
   
   
   
   The MSTP process view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is needed only when you perform configuration in an MSTP process with a non-zero ID. If you perform configuration in MSTP process 0, skip this step.
3. Run [**stp bridge-diameter**](cmdqueryname=stp+bridge-diameter) *diameter*
   
   
   
   The network diameter is configured.
   
   
   
   * RSTP uses a single spanning tree instance on the entire network, which cannot prevent the performance from deteriorating when the network scale grows. Therefore, the network diameter cannot be larger than 7.
   * It is recommended that you run the [**stp bridge-diameter**](cmdqueryname=stp+bridge-diameter) *diameter* command to set the network diameter. Then, the device calculates the optimal Forward Delay period, Hello time, and Max Age period based on the set network diameter.
4. Run [**stp timer-factor**](cmdqueryname=stp+timer-factor) *factor*
   
   
   
   The timeout period for waiting for BPDUs from the upstream of a device is set.
5. (Optional) If the current device is at the edge of a network, run both or either of the following commands as needed:
   
   
   * To configure all ports on the devices as edge ports, run [**stp edged-port default**](cmdqueryname=stp+edged-port+default) command.
     
     After ports on a network edge device are configured as edge ports, the ports no longer participate in spanning tree calculation. This speeds up network topology convergence and improves network stability.
   * To configure all ports on the devices as BPDU filter ports, run the [**stp bpdu-filter default**](cmdqueryname=stp+bpdu-filter+default) command.
     
     After ports on a network edge device are configured as BPDU filter ports, the ports no longer process or send BPDUs.![](../../../../public_sys-resources/caution_3.0-en-us.png) 
   
   After the [**stp bpdu-filter default**](cmdqueryname=stp+bpdu-filter+default) and [**stp edged-port default**](cmdqueryname=stp+edged-port+default) commands are run in the system view, all ports on the device no longer actively send BPDUs or negotiate with directly-connected ports; instead, all the ports are in the Forwarding state. This may lead to a loop on the network, causing broadcast storms. Exercise caution when running these commands.
6. (Optional) To set the Forward Delay period, Hello time, and Max Age period, perform the following operations:
   
   
   * Run the [**stp timer forward-delay**](cmdqueryname=stp+timer+forward-delay) *forward-delay* command to set the Forward Delay period for a device.
   * Run the [**stp timer hello**](cmdqueryname=stp+timer+hello) *hello-time* command to set the Hello time for a device.
   * Run the [**stp timer max-age**](cmdqueryname=stp+timer+max-age) *max-age* command to set the Max Age period for a device.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The values of the Hello time, Forward Delay period, and Max Age period must comply with the following formulas. Otherwise, networking flapping occurs.
   
   * 2 Ã (Forward Delay - 1.0 second) >= Max Age
   * Max Age >= 2 Ã (Hello Time + 1.0 second)
7. Run [**stp max-hops**](cmdqueryname=stp+max-hops) *hop*
   
   
   
   The maximum hop count is set for the MST region.
8. Run [**stp mcheck**](cmdqueryname=stp+mcheck)
   
   
   
   The MCheck operation is performed.
   
   
   
   On a device running MSTP, if an interface is connected to a device running STP, the interface automatically transitions to the STP mode.
   
   Performing MCheck on the interface is required to manually switch the interface to the MSTP mode because the interface fails to automatically transition to the MSTP mode in the following situations:
   
   * The device running STP is shut down or moved.
   * The device running STP transitions to the MSTP mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you run the [**stp mcheck**](cmdqueryname=stp+mcheck) command in the system view, the MCheck operation is performed on all the interfaces.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.