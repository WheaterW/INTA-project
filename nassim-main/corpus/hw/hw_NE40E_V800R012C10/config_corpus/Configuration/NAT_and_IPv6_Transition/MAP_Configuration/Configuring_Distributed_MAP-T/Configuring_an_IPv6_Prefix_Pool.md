Configuring an IPv6 Prefix Pool
===============================

In distributed MAP-T scenarios, IPv6 prefix pools can be configured in either delegation or remote mode. In delegation mode, the BMR configured using the **map-rule** command is used to assign prefixes to MAP users. When a device functions as a DHCPv6 relay agent, it uses an IPv6 remote prefix pool to manage prefixes.

#### Procedure

* Configure an IPv6 delegation prefix pool.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **delegation**
     
     
     
     An IPv6 prefix pool is created, and its view is displayed.
  3. Run [**map-rule**](cmdqueryname=map-rule) *rule-name*
     
     
     
     A MAP rule is bound to the IPv6 prefix pool.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an IPv6 remote prefix pool.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **remote**
     
     
     
     An IPv6 prefix pool is created, and its view is displayed.
  3. Run [**link-address**](cmdqueryname=link-address) *prefix-address/prefix-length*
     
     
     
     A link-local address is configured.
     
     
     
     When the remote server allocates addresses or prefixes, link-local addresses must be configured on the relay.
  4. Run [**remote-ip lease manage**](cmdqueryname=remote-ip+lease+manage)
     
     
     
     The lease management function is enabled for the IPv6 remote prefix pool users.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.