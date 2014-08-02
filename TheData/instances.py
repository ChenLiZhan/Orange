import Orange
from collections import Counter

data = Orange.data.Table('iris')
print 'First three data instances:'
for d in data[:3]:
	print d

print '25-th data instance:'
print data[24]

name = 'sepal width'
print 'Value of %s for the first instances:' % name, data[0][name]
print 'The 3rd value of the 25th data instance:', data[24][2]


average = lambda xs: sum(xs) / float(len(xs))

data = Orange.data.Table('iris')
print '%-15s %s' % ('Feature', 'Mean')
for x in data.domain.features:
	print '%-15s %.2f' % (x.name, average([d[x] for d in data]))


targets = data.domain.class_var.values
print '%-15s %s' % ('Feature', ' '.join('%15s' % c for c in targets))
for x in data.domain.features:
	dist = ['%15.2f' % average([d[x] for d in data if d.get_class() == c]) for c in targets]
	print '%-15s' % x.name, ' '.join(dist)


data = Orange.data.Table('lenses')
print Counter(str(d.get_class()) for d in data)
