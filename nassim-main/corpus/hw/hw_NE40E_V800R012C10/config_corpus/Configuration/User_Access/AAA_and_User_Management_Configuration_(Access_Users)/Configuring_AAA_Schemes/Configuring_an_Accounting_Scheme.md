Configuring an Accounting Scheme
================================

You must configure an accounting scheme before implementing accounting for users.

#### Context

Users successfully go online after they are authenticated and authorized, and accounting starts when they access services. Accounting is performed based on online duration, traffic volume, or both. The accounting process is as follows: The NE40E collects statistics about the online duration and the upstream and downstream traffic, and sends the statistics to the RADIUS server in the format specified by the RADIUS protocol. The RADIUS server then returns a message indicating whether the accounting succeeds.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. (Optional) Run [**realtime-accounting backup enable**](cmdqueryname=realtime-accounting+backup+enable)
   
   
   
   Real-time accounting backup is enabled between the active and standby main control boards.
   
   
   
   The [**realtime-accounting backup enable**](cmdqueryname=realtime-accounting+backup+enable) command needs to be run if the RADIUS server has a strict requirement on the interval at which real-time accounting packets are sent. After this command is run, the real-time accounting timer is reset on the active and standby main control boards. In this manner, even if an active/standby main control board switchover occurs during the interval for sending real-time accounting packets, the device still sends real-time accounting packets at the configured interval.
4. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *acct-scheme-name*
   
   
   
   An accounting scheme is created.
   
   
   
   The NE40E provides two fixed accounting schemes, namely default0 and default1, which can be modified but not deleted.
   * In the default0 accounting scheme, non-accounting is performed by default.
   * In the default1 and user-defined accounting schemes, RADIUS accounting is performed by default.
5. Run [**accounting-mode**](cmdqueryname=accounting-mode) { **hwtacacs** | **none** | **radius** }
   
   
   
   An accounting mode is configured.
   
   
   
   The NE40E supports RADIUS accounting, HWTACACS accounting, and none accounting.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   HWTACACS accounting can be performed for administrative users only.
6. (Optional) Run [**accounting interim interval**](cmdqueryname=accounting+interim+interval) *interval* [ **second** ] [ **traffic** ] [ **hash** ]
   
   
   
   The interval for performing real-time accounting, conditions for sending real-time accounting packets, and hash processing of real-time accounting packets are configured.
   
   
   
   Real-time accounting indicates that the NE40E periodically generates accounting packets and send them to the remote accounting server when a user is online. Real-time accounting minimizes loss of accounting information when the communication between the NE40E and the remote server is interrupted.
   
   The interval for real-time accounting can be set to minutes or seconds.
7. (Optional) Run [**accounting interim no-send remain-time**](cmdqueryname=accounting+interim+no-send+remain-time) *time-value*
   
   
   
   The device is configured not to send real-time accounting packets when the remaining time quota of a user is less than or equal to the configured interval.
8. (Optional) Run [**accounting start-fail**](cmdqueryname=accounting+start-fail) { **offline** | **online** [ **keep-accounting** ] }
   
   
   
   The policy for handling accounting start failures is configured.
   
   
   
   If the NE40E does not receive any response after sending an Accounting Start packet to the remote accounting server, the NE40E adopts the policy for handling accounting start failures. This policy may keep the user online or log the user out.
9. (Optional) Run [**accounting interim-fail**](cmdqueryname=accounting+interim-fail) [ **max-times** *times* ] { **offline** | **online** }
   
   
   
   The policy for handling real-time accounting failures is configured.
   
   
   
   If the NE40E does not receive any response packet after re-sending a real-time accounting packet to the remote accounting server for a specified number of times, the NE40E adopts the policy for handling real-time accounting failures. This policy may keep the user online or log the user out.
   
   If RADIUS/HWTACACS accounting is used, it is recommended that the number of retransmissions of real-time accounting packets be greater than the number of retransmissions of RADIUS/HWTACACS packets.
