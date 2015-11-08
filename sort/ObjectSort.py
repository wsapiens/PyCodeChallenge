__author__ = 'spark'


import operator


class Country(object):
	def __init__(self, name):
		self.name = name
	def __lt__(self, other):
		if self.name == 'united states':
			return True
		elif other.name == 'united states':
			return False
		return self.name < other.name

if __name__ == '__main__':
    us = Country('united states')
    china = Country('china')
    france = Country('france')
    italy = Country('italy')
    zimbabwe = Country('zimbabwe')
    l = [china, italy, zimbabwe, us, france]
    print('before sort')
    for c in l:
        print c.name

    sorted_l = sorted(l, key=operator.attrgetter('name'))
    print('\nafter sort by operator')
    for c in sorted_l:
        print c.name

    print('\nafter sort by __lt__')
    l.sort()
    for c in l:
        print c.name


