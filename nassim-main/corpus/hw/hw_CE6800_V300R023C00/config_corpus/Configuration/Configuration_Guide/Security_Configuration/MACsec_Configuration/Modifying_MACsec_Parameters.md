Modifying MACsec Parameters
===========================

Modifying MACsec Parameters

#### Context

You can create and configure a MACsec profile, or modify parameters in an existing MACsec profile.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MACsec profile view.
   
   
   ```
   [mac-security-profile name](cmdqueryname=mac-security-profile+name) profile-name
   ```
3. Configure MACsec parameters.
   
   
   
   **Table 1** Configuring MACsec parameters
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure an MKA key generation algorithm. | **[**mka cryptographic-algorithm**](cmdqueryname=mka+cryptographic-algorithm)** { **aes-cmac-128** | **aes-cmac-256** | **sm4-cmac-128** } | The device uses an MKA key generation algorithm to generate the KEK, ICK, and SAK based on the CAK and CKN.  By default, the MKA key generation algorithm is AES-CMAC-128.  After generating the SAK, the key server sends the encrypted SAK to the peer device through an MKA packet. Upon receipt of the MKA packet, the peer device checks the integrity of the packet. If the check fails, the peer device drops the packet. If the check succeeds, the peer device decrypts the packet to obtain the original SAK. In addition, ensure that the key generation algorithms configured on both ends are the same. Otherwise, the negotiation may fail.  The sm4-cmac-128 algorithm is supported only on the CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL in common forwarding mode, CE6885-SAN, CE6855-48XS8CQ, and CE6863E-48S8CQ. |
   | Configure an encryption algorithm for MACsec data packets. | **[**macsec cipher-suite**](cmdqueryname=macsec+cipher-suite)** { **gcm-aes-128** | **gcm-aes-256** | **gcm-aes-xpn-128** | **gcm-aes-xpn-256** | **gcm-sm4-128** | **gcm-sm4-xpn-128** } \* | After session negotiation is complete, the devices at both ends use the SAK to encrypt and decrypt data packets for encrypted communication.  By default, the encryption algorithms supported by different devices vary. The actually used algorithm is automatically negotiated by the devices at both ends in descending order of encryption strength.  The gcm-sm4-128 and gcm-sm4-xpn-128 algorithms are supported only on the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in common forwarding mode, CE6863E-48S8CQ, CE6885-SAN, and CE6885-SAN. |
   | Configure the MACsec encryption offset. | **[**macsec confidentiality-offset**](cmdqueryname=macsec+confidentiality-offset)** *offset-value* | The MACsec encryption offset indicates from which byte behind the MACsec tag field a data frame is encrypted. The protocol provides three encryption offsets: 0 bytes, 30 bytes, and 50 bytes. For some applications (such as load balancing) that need to identify IPv4/IPv6 headers, packet headers must not be encrypted. In this case, you need to configure the encryption offset.  By default, the MACsec encryption offset is 0 bytes.  If the local end is not the key server, the encryption offset advertised by the key server is used. If the local end is the key server, the locally configured encryption offset is used, and the local end advertises the offset to the remote end. |
   | Configure the MACsec replay protection window size. | **[**macsec replay-window**](cmdqueryname=macsec+replay-window)** *window-size* | To prevent malicious users from repeatedly sending captured data packets, the receiver discards duplicate or out-of-order data packets by default. In some cases, however, data packets are reordered during transmission because their sending priorities are different. As a result, the data packets are out of order when they reach the receiver. To ensure that these out-of-order data packets can be received normally, configure the replay protection window size.  Assume that the replay protection window size configured on the device is a. If the device receives a packet with the sequence number x, the sequence number of the next packet that is allowed to be received must be greater than or equal to (x + 1 - a). Set an appropriate replay protection window size based on the data packet forwarding path on the network. If data packets may be forwarded multiple times, there is a high probability that many of them become out of order. To address this issue, you are advised to increase the replay protection window size. Otherwise, decrease the window size.  By default, the MACsec replay protection window size is 0. |
   | Configure the device to add an SCI to the MACsec frame header. | **[**macsec include-sci**](cmdqueryname=macsec+include-sci)** | An SCI identifies the source of a packet. It consists of the MAC address of an interface and the last two bytes of the interface index. When the device is connected to a non-Huawei device and MACsec is configured on them, the MACsec frame header may need to contain the SCI to identify the source of packets because the implementation of MACsec on the device is different from that on the non-Huawei device. Currently, the device supports only device-to-device MACsec. The two MACsec-enabled interfaces on both devices only establish a session with each other. In this case, the MACsec frame header does not need to contain an SCI.  By default, the MACsec frame header contains an SCI.  The settings of whether the MACsec frame header contains an SCI must be the same at both ends. That is, the MACsec frame header contains an SCI or does not contain an SCI at both ends. |
   | Configure the MKA session timeout period. | **[**mka timer mka-life**](cmdqueryname=mka+timer+mka-life)** *life-time* | After session negotiation is complete and a secure channel is established, the two devices exchange MKA protocol packets to ensure that the session is alive. The MKA protocol defines an MKA session keepalive timer that specifies the timeout period of an MKA session. The local device starts the timer after receiving MKA protocol packets from the remote device.  * If the local device receives subsequent MKA protocol packets within the timeout period, it restarts the timer. * If the local device does not receive subsequent MKA protocol packets within the timeout period, it considers the session insecure, deletes the session, and performs MKA session negotiation again. By default, the MKA session timeout period is 6 seconds. |
   | Configure the SAK timeout period. | **[**mka timer sak-life**](cmdqueryname=mka+timer+sak-life)** *life-time* | When MACsec is used for secure communication, an SAK is used to encrypt and decrypt data packets. To improve the security of data packets, an SAK needs to be replaced when the number of data packets encrypted using the SAK reaches a certain value or the time for using the SAK exceeds a certain period. In this case, the key server generates and advertises a new SAK. You can adjust the SAK timeout period based on site requirements.  By default, the SAK timeout period is 3600 seconds.  If the local end is not the key server, the SAK timeout period advertised by the key server is used. If the local end is the key server, the locally configured SAK timeout period is used, and the local end advertises the SAK timeout period to the remote end. |
   | Configure the MACsec capability value. | [**macsec capability**](cmdqueryname=macsec+capability) *capability-value* | Meanings of MACsec capability values:  * 2: Both integrity check and confidentiality check are supported. Encryption can only start from the packet header. * 3: Both integrity check and confidentiality check are supported. The encryption offset can be 0 bytes (encryption starting from the packet header), 30 bytes, or 50 bytes. By default, the MACsec capability value is 3.  If the local and peer device types are different and the peer device supports only MACsec capability 2, you need to set the MACsec capability value of the local device to be the same as that of the peer device.  When the MACsec capability value is set to 2, setting the MACsec encryption offset to 30 or 50 using the [**macsec confidentiality-offset**](cmdqueryname=macsec+confidentiality-offset) command does not take effect. In this case, the MACsec encryption offset is always 0 (encryption starting from the packet header). |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```