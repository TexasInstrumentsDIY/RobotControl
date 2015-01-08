#!/usr/bin/env python

def to(v):
    x = v & 0x0F
    y = (v >> 4) & 0x07
    print "x: {:02}, 2^y: {:03} ".format(x, 2**y),
    return 0.262 * x * 2**y


for i in range(128):
    print "{:03}({})({}): {}".format(i, hex(i), bin(i), to(i))


# 2**y == [1, 2, 4, 8, 16, 32, 64, 128]
# x == [0-15]

"""
x: 00, 2^y: 001  000(0x0)(0b0): 0.0
x: 01, 2^y: 001  001(0x1)(0b1): 0.262
x: 02, 2^y: 001  002(0x2)(0b10): 0.524
x: 03, 2^y: 001  003(0x3)(0b11): 0.786
x: 04, 2^y: 001  004(0x4)(0b100): 1.048
x: 05, 2^y: 001  005(0x5)(0b101): 1.31
x: 06, 2^y: 001  006(0x6)(0b110): 1.572
x: 07, 2^y: 001  007(0x7)(0b111): 1.834
x: 08, 2^y: 001  008(0x8)(0b1000): 2.096
x: 09, 2^y: 001  009(0x9)(0b1001): 2.358
x: 10, 2^y: 001  010(0xa)(0b1010): 2.62
x: 11, 2^y: 001  011(0xb)(0b1011): 2.882
x: 12, 2^y: 001  012(0xc)(0b1100): 3.144
x: 13, 2^y: 001  013(0xd)(0b1101): 3.406
x: 14, 2^y: 001  014(0xe)(0b1110): 3.668
x: 15, 2^y: 001  015(0xf)(0b1111): 3.93
x: 00, 2^y: 002  016(0x10)(0b10000): 0.0
x: 01, 2^y: 002  017(0x11)(0b10001): 0.524
x: 02, 2^y: 002  018(0x12)(0b10010): 1.048
x: 03, 2^y: 002  019(0x13)(0b10011): 1.572
x: 04, 2^y: 002  020(0x14)(0b10100): 2.096
x: 05, 2^y: 002  021(0x15)(0b10101): 2.62
x: 06, 2^y: 002  022(0x16)(0b10110): 3.144
x: 07, 2^y: 002  023(0x17)(0b10111): 3.668
x: 08, 2^y: 002  024(0x18)(0b11000): 4.192
x: 09, 2^y: 002  025(0x19)(0b11001): 4.716
x: 10, 2^y: 002  026(0x1a)(0b11010): 5.24
x: 11, 2^y: 002  027(0x1b)(0b11011): 5.764
x: 12, 2^y: 002  028(0x1c)(0b11100): 6.288
x: 13, 2^y: 002  029(0x1d)(0b11101): 6.812
x: 14, 2^y: 002  030(0x1e)(0b11110): 7.336
x: 15, 2^y: 002  031(0x1f)(0b11111): 7.86
x: 00, 2^y: 004  032(0x20)(0b100000): 0.0
x: 01, 2^y: 004  033(0x21)(0b100001): 1.048
x: 02, 2^y: 004  034(0x22)(0b100010): 2.096
x: 03, 2^y: 004  035(0x23)(0b100011): 3.144
x: 04, 2^y: 004  036(0x24)(0b100100): 4.192
x: 05, 2^y: 004  037(0x25)(0b100101): 5.24
x: 06, 2^y: 004  038(0x26)(0b100110): 6.288
x: 07, 2^y: 004  039(0x27)(0b100111): 7.336
x: 08, 2^y: 004  040(0x28)(0b101000): 8.384
x: 09, 2^y: 004  041(0x29)(0b101001): 9.432
x: 10, 2^y: 004  042(0x2a)(0b101010): 10.48
x: 11, 2^y: 004  043(0x2b)(0b101011): 11.528
x: 12, 2^y: 004  044(0x2c)(0b101100): 12.576
x: 13, 2^y: 004  045(0x2d)(0b101101): 13.624
x: 14, 2^y: 004  046(0x2e)(0b101110): 14.672
x: 15, 2^y: 004  047(0x2f)(0b101111): 15.72
x: 00, 2^y: 008  048(0x30)(0b110000): 0.0
x: 01, 2^y: 008  049(0x31)(0b110001): 2.096
x: 02, 2^y: 008  050(0x32)(0b110010): 4.192
x: 03, 2^y: 008  051(0x33)(0b110011): 6.288
x: 04, 2^y: 008  052(0x34)(0b110100): 8.384
x: 05, 2^y: 008  053(0x35)(0b110101): 10.48
x: 06, 2^y: 008  054(0x36)(0b110110): 12.576
x: 07, 2^y: 008  055(0x37)(0b110111): 14.672
x: 08, 2^y: 008  056(0x38)(0b111000): 16.768
x: 09, 2^y: 008  057(0x39)(0b111001): 18.864
x: 10, 2^y: 008  058(0x3a)(0b111010): 20.96
x: 11, 2^y: 008  059(0x3b)(0b111011): 23.056
x: 12, 2^y: 008  060(0x3c)(0b111100): 25.152
x: 13, 2^y: 008  061(0x3d)(0b111101): 27.248
x: 14, 2^y: 008  062(0x3e)(0b111110): 29.344
x: 15, 2^y: 008  063(0x3f)(0b111111): 31.44
x: 00, 2^y: 016  064(0x40)(0b1000000): 0.0
x: 01, 2^y: 016  065(0x41)(0b1000001): 4.192
x: 02, 2^y: 016  066(0x42)(0b1000010): 8.384
x: 03, 2^y: 016  067(0x43)(0b1000011): 12.576
x: 04, 2^y: 016  068(0x44)(0b1000100): 16.768
x: 05, 2^y: 016  069(0x45)(0b1000101): 20.96
x: 06, 2^y: 016  070(0x46)(0b1000110): 25.152
x: 07, 2^y: 016  071(0x47)(0b1000111): 29.344
x: 08, 2^y: 016  072(0x48)(0b1001000): 33.536
x: 09, 2^y: 016  073(0x49)(0b1001001): 37.728
x: 10, 2^y: 016  074(0x4a)(0b1001010): 41.92
x: 11, 2^y: 016  075(0x4b)(0b1001011): 46.112
x: 12, 2^y: 016  076(0x4c)(0b1001100): 50.304
x: 13, 2^y: 016  077(0x4d)(0b1001101): 54.496
x: 14, 2^y: 016  078(0x4e)(0b1001110): 58.688
x: 15, 2^y: 016  079(0x4f)(0b1001111): 62.88
x: 00, 2^y: 032  080(0x50)(0b1010000): 0.0
x: 01, 2^y: 032  081(0x51)(0b1010001): 8.384
x: 02, 2^y: 032  082(0x52)(0b1010010): 16.768
x: 03, 2^y: 032  083(0x53)(0b1010011): 25.152
x: 04, 2^y: 032  084(0x54)(0b1010100): 33.536
x: 05, 2^y: 032  085(0x55)(0b1010101): 41.92
x: 06, 2^y: 032  086(0x56)(0b1010110): 50.304
x: 07, 2^y: 032  087(0x57)(0b1010111): 58.688
x: 08, 2^y: 032  088(0x58)(0b1011000): 67.072
x: 09, 2^y: 032  089(0x59)(0b1011001): 75.456
x: 10, 2^y: 032  090(0x5a)(0b1011010): 83.84
x: 11, 2^y: 032  091(0x5b)(0b1011011): 92.224
x: 12, 2^y: 032  092(0x5c)(0b1011100): 100.608
x: 13, 2^y: 032  093(0x5d)(0b1011101): 108.992
x: 14, 2^y: 032  094(0x5e)(0b1011110): 117.376
x: 15, 2^y: 032  095(0x5f)(0b1011111): 125.76
x: 00, 2^y: 064  096(0x60)(0b1100000): 0.0
x: 01, 2^y: 064  097(0x61)(0b1100001): 16.768
x: 02, 2^y: 064  098(0x62)(0b1100010): 33.536
x: 03, 2^y: 064  099(0x63)(0b1100011): 50.304
x: 04, 2^y: 064  100(0x64)(0b1100100): 67.072
x: 05, 2^y: 064  101(0x65)(0b1100101): 83.84
x: 06, 2^y: 064  102(0x66)(0b1100110): 100.608
x: 07, 2^y: 064  103(0x67)(0b1100111): 117.376
x: 08, 2^y: 064  104(0x68)(0b1101000): 134.144
x: 09, 2^y: 064  105(0x69)(0b1101001): 150.912
x: 10, 2^y: 064  106(0x6a)(0b1101010): 167.68
x: 11, 2^y: 064  107(0x6b)(0b1101011): 184.448
x: 12, 2^y: 064  108(0x6c)(0b1101100): 201.216
x: 13, 2^y: 064  109(0x6d)(0b1101101): 217.984
x: 14, 2^y: 064  110(0x6e)(0b1101110): 234.752
x: 15, 2^y: 064  111(0x6f)(0b1101111): 251.52
x: 00, 2^y: 128  112(0x70)(0b1110000): 0.0
x: 01, 2^y: 128  113(0x71)(0b1110001): 33.536
x: 02, 2^y: 128  114(0x72)(0b1110010): 67.072
x: 03, 2^y: 128  115(0x73)(0b1110011): 100.608
x: 04, 2^y: 128  116(0x74)(0b1110100): 134.144
x: 05, 2^y: 128  117(0x75)(0b1110101): 167.68
x: 06, 2^y: 128  118(0x76)(0b1110110): 201.216
x: 07, 2^y: 128  119(0x77)(0b1110111): 234.752
x: 08, 2^y: 128  120(0x78)(0b1111000): 268.288
x: 09, 2^y: 128  121(0x79)(0b1111001): 301.824
x: 10, 2^y: 128  122(0x7a)(0b1111010): 335.36
x: 11, 2^y: 128  123(0x7b)(0b1111011): 368.896
x: 12, 2^y: 128  124(0x7c)(0b1111100): 402.432
x: 13, 2^y: 128  125(0x7d)(0b1111101): 435.968
x: 14, 2^y: 128  126(0x7e)(0b1111110): 469.504
x: 15, 2^y: 128  127(0x7f)(0b1111111): 503.04
"""
