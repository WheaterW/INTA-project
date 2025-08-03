Understanding Defense Against Fragmentation Attacks
===================================================

A fragmentation attack is an attack in which error fragments are sent to a target device, which then crashes, restarts, or consumes a large amount of CPU resources when processing such fragments, ultimately impacting services. Fragmentation attack defense enables a device to detect packet fragments in real time and discard or rate-limit them to protect the device.

Fragmentation attacks are classified into the following types.

#### Excess-Fragment Attack

The offset of IP packets is measured in units of 8-byte blocks. Normally, an IP header has 20 bytes and the maximum payload of an IP packet is 65515 bytes. Therefore, an IP packet can be fragmented into up to 8189 (65515/8) fragments, above which the device would consume a large amount of CPU resources when reassembling packets.

The device considers a packet with over 8189 fragments malicious and discards all of its fragments.


#### Excess-Offset Attack

An attacker sends a fragment with a large offset value to a target device, which then allocates memory space to store all fragments, consuming a large amount of resources.

The offset field is 13 bits long and measured in units of 8-byte blocks, so its theoretical maximum value is 8191. In most cases, however, the value should be smaller than 8190, since an offset of 8190 will lead to the payload (8190 x 8 = 65520) exceeding the maximum (65515). Therefore, the maximum offset is 8189, and the last fragment has a maximum of 3-byte IP payload (8189 x 8 - 65515).

The device considers packets with an offset value larger than 8189 malicious and discards them.


#### Repeated Fragment Attack

A repeated fragment attack is an attack in which fragments are sent to a target host multiple times. Such an attack is carried out in one of two ways:

* The same fragments are sent multiple times, causing high CPU usage or a memory error on the target host.
* Different fragments with the same offset are sent. In this case, the target host cannot determine which fragment will be reserved and which fragment will be discarded, or whether all fragments need to be discarded. As a result, the target host may experience high CPU usage or a memory error.

With defense against packet fragment attacks enabled, the device applies the committed access rate (CAR) limit to packet fragments, reserves the first fragment, and discards all the remaining repeated fragments to protect the CPU.


#### Syndrop Attack

A Syndrop attack exploits the mechanism of IP fragmentation to put the second fragment into the first. The offset of the second fragment is smaller than that of the first fragment, and the offset plus the data field of the second fragment does not exceed the tail of the first fragment. A Syndrop attack uses TCP packets that carry a SYN flag and also IP payload.

As shown in [Figure 1](#EN-US_CONCEPT_0000001513156502__fig_dc_feature_attackdefence_000502):

* The IP payload in the first fragment is 28 bytes, and the IP header is 20 bytes.
* The IP payload in the second fragment is 4 bytes, the IP header is 20 bytes, and the offset is 24 (should be 28).

**Figure 1** Syndrop attack  
![](figure/en-us_image_0000001563756969.png)  

Syndrop attacks cause the system to restart or even crash. With defense against fragmentation attacks enabled, the device discards all fragments in a Syndrop attack.


#### NewTear Attack

A NewTear attack uses error fragments. As shown in [Figure 2](#EN-US_CONCEPT_0000001513156502__fig695314344574), the protocol is UDP.

* The IP payload in the first fragment is 28 bytes including the UDP header. The UDP checksum is 0.
* The IP payload in the second fragment is 4 bytes, and the offset is 24 (should be 28).

**Figure 2** NewTear attack  
![](figure/en-us_image_0000001563996873.png)

NewTear attacks cause the system to restart or even crash. With defense against fragmentation attacks enabled, the device discards all fragments in a NewTear attack.


#### Bonk Attack

A Bonk attack uses error fragments. As shown in [Figure 3](#EN-US_CONCEPT_0000001513156502__fig_dc_feature_attackdefence_000504), the protocol is UDP.

* The IP payload in the first fragment is 36 bytes including the UDP header. The UDP checksum is 0.
* The IP payload in the second fragment is 4 bytes, and the offset is 32 (should be 36).

**Figure 3** Bonk attack  
![](figure/en-us_image_0000001513156598.png)

Bonk attacks cause the system to restart or even crash. With defense against fragmentation attacks enabled, the device discards all fragments in a Bonk attack.


#### Nesta Attack

A Nesta attack uses error fragments. As shown in [Figure 4](#EN-US_CONCEPT_0000001513156502__fig_dc_feature_attackdefence_000505):

* The IP payload in the first fragment is 18 bytes, the protocol used is UDP, and the checksum is 0.
* The offset in the second fragment is 48 and the IP payload is 116 bytes.
* The offset in the third fragment is 0, the More Frag field is 1 (meaning there are more fragments), the IP option (all EOLs) is 40 bytes, and the IP payload is 224 bytes.

**Figure 4** Nesta attack  
![](figure/en-us_image_0000001563756981.png)

Nesta attacks cause the system to restart or even crash. With defense against fragmentation attacks enabled, the device discards all fragments in a Nesta attack.