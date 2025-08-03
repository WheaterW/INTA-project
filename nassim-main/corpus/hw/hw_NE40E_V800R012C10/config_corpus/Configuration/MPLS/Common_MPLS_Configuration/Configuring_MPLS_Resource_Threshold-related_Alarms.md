Configuring MPLS Resource Threshold-related Alarms
==================================================

MPLS resource threshold-related alarms can be configured on a device to enable the device to report an alarm if the number of MPLS resources of a specified type reaches the upper limit. The alarms facilitate operation and maintenance.

#### Usage Scenario

If the proportion of used MPLS resources, such as LSPs and dynamic labels to all supported ones reaches a specified upper limit, new MPLS services may fail to be established because of insufficient resources. To facilitate operation and maintenance, an upper alarm threshold of MPLS resource usage can be set. If MPLS resource usage reaches the specified upper alarm threshold, an alarm is generated.


#### Pre-configuration Tasks

Before configuring MPLS resource threshold-related alarms, configure basic MPLS functions.


[Configuring Alarm Thresholds for LDP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0012.html)

This section describes how to configure alarm thresholds for Label Distribution Protocol (LDP) label switched paths (LSPs).

[Configuring Alarm Thresholds for Dynamic Labels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0013.html)

This section describes how to set the dynamic label thresholds for triggering an alarm. If the number of dynamic labels that the system uses reaches a specific threshold, the system generates an alarm, which facilitates operation and maintenance.

[Configuring Conditions That Trigger LDP Resource Threshold-Reaching Alarms](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0014.html)

Conditions that trigger LDP resource threshold-reaching alarms can be configured. If the number of remote LDP adjacencies or the number of outsegment entries reaches a specified upper alarm threshold, the device can report an alarm to an NMS.

[Configuring Alarm Thresholds for other TE Resource](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0015.html)

Conditions that trigger TE resource threshold-reaching alarms can be configured. If the number of auto bypass tunnel interfaces, or the number of auto primary tunnels reaches the upper alarm threshold, the device can report an alarm, which facilitates operation and maintenance.

[Configuring Alarm Thresholds for RSVP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0016.html)

This section describes how to configure alarm thresholds for RSVP LSPs.