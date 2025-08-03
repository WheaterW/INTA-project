Overview of PFC Deadlock Prevention
===================================

Overview of PFC Deadlock Prevention

#### Overview

Priority-based Flow Control (PFC) deadlock prevention is a technology used to prevent PFC deadlocks.


#### Purpose

PFC is a traffic control technology that effectively prevents packet loss and serves as the basis for lossless networks. However, if congestion occurs on multiple devices simultaneously due to a loop or other causes, the interface buffer usage of each device exceeds the threshold for triggering PFC frames. In this case, these devices send PFC frames to each other and wait for each other to release resources. As a result, data flows on these devices are permanently blocked. This network state is known as the PFC deadlock state.

To solve the PFC deadlock problem, the device provides the PFC deadlock prevention function. This function identifies service flows that can easily cause PFC deadlocks and modifies the queue priority to prevent PFC deadlocks.