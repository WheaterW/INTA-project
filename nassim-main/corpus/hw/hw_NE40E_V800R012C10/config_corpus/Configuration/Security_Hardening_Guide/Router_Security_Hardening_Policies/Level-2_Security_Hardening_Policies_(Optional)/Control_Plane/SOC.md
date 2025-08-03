SOC
===

To ensure system reliability and protect services against attacks, the NE40E supports security techniques, such as rate limiting by committed access rate (CAR), attack detection, and attack defense. However, in absence of a global management center that can summarize and analyze all attack information, attack detection and defense are not comprehensive.

To address this problem, the security operating center (SOC) is developed to summarize and analyze information reported by all security detection modules in the system. Then the SOC presents attack event reports, attack sources, cause analysis, and solutions in a centralized and concise manner.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The SOC does not display information about minor attack events that affect only a function in the system. The SOC also does not display information about events that cause system breakdown by sending constructed malformed packets or a small number of packets to attack the system. Information about the events that cause system breakdown due to internal bugs is displayed by service modules, the NMS, the log function, and the attack source tracing function.

The SOC displays only information about attack events that cause system risks. These attack events typically have the following characteristics:

* CPU usage when such an attack event occurs is much higher than that in normal cases.
* The rate of packet loss caused by CPCAR exceeds a normal threshold.
* A protocol module detects a large number of invalid packets or sessions, and the percentage of the number of invalid packets or sessions to the total number of packets or sessions exceeds a normal threshold.


#### Attack Detection

Attack detection allows the SOC to determine whether the device is under attack based on the collected statistics.

The SOC is triggered by timers to collect the CPU usage, protocol modules' state data (including the numbers of invalid packets and sessions), and CPCAR-related packet loss statistics. After attack detection is enabled, when the CPU usage, the percentage of the number of invalid packets or sessions to the total number of packets or sessions, or the packet loss rate exceeds the attack detection threshold, the SOC determines that the device is being attacked and starts attack source tracing. If attack detection is not enabled, the SOC still collects statistics as triggered by timers, but does not determine an attack event or start attack source tracing.


#### Attack Source Tracing

Attack source tracing allows the SOC to locate an attack event and determine the probability and cause of the attack event.

If the device is identified under attack by attack detection, the SOC samples attack packets and collects and analyzes statistics about the sampled attack packets based on multiple criteria, such as the source MAC address, source IP address, broadcast packets, packets with varied source addresses, protocol type, VLAN, QinQ, physical interface, and logical interface information. The SOC then lists the top N packets based on each criterion, filters the attack-related objects based on the attack source tracing thresholds, and generates attack event reports as well as alarms.


#### Attack Defense

Attack defense allows the SOC to automatically deliver attack defense policies and discard attack packets, protecting the device against attacks.

After attack defense is enabled, the SOC classifies attack packets, summarizes attack packet characteristics, and then delivers ACL rules based on the characteristics. The ACL rules specify the attack packet characteristics, interfaces under attack, and the mapping between the ACL rules and CAR IDs.

The SOC counts the numbers of discarded packets and packets sent to the CPU in real time and cancels the ACL rule if the rate of discarding packets is less than the specified threshold.


[SOC Configuration Method and Procedure](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sec_enhance_1041.html)