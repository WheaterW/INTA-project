Establishing a NETCONF Session
==============================

In a NETCONF session, the device functions as a NETCONF server, and the third-party NMS functions as a NETCONF client.

#### Establishing a NETCONF Session in CLI Mode

**A NETCONF client proactively establishes a NETCONF session with a NETCONF server.**

Configure an SSH user on a NETCONF server (device), enable NETCONF, and wait for a NETCONF client to trigger the establishment of a NETCONF session. The NETCONF client uses the SSH username and password configured on the device to establish a NETCONF connection with the device.

**A NETCONF server proactively establishes a NETCONF session with a NETCONF client.**

If an NMS does not support automatic device discovery, it cannot manage devices as soon as they go online. In this case, the NETCONF server (device) must proactively establish a NETCONF session with the NETCONF client (NMS). You can enable proactive NETCONF registration on the device to enable the device to proactively establish a NETCONF session with the NMS.

**Figure 1** Establishing a NETCONF session between a device and an NMS by enabling proactive NETCONF registration  
![](figure/en-us_image_0000001676562957.png "Click to enlarge")

1. Configure an SSH user and enable NETCONF and proactive NETCONF registration on a device.
2. The device proactively establishes a NETCONF session with the NMS.