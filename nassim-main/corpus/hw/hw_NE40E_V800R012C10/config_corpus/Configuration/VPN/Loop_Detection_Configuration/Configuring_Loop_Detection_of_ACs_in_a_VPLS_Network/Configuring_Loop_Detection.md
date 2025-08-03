Configuring Loop Detection
==========================

Loop detection and blocking priorities can be configured in the interface view.

#### Context

Perform the following steps on PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number* or [**interface**](cmdqueryname=interface) { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number.subnum*
   
   
   
   The interface view is displayed.
3. Run [**loop-detect enable**](cmdqueryname=loop-detect+enable)
   
   
   
   Loop detection is enabled on the interface.
4. Run [**loop-detect mac-withdraw enable**](cmdqueryname=loop-detect+mac-withdraw+enable)
   
   
   
   The sub-interface or main interface is enabled to delete MAC address entries when its loop detection status changes.
   
   
   
   After a sub-interface or main interface is configured to delete MAC address entries when its loop detection status changes, traffic switching is accelerated.
5. (Optional) Run [**loop-detect priority**](cmdqueryname=loop-detect+priority) *priority-value*
   
   
   
   The blocking priority of the interface is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A smaller *priority* value indicates a higher blocking priority. The interface with a higher blocking priority is preferentially blocked when a loop is detected. The default *priority* value is 0.
   * If two interfaces have the same blocking priority value, the one with the smaller MAC address is determined to have a higher blocking priority and is therefore preferentially blocked.
   * If their MAC addresses are also the same, the interface with the smaller interface index (used in loop detection configuration) is determined to have a higher blocking priority and is therefore preferentially blocked.
6. Run [**loop-detect block**](cmdqueryname=loop-detect+block) [ *block-time* ]
   
   
   
   The device is enabled to block the interface when a loop is detected.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The interface is unblocked if it receives no loop detection packet during *block-time*. To prevent interface flapping when the interface is enabled to temporarily go down (see Step 7), *block-time* should be no shorter than 10s.
   * If *block-time* is not set, the interface is blocked permanently. That is, the interface remains blocked after the loop is eliminated and no further loop detection packets are received.
   * For an interface in the permanent blocking state, if the blocking priorities of the interfaces on the network are adjusted, the interface is unblocked when another interface is set with a higher blocking priority. The interface with a higher blocking priority is then blocked permanently.
7. (Optional) Run [**loop-detect trigger interface-down enable**](cmdqueryname=loop-detect+trigger+interface-down+enable)
   
   
   
   The interface is enabled to temporarily go down after being blocked.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   By default, a blocked interface stops forwarding traffic but remains in the up state, meaning its tables (for example, the MAC address table) cannot be updated immediately. Consequently, user traffic is still sent to the blocked interface, leading to traffic interruption. If an interface is configured to temporarily go down after being blocked, relevant tables on the interface are updated after it goes down. When the corresponding timer times out (approximately 5s), the interface goes up again, preventing user traffic loss.
   
   Do not add member interfaces to or delete member interfaces from an Eth-Trunk interface when it is temporarily down. This is because all member interfaces go down when the Eth-Trunk interface is temporarily down and go up again when it recovers.
   * If you add member interfaces to an Eth-Trunk interface when it is temporarily down, after the Eth-Trunk interface recovers, all its member interfaces automatically go up.
   * If you delete member interfaces from an Eth-Trunk interface when it is temporarily down, the deleted interfaces remain down and cannot go up automatically.You can add member interfaces to or delete member interfaces from an Eth-Trunk interface after it recovers.
8. Run [**loop-detect only-alarm**](cmdqueryname=loop-detect+only-alarm)
   
   
   
   The interface is enabled to report an alarm without blocking itself when detecting a loop.
   
   
   
   If the interface detects a loop after the [**loop-detect only-alarm**](cmdqueryname=loop-detect+only-alarm) command is run in the interface view, it only reports an alarm and does not block itself. This command configuration has the following impact:
   * If a loop is detected on an interface after the [**loop-detect only-alarm**](cmdqueryname=loop-detect+only-alarm) command is run on the interface, the interface only reports an alarm and does not block itself.
   * Running the [**loop-detect only-alarm**](cmdqueryname=loop-detect+only-alarm) command on a blocked interface unblocks the interface. In this case, if you run the [**undo loop-detect only-alarm**](cmdqueryname=undo+loop-detect+only-alarm) command to restore the default configuration on the interface, you need to block the interface again to prevent loops.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**loop-detect block**](cmdqueryname=loop-detect+block) and **loop-detect only-alarm** commands must be both configured so that the alarm reporting function can take effect. If only the **loop-detect only-alarm** command is configured, no alarm can be reported.
9. Run [**loop-detect identifier**](cmdqueryname=loop-detect+identifier) *identifier-value*
   
   
   
   An authentication identifier for interface-based L2VPN loop detection is configured.
   
   
   
   If an authentication identifier for L2VPN loop detection is configured in both the interface view and global view, the configuration in the interface view takes effect.
   
   After an authentication identifier is configured on the local device, if the authentication identifier in the loop detection packet received from a peer device is different from the local one, the local device discards the packet.
10. (Optional) Run [**loop-detect detection vid**](cmdqueryname=loop-detect+detection+vid) *low-vid* [ **to** *high-vid* ]
    
    
    
    A VLAN range is configured for the main interface to send loop detection packets.
    
    
    
    This command can be configured only on dot1q VLAN tag termination sub-interfaces and main interfaces.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.