Configuring the Sticky DR Function
==================================

The sticky DR function keeps the role of the device that is elected as the DR unchanged.

#### Context

In PIM-SM, DRs need to be elected on a shared network segment. They are responsible for the registering of the local multicast source or the joining of receivers. The Routers exchange Hello messages carrying DR priorities to elect DRs. Each time the priority of a device on a network segment changes or a device joins or leaves a network segment, a DR election is performed again. As a result, the multicast forwarding paths may change frequently.

If all the devices on a network segment support Hello messages carrying DR priorities and are configured with the sticky DR function and a device is elected as a DR, the DR priority of this device changes to the sticky DR priority (4294967294, which is a pretty large value considering that the DR priority ranges from 0 to 4294967295). This prevents frequent DR role changes, which would otherwise cause traffic loss. You are advised to configure the sticky DR function on all Routers on the same network segment.

* After the sticky DR function is enabled on a Router, the DR priority cannot be set to a value greater than or equal to 4294967294.
* If the DR priority configured for a Router is greater than or equal to 4294967294, the sticky DR function cannot be enabled.
* The interface with the highest IP address on a Router is elected as a DR as long as one Router on the same network segment does not support Hello messages carrying DR priorities.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sticky-dr**](cmdqueryname=pim+sticky-dr)
   
   
   
   The sticky DR function is configured on the Router.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.