(Optional) Configuring Continuity Check on ATM Services
=======================================================

After ATM cell relay has been configured on an ATM interface or a logical interface whose link layer protocol is ATM, you can perform a continuity check on the ATM services.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.


Before performing a continuity check on ATM services, you must complete the following tasks:

1. Check that the physical layer status and protocol layer status of the interface on which the continuity check is to be performed are both Up. If the interface is a synchronous serial interface, configure ATM as the link layer protocol for the interface.
2. Configure a PVC or PVP on the interface.
3. Configure the end-point attribute for the connection point of the PVC or PVP on the device that initiates the continuity test.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**llid**](cmdqueryname=llid) *llid-number*
   
   
   
   An LLID is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **LLID** command must be configured both on the local and remote devices.
3. Run **[**test connectivity**](cmdqueryname=test+connectivity) **interface**** { **interface-type** **interface-number** | **interface-name**} { ****pvc**** **vpi/vci** |****pvp**** **vpi**} ****llid**** **llid-value**
   
   
   
   A continuity check is performed on ATM services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.