10. (Optional) Run [**accounting send-update**](cmdqueryname=accounting+send-update)
    
    
    
    The NE40E is configured to send a real-time accounting packet immediately after receiving an Accounting Start response.
    
    
    
    After receiving an Accounting Start response from the accounting server, the NE40E determines whether to immediately send real-time accounting packets according to the configuration.
11. (Optional) Enable the device to send Accounting Start packets for users after a specified delay.
    1. Run the [**quit**](cmdqueryname=quit) command to return to the AAA view.
    2. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the domain view.
    3. Run the [**accounting-start-delay**](cmdqueryname=accounting-start-delay) *delay-time* **online** **user-type** { **ppp** | **ipoe** | **l2tp** | **static** } \* or [**accounting-start-delay**](cmdqueryname=accounting-start-delay) *delay-time* **offline** [ **user-type** { **ppp** | **ipoe** | **l2tp** | **static** } \* ] command to configure the device to send Accounting Start packets after a delay.
    4. (Optional) Run the [**accounting-start-delay ipv4 start-accounting immediately**](cmdqueryname=accounting-start-delay+ipv4+start-accounting+immediately) command to configure the device to send an Accounting Start packet immediately after a dual-stack user goes online through the IPv4 stack.
       
       
       
       In a scenario where delayed accounting is enabled for a dual-stack user, if the dual-stack user goes online through the IPv4 stack first, an Accounting Start packet carrying the IPv4 address of the user is immediately sent. If the dual-stack user goes online through the IPv6 stack first, the device sends an Accounting Start packet after the dual-stack user also goes online through the IPv4 stack or the timeout period expires.
    5. (Optional) Run the [**accounting-start-delay traffic-forward before-start-accounting**](cmdqueryname=accounting-start-delay+traffic-forward+before-start-accounting) command to configure the device to allow a dual-stack user who goes online only from the IPv4 or IPv6 stack to access the network before accounting is started.
       
       
       
       If delayed accounting is enabled for a dual-stack user and the user does not go online through the second stack for quite some time, the user is allowed to access the network using the IP protocol stack through which the user has gone online.
    6. (Optional) Run the [**accounting-start-delay traffic-statistics before-start-accounting**](cmdqueryname=accounting-start-delay+traffic-statistics+before-start-accounting) command to configure the device to collect statistics about user traffic before Accounting Start packets are sent and report the statistics to the accounting server in a scenario where delayed accounting is enabled.
       
       
       
       If delayed accounting is enabled for a dual-stack user and the user goes online from the IPv4 or IPv6 stack, the device can collect statistics about user traffic before Accounting Start packets are sent and report the statistics to the accounting server.
    7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
12. (Optional) Run [**accounting-stop-packet include all-stack-ip user-type ipoe**](cmdqueryname=accounting-stop-packet+include+all-stack-ip+user-type+ipoe)
    
    
    
    The device is configured to add all the assigned IP addresses to an Accounting Stop packet to be sent to the RADIUS server for an IPoE user. This prevents accounting failures caused by incomplete IP information carried in an Accounting Stop packet when a dual-stack user goes offline only from the IPv4 or IPv6 stack.
13. (Optional) Configure an accounting copy scheme.
    1. Run the [**quit**](cmdqueryname=quit) command to enter the AAA view.
    2. Run the [**accounting-copy-group**](cmdqueryname=accounting-copy-group) *group-name* command to create an accounting copy group and enter its view.
    3. Run the [**radius-server group**](cmdqueryname=radius-server+group) *group-name* [ **interval** *interval-value* ] command to configure an accounting copy server group and the interval at which accounting copy packet information is sent to the accounting copy server group.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       You are advised to set **interval** *interval-value* to a value greater than or equal to 60.
    4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
    5. Run the [**quit**](cmdqueryname=quit) command to enter the AAA view.
    6. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the domain view.
    7. Run the [**accounting-copy-group**](cmdqueryname=accounting-copy-group) *group-name* command to bind the accounting copy group to the domain.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.