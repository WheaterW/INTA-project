Verifying the Configuration
===========================

After completing the configuration, check the tunnel establishment.

#### Prerequisites

The IPsec tunnel in IKE automatic negotiation mode has been configured.


#### Procedure

1. Check whether the IPsec VPN is available.
   
   
   
   In this example, intranet DeviceA and DeviceB are on two ends of an IPsec tunnel. Configure DeviceA to ping DeviceB.
   
   * If the ping succeeds, the IPsec VPN is established.
   * If the ping fails, the IPsec VPN is not established. This is because that intranet or Internet routes are unavailable, or the IPsec configuration is incorrect.
2. Check whether the route between each intranet device and the IPsec gateway is available, and whether the route between the IPsec gateways is available. If a route is unavailable, configure the route again. If the routes are available, check the IPsec configurations.
3. Run the [**display ipsec statistics**](cmdqueryname=display+ipsec+statistics) command to check statistics about packets processed (encrypted and decrypted) by IPsec.
4. Run the **display ike sa** [ { **remote** **remoteaddress** } | **verbose** { { **remote** **remoteaddress** } | { **conn\_id** *connid* **slot** *slot-id* } | { **peer** *peername* [ **identity** *peeridentity* ] } } | **slot** *slot-id* | { **peer** *peername* [ **identity** *peeridentity* ] } ] command to check SA establishment.
5. If the SA is not established, run the following commands in the user view to check the IPsec configurations.
   1. Run the [**display ike proposal**](cmdqueryname=display+ike+proposal) command to check IKE proposal information. Ensure that the encryption algorithm, authentication method, authentication algorithm, and DH group ID used at one end of the IPsec tunnel are the same as those used at the other end.
   2. Run the [**display ike peer**](cmdqueryname=display+ike+peer+name+brief) [ **name** *peer-name* | **brief** ] command to check IKE peer configurations. Ensure that the IKE version and authentication method used at one end of the IPsec tunnel are the same as those used at the other end.
   3. Run the [**display ipsec proposal**](cmdqueryname=display+ipsec+proposal) command to check IPsec proposal information. Ensure that the encapsulation mode, security protocol, encryption algorithm, and authentication algorithm used at one end of the IPsec tunnel are the same as those used at the other end.
   4. Run the [**display ipsec policy-template**](cmdqueryname=display+ipsec+policy-template+brief+name) [ **brief** | **name** *policy-template-name* [ *seq-number* ] ] command to check IPsec policy template information.
   5. Run the [**display ipsec policy**](cmdqueryname=display+ipsec+policy+brief+name) [ **brief** | **name** *policy-name* [ *seq-number* ] ] command to check IPsec policy information.
   6. Run the [**display ipsec sa**](cmdqueryname=display+ipsec+sa) command to check SA configurations. Ensure that the SA configurations at one end of the IPsec tunnel match those at the other end.
6. Run the [**display ike statistics**](cmdqueryname=display+ike+statistics+all+msg+v2+slot) { **all** | **msg** | **v2** } [ **slot** *slot-id* ] command to check IKE packet statistics.
7. Run the [**display ike offline history**](cmdqueryname=display+ike+offline+history+peer-ip+vpn-instance-name+port+slot) [ **peer-ip** *peer-ip* [ **vpn-instance-name** *vpn-instance-name* ] [ **port** *port* ] ] [ **slot** *slot-id* ] command to check historical logout information about IKE SAs.
8. Run the [**display ike error history**](cmdqueryname=display+ike+error+history+peer-ip+vpn-instance-name+port+slot) [ **peer-ip** *peer-ip* [ **vpn-instance-name** *vpn-instance-name* ] [ **port** *port* ] ] [ **slot** *slot-id* ] command to check error information about IKE SA negotiation failures.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the peer device is not a Huawei device and IKE negotiation authentication fails (Error REASON: Authentication Fail), the failure may be caused by the peer end's incompatibility with the payload of the certificate request type in IKE negotiation packets. In this case, run the [**ike payload compatible enable**](cmdqueryname=ike+compatible+enable) command to enable IKE payload compatibility. After this function is enabled, payload of the certificate request type is not encapsulated in the IKE negotiation packets sent in shared-key mode. This prevents negotiation failures caused by payload incompatibility.
9. Run the [**display ipsec sa-expire statistics**](cmdqueryname=display+ipsec+sa-expire+statistics) command to check statistics about expired SAs.
10. Run the [**display ipsec bandwidth**](cmdqueryname=display+ipsec+bandwidth+slot) [ **slot** *slot-id* ] command to check the bandwidth configured in the IPsec license.