Configuring BGP Keepalive and Hold Timers
=========================================

The values of BGP Keepalive and Hold timers determine the speed at which BGP detects network faults. You can adjust the values of these timers to improve network performance.

#### Context

BGP uses Keepalive messages to maintain peer relationships. After establishing a BGP connection, two peers periodically send Keepalive messages to each other to detect BGP peer relationship status. If a device receives no Keepalive message from its peer after the Hold timer expires, the device considers the BGP connection interrupted.

* If short Keepalive time and holdtime are set, BGP can fast detect link faults. This speeds up BGP network convergence, but increases the number of Keepalive messages on the network and loads of Routers, and consumes more network bandwidth resources.
* If large values are set for the Keepalive timer and Hold timer, the number of Keepalive messages on the network and the burden on Routers are reduced. However, if the Keepalive time is too long, BGP cannot detect link status changes immediately after the changes occur, which slows down BGP network convergence and may cause packet loss.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Changing timer values using the [**timer**](cmdqueryname=timer) command or the [**peer timer**](cmdqueryname=peer+timer) command interrupts BGP peer relationships between Routers. Therefore, exercise caution when changing the values of the timers.

Keepalive and Hold timers can be configured either for all BGP peers or peer groups, or for a specific peer or peer group. Keepalive and Hold timers configured for a specific peer take precedence over those configured for the peer group of this peer. In addition, Keepalive and Hold timers configured for a specific peer or peer group take precedence over those configured for all peers or peer groups.


#### Procedure

* Set timers for all peers or peer groups.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**timer**](cmdqueryname=timer+keepalive+hold+min-holdtime) **keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ] command to set the BGP keepalive time and hold time, or run the [**timer**](cmdqueryname=timer+send-hold) **send-hold** *send-hold-time* command to set the hold time during which the local device does not proactively disconnect from the peer device.
     
     The proper maximum interval at which Keepalive messages are sent is one third the hold timer and cannot be less than 1s. If the hold time is not set to 0, it is 3s at least. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 1](#EN-US_TASK_0172366221__table410763711163).
     
     
     **Table 1** Mapping between the total number of BGP peers in all address families and the recommended minimum hold time
     | Total Number of Peers | Recommended Minimum Hold Time |
     | --- | --- |
     | 0â100 | 20s |
     | 101â200 | 30s |
     | 201â300 | 45s |
     | 301â400 | 60s |
     | 401â500 | 75s |
     | Greater than or equal to 501 | 90s |
     
     
     Avoid the following situations when setting values for the three timers:
     
     + The *keepalive-time* and *hold-time* values are both set to 0. In this case, BGP timers become invalid, and BGP will not send Keepalive messages.
     + The *hold-time* value is much greater than the *keepalive-time* value, for example, *keepalive-time* is set to 1 and *hold-time* is set to 65535. If the hold time is too long, BGP cannot detect the validity of the connection in time.
     + The *keepalive-time* value is set to 0. In this case, the keepalive timer does not start. As a result, the *send-hold-time* function does not take effect.
     
     After a connection is established between peers, the *keepalive-time* and *hold-time* values are negotiated by the peers. The smaller of the *hold-time* values carried in the Open messages exchanged between the peers is used as the final *hold-time* value. The smaller of one third of the negotiated *hold-time* value and the locally configured *keepalive-time* value is used as the final *keepalive-time*.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure timers for a specific peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**peer**](cmdqueryname=peer+timer+keepalive+hold+min-holdtime) { *ipv4-address* | *group-name* } **timer** **keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ] command to set the interval at which Keepalive messages are sent and the hold time for a peer or peer group. Alternatively, run the [**peer**](cmdqueryname=peer) *ipv4-address* [**timer**](cmdqueryname=timer+send-hold) **send-hold** *send-hold-time* command to set the hold time during which the local device does not proactively disconnect from the peer end.
     
     The relationship between the Keepalive and hold timer values in this case is the same as that in the scenario where global timers are configured.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 2](#EN-US_TASK_0172366221__table128097318210).
     
     
     
     **Table 2** Mapping between the total number of BGP peers in all address families and the recommended minimum hold time
     | Total Number of Peers | Recommended Minimum Hold Time |
     | --- | --- |
     | 0â100 | 20s |
     | 101â200 | 30s |
     | 201â300 | 45s |
     | 301â400 | 60s |
     | 401â500 | 75s |
     | Greater than or equal to 501 | 90s |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.