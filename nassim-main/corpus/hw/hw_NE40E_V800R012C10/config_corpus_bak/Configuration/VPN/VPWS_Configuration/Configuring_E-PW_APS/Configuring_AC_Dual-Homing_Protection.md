Configuring AC Dual-Homing Protection
=====================================

If a CE is dual-homed to two PEs, configure MC-LAG to implement AC dual-homing protection.

#### Context

In a scenario in which a CE is dual-homed to two PEs and the active/standby AC status needs to be determined by E-Trunk.


#### Procedure

1. Configure an Eth-Trunk interface.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
      
      
      
      An Eth-Trunk interface is created.
   3. (Optional) Run [**portswitch**](cmdqueryname=portswitch)
      
      
      
      The Eth-Trunk interface is switched to Layer 2 mode.
      
      
      
      This command is needed only on CEs. The Eth-Trunk sub-interfaces on PEs are the AC interfaces for PWs.
   4. Run [**mode lacp-static**](cmdqueryname=mode+lacp-static)
      
      
      
      The working mode of the Eth-Trunk interface is configured as the static LACP mode.
   5. (Optional) Run [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }
      
      
      
      The Eth-Trunk interface is configured to allow packets with specified VLAN tags to pass through.
      
      
      
      This command is needed only on CEs, and the specified VLANs must be configured on the CEs.
   6. Run [**trunkport**](cmdqueryname=trunkport) *interface-type interface-number*
      
      
      
      An interface is added to the Eth-Trunk interface.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**commit**](cmdqueryname=commit):
      
      
      
      The configuration is committed.
2. Configure E-Trunk.
   1. Run [**lacp e-trunk system-id**](cmdqueryname=lacp+e-trunk+system-id) *mac-address*
      
      
      
      An E-Trunk LACP system ID is configured.
      
      *mac-address* is in the format of H-H-H and cannot be all 0s or Fs.
      
      The LACP system IDs of the master and backup devices in an E-Trunk mechanism must be the same.
   2. Run [**lacp e-trunk priority**](cmdqueryname=lacp+e-trunk+priority) *priority*
      
      
      
      An E-Trunk LACP priority is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The LACP priorities of the master and backup devices in an E-Trunk mechanism must be the same.
   3. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      An E-Trunk mechanism is created.
   4. Run [**priority**](cmdqueryname=priority) *priority*
      
      
      
      *priority* is an integer ranging from 1 to 254. The default value is 100. The smaller the priority value, the higher the priority.
   5. Run [**peer-address**](cmdqueryname=peer-address) *peer-ip-address* **source-address** *source-ip-address*
      
      
      
      The local and peer IP addresses are configured.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   7. Run [**interface**](cmdqueryname=interface) **eth-trunk** *trunk-id*
      
      
      
      The Eth-Trunk interface view is displayed.
   8. Run [**e-trunk**](cmdqueryname=e-trunk) *e-trunk-id*
      
      
      
      The Eth-Trunk interface is added to the E-Trunk mechanism.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.