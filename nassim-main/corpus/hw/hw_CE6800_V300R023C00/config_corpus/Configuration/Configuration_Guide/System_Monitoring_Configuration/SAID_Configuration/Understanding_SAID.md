Understanding SAID
==================

Understanding SAID

#### SAID Node

A SAID node is a function node that is used by the SAID system to perform fault detection, diagnosis, and rectification. SAID nodes are classified into the following types:

* Diagnostic SAID node: With this node, the SAID system only determines whether the device is faulty based on the collected data, without rectifying faults.
* Self-healing SAID node: With this node, the SAID system determines whether the device is faulty based on the collected data and automatically rectifies faults.


#### SAID Detection Process

After the device completes the startup, the SAID system periodically performs fault detection. The process consists of the following tasks:

1. Data obtaining: The SAID system periodically collects detection data based on the detection period registered by an SAID node.
2. Data diagnosis: The SAID system sends the collected detection data to service modules for diagnosis. If the data indicates a fault, the system processes the data based on the SAID node type.
3. Troubleshooting: If the SAID node is a diagnostic node, the SAID system only records a log or reports an alarm, without performing self-healing. If the SAID node is a self-healing node, the SAID system instructs the service module to perform fault self-healing. After self-healing is complete, the SAID system records a log indicating that self-healing is complete.