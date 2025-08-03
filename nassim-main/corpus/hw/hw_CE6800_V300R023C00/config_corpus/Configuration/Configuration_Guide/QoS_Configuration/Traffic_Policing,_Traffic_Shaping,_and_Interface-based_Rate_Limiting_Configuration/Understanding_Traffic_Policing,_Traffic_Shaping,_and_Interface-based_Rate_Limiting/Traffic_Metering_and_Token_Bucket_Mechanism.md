Traffic Metering and Token Bucket Mechanism
===========================================

Traffic Metering and Token Bucket Mechanism

#### Overview

Traffic metering is the prerequisite for implementing traffic policing, traffic shaping, and interface-based rate limiting. In traffic metering, network devices determine whether the rate of incoming traffic exceeds a defined limit and take appropriate actions. Generally, the token bucket mechanism is used to measure traffic.

A token bucket is a container that stores a specific number of tokens. The system places tokens into a token bucket at the configured rate. If the token bucket is full, excess tokens overflow. The system determines whether the bucket has enough tokens for packet forwarding. Otherwise, the traffic rate exceeds or violates the rate limit.

RFC standards define the following token bucket algorithms:

* The single rate three color marker (srTCM) algorithm determines traffic bursts based on the length of packets.
* The two rate three color marker (trTCM) algorithm determines traffic bursts based on the rate of packets.

The token bucket algorithms mark packets red, yellow, or green based on the result of traffic metering. The system then processes the packets according to their marked color. The two aforementioned algorithms can work in color-aware and color-blind modes. The color-blind mode is used as an example in the following section.


#### Single-Rate-Two-Bucket Mechanism

The single-rate-two-bucket mechanism uses the srTCM algorithm defined in RFC 2697 to measure traffic and marks packets green, yellow, or red based on the metering result.

As shown in [Figure 1](#EN-US_CONCEPT_0000001564129865__fig1722881035111), bucket C (also called CIR token bucket) and bucket E (also called EIR token bucket) contain Tc and Te tokens, respectively. The single-rate-two-bucket mechanism uses three parameters:

* Committed information rate (CIR): indicates the rate at which tokens are placed into bucket C, that is, the average traffic rate that bucket C allows.
* Committed burst size (CBS): indicates the capacity of bucket C, that is, the maximum volume of burst traffic that bucket C allows.
* Excess burst size (EBS): indicates the capacity of bucket E, that is, the maximum volume of excess burst traffic that bucket E allows.

The system places tokens into bucket C at the CIR:

* If Tc is less than the CBS, Tc increases.
* If Tc is equal to the CBS but Te is less than the EBS, Te increases.
* If Tc is equal to the CBS and Te is equal to the EBS, Tc and Te do not increase.

B indicates the size of an arriving packet:

* If B is less than or equal to Tc, the packet is marked green, and Tc decreases by B.
* If B is greater than Tc and less than or equal to Te, the packet is marked yellow and Te decreases by B.
* If B is greater than Te, the packet is marked red, and Tc and Te remain unchanged.

The single-rate-two-bucket mechanism allows burst traffic. When the traffic rate is lower than the CIR, packets are marked green. When the burst traffic volume is greater than the CBS but lower than the EBS, packets are marked yellow. When the volume is greater than the EBS, packets are marked red.

**Figure 1** Single-rate-two-bucket mechanism  
![](figure/en-us_image_0000001951356464.png)

The preceding example uses the CIR of 1 Mbit/s and the CBS and EBS of 2000 bytes each. Buckets C and E are initially full of tokens. In single-rate-two-bucket mode, the token buckets process packets as follows:

![](public_sys-resources/note_3.0-en-us.png) 

Here, 1 Mbit/s is equal to 1 x 106 bit/s.

* Assuming that the first packet arriving at the interface is 1500 bytes long, the packet is marked green because the number of tokens in bucket C is greater than the packet length. The number of tokens in bucket C then decreases by 1500 bytes, with 500 bytes remaining. The number of tokens in bucket E remains unchanged.
* Assuming that the second packet arriving at the interface after a delay of 1 ms is 1500 bytes long, additional 125-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 1 ms = 1000 bits = 125 bytes). Bucket C now has 625-byte tokens, which are insufficient for the 1500-byte second packet. Bucket E has 2000-byte tokens, which are sufficient for the second packet. Therefore, the second packet is marked yellow. Subsequently, the number of tokens in bucket E decreases by 1500 bytes, with 500 bytes remaining. The number of tokens in bucket C remains unchanged.
* Assuming that the third packet arriving at the interface after a delay of 1 ms is 1000 bytes long, as with the second packet, additional 125-byte tokens are placed into bucket C. Bucket C now has 750-byte tokens, which are insufficient for the 1000-byte third packet. The tokens in bucket E are also insufficient; therefore, the third packet is marked red. The numbers of tokens in buckets C and E remain unchanged.
* Assuming that the fourth packet arriving at the interface after a delay of 20 ms is 1500 bytes long, as with the preceding packets, additional 2500-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 20 ms = 20000 bits = 2500 bytes). Bucket C now has 3250-byte tokens. The 1250-byte tokens exceeding the CBS (2000 bytes) are placed into bucket E. Now, bucket E has 1750-byte tokens. The packet is marked green because the number of tokens in bucket C is greater than the packet length. The number of tokens in bucket C decreases by 1500 bytes, with 500 bytes remaining. The number of tokens in bucket E remains unchanged.

