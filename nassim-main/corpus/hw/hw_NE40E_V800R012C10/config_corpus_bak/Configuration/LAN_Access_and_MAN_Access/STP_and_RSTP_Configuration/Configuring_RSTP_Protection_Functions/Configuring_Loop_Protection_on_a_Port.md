Configuring Loop Protection on a Port
=====================================

The loop protection function suppresses the loops caused by link congestion.

#### Context

On a network running Rapid Spanning Tree Protocol (RSTP), a device maintains the root port status and status of blocked ports by receiving Bridge Protocol Data Units (BPDUs) from an upstream device. If the device cannot receive BPDUs from the upstream because of link congestion or unidirectional-link failure, the device re-selects a root port. The original root port becomes a designated port and the original blocked ports change to the Forwarding state. This may cause network loops. To address such a problem, configure loop protection.

After loop protection is configured, if the root port or alternate port does not receive BPDUs from the upstream device, the root port is blocked and the device notifies the NMS that the port enters the Discarding state. The blocked port remains in the Blocked state and no longer forwards packets. This prevents loops on the network. The root port restores the Forwarding state after receiving new BPDUs.

![](../../../../public_sys-resources/note_3.0-en-us.png) An alternate port is a backup port of a root port. If a device has an alternate port, you need to configure loop protection on both the root port and the alternate port.

Do as follows on a root port and an alternate port on a device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the root port or alternate port is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp loop-protection**](cmdqueryname=stp+loop-protection)
   
   
   
   Loop protection for the root port or the alternate port is configured on the device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.