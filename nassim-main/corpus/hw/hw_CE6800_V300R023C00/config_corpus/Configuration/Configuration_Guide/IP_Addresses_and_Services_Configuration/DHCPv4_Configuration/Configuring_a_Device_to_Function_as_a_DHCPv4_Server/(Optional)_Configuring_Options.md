(Optional) Configuring Options
==============================

(Optional) Configuring Options

#### Context

Vendors can define options. A device functioning as a DHCPv4 server can allocate vendor-defined network parameters to clients.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enable the device to trust Option 82.
   
   
   ```
   [dhcp server trust option82](cmdqueryname=dhcp+server+trust+option82)
   ```
   
   By default, a device is enabled to trust Option 82.
3. (Optional) Enable the device to check and discard DHCPv4 messages with duplicate options.
   
   
   ```
   [dhcp anti-attack check duplicate option](cmdqueryname=dhcp+anti-attack+check+duplicate+option) [ option-start [ to option-end ] ] &<1-254>
   ```
   
   By default, a device is disabled from checking and discarding DHCPv4 messages with duplicate options.
4. (Optional) Configure the DHCPv4 server to forcibly insert a specified option into a reply message sent to a DHCPv4 client.
   * Configure the DHCPv4 server to forcibly insert a specified option into a reply message in the global address pool view.
     ```
     [ip pool](cmdqueryname=ip+pool) pool-name
     [force insert option](cmdqueryname=force+insert+option) value &<1-254>
     [quit](cmdqueryname=quit)
     ```
   * Configure the DHCPv4 server to forcibly insert a specified option into a reply message in the interface address pool view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [undo portswitch](cmdqueryname=undo+portswitch)
     [dhcp server force insert option](cmdqueryname=dhcp+server+force+insert+option) code &<1-254>
     [quit](cmdqueryname=quit)
     ```
     
     Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
   
   
   
   By default, a DHCPv4 server does not forcibly insert a specified option into a reply message.
5. Configure a user-defined option so that the DHCPv4 server allocates network parameters to a client based on the option requested by the client.
   * Configure a user-defined option in the global address pool view.
     ```
     [ip pool](cmdqueryname=ip+pool) pool-name
     [option](cmdqueryname=option) code [ sub-option sub-code ] { ascii ascii-string | hex hex-string | cipher cipher-string | ip-address ip-address &<1-8> }
     [quit](cmdqueryname=quit)
     ```
   * Configure a user-defined option in the interface address pool view.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     [undo portswitch](cmdqueryname=undo+portswitch)
     [dhcp server option](cmdqueryname=dhcp+server+option) code [ sub-option sub-code ] { ascii ascii-string | hex hex-string | cipher cipher-string | ip-address ip-address &<1-8> }
     [quit](cmdqueryname=quit)
     ```
     
     Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
   
   
   
   By default, no user-defined option that a DHCPv4 server allocates to a DHCPv4 client is configured.
   
   When configuring Option 33 (static route option), you must specify both the destination and next hop IP addresses.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Some options need to be configured using other commands in an address pool. The following table lists the options and their configuration methods.

