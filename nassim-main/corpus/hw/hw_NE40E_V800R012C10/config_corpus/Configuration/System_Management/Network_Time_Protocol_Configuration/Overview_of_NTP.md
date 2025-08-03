Overview of NTP
===============

This section introduces applications of NTP.

The Network Time Protocol (NTP) is an application layer protocol in the TCP/IP protocol suite. NTP synchronizes clocks of all devices on a network so that the devices can implement applications based on the uniform time.

Any local system that runs NTP can synchronize clocks from other clock sources, and also functions as a clock source to synchronize other clocks. In addition, mutual synchronization can be performed by exchanging NTP packets.

NTP packets are transmitted over UDP, using port 123.

#### NTP Application

NTP is applied in the following situations where all the clocks of hosts or Routers in a network need to be consistent:

* Network management: Analysis on logs or debugging information collected from different Routers must be performed based on time.
* Charging system: Requires the clocks of all devices to be consistent.
* Completing certain functions: For example, timing restart of all the Routers in a network requires the clocks of all the Routers to be consistent.
* Several systems working together on the same complicate event: Systems have to take the same clock for reference to ensure a proper sequence of implementation.
* Incremental backup between the backup server and clients: Clocks on the backup server and clients must be synchronized.

When all the devices on a network need to be synchronized, it is almost impossible for an administrator to manually change the system clock by executing commands. This is because the work load is heavy and clock accuracy cannot be ensured. NTP can quickly synchronize the clocks of network devices and ensure their precision.

NTP has the following advantages:

* Defining clock accuracy by means of stratum to synchronize the time of network devices in a short time
* Supporting access control and HMAC-SHA256 authentication
* Transmitting packets in unicast, multicast or broadcast mode