[Table 1](#EN-US_CONCEPT_0000001564129865__table_001) describes packet processing.

**Table 1** Packet processing in single-rate-two-bucket mode
| **Packet No.** | **Time (ms)** | **Packet Length (Bytes)** | **Delay (ms)** | **Token Addition (Bytes)** | **Number of Tokens Before Packet Processing (Bytes)** | | **Number of Tokens After Packet Processing (Bytes)** | | **Marking** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bucket C** | **Bucket E** | **Bucket C** | **Bucket E** |
| - | - | - | - | - | 2000 | 2000 | 2000 | 2000 | - |
| 1 | 0 | 1500 | 0 | 0 | 2000 | 2000 | 500 | 2000 | Green |
| 2 | 1 | 1500 | 1 | 125 | 625 | 2000 | 625 | 500 | Yellow |
| 3 | 2 | 1000 | 1 | 125 | 750 | 500 | 750 | 500 | Red |
| 4 | 22 | 1500 | 20 | 2500 | 2000 | 1750 | 500 | 1750 | Green |



#### Single-Rate-Single-Bucket Mechanism

If burst traffic is not allowed, the EBS must be set to 0 in single-rate-two-bucket mode. In this case, only one token bucket is used because there are always 0 tokens in bucket E.

As shown in [Figure 2](#EN-US_CONCEPT_0000001564129865__fig94607257511), bucket C contains Tc tokens. The single-rate-single-bucket mechanism uses two parameters:

* CIR: indicates the rate at which tokens are placed into bucket C, that is, the average traffic rate that bucket C allows.
* CBS: indicates the capacity of bucket C, that is, the maximum volume of burst traffic that bucket C allows.

The system places tokens into the bucket at the CIR. If Tc is less than the CBS, Tc increases. If Tc is greater than or equal to the CBS, Tc remains unchanged.

B indicates the size of an arriving packet:

* If B is less than or equal to Tc, the packet is marked green, and Tc decreases by B.
* If B is greater than Tc, the packet is marked red, and Tc remains unchanged.

The single-rate-single-bucket mechanism does not allow burst traffic. When the traffic rate is lower than the CIR, packets are marked green. When the rate is higher than the CIR, packets are marked red.

**Figure 2** Single-rate-single-bucket mechanism  
![](figure/en-us_image_0000001513169774.png)

This example uses the CIR of 1 Mbit/s and the CBS of 2000 bytes. Bucket C is initially full of tokens. In single-rate-single-bucket mode, the token bucket processes packets as follows:

![](public_sys-resources/note_3.0-en-us.png) 

Here, 1 Mbit/s is equal to 1 x 106 bit/s.

* Assuming that the first packet arriving at the interface is 1500 bytes long, the packet is marked green because the number of tokens in bucket C is greater than the packet length. The number of tokens in bucket C then decreases by 1500 bytes, with 500 bytes remaining.
* Assuming that the second packet arriving at the interface after a delay of 1 ms is 1500 bytes long, additional 125-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 1 ms = 1000 bits = 125 bytes). Bucket C now has 625-byte tokens. Tokens in bucket C are insufficient, so the second packet is marked red.
* Assuming that the third packet arriving at the interface after a delay of 1 ms is 1000 bytes long, additional 125-byte tokens are placed into bucket C. Bucket C now has 750-byte tokens. Tokens in bucket C are insufficient, so the third packet is marked red.
* Assuming that the fourth packet arriving at the interface after a delay of 20 ms is 1500 bytes long, additional 2500-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 20 ms = 20000 bits = 2500 bytes). Bucket C now has 3250-byte tokens. However, bucket C can have a maximum of 2000-byte tokens. Therefore, the CBS is 2000 bytes. The packet is marked green because the number of tokens in bucket C is greater than the packet length. The number of tokens in bucket C decreases by 1500 bytes, with 500 bytes remaining.

