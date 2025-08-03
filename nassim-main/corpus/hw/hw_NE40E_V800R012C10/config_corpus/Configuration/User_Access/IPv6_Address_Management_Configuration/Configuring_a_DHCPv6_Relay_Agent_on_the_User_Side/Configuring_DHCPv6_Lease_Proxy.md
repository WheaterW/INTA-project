Configuring DHCPv6 Lease Proxy
==============================

Configuring DHCPv6 Lease Proxy

#### Context

If a DHCPv6 server has assigned a long lease to a client, the user is logged out when the client or the link between the client and the BRAS fails. However, if the lease does not expire, the DHCPv6 server cannot detect the user logout or release the IPv6 address assigned to the user in a timely manner, wasting address resources. To prevent this problem, configure DHCPv6 lease proxy in a domain or on a BAS interface.


#### Procedure

* Configure DHCPv6 lease proxy in a domain.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     A domain is created, and the AAA domain view is displayed.
  4. Run [**dhcpv6 lease-proxy preferred-lifetime**](cmdqueryname=dhcpv6+lease-proxy+preferred-lifetime) *preferred-lifetime* [**valid-lifetime**](cmdqueryname=valid-lifetime) *valid-lifetime* [ **user-detect** ]
     
     
     
     DHCPv6 lease proxy is enabled and a proxy lease time is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If DHCPv6 lease proxy has been configured both in the BAS interface view and the AAA domain view, the command configured in the BAS interface view takes effect.
  5. (Optional) Configure CAR bandwidth for lease proxy rate limiting.
     
     
     1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
     3. Run the [**dhcpv6 lease-proxy rate-limit**](cmdqueryname=dhcpv6+lease-proxy+rate-limit) *rate-value* command to configure the CAR bandwidth for lease proxy rate limiting.
  6. (Optional) Run [**access-speed adjustment system-state threshold ipoe-keepalive cpu-usage alarm**](cmdqueryname=access-speed+adjustment+system-state+threshold+ipoe-keepalive+cpu-usage+alarm) *threshold-value* **resume** *threshold-value*
     
     
     
     The CPU usage threshold for increasing or resuming the DHCPv6 proxy lease is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable DHCPv6 lease proxy on a BAS interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**bas**](cmdqueryname=bas)
     
     
     
     The BAS interface view is displayed.
  4. Run **[**access-type**](cmdqueryname=access-type)** ****layer2-subscriber**** [ ****bas-interface-name**** **bname** | ****default-domain**** { **pre-authentication** **predname** | ****authentication**** [ ****force**** | ****replace**** ] **dname** } \* | ****accounting-copy**** ****radius-server**** **rd-name** ] \* or **[**access-type**](cmdqueryname=access-type)** ****layer3-subscriber**** [ ****default-domain**** { [ ****pre-authentication**** **predname** ] ****authentication**** [****force**** | **replace** ] *dname* } ]
     
     
     
     The type of the BAS interface is configured.
  5. Run [**dhcpv6 lease-proxy preferred-lifetime**](cmdqueryname=dhcpv6+lease-proxy+preferred-lifetime) *preferred-lifetime* [**valid-lifetime**](cmdqueryname=valid-lifetime) *valid-lifetime* [ **user-detect** ]
     
     
     
     DHCPv6 lease proxy is enabled and a proxy lease time is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If DHCPv6 lease proxy has been configured both in the BAS interface view and the AAA domain view, the command configured in the BAS interface view takes effect.
  6. (Optional) Configure CAR bandwidth for lease proxy rate limiting.
     
     
     1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     2. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
     3. Run the [**dhcpv6 lease-proxy rate-limit**](cmdqueryname=dhcpv6+lease-proxy+rate-limit) *rate-value* command to configure the CAR bandwidth for lease proxy rate limiting.
  7. (Optional) Run [**access-speed adjustment system-state threshold ipoe-keepalive cpu-usage alarm**](cmdqueryname=access-speed+adjustment+system-state+threshold+ipoe-keepalive+cpu-usage+alarm) *threshold-value* **resume** *threshold-value*
     
     
     
     The CPU usage threshold for increasing or resuming the DHCPv6 proxy lease is configured.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.