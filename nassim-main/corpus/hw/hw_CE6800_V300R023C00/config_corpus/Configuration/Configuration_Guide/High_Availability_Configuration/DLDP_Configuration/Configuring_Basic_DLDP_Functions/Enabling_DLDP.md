Enabling DLDP
=============

Enabling DLDP

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DLDP globally.
   
   
   ```
   [dldp enable](cmdqueryname=dldp+enable)
   ```
   
   By default, DLDP is disabled globally.
3. (Optional) Configure a working mode of DLDP.
   
   
   ```
   [dldp work-mode](cmdqueryname=dldp+work-mode) { enhance | normal }
   ```
   
   The default working mode of DLDP is **enhance**, which indicates the enhanced mode.
4. (Optional) Configure a DLDP shutdown mode.
   
   
   ```
   [dldp unidirectional-shutdown](cmdqueryname=dldp+unidirectional-shutdown) { auto | manual }
   ```
   
   
   
   By default, **auto** is used.
   
   An interface in the Down state still sends RecoverProbe packets periodically. If the interface receives correct RecoverEcho packets, the unidirectional link changes to bidirectional and the interface becomes up.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * When the network performance is good, the automatic mode is recommended. When the network performance is poor, the DLDP packet reception is delayed, and a unidirectional link may be mistakenly detected in automatic mode. In this case, the manual mode is recommended. In this mode, the network administrator manually shuts down the interface, preventing packet receiving and sending from being affected by automatic interface shutdown.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
6. Enter the interface or interface group view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   [port-group](cmdqueryname=port-group) port-group-name
   ```
7. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch) 
   ```
   
   Determine whether to perform this step based on the current interface working mode.
8. Enable DLDP on an interface.
   
   
   ```
   [dldp enable](cmdqueryname=dldp+enable)
   ```
   
   By default, DLDP is disabled on an interface.
   
   If you enable DLDP in the interface group view, DLDP is enabled on all member interfaces of the interface group.
9. (Optional) Configure a DLDP-compatible mode.
   
   
   ```
   [dldp compatible-mode enable](cmdqueryname=dldp+compatible-mode+enable)
   ```
   
   If the links connecting two interfaces are cross-connected, the DLDP-compatible mode must be the same (enabled or disabled) on both interfaces.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display dldp**](cmdqueryname=display+dldp) [ **interface** *interface-type* *interface-number* ] command to check the DLDP configuration and neighbor entries.
* Run the [**display dldp statistics**](cmdqueryname=display+dldp+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics about DLDPDUs on all interfaces or a specific one.
* Run the [**display fwm dldp statistics**](cmdqueryname=display+fwm+dldp+statistics) [ **all** ] **slot** *slot-id* command in any view to check statistics about the DLDP module on a specified board.