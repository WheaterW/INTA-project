Configuring the Limit on the Number of Access Users
===================================================

You can limit the number of access users to control the user access rate and prevent threshold-crossing CPU usage.

#### Context

Perform the following steps on the device for network access:

In the following user access limit configuration, perform the steps based on service requirements.


#### Procedure

* Limiting the number of users who go online from a single VLAN
  
  
  
  If the number of online users in a single VLAN exceeds 3K, run the [**vlan-host-car**](cmdqueryname=vlan-host-car) command to increase the bandwidth for the user-side packets that are sent to the CPU and carry the same VLAN ID. After the configuration is complete, the packets of excess users are discarded, and these users are logged out.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  1. The device supports CAR rate limiting to prevent a large number of user-side packets from compromising the CPU processing efficiency. By default, the CAR function is enabled, or default parameter values are available. For configuration details, see *Configuring CAR*.
* Limiting PPP user access
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ppp-user-slot-warning-threshold**](cmdqueryname=ppp-user-slot-warning-threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of PPP users who go online from a service board is configured. If the proportion of the number of PPP users who go online from the board to the total number of access users exceeds the threshold, an alarm is generated.
  3. Run [**ppp-user-warning-threshold**](cmdqueryname=ppp-user-warning-threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of PPP users who go online from the device is configured. If the proportion of the number of PPP users who go online from the NE40E to the total number of access users exceeds the threshold, an alarm is generated.
  4. Run [**ppp connection chasten**](cmdqueryname=ppp+connection+chasten) **option105** *request-sessions* *request-period* *blocking-period* [ **padi-discard** ] [ **quickoffline** ] or [**ppp connection chasten**](cmdqueryname=ppp+connection+chasten) *request-sessions* *request-period* *blocking-period* [ **padi-discard** ] [ **quickoffline** ] [ **multi-sessions-permac** ]
     
     
     
     The number of PPP user access requests is limited.
     
     
     
     Limiting the number of access attempts can prevent unauthorized users from using a brute force attack to crack the password of an authorized user. If a user fails to pass the authentication for N times during a specified period, the user account is frozen for a period of time, thwarting unauthorized users' efforts in cracking the password of the authorized user.
     
     In a scenario in which a large number of users go offline immediately after they go online, the CPU may be overloaded and the RADIUS server may even go down. To prevent this problem, you can configure the **quickoffline** parameter to limit the number of times a PPP user can go offline immediately after the user goes online within a specified period. If the PPP user immediately goes offline after going online *request-sessions* times within *request-period*, the user account is blocked for *blocking-period* seconds.
     
     In the system view, this command takes effect on all users who go online from the NE40E. In the VLAN view, the command takes effect only on the users who go online from the interface where the VLAN resides. If this command is run in both the system and VLAN views, the command that first meets the restriction condition takes effect.
  5. Run [**pppoe-server**](cmdqueryname=pppoe-server) *slot-number* **max-sessions** *session-number*
     
     
     
     The maximum number of users allowed to go online from an interface board is configured.
  6. Run [**pppoe-server max-sessions remote-mac**](cmdqueryname=pppoe-server+max-sessions+remote-mac) *session-number* [ **with-check-location** [ **padi-mac-check** ] ]
     
     
     
     The maximum number of users allowed to go online when one MAC address is used for access from different physical locations is configured. Only one access user is allowed at the same physical location.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the [**pppoe-server max-sessions remote-mac**](cmdqueryname=pppoe-server+max-sessions+remote-mac) command is run to set the maximum number of users allowed to go online based on one MAC address to be greater than 1, if **option105** is not specified in the [**ppp connection chasten**](cmdqueryname=ppp+connection+chasten) command, the function of limiting the number of PPP user access requests based on MAC addresses does not take effect. For this function to take effect, specify the **multi-sessions-permac** parameter. If **option105** is specified in the [**ppp connection chasten**](cmdqueryname=ppp+connection+chasten) command, the function of limiting the number of PPP user access requests based on Option 105 still takes effect.
     
     After running the [**pppoe-server max-sessions remote-mac**](cmdqueryname=pppoe-server+max-sessions+remote-mac) *session-number* command, you can also allow multiple users to access the network based on one MAC address. In this case, however, physical location information is not checked.
  7. Run [**pppoe-server same-user forbid**](cmdqueryname=pppoe-server+same-user+forbid)
     
     
     
     The device is enabled to deny a PPPoE user's login request if another PPPoE user having the same MAC address has gone online from the same physical location when each MAC address maps a unique session.
  8. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  9. Run [**ppp username check**](cmdqueryname=ppp+username+check)
     
     
     
     The device is configured to check whether a PPP user access request contains a username and to deny the request if it does not contain a username.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Limiting the number of IP addresses for PPP users
  
  
  
  A user can access the device through multiple links. If the number of IP addresses of PPP users attempting to access the network reaches the threshold specified for a BAS interface or board, the BAS interface or board does not respond to the PADO packets sent by PPP users and no more PPP users can access the BAS interface or board. In this case, PPP users can go online only through other interfaces or boards. This achieves load balancing among different interfaces and boards.
  
  The configured access limit is the limit on the number of IP addresses of PPP users. This configuration applies only to PPPoE and L2TP users. A single-stack user is counted as one user, and a dual-stack user is counted as two users. When the number of IP addresses of PPP users attempting to access the network from a BAS interface or board reaches the threshold specified, the BAS interface or board stops responding to the PADO packets sent by PPP users and no more PPP users can access the BAS interface or board.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**access-ip-limit**](cmdqueryname=access-ip-limit) *max-number* **user-type ppp**
     
     
     
     The maximum number of IP addresses for PPP users allowed to access the network from a specified board is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  6. Run [**bas**](cmdqueryname=bas)
     
     
     
     A BAS interface is created, and its view is displayed.
  7. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **bas-interface-name** *name* | **default-domain** { **pre-authentication** *domain-name* | **authentication** [ **force** | **replace** ] *domain-name* } \* | **accounting-copy radius-server** *radius-name* ] \*
     
     
     
     The access type and related attributes are configured for Layer 2 common users.
  8. Run [**access-ip-limit**](cmdqueryname=access-ip-limit) *max-number* **user-type ppp** [ **exclude** ]
     
     
     
     The maximum number of IP addresses for PPP users allowed to access the network from a specified BAS interface is configured. If the number of PPP users who access the network from a BAS interface reaches the maximum number of IP addresses for PPP users allowed to access the network from a board, the BAS interface stops responding to the PADO packets sent by subsequent PPP users. However, this restriction does not apply to BAS interfaces configured with the **exclude** parameter.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limiting the number of user access packets
  
  
  
  When a large number of ARP/IPv4/IPv6/ND packets are sent to launch attacks or unauthorized clients send requests continuously, the CPU usage of the main control board becomes high. In this case, you can limit the number of users on a board within a specified period so that excess packets are discarded.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**access trigger packet-limit**](cmdqueryname=access+trigger+packet-limit) *packets-num* **time** *seconds* [ **all** ]
     
     
     
     The maximum number of user packets that are allowed to pass through a specified board within a specified period is configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limiting DHCP user access
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp-user-slot-warning-threshold**](cmdqueryname=dhcp-user-slot-warning-threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of DHCP users who go online from a service board is configured. If the proportion of DHCP users accessing the board exceeds the threshold, an alarm is generated.
  3. Run [**dhcp-user-warning-threshold**](cmdqueryname=dhcp-user-warning-threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of DHCP users who go online from the device is configured. If the proportion of DHCP users accessing the NE40E exceeds the threshold, an alarm is generated.
  4. Run [**dhcp connection chasten**](cmdqueryname=dhcp+connection+chasten) { [**authen-packets**](cmdqueryname=authen-packets) *authen-packets* | **request-packets** *request-packets* } \* **check-period** *check-period* **restrain-period** *restrain-period* [ **slot** *slotid* ]
     
     
     
     A limit is configured for DHCP access users.
     
     
     
     + You can run the [**display dhcp chasten-user**](cmdqueryname=display+dhcp+chasten-user) **slot** *slotid* [ **mac-address** *mac-address* ] [ **state** { **restrain** | **check** } ] command to check information about DHCP access users for whom a limit is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limiting the number of users who go online from a board
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot-warning-threshold**](cmdqueryname=slot-warning-threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of users who go online from a board is configured. If the proportion of users accessing the board exceeds the threshold, an alarm is generated.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limiting the access response delay
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-delay step**](cmdqueryname=access-delay+step) *step-value* **minimum** *minimum-time* **maximum** *maximum-time* [ **slot** *slot-id* ]
     
     
     
     The user access response delay function is enabled, and the maximum and minimum access response delays are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the access response delay function is enabled both globally and on a BAS interface, the configuration on the BAS interface takes effect.
     
     The access response delay depends on the number of access users and the configured parameters including the step, maximum access response delay, and minimum access response delay. The access response delay is the rounded-down value obtained by dividing the number of access users by the step plus the minimum access response delay. Compare the calculated access response delay (assuming the value is N) with the maximum access response delay:
     
     + If N is less than or equal to the maximum access response delay, the access response delay is N multiplying 10 ms.
     + If N is greater than the maximum access response delay, the access response delay is the maximum access response delay multiplying 10 ms.
     
     An example assumes that the step is 3000, the maximum access response delay is 7, and the minimum access response delay is 3. The delay for access users numbered 0 to 2999 is 3 x 10 ms, the delay for access users numbered 3000 to 5999 is 4 x 10 ms, the delay for access users numbered 6000 to 8999 is 5 x 10 ms, the delay for access users numbered 9000 to 11999 is 6 x 10 ms, and the delay for access users numbered 12000 and later is 7 x 10 ms.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. (Optional) Run [**access delay load-balance**](cmdqueryname=access+delay+load-balance) **group** *group-name* [ *delay-time* ]
     
     
     
     A load balancing group is configured for user access.
     
     
     
     If two devices
     with the same configuration are deployed, users can go online from
     any of the two devices that work in master/backup mode. If load balancing
     groups are configured on both the master and backup devices, run the **access delay load-balance** **group** *group-name* *delay-time* command to configure
     a response delay policy for the load balancing group on the backup
     device. In this way, even if an interface on the backup device is
     selected in a Hash operation, the interface will not respond to user
     login requests until the time specified by *delay-time* elapses. This ensures that users go online preferentially through an interface
     on the master device. Users will go online through an interface on the backup device
     only when the master device is faulty.
  6. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  7. Run [**bas**](cmdqueryname=bas)
     
     
     
     A BAS interface is created, and its view is displayed.
  8. (Optional) Run [**access-delay**](cmdqueryname=access-delay) *delay-time* **load-balance-group** *group-name*
     
     
     
     The interface that requires load balancing is added to the load balancing group. The interfaces in the same load balancing group determine the access response delay based on the hash result of user MAC addresses, achieving inter-board load balancing.
     
     
     
     If the access response delay is not configured for a load balancing group:
     
     + If the interface through which users go online is selected in a Hash operation, the interface immediately responds to the received login requests.
     + If the interface through which users go online is not selected in a Hash operation, the interface responds to the received login requests after the delay time configured for the BAS interface elapses.If the access response delay is configured for a load balancing group:
     + If the interface through which users go online is selected in a Hash operation, the interface responds to the received login requests after the delay time configured for the load balancing group elapses.
     + If the interface through which users go online is not selected in a Hash operation, the interface responds to the received login requests after the delay time configured for the load balancing group plus the delay time configured for the BAS interface elapses.
  9. (Optional) Run [**access-delay**](cmdqueryname=access-delay) *delay-time* [ **circuit-id-include** *text-value* | **even-mac** | **odd-mac** ]
     
     
     
     An access response delay policy is configured on the BAS interface.
     
     
     
     If **circuit-id-include** is specified, you must run the [**client-option82**](cmdqueryname=client-option82) command in the BAS interface view to configure the device to trust the DHCP Option 82 field (for a DHCP user) or the PPPoE+ field (for a PPP user) for the response delay to take effect.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. (Optional) Run [**access delay load-balance algorithm enhance**](cmdqueryname=access+delay+load-balance+algorithm+enhance) **enable**
      
      
      
      The enhanced load balancing algorithm is enabled.
      
      To configure the frequency for updating the preferred access interface in the load balancing group, run the [**access delay load-balance algorithm enhance**](cmdqueryname=access+delay+load-balance+algorithm+enhance) **update-frequency** *update-frequency* command.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Currently, this command applies only to PPPoE users.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Limiting user packets of a specified type
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**access packet strict-check**](cmdqueryname=access+packet+strict-check) { **all** | { **nd** | **dhcpv6** | **dhcp** | **ppp** | **l2tp** | **dot1x** } \* }
     
     
     
     The device is configured to strictly check user packets of a specified type.
     
     
     
     Even if the destination MAC address of the packets sent by a user is not the MAC address of the BAS interface, the user may still receive a response. To prevent the device from being affected by malicious attacks, run this command to configure strict check on the user packets so that the packets that do not comply with the standard protocol are discarded.
     
     Additionally, if terminal devices do not strictly comply with the standard protocol, the involved users may not log in. Therefore, exercise caution when running this command.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to dynamically adjust the number of access users based on the system status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment system-state**](cmdqueryname=access-speed+adjustment+system-state) **enable** [ **strict-check** ]
     
     
     
     The device is configured to adjust the user access rate based on the system status.
  4. Run [**access-speed adjustment system-state threshold**](cmdqueryname=access-speed+adjustment+system-state+threshold) { **main-cpu-usage** | **main-memory-usage** | **access-queue** | **slot-cpu-usage** | **slot-memory-usage** | **ppp-cpcar-drop** | **ppp-receive-queue** | **pppoe-receive-queue** | **l2tp-queue** | **dhcp-slot-queue** | **fes-queue** | [**lns-cpcar-drop**](cmdqueryname=lns-cpcar-drop) | [**dhcp-server-queue**](cmdqueryname=dhcp-server-queue) | [**dhcpv6-server-queue**](cmdqueryname=dhcpv6-server-queue) | **[**eap-cpcar-drop**](cmdqueryname=eap-cpcar-drop)** | **queue-delay** } **alarm** *alarm-threshold-value* **resume** *resume-threshold-value*
     
     
     
     The system status threshold for decreasing the user access rate and the threshold for restoring the user access rate are configured.
  5. Run [**access-speed adjustment system-state user-type**](cmdqueryname=access-speed+adjustment+system-state+user-type) { { **dhcp** | **pppoe** | **ipv4-trigger** | **ipv6-trigger** | **dot1x** } \* | **none** }
     
     
     
     The user type for which the device adjusts the user access rate based on the system status is configured.
  6. Run [**access-speed adjustment system-state time**](cmdqueryname=access-speed+adjustment+system-state+time) **interval** *adjust-interval* **delay-count** *adjust-delay-count* [ **slot** ]
     
     
     
     An interval at which the user access rate is adjusted based on the system status and the minimum number of delay periods for increasing the user access rate are configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to adjust the UM message queue threshold based on the system status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment system-state threshold access-queue**](cmdqueryname=access-speed+adjustment+system-state+threshold+access-queue) **length** *length-value*
     
     
     
     The device is configured to adjust the threshold for the UM message queue usage based on the system status. When the UM message queue usage reaches the threshold, the CPCAR value is decreased or increased as required to control the number of user packets to be sent to the CPU.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to adjust the rate at which ARP/IP/IPv6/ND packets that trigger user login are sent to the CPU based on the system status.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment system-state packet-limit trigger enable**](cmdqueryname=access-speed+adjustment+system-state+packet-limit+trigger+enable)
     
     
     
     The device is enabled to adjust the rate at which ARP/IP/IPv6/ND packets that trigger user login are sent to the CPU based on the system status.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to preferentially allocate CPU resources to online users.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment edsg-queue enable**](cmdqueryname=access-speed+adjustment+edsg-queue+enable)
     
     
     
     The device is enabled to preferentially allocate CPU resources to online users. In this case, EDSG services enter the activation queue and are not activated immediately.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to generate an alarm when the user resource usage or CPU usage exceeds a specified threshold and to clear the alarm when the user resource usage or CPU usage falls below the threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**access-user exhaust warning enable**](cmdqueryname=access-user+exhaust+warning+enable)
     
     
     
     The device is configured to generate an alarm when the user resource usage or CPU usage reaches a specified threshold and to clear the alarm when the user resource usage or CPU usage falls below the threshold.
  3. Run [**access-user exhaust threshold-alarm**](cmdqueryname=access-user+exhaust+threshold-alarm) { **main-resource-usage** | **slot-resource-usage** | **main-cpu-usage** | **slot-cpu-usage** } **upper-limit** *upper-limit* **lower-limit** *lower-limit*
     
     
     
     The alarm threshold and alarm clearing threshold for the user resource usage or CPU usage are configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the maximum number of active sessions when the device functions as a RADIUS proxy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment system-state radius-proxy active-session threshold restrain**](cmdqueryname=access-speed+adjustment+system-state+radius-proxy+active-session+threshold+restrain) *restrain-threshold-value* **resume** *resume-threshold-value*
     
     
     
     The suppression threshold and recovery threshold for the maximum number of active sessions are configured for the RADIUS proxy.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure parameters of the avalanche prevention alarm function for user login.  
  When the user access rate is high and the system is overloaded, an avalanche occurs. As a result, users cannot access the network for a long time. To prevent this problem, the system can be configured to monitor some device indicators. When an indicator meets the condition for generating an avalanche prevention alarm, the device generates such an alarm. This allows the device to adjust the access rate or reduce the number of received packets in a timely manner, ensuring slow user access when the device load is heavy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     The AAA view is displayed.
  3. Run [**access-speed adjustment system-state alarm**](cmdqueryname=access-speed+adjustment+system-state+alarm) **interval** *alarm-interval* **threshold** *alarm-threshold-value* [**percent**](cmdqueryname=percent) *alarm-percent-value*
     
     The detection interval for generating an avalanche prevention alarm, health threshold, and the percentage of time during which the system health is lower than the threshold are configured. Within a detection interval, if the percentage of the duration in which the system health is lower than the health threshold to the detection interval is greater than the configured percentage, the system generates an avalanche prevention alarm.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.