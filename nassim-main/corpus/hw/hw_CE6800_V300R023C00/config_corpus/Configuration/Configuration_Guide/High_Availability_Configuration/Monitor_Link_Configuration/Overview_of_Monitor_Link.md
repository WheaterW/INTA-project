Overview of Monitor Link
========================

Overview of Monitor Link

#### Definition

Monitor Link is an interface association mechanism that monitors the uplink interface in a Monitor Link group and synchronizes the status of downlink interfaces in the group with the uplink interface status. Monitor Link triggers a Layer 2 topology protocol on a downstream device to perform a link switchover.


#### Purpose

If an uplink fails on a network where a Layer 2 topology protocol is deployed, the downstream device cannot detect the link failure. As a result, the topology protocol cannot perform a link switchover. Monitor Link monitors an uplink interface and synchronizes the downlink interface status with the uplink interface status. If the uplink fails, Monitor Link notifies the downstream device of the failure, triggering the topology protocol on the downstream device to perform a link switchover. This prevents packet loss arising from an uplink failure.