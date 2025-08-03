Disabling a Device from Emptying a MAC Address Queue
====================================================

Disabling_a_Device_from_Emptying_a_MAC_Address_Queue

#### Context

A device needs to learn MAC addresses after being added to a Layer 2 network. When MAC address entries are deleted automatically through associating with other modules or deleted manually, a device empties the MAC address queue by default. During the emptying process, the device cannot learn new MAC addresses. To allow the device to learn new MAC addresses and at the same time delete unneeded MAC addresses, disable the device from emptying the MAC address queue.

After a device is disabled from emptying a MAC address queue, the MAC addresses in the queue may fail to be deleted. To allow a device to delete the dynamic MAC address entries, run the [**reset mac-address**](cmdqueryname=reset+mac-address) command on the device.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**mac-address queue-emptying disable**](cmdqueryname=mac-address+queue-emptying+disable) command to disable the device from emptying a MAC address queue.
   
   
   
   In VS mode, this command is supported only by the admin VS.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.