Configuring Port Attack Defense
===============================

Configuring Port Attack Defense

#### Context

The port attack defense function effectively limits the number of packets sent from a port to the CPU.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an attack defense policy and enter the attack defense policy view.
   
   
   ```
   [cpu-defend policy](cmdqueryname=cpu-defend+policy) policy-name
   ```
3. Enable port attack defense.
   
   
   ```
   [auto-port-defend enable](cmdqueryname=auto-port-defend+enable)
   ```
4. (Optional) Disable port attack defense for a specified protocol.
   
   
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), and CE6885-T:
   
   ```
   [auto-port-defend protocol](cmdqueryname=auto-port-defend+protocol) { arp-request | arp-request-uc | arp-reply | dhcp-request | dhcp-reply | dhcpv6-discovery | dhcpv6-reply | dhcpv6-request | icmp | igmp | ip-fragment | isis | isis-overlay | lacp  |  nd | ospf | ospf-hello | ospf-overlay | ospf-hello-overlay | ospfv3 | ospfv3-overlay | pim | pim-mc | vrrp | vrrp6 } disable
   ```
   
   For the CE6885-LL working in low latency mode:
   
   ```
   auto-port-defend protocol { arp-request | arp-request-uc | arp-reply | dhcp-request | dhcp-reply | icmp | igmp | ip-fragment | isis | lacp | ospf | pim | pim-mc | vrrp } disable
   ```
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   ```
   [auto-port-defend protocol](cmdqueryname=auto-port-defend+protocol) { arp-request | arp-request-uc | arp-reply | [dhcp-discovery](cmdqueryname=dhcp-discovery) | dhcp-request | dhcp-reply | dhcpv6-discovery | dhcpv6-reply | dhcpv6-request | icmp | igmp | ip-fragment | isis | isis-overlay | lacp | nd | ospf | ospf-hello | ospf-overlay | ospf-hello-overlay | ospfv3 | ospfv3-overlay | pim | pim-mc| vrrp | vrrp6 } disable
   ```
   
   If only a small proportion of all packets exceeding the rate threshold are attack packets, you can disable port attack defense for specific protocols, preventing normal services from being impacted due to excessive rate limiting.
5. (Optional) Set the rate threshold for port attack defense.
   
   
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), and CE6885-T:
   
   ```
   auto-port-defend protocol { arp-request | arp-request-uc | arp-reply | dhcp-request | dhcp-reply | dhcpv6-discovery | dhcpv6-reply | dhcpv6-request | icmp | igmp | ip-fragment | isis | isis-overlay | lacp | nd | ospf | ospf-hello | ospf-overlay | ospf-hello-overlay | ospfv3 | ospfv3-overlay | pim | pim-mc | vrrp | vrrp6 } threshold threshold-value
   ```
   
   For the CE6885-LL working in low latency mode:
   
   ```
   auto-port-defend protocol { arp-request | arp-request-uc | arp-reply | dhcp-request | dhcp-reply | icmp | igmp | ip-fragment | isis | lacp | ospf | pim | pim-mc | vrrp } threshold threshold-value
   ```
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   ```
   auto-port-defend protocol { arp-request | arp-request-uc | arp-reply | dhcp-discovery | dhcp-request | dhcp-reply | dhcpv6-discovery | dhcpv6-reply | dhcpv6-request | icmp | igmp | ip-fragment | isis | isis-overlay | lacp | nd | ospf | ospf-hello | ospf-overlay | ospf-hello-overlay | ospfv3 | ospfv3-overlay | pim | pim-mc | vrrp | vrrp6 } threshold threshold-value
   ```
6. (Optional) Set the protocol packet sampling ratio for port attack defense.
   
   
   ```
   [auto-port-defend sample](cmdqueryname=auto-port-defend+sample) sample-value
   ```
7. (Optional) Set the aging time for port attack defense.
   
   
   ```
   [auto-port-defend aging-time](cmdqueryname=auto-port-defend+aging-time) aging-time
   ```
8. (Optional) Configure a whitelist for port attack defense.
   
   
   ```
   [auto-port-defend whitelist](cmdqueryname=auto-port-defend+whitelist) whitelist-id { acl acl-number | acl ipv6 ipv6-acl-number | interface interface-type interface-number }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support **ipv6** *ipv6-acl-number*.
   
   By default, no whitelist is configured for port attack defense.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Note the following when configuring an ACL-based whitelist for port attack defense:
   
   * Before referencing an ACL in a whitelist, create the ACL and configure rules.
   * The ACL referenced can be a basic ACL, advanced ACL, Layer 2 ACL, basic ACL6, or advanced ACL6.
   * All packets matching an ACL referenced by a whitelist are considered legitimate and are not processed based on port attack defense, regardless of whether the ACL rule is permit or deny.
   * If an ACL has no rule, the whitelist that references the ACL does not take effect.
   * If an ACL rule is defined by a protocol, ensure that the port attack defense function supports this protocol.
   * Insufficient ACL resources may lead to an ineffective whitelist.
9. (Optional) Enable the function of reporting port attack defense events.
   
   
   ```
   [undo auto-port-defend alarm disable](cmdqueryname=undo+auto-port-defend+alarm+disable)
   ```
   
   By default, the function of reporting port attack defense events is enabled.
10. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. Apply the attack defense policy.
    
    
    * Configure attack defense policies in batches.
      ```
      [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name batch slot { start-slot [ to end-slot ] } &<1-12>
      ```
    * Configure an attack defense policy separately.
      ```
      [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name [ slot slot-id ]
      ```
    
    After an attack defense policy is created, you must apply the policy in the system view. Otherwise, the policy does not take effect.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Example

Enable port attack defense in the attack defense policy named **test**. Use the default rate threshold, set the sampling ratio to 7 and aging time to 200s, and add 100GE 1/0/1 to a whitelist so that port attack defense will not be applied to this interface.

```
<HUAWEI> system-view
[~HUAWEI] [cpu-defend policy](cmdqueryname=cpu-defend+policy) test
[*HUAWEI-cpu-defend-policy-test] auto-port-defend enable
[*HUAWEI-cpu-defend-policy-test] [auto-port-defend sample](cmdqueryname=auto-port-defend+sample) 7
[*HUAWEI-cpu-defend-policy-test] [auto-port-defend aging-time](cmdqueryname=auto-port-defend+aging-time) 200
[*HUAWEI-cpu-defend-policy-test] auto-port-defend whitelist 1 interface 100ge 1/0/1
[*HUAWEI-cpu-defend-policy-test] quit
[*HUAWEI] [cpu-defend-policy](cmdqueryname=cpu-defend-policy) test
[*HUAWEI] commit
```