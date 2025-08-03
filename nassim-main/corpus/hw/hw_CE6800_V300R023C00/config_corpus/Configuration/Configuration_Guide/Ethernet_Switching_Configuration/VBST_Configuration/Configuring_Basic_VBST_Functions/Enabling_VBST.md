Enabling VBST
=============

Enabling VBST

#### Context

Enabling VBST on a ring network immediately triggers spanning tree calculation on the network. Parameters such as the device priority and port priority affect spanning tree calculation, and changing them during calculation may cause network flapping. To ensure fast and stable spanning tree calculation, set parameters such as the device priority and port priority before enabling VBST.

The number of PVs is equal to the sum of existing VBST-enabled VLANs that all VBST-enabled interfaces are added to. For example, if VBST is enabled on 10 device interfaces, and each interface is added to 100 existing VBST-enabled VLANs, then the number of PVs occupied by all the interfaces is 1000. If the number of occupied PVs exceeds the specifications, the CPU usage may be high. This results in the device being incapable of promptly processing tasks, affects protocol calculation, and even makes the device unmanageable (by the NMS).

* The CPU usage of VBST is in direct proportion to the number of occupied PVs. If parameter settings are not adjusted in a scenario where a large number of PVs exist, the CPU usage will be too high.
* You can run the [**display vbst port-vlan statistics**](cmdqueryname=display+vbst+port-vlan+statistics) command in any view to check the supported maximum number of PVs of VBST.

![](public_sys-resources/note_3.0-en-us.png) 

* On a network running VBST, configure the core device as the root bridge to ensure the stability of the Layer 2 network. Failing to do so may cause temporary service interruptions if deployment of new devices on the network triggers switchover of the root bridge.
* When VBST is enabled on a ring network, VBST immediately starts spanning tree calculation. Parameters such as the device priority and port priority affect spanning tree calculation, and changing these parameters during the calculation may cause network flapping. To ensure fast and stable spanning tree calculation, perform basic configurations on the switching device and its ports before enabling VBST.
* VBST constructs a spanning tree in each VLAN so that traffic in different VLANs can be forwarded along different spanning trees. However, it cannot prevent performance deterioration due to significantly increasing network scale.

* When the number of PVs on a VBST network reaches the upper limit (you can run the [**display vbst port-vlan statistics**](cmdqueryname=display+vbst+port-vlan+statistics) command to check the number of occupied PVs and the maximum number of PVs supported by the device):
  + You are advised to adjust the device configurations to reduce the number of occupied PVs. For example, check whether the interfaces that participate in VBST calculation are added to unnecessary VLANs; if so, remove the interfaces from these VLANs. Alternatively, run the [**stp disable**](cmdqueryname=stp+disable) command on the interfaces that do not need to participate in VBST calculation, or run the [**stp vlan disable**](cmdqueryname=stp+vlan+disable) command in the system view to disable VBST in the VLANs that do not require VBST.
  + If the number of occupied PVs cannot be reduced, run the [**stp vlan timer hello**](cmdqueryname=stp+vlan+timer+hello) command to set Hello Time to a value greater than or equal to 4 seconds and adjust Forward Delay and Max Age values accordingly.
  + If a large number of PVs are required, you are advised to set Hello Time to a larger value and adjust Forward Delay and Max Age values accordingly. If the number of PVs is 8000, you are advised to set Hello Time to 4 seconds. If the number of PVs is 16000, you are advised to set Hello Time to 8 seconds. If the number of PVs is 24000, you are advised to set Hello Time to 10 seconds.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the spanning tree working mode to VBST.
   
   
   ```
   [stp mode vbst](cmdqueryname=stp+mode+vbst)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The VBST mode is mutually exclusive with the STP, RSTP, and MSTP modes.
   
   If 1:*N* (*N* > 1) mapping between instances and VLANs has been configured on the device, you must delete the mapping before changing the spanning tree working mode to VBST.
   
   If the [**stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command has been configured on the device, you must run the [**undo stp vpls-subinterface enable**](cmdqueryname=stp+vpls-subinterface+enable) command on the corresponding interface before changing the spanning tree working mode to VBST.
3. Enable VBST.
   
   
   ```
   [stp enable](cmdqueryname=stp+enable)
   ```
4. Enable VBST in VLANs.
   
   
   ```
   [undo stp vlan](cmdqueryname=stp+vlan+disable) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> disable
   ```
   
   By default, VBST is enabled in all VLANs.
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Enable VBST.
   
   
   ```
   [stp enable](cmdqueryname=stp+enable)
   ```
   
   By default, VBST is enabled on all interfaces.
8. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. (Optional) Configure a protection mode when VBST detects different PVIDs on directly connected interfaces.
   
   
   ```
   [stp pvid-consistency protection mode block](cmdqueryname=stp+pvid-consistency+protection+mode+block)
   ```
   
   By default, no protection mode is configured for PVID inconsistency detected between directly connected interfaces. If the PVIDs of two directly connected interfaces are different, VBST will not block the interfaces in their default VLANs. However, if the protection mode is set to block in the preceding situation, VBST will block these interfaces in their default VLANs.
   
   If the interfaces at both ends of a link are trunk interfaces and their PVIDs are changed, you are advised to configure the protection mode for PVID inconsistency. This prevents traffic forwarding exceptions caused by improper configurations.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```