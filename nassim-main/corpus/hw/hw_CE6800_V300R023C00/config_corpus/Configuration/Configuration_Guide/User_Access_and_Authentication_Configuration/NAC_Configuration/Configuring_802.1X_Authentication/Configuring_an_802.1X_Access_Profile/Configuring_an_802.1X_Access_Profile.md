Configuring an 802.1X Access Profile
====================================

Configuring an 802.1X Access Profile

#### Context

The device uses 802.1X access profiles to uniformly manage 802.1X access configurations. Before configuring 802.1X authentication, you need to create an 802.1X access profile. You need to select a proper authentication mode based on the ones supported by the 802.1X client and authentication server as well as the processing capabilities of the device and server.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an 802.1X access profile and enter the 802.1X access profile view.
   
   
   ```
   [dot1x-access-profile](cmdqueryname=dot1x-access-profile) name access-profile-name
   ```
   
   To delete an 802.1X access profile, ensure that it is not bound to any authentication profile.
3. Configure the authentication mode for 802.1X users.
   
   
   ```
   [dot1x authentication-method](cmdqueryname=dot1x+authentication-method) { chap | pap | eap }
   ```
   
   By default, the authentication mode of 802.1X users is **eap**, namely, EAP relay authentication.
   
   The processing capabilities of the RADIUS server determine whether EAP termination or EAP relay authentication is used. If the RADIUS server has high processing capabilities and can parse a large number of EAP packets before authentication, the EAP relay mode (specified by the **eap** parameter) is recommended. If the processing capabilities of the RADIUS server cannot parse a large number of EAP packets and complete authentication, the EAP termination mode (specified by the **pap** or **chap** parameter) is recommended, where the device parses EAP packets for the RADIUS server. When configuring the authentication packet processing method, ensure that both the client and server support it; otherwise, the user cannot pass authentication.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Both CHAP authentication and PAP authentication use the insecure MD5 algorithm, so EAP authentication is recommended.
   * The authentication mode for 802.1X users can be set to EAP relay only when RADIUS authentication is used.
   * If AAA local authentication is used, the authentication mode for 802.1X users can only be set to EAP termination.
   * If the 802.1X client uses MD5 encryption, the authentication mode can be set to EAP or CHAP on the device. If the 802.1X client uses PEAP authentication, the authentication mode can be set to EAP on the device.
   * When there is an online 802.1X user on an interface and the authentication mode is modified in the 802.1X access profile bound to the interface, the user is logged out if the authentication mode is changed between EAP termination and EAP relay. If the authentication mode is changed between CHAP and PAP in EAP termination mode, the user remains online.
4. (Optional) Configure the authorization state of an interface.
   
   
   ```
   [dot1x port-control](cmdqueryname=dot1x+port-control) { auto | authorized-force | unauthorized-force }
   ```
   
   By default, the authorization state of an interface is **auto**.
5. (Optional) Configure the packet type that can trigger 802.1X authentication.
   
   
   ```
   [authentication trigger-condition](cmdqueryname=authentication+trigger-condition) { dhcp | arp | dhcpv6 | nd | any-l2-packet } *
   ```
   
   By default, DHCP, ARP, DHCPv6, and ND packets can trigger 802.1X authentication.
6. (Optional) Configure the device to send EAP packets with a code number to 802.1X users.
   
   
   ```
   [dot1x eap-notify-packet](cmdqueryname=dot1x+eap-notify-packet) eap-code code-num data-type type-num
   ```
   
   By default, the device does not send EAP packets with a code number to 802.1X users.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an H3C iMC functions as the RADIUS server, run the **dot1x eap-notify-packet eap-code 10 data-type 25** command on the device.
7. (Optional) Run the [**dot1x send-packet untagged**](cmdqueryname=dot1x+send-packet+untagged) command to enable the function of removing VLAN tags from 802.1X packets sent from an access device to terminals.
   
   
   
   By default, the function of removing VLAN tags from 802.1X packets sent from an access device to terminals is not enabled.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```