[Table 2](#EN-US_CONCEPT_0000001564129865__table_002) describes packet processing.

**Table 2** Packet processing in single-rate-single-bucket mode
| Packet No. | Time (ms) | Packet Length (Bytes) | Delay (ms) | Token Addition (Bytes) | Number of Tokens Before Packet Processing (Bytes) | Number of Tokens After Packet Processing (Bytes) | Marking |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | - | 2000 | 2000 | - |
| 1 | 0 | 1500 | 0 | 0 | 2000 | 500 | Green |
| 2 | 1 | 1500 | 1 | 125 | 625 | 625 | Red |
| 3 | 2 | 1000 | 1 | 125 | 750 | 750 | Red |
| 4 | 22 | 1500 | 20 | 2500 | 2000 | 500 | Green |



#### Two-Rate-Two-Bucket Mechanism

The two-rate-two-bucket mechanism uses the trTCM algorithm defined in RFC 2698 to measure traffic and marks packets green, yellow, or red based on the metering result.

As shown in [Figure 3](#EN-US_CONCEPT_0000001564129865__fig13172140115116), buckets P and C contain Tp and Tc tokens respectively. The two-rate-two-bucket mechanism uses four parameters:

* Peak information rate (PIR): indicates the rate at which tokens are placed into bucket P, that is, the maximum traffic rate that bucket P allows. The PIR is greater than the CIR.
* CIR: indicates the rate at which tokens are placed into bucket C, that is, the average traffic rate that bucket C allows.
* Peak burst size (PBS): indicates the capacity of bucket P, that is, the maximum volume of burst traffic that bucket P allows.
* CBS: indicates the capacity of bucket C, that is, the maximum volume of burst traffic that bucket C allows.

The system places tokens into bucket P at the PIR and places tokens into bucket C at the CIR:

* If Tp is less than the PBS, Tp increases. If Tp is greater than or equal to the PBS, Tp remains unchanged.
* If Tc is less than the CBS, Tc increases. If Tc is greater than or equal to the CBS, Tp remains unchanged.

B indicates the size of an arriving packet:

* If B is greater than Tp, the packet is marked red.
* If B is greater than Tc and less than or equal to Tp, the packet is marked yellow and Tp decreases by B.
* If B is less than or equal to Tc, the packet is marked green, and Tp and Tc decrease by B.

The two-rate-two-bucket mechanism enables burst traffic rates. When the traffic rate is lower than the CIR, packets are marked green. When the rate is higher than the CIR but less than the PIR, packets are marked yellow. When the rate is higher than the PIR, packets are marked red.

**Figure 3** Two-rate-two-bucket mechanism  
![](figure/en-us_image_0000001564010041.png)

This example uses the CIR of 1 Mbit/s, the PIR of 2 Mbit/s, the CBS of 2000 bytes, and the PBS of 3000 bytes. Buckets C and P are initially full of tokens. In two-rate-two-bucket mode, the token buckets process packets as follows:

![](public_sys-resources/note_3.0-en-us.png) 

Here, 1 Mbit/s is equal to 1 x 106 bit/s.

* If the first packet arriving at the interface is 1500 bytes long, the packet is marked green because the numbers of tokens in both buckets P and C are greater than the packet length. The numbers of tokens in both buckets P and C then decrease by 1500 bytes, with 500 and 1500 bytes remaining in bucket C and bucket P, respectively.
* Assume that the second packet arriving at the interface after a delay of 1 ms is 1800 bytes long. Additional 250-byte tokens are placed into bucket P (PIR x time period = 2 Mbit/s x 1 ms = 2000 bits = 250 bytes). Bucket P now has 1750-byte tokens, and is smaller than the packet length. Additional 125-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 1 ms = 1000 bits = 125 bytes). Bucket C now has 625-byte tokens. Therefore, the second packet is marked red, and the numbers of tokens in buckets P and C remain unchanged.
* Assume that the third packet arriving at the interface after a delay of 1 ms is 1000 bytes long. Additional 250-byte tokens are placed into bucket P. Bucket P now has 2000-byte tokens, and is larger than the packet length. Additional 125-byte tokens are placed into bucket C. Bucket C now has 750-byte tokens, and is still smaller than the packet length. The packet is marked yellow. The number of tokens in bucket P decreases by 1000 bytes, with 1000 bytes remaining. The number of tokens in bucket C remains unchanged.
* Assume that the fourth packet arriving at the interface after a delay of 20 ms is 1500 bytes long. Additional 5000-byte tokens are placed into bucket P (PIR x time period = 2 Mbit/s x 20 ms = 40000 bits = 5000 bytes), but tokens that exceed the PBS (3000 bytes) are dropped. Bucket P has 3000-byte tokens, which are sufficient for the 1500-byte fourth packet. Additional 2500-byte tokens are placed into bucket C (CIR x time period = 1 Mbit/s x 20 ms = 20000 bits = 2500 bytes), but tokens that exceed the CBS (2000 bytes) are dropped. Bucket C then has 2000-byte tokens, which are sufficient for the 1500-byte fourth packet. Therefore, the fourth packet is marked green. The number of tokens in bucket P decreases by 1500 bytes, with 1500 bytes remaining. The number of tokens in bucket C decreases by 1500 bytes, with 500 bytes remaining.

[Table 3](#EN-US_CONCEPT_0000001564129865__table_003) describes packet processing.

**Table 3** Packet processing in two-rate-two-bucket mode
| **Packet No.** | **Time (ms)** | **Packet Length (Bytes)** | **Delay (ms)** | **Token Addition (Bytes)** | | **Number of Tokens Before Packet Processing (Bytes)** | | **Number of Tokens After Packet Processing (Bytes)** | | **Marking** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Bucket C** | **Bucket P** | **Bucket C** | **Bucket P** | **Bucket C** | **Bucket P** |
| - | - | - | - | - | - | 2000 | 3000 | 2000 | 3000 | - |
| 1 | 0 | 1500 | 0 | 0 | 0 | 2000 | 3000 | 500 | 1500 | Green |
| 2 | 1 | 1800 | 1 | 125 | 250 | 625 | 1750 | 625 | 1750 | Red |
| 3 | 2 | 1000 | 1 | 125 | 250 | 750 | 2000 | 750 | 1000 | Yellow |
| 4 | 22 | 1500 | 20 | 2500 | 5000 | 2000 | 3000 | 500 | 1500 | Green |



#### Difference and Application of Three Token Bucket Modes

[Table 4](#EN-US_CONCEPT_0000001564129865__table_004) describes the difference and relationship between the three token bucket modes.

**Table 4** Difference and relationship of three token bucket modes
| Difference | Single-Rate-Single-Bucket | Single-Rate-Two-Bucket | Two-Rate-Two-Bucket |
| --- | --- | --- | --- |
| Parameters | CIR and CBS | CIR, CBS, and EBS | CIR, CBS, PIR, and PBS |
| Mode in which tokens are placed | Tokens are placed into bucket C at the CIR. Excess tokens are dropped when bucket C is full. | When bucket C is full, excess tokens are placed into bucket E. When buckets C and E are not full, tokens are placed only into bucket C. | Tokens are placed into bucket C at the CIR and into bucket P at the PIR. Buckets C and P are independent. Excess tokens are dropped when buckets C and P are full. |
| Burst traffic | Traffic burst is not allowed. Packet processing is implemented only when bucket C has a sufficient number of tokens. | Traffic burst is allowed. Tokens in bucket C are used first. When tokens in bucket C are insufficient, tokens in bucket E are used. | Traffic burst is allowed. When buckets C and P have sufficient tokens, tokens in both buckets are used. When tokens in bucket C are insufficient, tokens in only bucket P are used. |
| Marking result | Green or red | Green, yellow, or red | Green, yellow, or red |
| Relationship | In single-rate-two-bucket mode, if the EBS is 0, the effect is the same as that in single-rate-single-bucket mode.  In two-rate-two-bucket mode, if the PIR is equal to the CIR, the effect is the same as that in single-rate-two-bucket mode. | | |

[Table 5](#EN-US_CONCEPT_0000001564129865__table_005) describes the functions and scenarios of the three token bucket modes.

**Table 5** Functions and application scenarios of the three token bucket modes
| Token Bucket Mode | Function | Application Scenario |
| --- | --- | --- |
| Single-rate-single-bucket | Limits bandwidth. | Discards low-priority services, such as extranet HTTP traffic and excess traffic. |
| Single-rate-two-bucket | Limits bandwidth, allows certain traffic bursts, and distinguishes burst and normal services. | Reserves bandwidth for important services or burst traffic (for example, email data). |
| Two-rate-two-bucket | Limits bandwidth, allocates bandwidth, and determines whether the bandwidth is less than the CIR or is in the range of the CIR and PIR. | Recommended for important services because it better monitors burst traffic and guides traffic analysis. |



#### Color-Aware Mode

In color-aware mode, the color of an arriving packet affects the metering results of the token bucket mechanism in the following ways:

* If the packet has been marked green, the metering mechanism is the same as that in color-blind mode.
* If the packet has been marked yellow, the system marks the packet yellow if it conforms to the limit or marks the packet red if it violates the limit. This depends on the packet length and the number of tokens. In single-rate-single-bucket mode, the packet is marked red directly.
* If the packet has been marked red, it is also marked red in the token bucket.