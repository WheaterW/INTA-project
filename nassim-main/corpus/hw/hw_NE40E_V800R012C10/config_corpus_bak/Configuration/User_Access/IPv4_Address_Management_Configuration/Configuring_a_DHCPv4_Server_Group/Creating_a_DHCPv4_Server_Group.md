Creating a DHCPv4 Server Group
==============================

DHCPv4 servers in a DHCPv4 server group can work in load balancing, polling, or master/backup mode.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
   
   
   
   DHCP is enabled globally.
3. Run [**dhcp-server group**](cmdqueryname=dhcp-server+group) *group-name*
   
   
   
   A DHCPv4 server group is created and the DHCPv4 server group view is displayed.
4. Run [**dhcp-server**](cmdqueryname=dhcp-server) *ip-address* [ **vpn-instance** *vpn-instance* ] [ **weight** *weight-value* ]
   
   
   
   A DHCPv4 server is configured.
   
   
   
   A DHCPv4 server group can contain one master DHCPv4 server and a maximum of seven backup DHCPv4 servers.
5. (Optional) Run [**dhcp-server algorithm**](cmdqueryname=dhcp-server+algorithm) { **loading-share** | **master-backup** | **polling** [ **check-loose** ] }
   
   
   
   The algorithm for selecting DHCPv4 servers is configured.
   
   
   
   This command takes effect only when a DHCPv4 server group contains two DHCPv4 servers. The servers can work in load balancing, polling, or master/backup mode.
   
   * Load balancing: The NE40E distributes traffic based on the weights of DHCPv4 servers.
   * Master/backup: The server configured earlier is the master server, and the other is the backup server.
   * Polling: The NE40E sends a request message to both of the two servers and selects the server that receives the request message earlier. All the subsequent messages, except DHCP Discover and DHCP Request messages, are sent only to the selected server.
6. (Optional) Run [**release-agent**](cmdqueryname=release-agent)
   
   
   
   The DHCPv4 release agent function is configured.
   
   
   
   When a user wants to go offline and the DHCPv4 release agent function is enabled, the NE40E, instead of the user, sends DHCPv4 Release messages to DHCPv4 servers.
7. (Optional) Run [**dhcp rebind forward-mode all**](cmdqueryname=dhcp+rebind+forward-mode+all)
   
   
   
   The NE40E is configured to forward DHCP Rebind messages to all DHCPv4 servers in the DHCPv4 server group.
8. (Optional) Run [**dhcp-server giaddr**](cmdqueryname=dhcp-server+giaddr) { **interface** *interface-type* *interface-number* | *ip-address* [ **vpn-instance** *vpn-instance* ] } [ **forward-rui-slave** ]
   
   
   
   The GiAddr address of the DHCP messages sent from the DHCPv4 server group is configured.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Run [**access user-ip-address trust dhcp-server user-type ppp**](cmdqueryname=access+user-ip-address+trust+dhcp-server+user-type+ppp)
    
    
    
    The NE40E is enabled to perform loose check on the IP addresses assigned by DHCPv4 servers from a remote address pool for PPP and L2TP users.
11. (Optional) Run [**dhcp-server**](cmdqueryname=dhcp-server) [ *ip-address* [ **vpn-instance** *vpn-instance* ] ] { **dead-count** *dead-count*  | **timeout** *timeout-value* | **dead-time** *dead-time* }\*
    
    
    
    The maximum number of times no response message is sent by a DHCPv4 server as a response to a request message is configured.
    
    
    
    This command is used to resolve the problem of repeated status switching of a DHCPv4 server. After this command is configured, a DHCPv4 server automatically goes down after the number of times no reply message is sent by a DHCPv4 server as a response to a request message exceeds the specified threshold.
12. (Optional) Run [**dhcp-server**](cmdqueryname=dhcp-server) [ *ip-address* [ **vpn-instance** *vpn-instance* ] ] **nak-count** *nak-count*
    
    
    
    The maximum number of consecutive DHCP Nak messages that can be received from a DHCPv4 server is configured. A DHCPv4 server automatically goes down if the number of consecutive DHCP Nak messages received from the DHCPv4 server exceeds the specified threshold.
13. (Optional) Run [**dhcp option-82 agent-remote-id strip**](cmdqueryname=dhcp+option-82+agent-remote-id+strip)
    
    
    
    The Router is enabled to remove the remote-id information from the Option 82 attribute of DHCP messages.
14. (Optional) Configure CAR for whitelisted DHCPv4 sessions.
    1. (Optional) Run the [**undo whitelist session-car dhcp-server disable**](cmdqueryname=undo+whitelist+session-car+dhcp-server+disable) command to enable CAR for whitelisted DHCPv4 sessions.
    2. Run the **whitelist session-car dhcp-server** { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \* command to configure the bandwidth parameters of CAR for whitelisted DHCPv4 sessions.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.