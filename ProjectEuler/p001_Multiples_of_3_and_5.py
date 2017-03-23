#!/usr/bin/env python
# -*- coding:utf-8 -*-
LIMIT=1000
print sum([i for i in range(LIMIT) if i%3==0 or i%5==0])
