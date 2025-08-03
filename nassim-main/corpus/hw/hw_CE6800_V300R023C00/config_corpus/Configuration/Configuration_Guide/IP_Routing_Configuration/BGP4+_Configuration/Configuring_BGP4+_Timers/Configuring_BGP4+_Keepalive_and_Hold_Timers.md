Configuring BGP4+ Keepalive and Hold Timers
===========================================

Configuring BGP4+ Keepalive and Hold Timers

#### Prerequisites

Before configuring BGP4+ Keepalive and Hold timers, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

After establishing a BGP4+ connection, two peers periodically send Keepalive messages to each other to monitor the status of the BGP4+ peer relationship. If a BGP4+ device does not receive any Keepalive message or any other type of messages from its peer within the Hold time, the device considers the BGP4+ connection to be closed and terminates the BGP4+ connection.

When establishing a BGP4+ connection, two peers compare their Hold time periods and select a smaller value as a negotiation result. If the negotiation result is 0, no Keepalive message is sent and whether the Hold timer expires is not detected.

![](public_sys-resources/notice_3.0-en-us.png) 

Changing timer values using the [**peer timer**](cmdqueryname=peer+timer) command will interrupt peer relationships between devices. Therefore, exercise caution when changing timer values.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Set the Hold timer and Keepalive timer for a peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer+timer+keepalive+hold+min-holdtime) { ipv6-address | group-name } timer keepalive keepalive-time hold hold-time [ min-holdtime min-hold-value ]
   ```
   
   Alternatively, configure the hold time during which the local device does not proactively disconnect from the peer device.
   
   ```
   [peer](cmdqueryname=peer) ipv6-address [timer](cmdqueryname=timer+send-hold) send-hold send-hold-time
   ```
   
   The value of *hold-time* must be at least three times the value of *keepalive-time*. By default, the keepalive time is 60s, the hold time is 180s, and the hold time during which the local device does not proactively disconnect from the peer device is 360s.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 1](vrp_bgp_cfg_0089.html#EN-US_TASK_0000001130783924__table410763711163).
   
   
   **Table 1** Mapping between the total number of BGP peers in all address families and the recommended minimum hold time
   | Total Number of Peers | Recommended Minimum Hold Time |
   | --- | --- |
   | 0â100 | 20 |
   | 101â200 | 30 |
   | 201â300 | 45 |
   | 301â400 | 60 |
   | 401â500 | 75 |
   | Greater than or equal to 501 | 90 |
   
   Avoid the following situations when setting values for the timers:
   
   * The values of *keepalive-time* and *hold-time* are both set to 0. In this case, the BGP4+ timers become invalid, and BGP4+ cannot detect link faults based on the timers.
   * The *hold-time* value is much greater than the *keepalive-time* value, for example, **timer keepalive 1 hold 65535** is configured. In this case, link faults cannot be detected in time.
   * The *keepalive-time* value is set to 0. In this case, the keepalive timer does not start. As a result, the *send-hold-time* function does not take effect.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```