**Table 1** Options and their configuration methods
| Option | Configuration Method | Description |
| --- | --- | --- |
| Option 1 | * Interface address pool:   + Specified by *masklen* in the [**dhcp server mask**](cmdqueryname=dhcp+server+mask) { *mask* | *masklen* } command   + Specified by *mask-length* in the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command If both the preceding commands are run, the value of Option 1 is the value of *masklen* in the [**dhcp server mask**](cmdqueryname=dhcp+server+mask) { *mask* | *masklen* } command. * Global address pool: specified by *mask-length* in the [**network**](cmdqueryname=network) *ip-address* [ **mask** { *mask* | *mask-length* } ] command | Subnet mask |
| Option 3 | * Interface address pool: specified by *ip-address* in the **ip address** *ip-address* { *mask* | *mask-length* } command * Global address pool: configured using the [**gateway-list**](cmdqueryname=gateway-list) *ip-address* &<1-8> command | Gateway address |
| Option 6 | * Interface address pool: configured using the [**dhcp server dns-list**](cmdqueryname=dhcp+server+dns-list) *ip-address* &<1-8> command * Global address pool: configured using the [**dns-list**](cmdqueryname=dns-list) *ip-address* &<1-8> command | DNS server address |
| Option 15 | * Interface address pool: configured using the [**dhcp server domain-name**](cmdqueryname=dhcp+server+domain-name) *domain-name* command * Global address pool: configured using the [**domain-name**](cmdqueryname=domain-name) *domain-name* command | Domain name |
| Option 44 | * Interface address pool: configured using the [**dhcp server nbns-list**](cmdqueryname=dhcp+server+nbns-list) *ip-address* &<1-8> command * Global address pool: configured using the [**nbns-list**](cmdqueryname=nbns-list) *ip-address* &<1-8> command | NetBIOS server address |
| Option 46 | * Interface address pool: configured using the [**dhcp server netbios-type**](cmdqueryname=dhcp+server+netbios-type) { **b-node** | **h-node** | **m-node** | **p-node** } command * Global address pool: configured using the [**netbios-type**](cmdqueryname=netbios-type) { **b-node** | **h-node** | **m-node** | **p-node** } command | NetBIOS node type |
| Option 50 | This option does not need to be configured on the DHCPv4 server. | Requested IPv4 address |
| Option 51 | * Interface address pool: configured using the [**dhcp server lease**](cmdqueryname=dhcp+server+lease) { **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | **unlimited** } command * Global address pool: configured using the [**lease**](cmdqueryname=lease) { **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | **unlimited** } command | IPv4 address lease |
| Option 52 | This option does not need to be configured on the DHCPv4 server. | Additional option |
| Option 53 | This option does not need to be configured on the DHCPv4 server. | DHCPv4 message type |
| Option 54 | This option does not need to be configured on the DHCPv4 server. | Server identification |
| Option 55 | This option does not need to be configured on the DHCPv4 server. | Parameter request list |
| Option 57 | This option does not need to be configured on the DHCPv4 server. | Maximum DHCPv4 message length |
| Option 58 | This option does not need to be configured on the DHCPv4 server. | Lease renewal time (T1), which is generally 50% of the lease |
| Option 59 | This option does not need to be configured on the DHCPv4 server. | Lease renewal time (T2), which is generally 87.5% of the lease |
| Option 61 | This option does not need to be configured on the DHCPv4 server. | Client identifier |
| Option 82 | This option does not need to be configured on the DHCPv4 server. | Relay agent information |
| Option 120 | * Interface address pool: configured using the [**dhcp server sip-server**](cmdqueryname=dhcp+server+sip-server) { **ip-address** *ip-address* &<1-2> | **list** *domain-name* &<1-2> } command * Global address pool: configured using the [**sip-server**](cmdqueryname=sip-server) { **ip-address** *ip-address* &<1-2> | **list** *domain-name* &<1-2> } command | SIP server IPv4 address |
| Option 121 | * Interface address pool: configured using the [**dhcp server option121**](cmdqueryname=dhcp+server+option121) **ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8> command * Global address pool: configured using the [**option121**](cmdqueryname=option121) **ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8> command | Classless route |
| Option 184 | * Interface address pool: configured using the [**dhcp server option184**](cmdqueryname=dhcp+server+option184) { **as-ip** *ip-address* | **fail-over** *ip-address* *dialer-string* | **ncp-ip** *ip-address* | **voice-vlan** *vlan-id* } command * Global address pool: configured using the [**option184**](cmdqueryname=option184) { **as-ip** *ip-address* | **fail-over** *ip-address* *dialer-string* | **ncp-ip** *ip-address* | **voice-vlan** *vlan-id* } command | Voice parameters |