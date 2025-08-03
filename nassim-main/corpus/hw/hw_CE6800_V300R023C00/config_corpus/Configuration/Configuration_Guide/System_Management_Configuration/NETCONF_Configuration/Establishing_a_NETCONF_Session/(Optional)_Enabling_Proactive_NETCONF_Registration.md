(Optional) Enabling Proactive NETCONF Registration
==================================================

(Optional) Enabling Proactive NETCONF Registration

#### Context

If an NMS does not support automatic device discovery, it cannot manage devices as soon as they go online. To address this problem, you can configure proactive NETCONF registration. This enables a device to send a NETCONF connection request to the NMS when the device goes online, allowing the NMS to manage the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the NETCONF user interface view.
   
   
   ```
   [netconf](cmdqueryname=netconf)
   ```
3. Create a callhome template and enter the callhome template view.
   
   
   ```
   [callhome](cmdqueryname=callhome) callhome-name
   ```
4. Configure the interval at which the device sends NETCONF connection requests to the NMS.
   
   
   ```
   [reconnection interval](cmdqueryname=reconnection+interval) interval
   ```
   
   By default, a device sends a NETCONF connection request to the NMS at an interval of 5s.
5. Create a NETCONF connection instance and enter the NETCONF connection instance view.
   
   
   ```
   [endpoint](cmdqueryname=endpoint) endpoint-name
   ```
6. Configure a callhome keepalive interval.
   
   
   ```
   [keepalive-interval](cmdqueryname=keepalive-interval) intervalTime
   ```
7. Configure the number of callhome keepalive times.
   
   
   ```
   [keepalive-maxcount](cmdqueryname=keepalive-maxcount) maxcount
   ```
8. Configure the IP address and TCP port number of the NMS that establishes a NETCONF connection with the device, as well as the device's source IP address and VPN instance.
   
   
   ```
   { [peer-ip](cmdqueryname=peer-ip) ip-address | peer { peerName ipv6 | peerName } port port-number { [ [ local-address source-ip ] | [ vpn-instance vpn-instance | public-net ] ] * | [ source-interface { interface-name | interface-type interface-num } ] }
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```