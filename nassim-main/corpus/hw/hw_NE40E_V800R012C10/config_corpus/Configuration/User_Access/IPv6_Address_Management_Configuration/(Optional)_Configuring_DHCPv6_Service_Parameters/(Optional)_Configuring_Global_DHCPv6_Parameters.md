(Optional) Configuring Global DHCPv6 Parameters
===============================================

You can configure transparent transmission of DHCPv6 messages, unicast communication, and two-message exchange between a DHCPv6 client and a DHCPv6 server based on actual network conditions.

#### Context

* Transparent transmission of DHCPv6 messages and the rate threshold for sending Solicit messages
  
  After receiving a Solicit message from an online user, the NE40E logs out the user and waits for the user to re-send a Solicit message to obtain an IPv6 address.
  
  If a user terminal that does not support retransmission of DHCP Solicit messages is quickly restarted, the NE40E cannot detect the user logout event. In this case, you need to enable transparent transmission of DHCPv6 messages so that the user can go online normally.
  
  To limit the rate at which users go online, configure the rate threshold for sending Solicit messages.
* Configure DHCPv6 server unicast mode and two-message exchange between a DHCPv6 client and a server.
  
  For a DHCPv6 server and a DHCPv6 client to communicate in unicast mode, you need to configure the DHCPv6 server unicast mode.
  
  In certain situations (for example, a client already has an IP address assigned during the last startup), the client can obtain an IPv6 address through a rapid two-message (Solicit/Reply) exchange as long as the Solicit message sent from the client carries the Rapid Commit option and the server also supports this option.
* Enable immediate detection of abnormal logouts of DHCPv6 users.
  
  In some abnormal scenarios, users are offline on the BRAS but are still online on the CPE. For example, the BRAS logs out a user or a user is logged out due to a network fault. In this case, the CPE cannot detect that the user is already offline on the BRAS and still sends a Renew or Rebind message to the BRAS after the timer expires. To allow the CPE to detect a user logout immediately after the user goes offline from the BRAS, run the [**dhcpv6 rebind no-user action reply**](cmdqueryname=dhcpv6+rebind+no-user+action+reply) command. Then, after receiving a Rebind message, the BRAS responds with a Reply message indicating the no-binding state, prompting the CPE to re-dial up for IP address application.

#### Procedure

* Configure transparent transmission of DHCPv6 messages.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**dhcpv6 through-packet**](cmdqueryname=dhcpv6+through-packet) command to enable the device to transparently transmit DHCPv6 messages.
  3. Run the [**dhcpv6 solicit-speed-threshold**](cmdqueryname=dhcpv6+solicit-speed-threshold) *threshold-value* *value* command to configure the rate threshold for sending Solicit messages.
     
     
     
     The more Solicit messages are sent within a specified period of time, the faster users go online.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure DHCPv6 server unicast mode and two-message exchange between a DHCPv6 client and a server.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ipv6 pool**](cmdqueryname=ipv6+pool) *pool-name* { **bas** { **local** | **delegation** | **relay** } } command to create an IPv6 address pool and enter its view.
  3. (Optional) Run the [**dhcpv6 unicast-option**](cmdqueryname=dhcpv6+unicast-option) command to configure the DHCPv6 server unicast mode. After this command is run, the server can receive unicast DHCPv6 messages and instruct the client to use unicast communication.
  4. (Optional) Run the [**dhcpv6 rapid-commit**](cmdqueryname=dhcpv6+rapid-commit) command to configure the server to support DHCPv6 two-message exchange.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Enable immediate detection of abnormal logouts of DHCPv6 users.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**dhcpv6 rebind no-user action reply**](cmdqueryname=dhcpv6+rebind+no-user+action+reply) command to configure the device to reply with a Reply message indicating the no-binding state after receiving a DHCPv6 Rebind message if no user entry exists on the device.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.