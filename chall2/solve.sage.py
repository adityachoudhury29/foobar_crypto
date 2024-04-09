

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_148982911401264734500617017580518449923542719532318121475997727602675813514863 = Integer(148982911401264734500617017580518449923542719532318121475997727602675813514863); _sage_const_2 = Integer(2); _sage_const_99943368625476277151400768907519717344447758596311103260066302523387843692499 = Integer(99943368625476277151400768907519717344447758596311103260066302523387843692499); _sage_const_82164720827627951718117576622367372918842412631288684063666489980382312886875 = Integer(82164720827627951718117576622367372918842412631288684063666489980382312886875); _sage_const_20555462814568596793812771425415543791560033744700837082533238767135 = Integer(20555462814568596793812771425415543791560033744700837082533238767135); _sage_const_121728190859093179709167853051428045020048650314914045286511335302789797110644 = Integer(121728190859093179709167853051428045020048650314914045286511335302789797110644); _sage_const_18832686601255134631820635660734300367214611070497673143677605724980 = Integer(18832686601255134631820635660734300367214611070497673143677605724980); _sage_const_70503066417308377066271947367911829721247208157460892633371511382189117698027 = Integer(70503066417308377066271947367911829721247208157460892633371511382189117698027); _sage_const_18679076989831101699209257375687089051054511859966345809079812661627 = Integer(18679076989831101699209257375687089051054511859966345809079812661627); _sage_const_129356717302185231616252962266443899346987025366769583013987552032290057284641 = Integer(129356717302185231616252962266443899346987025366769583013987552032290057284641); _sage_const_2084781842220461075274126508657531826108703724816608320266110772897 = Integer(2084781842220461075274126508657531826108703724816608320266110772897); _sage_const_0 = Integer(0); _sage_const_96 = Integer(96); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_160 = Integer(160); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_16 = Integer(16)
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from hashlib import sha224
from binascii import unhexlify

p =  _sage_const_148982911401264734500617017580518449923542719532318121475997727602675813514863 
g =  _sage_const_2 
y =  _sage_const_99943368625476277151400768907519717344447758596311103260066302523387843692499 
data = [(_sage_const_82164720827627951718117576622367372918842412631288684063666489980382312886875 , _sage_const_20555462814568596793812771425415543791560033744700837082533238767135 ),
(_sage_const_121728190859093179709167853051428045020048650314914045286511335302789797110644 , _sage_const_18832686601255134631820635660734300367214611070497673143677605724980 ),
(_sage_const_70503066417308377066271947367911829721247208157460892633371511382189117698027 , _sage_const_18679076989831101699209257375687089051054511859966345809079812661627 ),
(_sage_const_129356717302185231616252962266443899346987025366769583013987552032290057284641 , _sage_const_2084781842220461075274126508657531826108703724816608320266110772897 )]
ss = []
es = []
# k - x*e - s = 0 mod p
q = p//_sage_const_2 
for i in range(len(data)):
    ss.append(data[i][_sage_const_0 ] * pow(_sage_const_2 ,-_sage_const_96 ,q))
    es.append(data[i][_sage_const_1 ] * pow(_sage_const_2 ,-_sage_const_96 ,q))


news = []
newe = []
for i in range(_sage_const_3 ):
    news.append(int(ss[i] - ss[i+_sage_const_1 ]))
    newe.append(int(es[i] - es[i+_sage_const_1 ]))

# We have three things where 
# 2^160 - e*x - s = 0 mod p
# Perfect HNP scenario!

# Let's just do standard HNP lattice thing lol
B = _sage_const_2 **_sage_const_160 
M = matrix(QQ, _sage_const_5 , _sage_const_5 )
for i in range(_sage_const_3 ):
    M[i,i] = q

for i in range(_sage_const_3 ):
    M[_sage_const_4 , i] = news[i]
    M[_sage_const_3 , i] = newe[i]

    M[_sage_const_3 , _sage_const_3 ] = QQ(B)/QQ(q)
M[_sage_const_4 , _sage_const_4 ] = QQ(B)
M = (M.LLL())
d =  int(M[_sage_const_1 ][-_sage_const_2 ] * q/B) % p
# Note, you might need to add q
d = int(d) + p//_sage_const_2 
print("privkey =", d)
key = sha224(long_to_bytes(d)).digest()[:_sage_const_16 ]
iv = unhexlify("563391612e7c7d3e6bd03e1eaf76a0ba")
ct = unhexlify("e426c232b20fc298fb4499a2fff2e248615a379c5bc1a7447531f8a66b13fb57e2cf334247a0589be816fc52d80c064b61fa60261e925beb34684655278955e0206709f95173ad292f5c60526363766061e37dd810ee69d1266cbe5124ae18978214e8b39089b31cad5fd91b9a99e344830b76d456bbf92b5585eebeaf85c990")

cipher = AES.new(key, AES.MODE_CBC, iv)
print(cipher.decrypt(ct))
