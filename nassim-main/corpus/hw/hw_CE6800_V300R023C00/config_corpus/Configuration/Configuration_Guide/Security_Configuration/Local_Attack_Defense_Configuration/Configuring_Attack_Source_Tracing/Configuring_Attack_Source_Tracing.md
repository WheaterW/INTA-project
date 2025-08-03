Configuring Attack Source Tracing
=================================

Configuring Attack Source Tracing

#### Context

After attack source tracing is configured, the device analyzes packets sent to the CPU to determine if the CPU is under attack. If so, the device traces the attack source and notifies the administrator through logs or alarms, who can then take appropriate measures to defend against the attack source.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an attack defense policy and enter the attack defense policy view.
   
   
   ```
   [cpu-defend policy](cmdqueryname=cpu-defend+policy) policy-name
   ```
3. Enable attack source tracing.
   
   
   ```
   [auto-defend enable](cmdqueryname=auto-defend+enable)
   ```
4. Set the rate threshold of attack source tracing.
   
   
   ```
   [auto-defend threshold](cmdqueryname=auto-defend+threshold) threshold-value
   ```
5. Set the packet sampling ratio for attack source tracing.
   
   
   ```
   [auto-defend attack-packet sample](cmdqueryname=auto-defend+attack-packet+sample) sample-value
   ```
6. Specify the type of packets to which attack source tracing is applied.
   
   
   ```
   [auto-defend protocol](cmdqueryname=auto-defend+protocol) { { arp | icmp | dhcp | ttl-expired | tcp | udp | telnet | [dhcpv6](cmdqueryname=dhcpv6) | dns | nd | icmpv6 | tcpv6 | igmp | mld } * | all }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support nd, icmpv6, dhcpv6, mld, or tcpv6.
7. Set the attack source tracing mode.
   
   
   ```
   [auto-defend trace-type](cmdqueryname=auto-defend+trace-type) { source-mac | source-ip | source-portvlan } *
   ```
   
   The source tracing modes are listed in descending order of priority as follows: MAC address-based > IP address-based > interface- and VLAN-based. If multiple source tracing modes are configured, the configured modes take effect according to this order of priorities.
8. (Optional) Configure a whitelist for attack source tracing.
   
   
   ```
   [auto-defend whitelist](cmdqueryname=auto-defend+whitelist) whitelist-id { acl acl-number | acl ipv6 ipv6-acl-number | interface interface-type interface-number }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ipv6** *ipv6-acl-number*.
   
   By default, no whitelist is configured for attack source tracing.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Note the following when configuring an ACL-based whitelist for attack source tracing:
   
   * Before referencing an ACL in a whitelist, create the ACL and configure rules. If an ACL has no rule, the whitelist that references the ACL does not take effect.
   * The ACL referenced can be a basic ACL, advanced ACL, Layer 2 ACL, basic ACL6, or advanced ACL6.
   * All packets matching an ACL referenced by a whitelist are considered legitimate, and will not be source-traced or punished regardless of whether the ACL rule is permit or deny.
   * If an ACL rule is defined by a protocol, ensure that the attack source tracing function supports this protocol.
   * Insufficient ACL resources may lead to an ineffective whitelist.
9. (Optional) Configure the event reporting function for attack source tracing.
   1. Enable the event reporting function for attack source tracing.
      
      
      ```
      [auto-defend alarm enable](cmdqueryname=auto-defend+alarm+enable)
      ```
      
      By default, the event reporting function for attack source tracing is disabled.
   2. Configure the rate threshold for triggering event reporting in attack source tracing.
      
      
      ```
      [auto-defend alarm threshold](cmdqueryname=auto-defend+alarm+threshold) alarm-threshold
      ```
10. Configure the punishment action for attack source tracing.
    
    
    ```
    [auto-defend action](cmdqueryname=auto-defend+action) { deny [ timeout timeout-num ] | error-down }
    ```
    ![](public_sys-resources/note_3.0-en-us.png) 
    * A device can set the status of an interface to error-down when it detects a fault on the interface. An interface in error-down state cannot receive or send packets and the interface indicator is off.
      
      If the punishment action results in the interface that receives attack packets being set to the error-down state, services of authorized users on this interface will be interrupted. Exercise caution when setting this punishment action.
    * The device does not take punishment actions on whitelisted users.
11. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
12. Apply the attack defense policy.
    
    
    * Configure attack defense policies in batches.
      ```
      [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name batch slot { start-slot [ to end-slot ] } &<1-12>
      ```
    * Configure an attack defense policy separately.
      ```
      [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name [ slot slot-id ]
      ```
    
    After an attack defense policy is created, you must apply the policy in the system view. Otherwise, the policy does not take effect.
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Example

In the attack defense policy named **test**, enable attack source tracing; and set the rate threshold to 200 pps, sampling ratio to 7, attack source tracing mode to source IP address-based, and punishment action to discarding attack packets.

```
<HUAWEI> system-view
[~HUAWEI] [cpu-defend policy](cmdqueryname=cpu-defend+policy) test
[*HUAWEI-cpu-defend-policy-test] [auto-defend enable](cmdqueryname=auto-defend+enable)
[*HUAWEI-cpu-defend-policy-test] [auto-defend threshold](cmdqueryname=auto-defend+threshold) 200
[*HUAWEI-cpu-defend-policy-test] [auto-defend attack-packet sample](cmdqueryname=auto-defend+attack-packet+sample) 7
[*HUAWEI-cpu-defend-policy-test] [auto-defend trace-type](cmdqueryname=auto-defend+trace-type) source-ip
[*HUAWEI-cpu-defend-policy-test] [auto-defend action](cmdqueryname=auto-defend+action) deny
[*HUAWEI-cpu-defend-policy-test] quit
[*HUAWEI] [cpu-defend-policy](cmdqueryname=cpu-defend-policy) test
[*HUAWEI] commit
```

#### Follow-up Procedure

If the punishment action for attack source tracing is set to error-down, the device sets the status of the interface that receives attack packets to down after identifying the attack source. After the interface is set to down, you are advised to eliminate attacks before recovering the interface to the up state.

**Table 1** Methods of recovering an interface to the up state
| Method | Application Scenario | Procedure |
| --- | --- | --- |
| Manual recovery | * A small number of interfaces are expected to go down. * The interface has been set to down. | Run the **shutdown** and **undo shutdown** commands, or run the **restart** command in the interface view to restart the interface. |
| Automatic recovery | * A large number of interfaces are expected to go down. Manually restoring the interface status one by one is time-consuming and may result in omissions. * The interface has not been set to down. This mode does not take effect on interfaces that are already in down state. | Run the **error-down auto-recovery** **cause auto-defend** **interval** command in the system view to enable automatic interface recovery after a specified delay. You can run the **display error-down recovery** command to view information about automatic interface recovery. |