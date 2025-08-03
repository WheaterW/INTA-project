Configuring the ETH-LCK Function in BD EVPN Networking
======================================================

The ETH-LCK function notifies the server-layer (sub-layer) MEP of an administrative lock event. Then the data sent to the MEP is interrupted.

#### Context

As shown in [Figure 1](#EN-US_TASK_0172362147__fig_dc_vrp_cfg_01154401), PE1 and PE2 are connected through an EVPN, and CE1 and CE2 are connected to the EVPN through a BD. The MEPs configured on the access interfaces of CE1 and CE2 reside in level-6 MD1. The MEPs configured on PE1 and PE2 reside in level-3 MD2. If the link between PE1 and PE2 fails and the CC is Down, the MEP in level-3 MD2 detects the fault and sends an alarm to the NMS. After a certain period, a MEP in level-6 MD1 also detects the fault and sends the same alarm to the NMS. In this case, you need to configure the ETH-LCK function to prevent the MEP in the high-level MD from sending alarms to the NMS.

To suppress CC alarms from being generated in the outer MD, ETH-LCK is implemented with out-of-service ETH-Test. A MEP in the inner MD with a lower level initiates ETH-Test by sending an ETH-LCK frame to a MEP in the outer MD. Upon receipt of the ETH-LCK frame, the MEP in the outer MD suppresses all CC alarms immediately and reports an ETH-LCK alarm indicating administrative locking. Before out-of-service ETH-Test is complete, the MEP in the inner MD sends ETH-LCK frames to the MEP in the outer MD. After out-of-service ETH-Test is complete, the MEP in the inner MD stops sending ETH-LCK frames. If the MEP in the outer MD does not receive ETH-LCK frames for a period 3.5 times as long as the specified interval, it releases the alarm suppression and reports a clear ETH-LCK alarm.

**Figure 1** Networking diagram for configuring the ETH-LCK function of the BD EVPN  
![](images/fig_dc_vrp_cfg_01155701.png)

#### Procedure

1. Perform the following steps on the PE:
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name* [ **level** *level* ]
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   4. Run [**map**](cmdqueryname=map) **bridge-domain**  *bd-id*
      
      The MA is bound to a specified BD.
   5. Run [**mep mep-id**](cmdqueryname=mep+mep-id) **interface** *interface-type interface-number* **inward**
      
      A MEP is configured.
   6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
      
      The MEP is enabled to send CCMs.
   7. Run [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **lck** **enable** **level** *level*
      
      The ETH-LCK function is enabled.
   8. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
      
      An RMEP is configured.
   9. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
      
      The device is enabled to receive CCMs.
   10. Run [**eth-test enable**](cmdqueryname=eth-test+enable) **mep** *mep-id*
       
       The ETH-test function is enabled.
   11. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
2. Perform the following steps on the CE.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name* [ **level** *level* ]
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   4. Run [**map vlan**](cmdqueryname=map+vlan) *vlan-id*
      
      The MA is bound to the VLAN.
   5. Run [**mep mep-id**](cmdqueryname=mep+mep-id) **interface** *interface-type interface-number* **inward**
      
      A MEP is configured.
   6. Run [**mep ccm-send enable**](cmdqueryname=mep+ccm-send+enable)
      
      The MEP is enabled to send CCMs.
   7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
      
      An RMEP is configured.
   8. Run [**remote-mep ccm-receive**](cmdqueryname=remote-mep+ccm-receive) [ **mep-id** *mep-id* ] **enable**
      
      The device is enabled to receive CCMs.
   9. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Verifying the Configuration

* After the configuration is complete, if the link between the PEs is shut down and the CC is Down, the CE reports an LCK alarm. Run the [**display alarm active**](cmdqueryname=display+alarm+active) command on the CE to check the task execution result.