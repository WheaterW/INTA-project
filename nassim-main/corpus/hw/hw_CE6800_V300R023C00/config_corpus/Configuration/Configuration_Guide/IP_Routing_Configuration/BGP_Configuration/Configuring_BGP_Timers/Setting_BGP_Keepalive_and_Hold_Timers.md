Setting BGP Keepalive and Hold Timers
=====================================

Setting BGP Keepalive and Hold Timers

#### Prerequisites

Before setting BGP Keepalive and Hold timers, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

Keepalive messages are used to maintain BGP peer relationships. A pair of BGP peers periodically send Keepalive messages to each other to inform their local states. If a device receives no Keepalive message from its peer after the Hold timer expires, the device considers the BGP connection to be closed.

* If small values are set for the Keepalive timer and Hold timer, BGP can fast detect link faults. This speeds up BGP network convergence, but increases the number of Keepalive messages on the network and the burden of devices and consumes more network bandwidth resources.
* If large values are set for the Keepalive timer and Hold timer, the number of Keepalive messages on the network and the burden on devices are reduced. If the Keepalive time is too long, BGP cannot detect link status changes immediately after the changes occur, which slows down BGP network convergence and may cause packet loss.

![](public_sys-resources/notice_3.0-en-us.png) 

Changing timer values using the [**timer**](cmdqueryname=timer) command or the [**peer timer**](cmdqueryname=peer+timer) command interrupts BGP peer relationships. Therefore, exercise caution when changing the values of the timers.

Keepalive and Hold timers can be set for one or all peers or peer groups. Keepalive and Hold timers configured for a specific peer take precedence over those configured for the peer group to which this peer belongs. In addition, Keepalive and Hold timers configured for a specific peer or peer group take precedence over those configured for all peers or peer groups.


#### Procedure

* Set BGP timers for all peers or peer groups.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set BGP timers.
     
     
     
     Configure the Keepalive time and hold time for BGP.
     
     ```
     [timer](cmdqueryname=timer+keepalive+hold+min-holdtime) keepalive keepalive-time hold hold-time [ min-holdtime min-hold-value ]
     ```
     
     Alternatively, configure the hold time during which the local device does not proactively disconnect from the peer device.
     
     ```
     [timer](cmdqueryname=timer+send-hold) send-hold send-hold-time
     ```
     
     
     
     The proper maximum interval at which Keepalive messages are sent is one third the hold timer and cannot be less than 1s. If the hold time is not set to 0, it is 3s at least. By default, the keepalive time is 60s, the hold time is 180s, and the hold time during which the local device does not proactively disconnect from the peer device is 360s.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 1](#EN-US_TASK_0000001130783924__table410763711163).
     
     
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
     
     + The *keepalive-time* and *hold-time* values are both set to 0. In this case, BGP timers become invalid, and BGP will not send Keepalive messages.
     + The *hold-time* value is much greater than the *keepalive-time* value, for example, the *keepalive-time* value is set to 1 whereas *hold-time* is set to 65535. If the hold time value is too large, BGP cannot verify connection validity in time.
     + The *keepalive-time* value is set to 0. In this case, the keepalive timer does not start. As a result, the *send-hold-time* function does not take effect.
     
     After a connection is established between peers, the peers negotiate the *keepalive-time* and *hold-time* values. The smaller one of the *hold-time* values carried in Open messages of both peers is used as the effective *hold-time* value. The smaller value of one third of the negotiated *hold-time* value and the locally configured *keepalive-time* value is used as the effective *keepalive-time* value.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure timers for a specific peer or peer group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set the Keepalive and Hold timer values for a specific peer or peer group.
     
     
     ```
     [peer](cmdqueryname=peer+timer+keepalive+hold+min-holdtime) { ipv4-address | group-name } timer keepalive keepalive-time hold hold-time [ min-holdtime min-hold-value ]
     ```
     
     Alternatively, configure the hold time during which the local device does not proactively disconnect from the peer device.
     
     ```
     [peer](cmdqueryname=peer) ipv4-address [timer](cmdqueryname=timer+send-hold) send-hold send-hold-time
     ```
     
     For information about the relationship between the Keepalive and hold timer values, see [Set BGP timers for all peers or peer groups](#EN-US_TASK_0000001130783924__cmd1372590248214038).
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 1](vrp_bgp_cfg_0089.html#EN-US_TASK_0000001130783924__table410763711163).
     
     
     **Table 2** Mapping between the total number of BGP peers in all address families and the recommended minimum hold time
     | Total Number of Peers | Recommended Minimum Hold Time |
     | --- | --- |
     | 0â100 | 20 |
     | 101â200 | 30 |
     | 201â300 | 45 |
     | 301â400 | 60 |
     | 401â500 | 75 |
     | Greater than or equal to 501 | 90 |
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```