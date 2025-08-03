(Optional) Configuring a User-Defined Group for Which Attack Defense Is Enabled
===============================================================================

You can determine whether an attack event or source exists by checking alarm information and attack event reports. After an attack source is confirmed, you can configure a user-defined group for which attack defense is enabled to isolate the attack source.

#### Context

If a device works abnormally (for example, a device encounters CPU overloads, logout, route interruption), you can configure a user-defined group for which attack defense is enabled to isolate the attack sources.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only when attack events or sources are confirmed, you can run the [**attack-defend user-enable-group**](cmdqueryname=attack-defend+user-enable-group) command to configure a user-defined group for which attack defense is enabled. After a user-defined group for which attack defense is enabled and specific protocols are defined in the user-defined group, when a protocol attack is detected, the system automatically delivers an attack defense policy.



#### Procedure

1. Check whether the alarm [**SOC\_1.3.6.1.4.1.2011.5.25.165.1.11.12 hwBaseSocAttackTrap**](cmdqueryname=SOC_1.3.6.1.4.1.2011.5.25.165.1.11.12+hwBaseSocAttackTrap) is generated. The alarm content includes the attack position, protocol type, sub-interface, and MAC address information.
2. If the alarm is generated, run the [**display soc attack-event**](cmdqueryname=display+soc+attack-event) **slot** *slot-id* command in any view to query more detailed information about the attack event on the board in a specific slot, such as the attack possibility, physical interface under attacks, VLAN, and attack cause (protocol flooding or broadcast storm).
3. Locate and isolate the attack source based on the obtained attack position and cause.
   1. If CPU overloads, severe service damage, or even service interruptions occur, shut down the interface under attack based on the attack position and attack packet information (MAC address, IP address, and protocol type) or run the [**blacklist acl**](cmdqueryname=blacklist+acl) command in the attack defense policy view to blacklist the attack packets and make adjustment based on live network situation.
   2. If CPU overloads occur but services run properly with a few packets being dropped, analyze the service deployment on the interface and check whether attack protocol packets are sent to the interface. If attack protocol packets are confirmed, blacklist the attack protocol and make adjustment based on live network situation.
   
   
   
   If services are restored and run properly later after the preceding operations, deliver an attack defense policy to apply the blacklist and interface or sub-interface shutdown actions to the forwarding plane.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If CPU overloads frequently occur due to device attacks, you can check service deployment on the interface under attack based on the port information of the attack event. If unexpected protocol packet loss is detected, run the [**attack-defend user-enable-group**](cmdqueryname=attack-defend+user-enable-group) command to configure a user-defined group for which attack defense is enabled and define the protocol in the group. After that, when the protocol packets are sent to attack the device again, an attack defense policy is automatically delivered to protect the CPU.