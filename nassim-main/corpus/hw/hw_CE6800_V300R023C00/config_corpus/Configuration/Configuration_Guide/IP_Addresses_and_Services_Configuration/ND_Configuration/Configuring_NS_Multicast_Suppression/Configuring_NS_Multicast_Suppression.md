Configuring NS Multicast Suppression
====================================

Configuring NS Multicast Suppression

#### Context

On an IPv6 overlay network, IPv6 host neighbor discovery is implemented through NS multicast. When a gateway receives an NS message for IPv6 address resolution, it multicasts the message in its BD. If the gateway forwards a large number of NS messages that are received within a period of time, excessive VXLAN resources are consumed, affecting normal services. To address this issue, configure NS multicast suppression. After this function is configured, the gateway checks whether it can obtain the destination user information in a received NS message. If so, it performs proxy ND or multicast-to-unicast processing to reduce or suppress NS message flooding.

NS multicast suppression can also prevent ND spoofing attacks. In an ND spoofing attack, an attacker associates its MAC address with the IPv6 address of a host so that all traffic destined for the IPv6 address is sent to the attacker. After NS multicast suppression is enabled, an IPv6 address conflict alarm is generated through proxy ND table conflict detection to notify users of possible ND spoofing attacks.

Only VXLAN gateways support this function. For details about VXLAN support, see "[Configuration Precautions for VXLAN](spec/VXLAN_limitation_23.0.html)" in VXLAN Configuration.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id 
   ```
3. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
4. Enable NS multicast suppression.
   
   
   ```
   [ipv6 nd multicast-suppress { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable](cmdqueryname=ipv6+nd+multicast-suppress+%7B+proxy-reply+%5B+unknown-options-unicast+%5D+%7C+unicast-forward+%7D+%5B+mismatch-discard+%5D+enable)
   ```
5. Configure proxy ND parameters.
   
   
   
   **Table 1** Configure proxy ND parameters.
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the R flag for NA messages when proxy ND is performed. | [**ipv6 nd multicast-suppress**](cmdqueryname=ipv6+nd+multicast-suppress) { **host** | **router** } | During interconnection with a non-Huawei device, if the proxy ND entries that the local device synchronizes from the remote device through EVPN routes do not carry the R flag, the local device cannot determine whether the device that replies with an NA message is a routing device or host. To allow the local device to make this determination, configure the R flag for NA messages. |
   | Configure the maximum number of dynamic proxy ND entries that can be learned in a BD. | [**ipv6 nd multicast-suppress dynamic limit**](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+limit) *limit-value* | When an attacker sends a large number of RA messages to attack a device, the device learns a large number of dynamic proxy ND entries within a short period of time. As a result, the CPU usage increases quickly, and a large amount of memory resources are consumed. To limit the maximum number of dynamic proxy ND entries that can be learned in a BD, run this command. This effectively prevents the overflow of dynamic proxy ND entries and ensures normal device running. |
   | Configure an aging time for dynamic proxy ND entries. | [**ipv6 nd multicast-suppress dynamic expire-time**](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+expire-time) *expire-time-value* | Every dynamic proxy ND entry has a lifecycle, which is also called aging time. If a dynamic proxy ND entry is not updated after its lifecycle ends, this entry is deleted from the proxy ND table. If the entry is updated before its lifecycle ends, its aging time is recalculated. This command ensures that dynamic proxy ND entries are promptly updated. |
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
7. Enable the device to flood a proxy ND table or ND table through EVPN routes.
   * If no Layer 3 gateway exists, perform the following operations:
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the BD view.
        ```
        [bridge-domain](cmdqueryname=bridge-domain) bd-id
        ```
     3. Enable IPv6.
        ```
        [ipv6 enable](cmdqueryname=ipv6+enable)
        ```
     4. Enable the device to flood a proxy ND table through EVPN routes.
        ```
        [ipv6 nd collect host enable](cmdqueryname=ipv6+nd+collect+host+enable)
        ```
     5. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * If a Layer 3 gateway exists, perform the following operations:
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the VBDIF interface view.
        ```
        [interface vbdif](cmdqueryname=interface+vbdif) bd-id
        ```
     3. Enable IPv6.
        ```
        [ipv6 enable](cmdqueryname=ipv6+enable)
        ```
     4. Enable the device to flood an ND table through EVPN routes.
        ```
        [ipv6 nd collect host enable](cmdqueryname=ipv6+nd+collect+host+enable)
        ```
     5. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
8. Configure BGP EVPN to advertise routes.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BGP view or BGP multi-instance view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
      ```
   3. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
   4. Configure IRBv6 or ND route advertisement.
      
      
      ```
      [peer](cmdqueryname=peer) { ipv4-address | group-name } advertise { irbv6 | nd }
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display ipv6 nd multicast-suppress bridge-domain**](cmdqueryname=display+ipv6+nd+multicast-suppress+bridge-domain) [ *bd-id* ] [ **verbose** ] command to check information about the proxy ND table in the BD.