Overview of Port Security
=========================

Overview of Port Security

#### Definition

Port security converts the dynamic MAC addresses learned on an interface into secure MAC addresses.


#### Purpose

When unauthorized users acquire an interface's MAC address, they may use this address as a destination MAC address to communicate with the device, initiating attacks.

To prevent such attacks, a device can enable port security to convert the dynamic MAC addresses learned on an interface into secure MAC addresses. After port security is enabled, dynamic MAC address entries that have been learned on the interface are deleted. When the number of MAC addresses learned again by the interface reaches the limit, the interface stops learning MAC addresses. If an interface receives packets whose source MAC address is not in the MAC address entries, these packets are considered unauthorized. Then the actions including discarding the packets, reporting alarms, or shutting down the interface are performed.