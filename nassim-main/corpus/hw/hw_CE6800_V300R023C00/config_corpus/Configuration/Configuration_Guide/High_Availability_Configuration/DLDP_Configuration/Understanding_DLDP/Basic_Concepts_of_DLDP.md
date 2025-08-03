Basic Concepts of DLDP
======================

Basic Concepts of DLDP

#### Types of DLDPDUs

DLDP allows a device to identify the remote device and detect whether a unidirectional link exists by exchanging DLDP Data Units (DLDPDUs) with the remote device. [Table 1](#EN-US_CONCEPT_0000001415015958__tab_dc_vrp_dldp_cfg_200201) shows the types of DLDPDUs.

**Table 1** Types of DLDPDUs
| Type | Description |
| --- | --- |
| Advertisement packet | Used to maintain a DLDP connection. |
| Probe packet | Used to probe a remote device. |
| Echo packet | Used to respond to Probe packets. |
| RecoverProbe packet | Used to detect whether a unidirectional link has been restored to bidirectional. |
| RecoverEcho packet | Used to respond to RecoverProbe packets. |
| Disable packet | Used to disable a unidirectional link so that the DLDP-enabled interface enters the Disable state. |
| Flush packet | Used to instruct the remote device to delete neighbor entries. |
| LinkDown packet | Used to notify the remote device of interface down events. |
| Advertisement packet with RSY tags | Sent when a DLDP neighbor entry is created or a neighbor disappears. |



#### DLDP States

DLDP allows a device to identify the remote device and detect whether a unidirectional link exists by exchanging DLDPDUs with the remote device. As shown in [Table 2](#EN-US_CONCEPT_0000001415015958__table568994513119), DLDP defines the following states: Initial, Inactive, Active, Advertisement, Probe, Disable, DelayDown, and Loop.

**Table 2** DLDP states
| State | Description |
| --- | --- |
| Initial | DLDP is disabled. |
| Inactive | DLDP is enabled but the link is down. |
| Active | DLDP is enabled and the link is up, or neighbor entries are deleted. |
| Advertisement | All neighbors are bidirectionally reachable or have been in the Active state for more than 5 seconds. This is a stable state when no unidirectional link has been detected. |
| Probe | Probe packets are sent to detect whether the link is unidirectional. When an interface enters this state, DLDP starts the Probe timer and an Echo timer for each neighbor to be detected. |
| Disable | When DLDP in enhanced mode detects a unidirectional link, the interface that fails to send optical signals enters the Disable state. |
| Delaydown | When a DLDP-enabled interface is in the Active, Advertisement, or Probe state, it does not delete the neighbor entry or switch to the Inactive state immediately after detecting an interface down event. Instead, the interface enters the DelayDown state. Interfaces in the DelayDown state retain DLDP neighbor entries and only respond to interface up events. |
| Loop | An interface enters the Loop state when both ends of an optical fiber are inserted in the same optical module, with one end in Rx and the other in Tx. |



#### Working Modes of DLDP

DLDP is used to detect unidirectional links caused by cross-connected optical fibers or a disconnected or broken optical fiber in a pair.

DLDP works in one of two modes depending on the type of unidirectional links:

* Normal mode: DLDP detects only the unidirectional links caused by cross-connected optical fibers.
* Enhanced mode: DLDP detects the unidirectional links caused by cross-connected optical fibers or a disconnected or broken optical fiber in a pair.