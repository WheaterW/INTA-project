Configuring a Destination Collector for Receiving Sampled Data
==============================================================

Configuring a Destination Collector for Receiving Sampled Data

#### Context

When configuring static telemetry subscription to collect sampled data, you need to create a destination group and specify its working mode, and configure a destination collector for receiving the sampled data (destination collector for short), including the IP address, port number, transport protocol, priority, and encryption mode.

A destination group works in one of the following modes:

* default: This is the default working mode of the destination group. In this mode, the device establishes telemetry connections with all destination collectors in the destination group.
* priority: In this mode, the device establishes a telemetry connection with only one destination collector in the destination group. The device first initiates a telemetry connection with the highest-priority destination collector in the destination group. If the connection fails, the device attempts to establish a telemetry connection with the second-priority destination collector, and so on and so forth. If the current connection is not of the highest priority, the device continuously attempts to establish a telemetry connection with a higher-priority destination collector.
  
  A device establishes a telemetry connection with a destination collector in descending order of priority: high > medium > low. If destination collectors have the same priority, they are first sorted based on the VPN name, then based on IP addresses (in ascending order), and finally based on port numbers (in ascending order).
  
  + Priorities of VPN names: A public VPN has a higher priority than a private VPN. The priorities of private VPNs are sorted in the lexicographic order (ASCII code) of VPN names.
  + Priorities of IP addresses: An IPv4 address has a higher priority than an IPv6 address. IP addresses of the same type are sorted in ascending order.
  + Priorities of port numbers: Port numbers are sorted in ascending order.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the telemetry view.
   
   
   ```
   [telemetry](cmdqueryname=telemetry) [ openconfig ]
   ```
3. Create a destination group where a destination collector belongs and enter the destination group view.
   
   
   ```
   [destination-group](cmdqueryname=destination-group) destination-group-name
   ```
   
   By default, no destination group where a destination collector belongs is created.
4. (Optional) Set the working mode of the destination group to priority.
   
   
   ```
   [work-mode priority](cmdqueryname=work-mode+priority)
   ```
   
   By default, a destination group works in default mode.
5. Configure a destination collector, including its IP address, port number, transport protocol, priority, and encryption mode.
   
   When the destination group works in default mode, perform the following steps to configure the destination collector.
   * Run the following command if the destination collector uses an IPv4 address:
     ```
     [ipv4-address](cmdqueryname=ipv4-address) ip-address-ipv4 port port-value [ vpn-instance vpn-name ] [ protocol { grpc [ no-tls ] [ compression gzip ] | udp } ]
     ```
     
     By default, no IPv4 destination collector is configured.
   * Run the following command if the destination collector uses an IPv6 address:
     ```
     [ipv6-address](cmdqueryname=ipv6-address) ip-address-ipv6 port port-value [ vpn-instance vpn-name ] [ protocol { grpc [ no-tls ] [ compression gzip ] | udp } ]
     ```
     
     By default, no IPv6 destination collector is configured.![](public_sys-resources/note_3.0-en-us.png) 
   * A maximum of 10 destination groups can be configured.
   * A maximum of 10 IP addresses can be configured for each destination group. That is, the total number of IPv4 and IPv6 addresses cannot exceed 10.
   * A maximum of 10 IP addresses can be configured globally. That is, the total number of IPv4 and IPv6 addresses cannot exceed 10.Both these commands and the [**protocol**](cmdqueryname=protocol) [**(subscription view)**](cmdqueryname=%28subscription+view%29) command can be run to configure a protocol and encryption mode for the destination collector. If the destination collector is associated with a subscription, command configurations take effect based on the following rules:
   * If the [**protocol**](cmdqueryname=protocol) command has been run in the subscription view, the protocol and encryption mode configured in the subscription view take effect.
   * If the [**protocol**](cmdqueryname=protocol) command has not been run in the subscription view, the protocol and encryption mode configured in the destination group view take effect.
   
   
   When the destination group works in priority mode, perform the following steps to configure the destination collector.
   * Run the following command if the destination collector uses an IPv4 address:
     ```
     [ipv4-address](cmdqueryname=ipv4-address) ip-address-ipv4 port port-value [ vpn-instance vpn-name ] [ protocol grpc [ no-tls ] [ compression gzip ] ] priority { low | medium | high }
     ```
     
     By default, no IPv4 destination collector is configured.
   * Run the following command if the destination collector uses an IPv6 address:
     ```
     [ipv6-address](cmdqueryname=ipv6-address) ip-address-ipv6 port port-value [ vpn-instance vpn-name ] [ protocol grpc [ no-tls ] [ compression gzip ] ] priority { low | medium | high }
     ```
     
     By default, no IPv6 destination collector is configured.![](public_sys-resources/note_3.0-en-us.png) 
   
   These commands can be run no more than 40 times for each destination group.
   
   Both these commands and the [**protocol**](cmdqueryname=protocol) [**(subscription view)**](cmdqueryname=%28subscription+view%29) command can be run to configure a protocol and encryption mode for the destination collector. If the destination collector is associated with a subscription, command configurations take effect based on the following rules:
   * If the [**protocol**](cmdqueryname=protocol) command has been run in the subscription view, the protocol and encryption mode configured in the subscription view take effect.
   * If the [**protocol**](cmdqueryname=protocol) command has not been run in the subscription view, the protocol and encryption mode configured in the destination group view take effect.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display telemetry destination**](cmdqueryname=display+telemetry+destination) [ *dest-name* ] command to check information about the destination group.