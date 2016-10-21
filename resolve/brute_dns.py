# -*- coding=utf-8 -*-
import dns.resolver
from itertools import permutations



answers = dns.resolver.query('www.baidu.cn','A')
for rdata in answers:
    print rdata

shengmu_list=['b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s']

def domainGenerator():
    for i+1 in range(1,18)
        for i in permutations(shengmu_list,i):
            temp = ''
            for j in i:
                temp+=str(j)
            print temp
            yield temp



