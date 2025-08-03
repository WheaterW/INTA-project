STP/RSTP/MSTP Timers
====================

Hello Time, Forward Delay, Max Age, and Message Age are four time-related fields carried in BPDUs, of which Hello Time, Forward Delay, and Max Age are timers with default values of 2 seconds, 15 seconds, and 20 seconds, respectively. These timers can be manually configured for devices.

#### Hello Time Timer and Timeout Period

Hello Time specifies the interval at which BPDUs are sent. A device sends BPDUs at the specified interval to detect link failures. A device recalculates the spanning tree if it does not receive any BPDUs from upstream devices within the timeout period, which is calculated according to the formula below. Note that the default value of Timer Factor is 3, and this value can be manually configured for a device to adjust the timeout period.

Timeout period = Hello Time Ã 3 Ã Timer Factor

After the network topology becomes stable, the new value of the Timer Factor takes effect only when a new root bridge is elected. The new root bridge adds the new timeout period value in BPDUs it sends to non-root bridges. When the network topology changes, TCN BPDUs are transmitted immediately, without waiting for the time period to expire.


#### Forward Delay Timer

Forward Delay specifies the time during which a port waits before transitioning between states after a link fails. When a link fails, spanning tree calculation is triggered and the spanning tree structure changes. However, because it takes some time for the new configuration BPDUs to spread throughout the entire network, if the new root port and designated port start to forward data immediately, transient loops may occur. Therefore, spanning tree protocols define the Forward Delay to provide a port state transition delay mechanism. The newly selected root port and designated port must wait for two Forward Delay intervals before transitioning to the Forwarding state. This provides enough time to transmit new configuration BPDUs over the network, preventing transient loops.

The Forward Delay value is 15s by default. This means that the port stays in the Listening state for 15s and then in the Learning state for another 15s before finally transitioning to the Forwarding state. The port does not forward user traffic when it is in the Listening or Learning state, which is key to preventing transient loops.


#### Max Age Timer and Message Age

Max Age specifies the aging time of BPDUs. This parameter can be configured on the root bridge using commands.

BPDUs are sent to ensure that the entire network uses the same Max Age value. Specifically, after a non-root bridge receives a configuration BPDU, it compares the Message Age value with the Max Age value before deciding whether to forward or discard the configuration BPDU. The details are as follows:

* If the Message Age value is less than or equal to the Max Age value, the non-root bridge forwards the configuration BPDU.
* If the Message Age value is larger than the Max Age value, the configuration BPDU is aged out and the non-root bridge discards the configuration BPDU. In this case, the network diameter is considered too large and the non-root bridge disconnects from the root bridge.

The following uses configuration BPDUs as an example (RST BPDUs and MST BPDUs work in a similar way). If the configuration BPDU is sent from the root bridge, the Message Age value is 0. Otherwise, the value of Message Age is the total time spent to transmit the BPDU from the root bridge to the local bridge, including the transmission delay. In real-world situations, the Message Age value of a configuration BPDU is incremented by 1 each time the configuration BPDU passes through a bridge.

As shown in [Figure 1](#EN-US_CONCEPT_0000001292398344__fig617513574117):

* DeviceB and DeviceC receive a configuration BPDU from DeviceA with a Message Age value of 0. The aging time of the BPDU is set to (Max Age - 0) on the ports connecting DeviceB and DeviceC to DeviceA.
* DeviceD and DeviceE receive a configuration BPDU from DeviceB with a Message Age value of 1. The aging time of the BPDU is set to (Max Age - 1) on the ports connecting DeviceD and DeviceE to DeviceA.
* DeviceF receives a configuration BPDU from DeviceE with a Message Age value of 2. The aging time of the BPDU is set to (Max Age - 2) on the port connecting DeviceF to DeviceA.

**Figure 1** Message Age  
![](figure/en-us_image_0000001345478669.png)