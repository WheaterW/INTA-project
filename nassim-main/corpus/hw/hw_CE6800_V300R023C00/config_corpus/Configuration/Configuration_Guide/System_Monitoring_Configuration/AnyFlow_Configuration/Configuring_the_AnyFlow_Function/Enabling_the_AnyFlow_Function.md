Enabling the AnyFlow Function
=============================

Enabling the AnyFlow Function

#### Context

After AnyFlow is enabled on a device, the device creates flow entries for all TCP, UDP, VXLAN, and RoCEv2 traffic entering the device based on fields such as 5-tuple in order to collect traffic statistics and detect abnormal traffic.

To monitor specified TCP, UDP, VXLAN, and RoCEv2 traffic, configure the modular QoS command line interface (MQC). Packets are matched based on the 5-tuple. The common matching rules are as follows:

* Rule 1: TCP + destination IPv4 or IPv6 address
* Rule 2: TCP + destination IPv4 or IPv6 address + destination TCP port number
* Rule 3: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address
* Rule 4: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + destination TCP port number
* Rule 5: UDP + destination IPv4 or IPv6 address
* Rule 6: UDP + destination IPv4 or IPv6 address + destination UDP port number
* Rule 7: UDP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address
* Rule 8: UDP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + destination UDP port number
* Rule 9: TCP + all (matching all TCP packets)
* Rule 10: UDP + all (matching all UDP packets)
* Rule 11: destination QP field of RoCEv2 packets
* Rule 12: destination QP field of RoCEv2 packets + source IPv4 or IPv6 address
* Rule 13: destination QP field of RoCEv2 packets + destination IPv4 or IPv6 address
* Rule 14: destination QP field of RoCEv2 packets + source IPv4 or IPv6 address + destination IPv4 or IPv6 address

When a rule (destination QP field of RoCEv2 packets + IPv6 address) is matched, only the most significant 64 bits of the IPv6 address can be matched.

Perform either of the following configurations.


#### Procedure

* Monitor all TCP, UDP, VXLAN, and RoCEv2 traffic.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the AnyFlow view.
     
     
     ```
     [any-flow](cmdqueryname=any-flow)
     ```
  3. Enable the AnyFlow function.
     
     
     ```
     [enable](cmdqueryname=enable)
     ```
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Monitor specified TCP, UDP, VXLAN, and RoCEv2 traffic.
  
  
  
  To use MQC to monitor specified TCP, UDP, VXLAN, and RoCEv2 traffic, you must define the **any-flow enable** action in the MQC traffic behavior.
  
  
  
  1. Configure a traffic classifier.
  2. Configure a traffic behavior.
     
     
     1. Create a traffic behavior.
        ```
        [traffic behavio](cmdqueryname=traffic+behavio)r behavior-name
        ```
     2. Define an action in the traffic behavior to enable the AnyFlow function.
        ```
        [any-flow enable](cmdqueryname=any-flow+enable)
        ```
     3. Exit the traffic behavior view.
        ```
        [quit](cmdqueryname=quit)
        ```
     4. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
  3. Configure a traffic policy.
  4. Apply the traffic policy globally.
  
  
  
  For details, see "Configuring MQC-based Packet Filtering" in Configuration Guide > QoS Configuration.