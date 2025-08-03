Configuration Precautions for Eth-Trunk Interface
=================================================

Configuration Precautions for Eth-Trunk Interface

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The default weight of an Eth-Trunk member interface is 1, which can be modified through configuration. However, the modification changes the forwarding behavior of trunk interfaces. The hash operation is more likely to be performed on member interfaces with greater weight. The total weight of all member interfaces cannot exceed the maximum number of trunk member interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The user specification supported by an intra-board trunk interface is the same as the user specification supported on the board. The user specification supported by an inter-board trunk interface is the same as the minimum user specification supported on all member boards.  You are advised to ensure that the number of users on a trunk does not exceed the minimum user specification supported on all member boards. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In an Eth-Trunk in 1:N static LACP mode, the maximum number of member links in up state is set to 1. If the active link becomes down, its down event is not reported to the Eth-Trunk interface before a backup link becomes the active link. The down event of the original active link is reported to the Eth-Trunk interface only when either of the following conditions is met. This prevents route recalculation on the entire network caused by the Eth-Trunk interface down event.  1. The 60-second timer for reporting the down event expires.  2. The backup link fails and cannot go up.  The preceding description does not apply to scenarios where an Eth-Trunk in static LACP mode or E-Trunk is associated with VRRP. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Layer 2 Eth-Trunk interfaces support manual 1:1 active/standby mode. Layer 3 Eth-Trunk interfaces do not support manual 1:1 active/standby mode.  You are advised to plan the IP address properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When Eth-Trunk interfaces work in static LACP mode, the two devices forming an E-Trunk must be configured with the same LACP system ID and LACP priority. The Eth-Trunk interface status cannot be switched based on the status advertised by the E-Trunk. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |